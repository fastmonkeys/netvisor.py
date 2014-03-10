# -*- coding: utf-8 -*-
from datetime import date
import decimal

import pytest

from netvisor.schemas.sales_invoice import (
    GetSalesInvoiceSchema,
    SalesInvoiceListSchema,
)
from netvisor.responses.sales_invoices import (
    GetSalesInvoiceResponse,
    SalesInvoiceListResponse,
)
from .base import SchemaTestCase


class TestSalesInvoiceFromGetSalesInvoiceResponse(SchemaTestCase):
    response_filename = 'GetSalesInvoice.xml'
    response_cls = GetSalesInvoiceResponse
    schema_cls = GetSalesInvoiceSchema

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('number', 3),
            ('date', date(2012, 1, 27)),
            ('delivery_date', date(2012, 1, 27)),
            ('due_date', date(2012, 2, 11)),
            ('reference_number', u'1070'),
            ('amount', decimal.Decimal('244.00')),
            ('seller', u'Jarmo'),
            ('status', u'Unsent'),
            ('free_text_before_lines', u''),
            ('free_text_after_lines', u''),
            ('our_reference', u''),
            ('your_reference', u''),
            ('private_comment', u''),
            ('match_partial_payments_by_default', False),
            ('delivery_method', u''),
            ('delivery_term', u''),
            ('payment_term_net_days', 14),
            ('payment_term_cash_discount_days', 5),
            ('payment_term_cash_discount', decimal.Decimal(9)),
        ]
    )
    def test_sales_invoice_attributes(self, data, name, value):
        assert data[name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Matti Mallikas'),
            ('street', u'Pajukuja 1'),
            ('postal_code', u'53100'),
            ('post_office', u'Lappeenranta'),
            ('country', u'FINLAND'),
        ]
    )
    def test_sales_invoice_billing_address_attributes(self, data, name, value):
        assert data['billing_address'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Netvisor Oy'),
            ('street', u'Snelmanninkatu 12'),
            ('postal_code', u'53100'),
            ('post_office', u'LPR'),
            ('country', u'FINLAND'),
        ]
    )
    def test_sales_invoice_delivery_address_attributes(
        self, data, name, value
    ):
        assert data['delivery_address'][name] == value

    def test_number_of_lines(self, data):
        assert len(data['lines']) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('product_code', u'PELSU'),
            ('name', u'Omena'),
            ('free_text', u''),
            ('quantity', decimal.Decimal('2')),
            ('unit_price', decimal.Decimal('6.9000')),
            ('discount_percentage', decimal.Decimal('0')),
            ('vat_percentage', decimal.Decimal('22')),
            ('vat_code', u'KOMY'),
            ('vat_amount', decimal.Decimal('3.04')),
            ('amount', decimal.Decimal('16.84')),
            ('accounting_suggestion', u'551'),
        ]
    )
    def test_sales_invoice_line_attributes(self, data, name, value):
        assert data['lines'][0][name] == value


class TestSalesInvoiceFromSalesInvoiceListResponse(SchemaTestCase):
    response_filename = 'SalesInvoiceList.xml'
    response_cls = SalesInvoiceListResponse
    schema_cls = SalesInvoiceListSchema

    def test_has_one_sales_invoice(self, data):
        assert len(data['objects']) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 165),
            ('number', 5),
            ('date', date(2013, 11, 9)),
            ('status', u'open'),
            ('substatus', u'overdue'),
            ('reference_number', u'1070'),
            ('amount', decimal.Decimal('123.45')),
            ('open_amount', decimal.Decimal('45.67')),
        ]
    )
    def test_sales_invoice_attributes(self, data, name, value):
        assert data['objects'][0][name] == value
