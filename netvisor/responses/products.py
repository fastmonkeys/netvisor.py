# -*- coding: utf-8 -*-
"""
    netvisor.responses.products
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import GetProductSchema, ProductListSchema
from .base import Response


class ProductListResponse(Response):
    schema_cls = ProductListSchema
    tag_name = 'product_list'


class GetProductResponse(Response):
    schema_cls = GetProductSchema
    tag_name = 'product'
