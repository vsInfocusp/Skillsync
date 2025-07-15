from pydantic import EmailStr, BaseModel, Field


class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@test.com")
    username: str = Field(..., example="John Doe")


class UserCreate(UserBase):
    password: str = Field(..., example="password123")


class UserUpdate(UserBase):
    password: str | None = Field(None, example="password123")


class User(UserBase):
    id: int = Field(..., example=1)
    is_active: bool = Field(..., example=True)
    is_superuser: bool = Field(..., example=False)
