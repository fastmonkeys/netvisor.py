# -*- coding: utf-8 -*-
"""
    netvisor.schemas.sales_invoices.create
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import fields, post_dump

from ..common import RejectUnknownFieldsSchema
from ..fields import Decimal


class VatPercentageSchema(RejectUnknownFieldsSchema):
    percentage = Decimal()
    code = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['percentage'],
            '@vatcode': data['code']
        }


class UnitPriceSchema(RejectUnknownFieldsSchema):
    amount = Decimal()
    type = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['amount'],
            '@type': data['type']
        }


class SalesInvoiceProductLineSchema(RejectUnknownFieldsSchema):
    product_identifier = fields.String(attribute='identifier', default='')
    product_name = fields.String(attribute='name')
    product_unit_price = fields.Nested(UnitPriceSchema, attribute='unit_price')
    product_vat_percentage = fields.Nested(
        VatPercentageSchema,
        attribute='vat_percentage'
    )
    sales_invoice_product_line_quantity = Decimal(attribute='quantity')
    sales_invoice_product_line_discount_percentage = Decimal(
        attribute='discount_percentage'
    )
    accounting_account_suggestion = fields.String()

    class Meta:
        ordered = True

    def __setattr__(self, attr, value):
        if attr == 'ordered':
            value = True
        super(SalesInvoiceProductLineSchema, self).__setattr__(attr, value)

    @post_dump
    def post_dump(self, data):
        data['product_identifier'] = {
            '#text': data['product_identifier'],
            '@type': 'netvisor'
        }
        return data


class CreateSalesInvoiceSchema(RejectUnknownFieldsSchema):
    sales_invoice_number = fields.Integer(attibute='number')
    sales_invoice_date = fields.Date(attribute='date')
    sales_invoice_delivery_date = fields.Date(attribute='delivery_date')
    sales_invoice_reference_number = fields.String(
        attribute='reference_number'
    )
    sales_invoice_amount = Decimal(attribute='amount')
    seller_identifier = fields.String()
    seller_name = fields.String()
    invoice_type = fields.String()
    sales_invoice_status = fields.String(attribute='status')
    sales_invoice_free_text_before_lines = fields.String(
        attribute='free_text_before_lines'
    )
    sales_invoice_free_text_after_lines = fields.String(
        attribute='free_text_after_lines'
    )
    sales_invoice_our_reference = fields.String(attribute='our_reference')
    sales_invoice_your_reference = fields.String(attribute='your_reference')
    sales_invoice_private_comment = fields.String(attribute='private_comment')
    invoicing_customer_identifier = fields.String()
    invoicing_customer_name = fields.String()
    invoicing_customer_name_extension = fields.String()
    invoicing_customer_address_line = fields.String()
    invoicing_customer_additional_address_line = fields.String()
    invoicing_customer_post_number = fields.String()
    invoicing_customer_town = fields.String()
    invoicing_customer_country_code = fields.String()
    delivery_address_name = fields.String()
    delivery_address_name_extension = fields.String()
    delivery_address_line = fields.String()
    delivery_address_post_number = fields.String()
    delivery_address_town = fields.String()
    delivery_address_country_code = fields.String()
    delivery_method = fields.String()
    delivery_term = fields.String()
    payment_term_net_days = fields.Integer()
    payment_term_cash_discount_days = fields.Integer()
    payment_term_cash_discount = Decimal()
    invoice_lines = fields.List(
        fields.Nested(SalesInvoiceProductLineSchema),
        default=list
    )

    class Meta:
        ordered = True

    @post_dump
    def post_dump(self, data):
        if 'seller_identifier' in data:
            data['seller_identifier'] = {
                '#text': data['seller_identifier'],
                '@type': 'netvisor'
            }

        if 'sales_invoice_status' in data:
            data['sales_invoice_status'] = {
                '#text': data['sales_invoice_status'],
                '@type': 'netvisor'
            }

        if 'invoicing_customer_identifier' in data:
            data['invoicing_customer_identifier'] = {
                '#text': data['invoicing_customer_identifier'],
                '@type': 'netvisor'
            }

        if 'payment_term_cash_discount' in data:
            data['payment_term_cash_discount'] = {
                '#text': data['payment_term_cash_discount'],
                '@type': 'percentage'
            }

        data['invoice_lines'] = {
            'invoice_line': [
                {'sales_invoice_product_line': line}
                for line in data['invoice_lines']
            ]
        }
        return data
