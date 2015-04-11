# -*- coding: utf-8 -*-
"""
    netvisor.services.product
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..requests.product import GetProductRequest, ProductListRequest
from .base import Service


class ProductService(Service):
    def get(self, id):
        request = GetProductRequest(self.client, params={'id': id})
        return request.make_request()

    def list(self):
        request = ProductListRequest(self.client)
        return request.make_request()
