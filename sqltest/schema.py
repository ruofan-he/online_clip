#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

Base=declarative_base()

class User(Base):
    __tablename__="test_user" #テーブル名を指定
    user_id=Column(Integer, primary_key=True)
    first_name=Column(String(255))
    last_name=Column(String(255))
    fucker=Column(String(1919))
    age=Column(Integer)
    def full_name(self):#フルネームを返すメソッド
        return "{self.first_name} {self.last_name}"