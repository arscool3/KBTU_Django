from worker.worker import celery_worker
from app.models.models import User, Application, ProfileUpdateApplication
from app.db.session import get_db
from sqlalchemy import func
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

@celery_worker.task
def create_application(user_id, data):
    try:
        db = get_db()

        # current user profile
        user = db.query(User).filter(User.id == user_id).first()
        application = db.query(Application).filter(Application.user_id == user_id, Application.status == 'Создано').first()

        application_id = None
        if application:
            application_id = application.id
            for detail in application.application_details:
                if detail.key in data.keys():
                    detail.new_value = data[detail.key]

                    del data[detail.key]

            application.updated_at = func.now()
        else:
            new_application = Application(
                user_id=user_id
            )
            db.add(new_application)
            db.commit()

            application_id = new_application.id

        for key, value in data.items():
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

        db.commit()
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

        application = db.query(Application).filter(Application.id == application_id, Application.status == 'Создано').first()

        if not application:
            return

        #1
        application.manager_id = manager_id
        application.status = 'Утверждено' if is_approved else 'Отклонено'
        application.closed_at = func.now()

        #2
        if is_approved:
            user = application.user
            user.updated_at = func.now()
            for detail in application.application_details:
                setattr(user, detail.key, detail.new_value)

        db.commit()

        if user.email:
            send_email.delay('Hello', 'World', user.email)
    except Exception as e:
        print(f'{e}')
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@celery_worker.task
def send_email(subject, body, recipient_email):
    message = MIMEMultipart()
    message["To"] = 'To line here.'
    message["From"] = 'From line here.'
    message["Subject"] = subject

    message.attach(MIMEText(body, 'plain'))

    email = os.getenv('GMAIL_EMAIL')
    password = os.getenv('GMAIL_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email, password)
    server.sendmail(email, recipient_email, message.as_string())

    server.quit()
    print('Email sent successfully')
