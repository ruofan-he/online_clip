#!/usr/bin/env python3
import click
from .__init__ import init_db, migrate
from .util import get_uri

@click.group()
def cmd():
    pass

cmd.command('init-db')(init_db)
cmd.command('migrate')(migrate)
cmd.command('uri')(lambda: print(get_uri()))


if __name__ == '__main__':
    cmd()