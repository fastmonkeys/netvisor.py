import os
import re

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'netvisor', '__init__.py')
    contents = open(filename).read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


setup(
    name='netvisor',
    version=get_version(),
    description='Python wrapper for the Netvisor API',
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()
    ),
    author='Janne Vanhala',
    author_email='janne@fastmonkeys.com',
    url='http://github.com/fastmonkeys/netvisor.py',
    packages=find_packages(),
    package_data={
        '': ['LICENSE']
    },
    license=open('LICENSE').read(),
    platforms='any',
    install_requires=[
        'inflection',
        'marshmallow>=2.0.0',
        'requests',
        'xmltodict',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
