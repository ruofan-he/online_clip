#!/usr/bin/env python3
from .engine import engine
from sqlalchemy.orm import sessionmaker
from .util import SessionHandler
from .schema import Account, Entry
from sqlalchemy import desc, or_

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
            return False, {}
        
        return fetched_account.pw_hash == pw_hash, {'account_key': fetched_account.key}

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
            return register_success, {}

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
            account.key
        
        return register_success, {'account_key': account.key}
    
    def get_recent_entry(self, num, public=True, account_key=None):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        fetched_entry = None
        
        with open_session() as session:

            query = (
                session
                .query(Entry)
                .order_by(desc(Entry.created_at))
            )
            
            if account_key:
                if public:
                    query = (
                        query
                        .filter(or_(Entry.is_public == True,Entry.account_key == account_key))
                    )
                else:
                    query = query.filter(Entry.account_key == account_key)
            else:
                query = query.filter(Entry.is_public ==  True)
            
            fetched_entry = query.limit(num).all()
            for entry in fetched_entry: entry.account # for lazy loading
        
        return fetched_entry

    def get_entry(self, entry_key):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        fetched_entry = None
        
        with open_session() as session:
            fetched_entry = (
                session
                .query(Entry)
                .get(entry_key)
            )
        
        return fetched_entry

    def append_entry(self, account_key):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)
        
        with open_session() as session:
            entry = Entry(
                account_key = account_key,
                text = '',
                is_public = False
            )
            session.add(entry)
            session.commit()
        
    def update_entry(self, entry):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        entry_key = entry.key
        entry_text = entry.text
        entry_is_public = entry.is_public

        
        with open_session() as session:
            fetched_entry = session.query(Entry).get(entry_key)
            fetched_entry.text = entry_text
            fetched_entry.is_public = entry_is_public
            session.commit()

    def delete_entry(self, entry):
        SessionClass    = sessionmaker(self.engine)
        open_session    = SessionHandler(SessionClass)

        entry_key = entry.key
        
        with open_session() as session:
            fetched_entry = session.query(Entry).get(entry_key)
            session.delete(fetched_entry)
            session.commit()