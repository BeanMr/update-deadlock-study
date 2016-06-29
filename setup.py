# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DeadlockStudy',
    version='0.0.1',
    description='Update according Index at the same index-key, deadlock detected',
    long_description=readme,
    author='Fengdd',
    author_email='beanmrx@gmail.com',
    url='https://github.com/BeanMr/update-deadlock-study',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

