from datetime import date
from typing import Optional

from pydantic import BaseModel


class Person(BaseModel):
    id: Optional[str] = None
    apelido: str
    nome: str
    nascimento: date
    # stack: list[str]