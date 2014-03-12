"""
    netvisor.client
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Janne Vanhala.
    :license: BSD, see LICENSE for more details.
"""
import requests
import xmltodict
from .exc import NetvisorError


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
        response = Response(self.requester.request(method, url, **kwargs))
        response.raise_for_failure()
        return response

    def make_url(self, path):
        return '{host}/{path}'.format(host=self.host, path=path)


class Response(object):

    def __init__(self, response):
        self.response = response
        self.data = xmltodict.parse(self.response.text)

    def raise_for_failure(self):
        if not self.is_ok:
            raise NetvisorError.from_status(self.statuses[1])

    @property
    def statuses(self):
        return self.data['Root']['ResponseStatus']['Status']

    @property
    def is_ok(self):
        return self.statuses == 'OK'
