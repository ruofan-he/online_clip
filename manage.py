#!/usr/bin/env python3
import click
import os

@click.group()
def cmd():
    pass

db_group = cmd.group('init-db')(lambda: None)
@db_group.command('reset')
def init_db_reset():
    from database import init_db
    init_db()

@db_group.command('clear')
def init_db_clear():
    from database import clear_db
    clear_db()

@db_group.command('table')
def init_db_table():
    from database import create_table
    create_table


migrate_group = cmd.group('migrate')(lambda: None)
@migrate_group.command('revision')
@click.option('-a','--autogenerate', is_flag=True)
@click.option('-m','--message')
def revision(autogenerate, message):
    from database import revision
    revision(autogenerate, message)

@migrate_group.command('upgrade')
def upgrade():
    from database import upgrade
    upgrade()

@cmd.command('uri')
def uri():
    from database.util import get_uri
    print(get_uri())


if __name__ == '__main__':
    cmd()