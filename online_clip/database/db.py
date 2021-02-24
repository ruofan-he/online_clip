#!/usr/bin/env python3
from .engine import engine
from sqlalchemy.orm import sessionmaker
from .util import SessionHandler
from .schema import Account, Entry
from sqlalchemy import desc

class Database():
    def __init__(self):
        self.engine     = engine
    
    def auth_user(self, user_id, pw_hash):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        with open_session() as session:
            fetched_account = (
                session
                .query(Account)
                .filter(Account.user_id == user_id)
                .first()
            )

        if fetched_account is None:
            return False
        
        return fetched_account.pw_hash == pw_hash

    def register_user(self, user_id, pw_hash, first_name, last_name):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        register_success = None

        with open_session() as session:
            fetched_account = (
                session
                .query(Account.user_id)
                .filter(Account.user_id == user_id)
                .first()
            )

        if fetched_account:
            register_success = False
            return register_success

        with open_session() as session:
            account = Account(
                user_id     = user_id,
                pw_hash     = pw_hash,
                first_name  = first_name,
                last_name   = last_name
            )
            session.add(account)
            session.commit()
            register_success = True
        
        return register_success
    
    def get_entry(self, cursor):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        fetched_entry = None
        
        with open_session() as session:
            fetched_entry = (
                session
                .query(Entry)
                .order_by(desc(Entry.created_at))
                .limit(cursor)
                .all()
            )
        
        return fetched_entry
    