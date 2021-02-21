#!/usr/bin/env python3
from .engine import engine
from sqlalchemy.orm import sessionmaker
from .schema import Base, User


def init_db():
    clear_db()
    create_table()
    write_element()

def clear_db():
    print('clear DB')
    sql         = 'SELECT relname AS table_name FROM pg_stat_user_tables;'
    result      = engine.execute(sql).fetchall()
    table_list  = [dict(row.items()).get('table_name') for row in result ]
    if 'user' in table_list: table_list.remove('user')
    for table in table_list:
        sql     = f'DROP TABLE IF EXISTS {table};'
        engine.execute(sql)

def create_table():
    print('create table')
    Base.metadata.create_all(engine, checkfirst=True)

def write_element():
    print('write elements')
    SessionClass    = sessionmaker(engine)
    session         = SessionClass()
    user_list       = [ User(   first_name="first_b{}".format(i),
                                last_name="last_b{}".format(i),
                                age=20+i) for i in range(20) ]
    for user in user_list: session.add(user)
    session.commit()