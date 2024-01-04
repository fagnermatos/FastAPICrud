from sqlalchemy import Date, Column, Integer, String, ARRAY

from .database import Base


class People(Base):
    __tablename__ = 'pessoas'

    id = Column(String, primary_key=True, index=True, server_default='uuid_generate_v4()')
    apelido = Column(String, unique=True, index=True)
    nome = Column(String)
    nascimento = Column(Date)
    # stack = Column(ARRAY)