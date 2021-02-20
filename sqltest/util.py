#!/usr/bin/env python3
import json
import os

def get_uri():
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
