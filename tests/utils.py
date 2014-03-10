import io
import os


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), 'data')


def get_responses_dir():
    return os.path.join(get_data_dir(), 'responses')


def get_response_content(filename):
    filename = os.path.join(get_responses_dir(), filename)
    with io.open(filename, 'rb') as f:
        return f.read()


def get_response_text(filename):
    return get_response_content(filename).decode('utf-8')
