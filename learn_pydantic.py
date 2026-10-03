from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI

app = FastAPI()


data = {
    "email": "a@mail.com",
    "bio": 'Iam nigger',
    "age": 12,
    
}

data_no_age = {
    "email": "a@mail.com",
    "bio": 'Iam nigger',
    "gender": "mail",
    "birthday": "1990"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    # model_config = ConfigDict(extra='forbid')

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "message": "User added"}

@app.get("/users")
def get_users() -> list[UserSchema]:
    return users
    

class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

user = UserAgeSchema(**data)
user2 = UserSchema(**data_no_age)
print(repr(user))
print(repr(user2))