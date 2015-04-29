# -*- coding: utf-8 -*-
"""
    netvisor.schemas.common
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, ValidationError, fields, pre_dump

from .fields import Decimal


class RejectUnknownFieldsSchema(Schema):
    @pre_dump
    def check_unknown_fields(self, data):
        field_names = set()
        for field_name, field in self.fields.items():
            attribute = getattr(field, 'attribute', None)
            field_names.add(field_name if attribute is None else attribute)
        for k in data:
            if k not in field_names:
                raise ValidationError("Unknown field name: '{}'".format(k))


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
