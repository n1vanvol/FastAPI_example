from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database,schemas, models , utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Aunthentication'])

@router.post('/login', response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    # This is a dependency class to collect the username and password as form data for an OAuth2 password flow.


    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user or not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
                            detail = f'Invalid Credentials')
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return{"access_token" : access_token, "token_type": "bearer"}