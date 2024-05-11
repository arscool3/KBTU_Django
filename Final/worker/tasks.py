from worker.worker import celery_worker
from app.models.models import User, Application, ProfileUpdateApplication
from app.db.session import get_db
from sqlalchemy import func
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from worker.assets.functions import get_expiration_timestamp
from dotenv import load_dotenv

load_dotenv()

@celery_worker.task
def create_application(user_id, data):
    try:
        db = get_db()
        print('i am here')
        # current user profile
        user = db.query(User).filter(User.id == user_id).first()
        application = db.query(Application).filter(Application.user_id == user_id, Application.status_id == 1).first()
        print('i am here 2')
        application_id = None
        if application:
            application_id = application.id
            for detail in application.application_details:
                if detail.key in data.keys() and data.get(detail.key):
                    detail.new_value = data[detail.key]

                    del data[detail.key]

            application.updated_at = func.now()
        else:
            new_application = None
            if not user.email and not data.get('email'):
                new_application = Application(
                    user_id=user_id,
                    status_id=2
                )
            else:
                new_application = Application(
                    user_id=user_id
                )

            db.add(new_application)
            db.commit()

            new_application.expires_at = get_expiration_timestamp(new_application.created_at.replace(second=0, microsecond=0))
            application_id = new_application.id
        print('i am here 3')
        for key, value in data.items():
            if not value:
                continue

            try:
                new_application_detail = ProfileUpdateApplication(
                    application_id=application_id,
                    key=key,
                    old_value=getattr(user, key),
                    new_value=value
                )

                db.add(new_application_detail)
            except Exception as e:
                print(f'{key} attribute does not exist in User Table')
        print('i am here 4')
        db.commit()
        print('i am here 5')
        if user.email and not application:
            send_email.delay(application_id, user.email)
        elif not user.email and data.get('email'):
            send_email.delay(application_id, data['email'])
    except Exception as e:
        print(f'{e}')
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@celery_worker.task
def change_status(manager_id, application_id, is_approved):
    try:
        db = get_db()

        application = db.query(Application).filter(Application.id == application_id).first()

        if not application:
            return

        #1
        application.manager_id = manager_id
        application.status_id = 3 if is_approved else 4
        application.closed_at = func.now()

        #2
        if is_approved:
            user = application.user
            user.updated_at = func.now()
            for detail in application.application_details:
                setattr(user, detail.key, detail.new_value)

        db.commit()
    except Exception as e:
        print(f'{e}')
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@celery_worker.task
def send_email(application_id, recipient_email):
    with open('worker/assets/confirmation_mail.html', 'r') as file:
        body = file.read()

    message = MIMEMultipart()
    message["Subject"] = 'Подтвердите заявку на изменение профиля Egov.kz'

    message.attach(MIMEText(body.format(application_id), 'html'))

    email = os.getenv('GMAIL_EMAIL')
    password = os.getenv('GMAIL_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email, password)
    server.sendmail(email, recipient_email, message.as_string())

    server.quit()
    print('Email sent successfully')
