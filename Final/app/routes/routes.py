from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from psycopg2.extras import Json
from sqlalchemy.orm import Session
from app.utils.tokens import create_token, revoked_tokens, verify_token
from app.db.session import get_db
from app.utils.utils import get_century_and_gender
from app.models.models import User
from worker.tasks import create_application

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

        token_data = {"sub": iinbin}
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
        iinbin = token["sub"]

        user = db.query(User).filter(User.iinbin == iinbin).first()
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
async def update_profile(request: Request, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    try:
        data = await request.json()
        iinbin = token["sub"]

        user = db.query(User).filter(User.iinbin == iinbin).first()
        user_id = user.id
        print('update_profile:', data, 'user_id:', user_id)
        create_application.delay(user_id, data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=401)
    finally:
        try:
            db.close()
        except:
            print('Connection already closed')
