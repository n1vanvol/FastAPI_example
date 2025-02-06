from typing import Annotated
from pydantic import BaseModel, ConfigDict, EmailStr, Field, conint
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True



class PostCreate(PostBase):
    pass

    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None
    

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]


