#!/usr/bin/env python3
# -----------------------
# basic database migrate management
# intended to be excuted from command line
# -----------------------

from alembic.config import Config
from alembic import command
from .util import get_uri
import os

alembic_cfg = Config(os.path.join(os.path.dirname(__file__),"alembic.ini"))
alembic_cfg.set_main_option('sqlalchemy.url', get_uri())
alembic_cfg.set_main_option('script_location',
    os.path.join(os.path.dirname(__file__), alembic_cfg.get_main_option('script_location'))
    )

def revision(is_autogen, message):
    command.revision(alembic_cfg, autogenerate=is_autogen, message=message)

def upgrade():
    command.upgrade(alembic_cfg, "head")
    