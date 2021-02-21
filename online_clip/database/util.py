#!/usr/bin/env python3

def get_uri():
    import json
    import os
    with open(os.path.join(os.path.dirname(__file__), 'database.json'), 'r') as f:
        database_param = json.load(f)
    uri = database_param.get('URI', None)
    if uri is None:
        uri = 'postgres://{}:{}@{}:{}/{}'.format(
            database_param['USER'],
            database_param['PASSWORD'],
            database_param['HOST'],
            database_param['PORT'],
            database_param['DATABASE'],
        )

    return uri


class SessionHandler:
    from sqlalchemy.orm import sessionmaker, Session
    def __init__(self, factory: sessionmaker):
        self.factory = factory

    def __call__(self):
        return self

    def __enter__(self) -> Session:
        self.session = self.factory()
        return self.session

    def __exit__(self, *exception):
        if exception[0] is not None:
            print('--------------------')
            print(exception)
            print('--------------------')
            self.session.rollback()
        self.session.close()
        print('close session')
        