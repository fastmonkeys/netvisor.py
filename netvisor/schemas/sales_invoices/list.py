# -*- coding: utf-8 -*-
"""
    netvisor.schemas.sales_invoices.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..common import DateSchema
from ..fields import Decimal


class StatusSchema(Schema):
    status = fields.String(load_from='#text')
    substatus = fields.String(load_from='@substatus')


class SalesInvoiceSchema(Schema):
    netvisor_key = fields.Integer()
    number = fields.Integer(load_from='invoice_number')
    date = fields.Nested(DateSchema, load_from='invoicedate')
    status = fields.Nested(StatusSchema, load_from='invoice_status')
    customer_code = fields.String()
    customer_name = fields.String()
    reference_number = fields.String()
    sum = Decimal(load_from='invoice_sum')
    open_sum = Decimal(load_from='open_sum')


@SalesInvoiceSchema.preprocessor
def preprocess_sales_invoice(schema, input_data):
    input_data['substatus'] = input_data['status']['substatus']
    input_data['status'] = input_data['status']['status']
    return input_data


class SalesInvoiceListSchema(Schema):
    sales_invoices = fields.List(
        fields.Nested(SalesInvoiceSchema),
        load_from='sales_invoice'
    )


@SalesInvoiceListSchema.preprocessor
def preprocess_sales_invoice_list(schema, input_data):
    return input_data['sales_invoices'] if input_data else []
