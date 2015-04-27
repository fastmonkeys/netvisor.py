# -*- coding: utf-8 -*-
"""
    netvisor.schemas.customers.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields


class CustomerSchema(Schema):
    netvisor_key = fields.Integer(load_from='netvisorkey', required=True)
    name = fields.String(required=True)
    code = fields.String(allow_none=True, required=True)
    organisation_identifier = fields.String(allow_none=True, required=True)


class CustomerListSchema(Schema):
    customers = fields.List(
        fields.Nested(CustomerSchema),
        load_from='customer'
    )


@CustomerListSchema.preprocessor
def preprocess_customer_list(schema, input_data):
    return input_data['customers'] if input_data else []
