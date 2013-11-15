from distutils.core import setup
import os
import re


HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'src', 'netvisor', '__init__.py')
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
    author_email='janne.vanhala@gmail.com',
    url='http://github.com/jpvanhal/python-netvisor',
    packages=['netvisor'],
    package_data={
        '': ['LICENSE']
    },
    package_dir={
        '': 'src'
    },
    license=open('LICENSE').read(),
    platforms='any',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
