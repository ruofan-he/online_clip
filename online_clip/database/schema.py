#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import Integer, String, DateTime, UnicodeText, Boolean
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship

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
    entries         = relationship('Entry', backref='account', cascade="save-update, merge, delete, delete-orphan")

    def __str__(self):
        return \
f"""\
id          : {self.id}
accout      : {self.account}
name        : {self.first_name} {self.last_name}
entries     : {[entry.text for entry in self.entries]}
age         : {self.age}
created_at  : {self.created_at}\
"""
    

class Entry(Base):
    __tablename__   = "entry"
    id              = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id         = Column(
        Integer,
        ForeignKey(f'{Account.__tablename__}.id'),
        nullable=False
    )
    text            = Column(UnicodeText, default='', nullable=False)
    is_public       = Column(Boolean, default=False, nullable=False)
    expire_datetime = Column(DateTime, nullable=True)

    def __str__(self):
        return \
f"""\
id       : {self.id}
user_id  : {self.user_id}
text     : {self.text}\
"""
    
