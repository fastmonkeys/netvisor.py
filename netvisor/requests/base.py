# -*- coding: utf-8 -*-
"""
    netvisor.requests.base
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""


class Request(object):
    def __init__(self, client, params=None):
        self.client = client
        self.params = params

    def make_request(self):
        response = self.client.request(
            method=self.method,
            path=self.uri,
            params=self.params
        )
        return self.parse_response(response)

    def parse_response(self, response):
        response = self.response_cls(response)
        response.raise_for_failure()
        return response.data['root'][self.resource_key]
