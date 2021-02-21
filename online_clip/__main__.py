#!/usr/bin/env python3
import click

@click.group()
def cmd():
    pass

db_group = cmd.group('init-db')(lambda: None)
@db_group.command('init')
def init_db_init():
    from .database import init_db
    init_db()

@db_group.command('clear')
def init_db_clear():
    from .database import clear_db
    clear_db()

@db_group.command('table')
def init_db_table():
    from .database import create_table
    create_table()

@db_group.command('write')
def init_db_write():
    from .database import write_element
    write_element()

@db_group.command('read')
def init_db_read():
    from .database import read_element
    read_element()


migrate_group = cmd.group('migrate')(lambda: None)
@migrate_group.command('revision')
@click.option('-a','--autogenerate', is_flag=True)
@click.option('-m','--message')
def revision(autogenerate, message):
    from .database import revision
    revision(autogenerate, message)

@migrate_group.command('upgrade')
def upgrade():
    from .database import upgrade
    upgrade()

@cmd.command('uri')
def uri():
    from .database.util import get_uri
    print(get_uri())


if __name__ == '__main__':
    cmd()