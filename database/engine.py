#!/usr/bin/env python3
from sqlalchemy import create_engine
from .util import get_uri

engine = create_engine(
    get_uri(),
    encoding = "utf-8",
    echo=True
)
