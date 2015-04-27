# -*- coding: utf-8 -*-
"""
    netvisor.services.customer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..requests.customer import (
    CreateCustomerRequest,
    CustomerListRequest,
    GetCustomerRequest
)
from .base import Service


class CustomerService(Service):
    def get(self, id):
        request = GetCustomerRequest(self.client, params={'id': id})
        return request.make_request()

    def list(self, query=None):
        request = CustomerListRequest(self.client, params={'Keyword': query})
        return request.make_request()

    def create(self, customer):
        request = CreateCustomerRequest(
            self.client,
            params={'method': 'add'},
            data=customer
        )
        return request.make_request()
