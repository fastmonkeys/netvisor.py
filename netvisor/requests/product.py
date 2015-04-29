# -*- coding: utf-8 -*-
"""
    netvisor.requests.product
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..exc import InvalidData
from ..responses.products import GetProductResponse, ProductListResponse
from .base import Request


class GetProductRequest(Request):
    method = 'GET'
    uri = 'GetProduct.nv'
    response_cls = GetProductResponse

    def parse_response(self, response):
        data = super(GetProductRequest, self).parse_response(response)
        self.ensure_not_empty(data)
        return data

    def ensure_not_empty(self, data):
        if data is None:
            raise InvalidData(
                'Data form incorrect:. '
                'Product not found with Netvisor identifier: {0}'.format(
                    self.params['id']
                )
            )


class ProductListRequest(Request):
    method = 'GET'
    uri = 'ProductList.nv'
    response_cls = ProductListResponse
