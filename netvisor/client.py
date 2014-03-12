"""
    netvisor.client
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Janne Vanhala.
    :license: BSD, see LICENSE for more details.
"""
import requests


class Client(object):

    def __init__(self, host, auth):
        self.host = host
        self.requester = requests.Session()
        self.requester.auth = auth

    def get(self, path, **kwargs):
        return self.request('GET', path, **kwargs)

    def post(self, path, **kwargs):
        return self.request('POST', path, **kwargs)

    def request(self, method, path, **kwargs):
        url = self.make_url(path)
        response = self.requester.request(method, url, **kwargs)
        return response

    def make_url(self, path):
        return '{host}/{path}'.format(host=self.host, path=path)
