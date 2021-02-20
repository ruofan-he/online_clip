#!/usr/bin/env python3
from .engine import engine
from alembic.config import Config
from alembic import command
from .util import get_uri
import os

def migrate():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__),"alembic.ini"))
    alembic_cfg.set_main_option('sqlalchemy.url', get_uri())
    alembic_cfg.set_main_option('script_location',
        os.path.join(os.path.dirname(__file__), alembic_cfg.get_main_option('script_location'))
        )
    command.upgrade(alembic_cfg, "head")