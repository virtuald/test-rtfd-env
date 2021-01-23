# this is a dirty hack to convince readthedocs to install a new version of pip

from setuptools import setup

setup(
    name="forcepip",
    version="1.0",
    install_requires=["pip>=20.3.3"],
)
