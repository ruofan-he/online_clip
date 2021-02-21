from setuptools import setup

setup(
    name="online_clip",
    version="1.0.0",
    install_requires=['click', 'SQLAlchemy', 'Flask', 'alembic'],
    packages=['online_clip'],
    extras_require={
        "develop": []
    },
)