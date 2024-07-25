"""
FLASK_DEBUG=1 FLASK_APP=blog.app:create_app flask shell
export FLASK_DEBUG=1
export FLASK_APP=blog.app:create_app
pip install -e .
"""

from setuptools import setup

setup(
    name="flask_blog",
    version="0.1.0",
    packages=["blog"],
    install_requires=[
        "flask",
        "flask-pymongo",
        "dynaconf",
        "flask-bootstrap",
        "mistune",
        "flask-simplelogin",
        "flask-admin",
    ],
)
