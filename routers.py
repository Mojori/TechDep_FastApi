import random

from fastapi import APIRouter

from sqlalchemy.orm import Session
from sqlalchemy import select

from database import engine, User

from schema import TrainSchema, PersonSchema, GetFromName

api_router = APIRouter()


@api_router.get("/hello")
def hello():
    return {"name": "papoe"}


@api_router.get("/random")
def hello():
    return {"random": random.randint(1, 1000)}


@api_router.post("/skley")
def skley(input_data: TrainSchema):
    first_row = input_data.fist_row
    second_row = input_data.second_row

    return {"new_row": f"{first_row}{second_row}"}


@api_router.post("/person", response_model=PersonSchema)
def person(input_data: PersonSchema):
    name = input_data.name
    surname = input_data.surname
    age = input_data.age

    with Session(engine) as session:
        person = User(
            name=name,
            surname=surname,
            age=age
        )
        session.add(person)
        session.commit()

    return {
        "name": name,
        "surname": surname,
        "age": age
    }


@api_router.post("/get_from_name", response_model=PersonSchema)
def get_from_name(input_data: GetFromName):
    name = input_data.name

    with Session(engine) as session:
        stmt = select(User).where(User.name == name)

        for user in session.scalars(stmt):
            user_info = {
                "name": user.name,
                "surname": user.surname,
                "age": user.age
            }
        return user_info
