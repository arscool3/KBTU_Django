from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from psycopg2.extras import Json
from sqlalchemy.orm import Session
from app.utils.tokens import create_token, revoked_tokens, verify_token
from app.db.session import get_db
from app.utils.utils import get_century_and_gender
from app.models.models import User, Application, ProfileUpdateApplication
from worker.tasks import create_application, change_status

router = APIRouter()

@router.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.json()
        iinbin = data.get("iinbin")
        year = int(iinbin[:2])
        month = iinbin[2:4]
        day = iinbin[4:6]
        century_and_gender_num = int(iinbin[6])
        century_and_gender = get_century_and_gender(century_and_gender_num)
        year = year + century_and_gender["century"]
        gender = century_and_gender["gender"]
        birthdate = f"{year}-{month}-{day}"
        password = data.get("password")
        fullname = data.get("name")
        birthplace = data.get("birthplace")
        nation = data.get("nation")

        new_user = User(
            iinbin=iinbin,
            password=password,
            fullname=fullname,
            birthdate=birthdate,
            birthplace=birthplace,
            nation=nation,
            gender=gender
        )

        db.add(new_user)
        db.commit()

        return {"message": "Account created successfully"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@router.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.json()
        iinbin = data.get("iinbin")
        password = data.get("password")

        user = db.query(User).filter(User.iinbin == iinbin).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not user.verify_password(password):
            raise HTTPException(status_code=401, detail="Incorrect password")

        role = "manager" if user.is_manager else "client"

        token_data = {"sub": str(user.id)}
        access_token = create_token(token_data)
        if iinbin in revoked_tokens:
            revoked_tokens.discard(iinbin)

        response_data = {"access_token": access_token, "token_type": "bearer", "role": role}
        return JSONResponse(content=response_data, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)


@router.post("/logout")
async def logout(token: str = Depends(verify_token)):
    revoked_tokens.add(token["sub"])
    return {"message": "Logout successful"}


@router.get("/profile", response_model=dict)
async def profile(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        user_id = token["sub"]

        user = db.query(User).filter(User.id == user_id).first()
        user_data = {
            'iinbin': user.iinbin,
            'fullname': user.fullname,
            'birthdate': user.birthdate,
            'birthplace': user.birthplace,
            'nation': user.nation,
            'gender': user.gender,
            'email': user.email,
            'phone_number': user.phone_number,
            'address': user.address
        }
        user_data = {key: 'Нет Данных' if value is None or value == "" else value for key, value in
                     user_data.items()}
        return user_data
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@router.post("/update_profile")
async def update_profile(request: Request, token: str = Depends(verify_token)):
    try:
        data = await request.json()
        user_id = token["sub"]

        create_application.delay(user_id, data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)


@router.get("/applications")
async def get_applications(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        user_id = token["sub"]
        user = db.query(User).filter(User.id == user_id).first()

        if user.is_manager:
            all_applications = db.query(Application).filter(Application.status == 'Создано')

            all_applications = [{'id': app.id,
                                 'iinbin': app.user.iinbin,
                                 'created_at': app.created_at}
                                for app in all_applications]

            return {'data': all_applications}
        else:
            user_applications = user.user_applications

            if not user_applications:
                raise HTTPException(status_code=401, detail="Profile not found")

            user_applications = [{'id': app.id,
                                  'created_at': app.created_at,
                                  'updated_at': app.updated_at,
                                  'closed_at': app.closed_at,
                                  'status': app.status}
                                 for app in user_applications]

            return {'data': user_applications}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@router.post("/application_detail")
async def get_application_detail(request: Request, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        data = await request.json()
        application_id = data.get("id_app")
        print('application_id:', application_id)

        application_detail = db.query(ProfileUpdateApplication).filter(ProfileUpdateApplication.application_id == application_id)
        application_detail = [{'column': row.key,
                              'old_value': row.old_value or 'Нет Данных',
                              'new_value': row.new_value}
                             for row in application_detail]

        return {'data': application_detail}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')


@router.post("/update_application_status")
async def update_application_status(request: Request, token: str = Depends(verify_token)):
    try:
        data = await request.json()
        print('data inside:', data)
        manager_id = token["sub"]
        application_id = data.get("id_app")
        is_approved = data.get("is_approved")

        print('manager_id:', manager_id)
        change_status.delay(manager_id, application_id, is_approved)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)

