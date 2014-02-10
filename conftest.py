import os

import pytest


@pytest.fixture(scope='session')
def data_dir():
    return os.path.join(os.path.dirname(__file__), 'tests', 'data')


@pytest.fixture(scope='session')
def responses_dir(data_dir):
    return os.path.join(data_dir, 'responses')
