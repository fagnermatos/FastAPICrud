from fastapi import FastAPI

from . import schemas
from .person_repository import PersonRepository

app = FastAPI()
repository = PersonRepository()


@app.post("/pessoas")
async def save(people: schemas.Person):
    return repository.save(people)


@app.get("/pessoas/{id}")
async def person(id: str):
    return repository.find_by(id)


@app.get("/pessoas")
async def people(filter: str = ''):
    return repository.search(filter)


@app.get("/contagem-pessoas")
async def count_people():
    return repository.count()
