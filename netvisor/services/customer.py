# -*- coding: utf-8 -*-
"""
    netvisor.services.customer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.customer import GetCustomerRequest, CustomerListRequest


class CustomerService(Service):
    def get(self, id):
        request = GetCustomerRequest(self.client, params={'id': id})
        return request.make_request()

    def list(self, query=None):
        request = CustomerListRequest(self.client, params={'Keyword': query})
        return request.make_request()
