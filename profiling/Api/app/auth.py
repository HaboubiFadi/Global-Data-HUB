import uvicorn
from fastapi import FastAPI


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel 
from fastapi import (
    Depends,
    
    status,
    
    HTTPException,
    Request,
)

from fastapi import APIRouter



router=APIRouter(prefix='/Authetification',
                 tags=['Authetification'])





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Authetification/token")

fake_users_db = {
    "Fadi": dict(
        username="Fadi",
        full_name="Fadi haboubi",
        email="fadi@addinn.com",
        hashed_password="fakehashedsecret",
        disabled=False,
    ),
    "addlinn": dict(
        username="addlinn",
        full_name="addlinn group",
        email="addinn@group.com",
        hashed_password="fakehashedsecret2",
        disabled=True,
    ),
}


def fake_hash_password(password: str):
    return f"fakehashed{password}"


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    return get_user(fake_users_db, token)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def get_me(current_user: User = Depends(get_current_active_user)):
    print('fafqsdqsdqsdqsd')
    print(current_user)
    return current_user


@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


































