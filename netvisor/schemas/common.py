# -*- coding: utf-8 -*-
"""
    netvisor.schemas.common
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from .fields import Decimal


class DateSchema(Schema):
    text = fields.Date(load_from='#text')


class StringSchema(Schema):
    text = fields.String(required=True, load_from='#text')


class DecimalSchema(Schema):
    text = Decimal(required=True, load_from='#text')


@DateSchema.preprocessor
@DecimalSchema.preprocessor
@StringSchema.preprocessor
def flatten_element(schema, input_data):
    return input_data['text']
