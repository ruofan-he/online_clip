from setuptools import setup, find_packages

setup(
    name="online_clip",
    version="1.0.0",
    install_requires=['click', 'SQLAlchemy', 'Flask', 'alembic'],
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        "develop": []
    },
)