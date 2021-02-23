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
    