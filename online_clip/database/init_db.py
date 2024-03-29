#!/usr/bin/env python3
# -----------------------
# basic database management
# intended to be excuted from command line
# -----------------------

import hashlib
from .engine import engine
from sqlalchemy.orm import sessionmaker
from .schema import Base, Account, Entry
from .util import SessionHandler


def init_db():
    clear_db()
    create_table()
    write_element()

# this can be used only for posgreSQL
# def clear_db():
#     print('clear DB')
#     sql         = 'SELECT relname AS table_name FROM pg_stat_user_tables;'
#     result      = engine.execute(sql).fetchall()
#     table_list  = [dict(row.items()).get('table_name') for row in result ]
#     if 'user' in table_list: table_list.remove('user')
#     for table in table_list:
#         sql     = f'DROP TABLE IF EXISTS {table} CASCADE;'
#         engine.execute(sql)

def clear_db():
    print('clear DB')
    Base.metadata.drop_all(engine)

def create_table():
    print('create table')
    Base.metadata.create_all(engine, checkfirst=True)

def write_element():
    print('write elements')
    SessionClass    = sessionmaker(engine)
    open_session    = SessionHandler(SessionClass)

    with open_session() as session:
        user_list       = [
            Account(
                user_id     = f"{hashlib.sha224(str(i).encode()).hexdigest()[:10]}",
                pw_hash     = 'pass',
                first_name  = f"first_b{i}",
                last_name   = f"last_b{i}",
                age         = 20+i
            )
            for i in range(20)]
        for user in user_list: session.add(user)
        session.flush() # instead of session.commit()
        # user-> after commit, id get non-null.
        # this dont happen if session.bulk_save_objects(user_list)
        # difference of session.commit() and session.flush()
        # commit() -> after insert, return the row with full column
        #                 that include already know data. So, that takes time.
        # flush()  -> after insert, return only some unknow data (e.g. autoincrement)
        #                 less returned informaiton, less time

        entry_list      = [
            Entry(
                account_key = account.key,
                text    = f'this entry is by key {account.key} user_id {account.user_id}',
                is_public = True
            ) for account in user_list
        ]
        session.bulk_save_objects(entry_list)   
        # bulk_save_objects take less time.
        # but devoid returned information
        # bulk_save_objects + flush => Error
        # bulk_save_objects + commit , recommended!
        session.commit() # recommanded! 
    
def read_element():
    print('read elements')
    SessionClass    = sessionmaker(engine)
    open_session    = SessionHandler(SessionClass)

    with open_session() as session:
        user = session.query(Account).first()
        entry = session.query(Entry).first()
        print('------------------')
        print(user)
        print('')
        print(entry)
        print('------------------')


def delete_element():
    print('delete element')
    SessionClass    = sessionmaker(engine)
    open_session    = SessionHandler(SessionClass)

    with open_session() as session:
        user = session.query(Account).first()
        entry = session.query(Entry).first()
        print('------------------')
        print(user)
        print('')
        print(entry)
        print('------------------')
        session.delete(user)
        session.commit()
