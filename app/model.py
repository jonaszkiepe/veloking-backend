from pydantic import BaseModel, Field, EmailStr


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "jkiepe@inkontor.com",
                "password": "pancake123",
            }
        }


class UserSchema(BaseModel):
    email: EmailStr = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    rentalPoint: str = Field(...)
    role: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
                "example": {
                    "email": "jkiepe@inkontor.com",
                    "firstName": "Jonasz",
                    "lastName": "Kiepe",
                    "rentalPoint": "baza",
                    "role": "manager",
                    "password": "pancake123",
                }
        }


class Rental(BaseModel):
    equipment: list
    forward_payment: float
    start_time: str
    end_time: str

    class Config:
        json_schema_extra = {
            "example": {
                "equipment": "RD-01, G1-02",
                "forward_payment": 30,
                "start_time": "some datetime",
                "end_time": "some datetime",
            }
        }