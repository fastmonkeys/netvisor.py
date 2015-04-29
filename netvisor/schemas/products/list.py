# -*- coding: utf-8 -*-
"""
    netvisor.schemas.products.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..fields import Decimal


class ProductSchema(Schema):
    netvisor_key = fields.Integer()
    name = fields.String()
    product_code = fields.String(allow_none=True)
    unit_price = Decimal()


class ProductListSchema(Schema):
    products = fields.List(fields.Nested(ProductSchema), load_from='product')


@ProductListSchema.preprocessor
def preprocess_product_list(schema, input_data):
    return input_data['products'] if input_data else []
