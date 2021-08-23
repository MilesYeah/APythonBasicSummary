# sqlalchemy查询结果转为list.md

```py
# encoding: utf-8

"""
@author: 
"""

import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect


BASE = declarative_base()


class Company(BASE):

    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    address = Column(Text)
    salary = Column(Float)

    def __repr__(self):
        return f"{self.__tablename__}:" \
               f"<Name:{str(self.name):<6}, Age:{str(self.age):<3}, Address:{str(self.address):<10}>"


# print(Company.__table__)
# print(Company.__tablename__)


engine = create_engine("sqlite:///sample_alchemy.db", echo=True)
BASE.metadata.create_all(engine)
SESSION = sessionmaker(bind=engine)
session = SESSION()

# Insert values
session.add(Company(name="Miles", age=29, address="CN", salary=9000))
session.commit()


ret = session.query(Company).filter_by(name="Lucy").first()
name = getattr(ret, "name")
age = getattr(ret, "age")


def ret2list(que):
    return [getattr(que, name) for name in inspect(que).mapper.columns.keys()]


def ret2dict(que):
    return {name: getattr(que, name) for name in inspect(que).mapper.columns.keys()}


ret_l = ret2list(ret)
ret_d = ret2dict(ret)


if __name__ == "__main__":

    print("")
    print("")

```
