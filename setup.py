# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server_reg"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Data registration service",
    author_email="",
    url="",
    keywords=["Swagger", "Data registration service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server_reg=swagger_server_reg.__main__:main']},
    long_description="""\
    API for Data registration service. © 2024, O-RAN ALLIANCE. All rights reserved. 
    """
)
