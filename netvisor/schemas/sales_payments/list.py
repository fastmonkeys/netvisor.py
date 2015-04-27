# -*- coding: utf-8 -*-
"""
    netvisor.schemas.sales_payments.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..fields import Decimal, FinnishDate


class BankStatusErrorDescriptionSchema(Schema):
    code = fields.String(load_from='@code')
    description = fields.String(load_from='#text')


class SalesPaymentSchema(Schema):
    netvisor_key = fields.Integer()
    name = fields.String()
    date = FinnishDate()
    sum = Decimal()
    foreign_currency_amount = Decimal(allow_none=True)
    reference_number = fields.String()
    invoice_number = fields.Integer()
    bank_status = fields.String()
    bank_status_error_description = fields.Nested(
        BankStatusErrorDescriptionSchema
    )


class SalesPaymentListSchema(Schema):
    sales_payments = fields.List(
        fields.Nested(SalesPaymentSchema),
        load_from='sales_payment'
    )


@SalesPaymentListSchema.preprocessor
def preprocess_sales_payment_list(schema, input_data):
    return input_data['sales_payments'] if input_data else []
