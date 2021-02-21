#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import Integer, String, DateTime, UnicodeText
from sqlalchemy.sql.functions import current_timestamp

Base=declarative_base()

class Account(Base):
    __tablename__   = "account" #テーブル名を指定
    id              = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    account         = Column(String(255), unique=True, nullable=False)
    pw_hash         = Column(String(255), nullable=False)
    first_name      = Column(String(255), nullable=True)
    last_name       = Column(String(255), nullable=True)
    age             = Column(Integer, nullable=True)
    created_at      = Column(DateTime, server_default=current_timestamp(), nullable=False)

    def __str__(self):
        return f"{self.id} {self.account} {self.first_name} {self.last_name} {self.age} {self.created_at}"
    

class Entry(Base):
    __tablename__   = "entry"
    id              = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id         = Column(Integer, ForeignKey(f'{Account.__tablename__}.id'), nullable=False)
    text            = Column(UnicodeText, default='', nullable=False)

    def __str__(self):
        return f"{self.id} {self.user_id} {self.text}"
    
