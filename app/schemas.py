from pydantic import BaseModel, EmailStr

class RegisterScheme(BaseModel):
   name: str 
   username: str
   email: EmailStr
   password: str

class UserOut(BaseModel):
    id: int
    name: str 
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int
