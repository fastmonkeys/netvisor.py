# -*- coding: utf-8 -*-
from datetime import date
import decimal

import pytest

from netvisor.schemas.sales_payment import SalesPaymentListSchema
from netvisor.responses.sales_payments import SalesPaymentListResponse
from .base import SchemaTestCase


class TestSalesPaymentFromSalesPaymentListResponse(SchemaTestCase):
    response_filename = 'SalesPaymentList.xml'
    response_cls = SalesPaymentListResponse
    schema_cls = SalesPaymentListSchema

    def test_has_one_sales_payment(self, data):
        assert len(data['objects']) == 2

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 165),
            ('name', u'Matti Mallikas'),
            ('date', date(2014, 2, 7)),
            ('amount', decimal.Decimal('249.90')),
            ('foreign_currency_amount', None),
            ('reference_number', u'1094'),
            ('invoice_number', 1),
        ]
    )
    def test_sales_payment_attributes(self, data, name, value):
        assert data['objects'][0][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('is_ok', False),
            ('error_code', u'ERROR_IN_DUE_DATE'),
            ('error_description', u'Eräpäivä virheellinen'),
        ]
    )
    def test_sales_payment_bank_status_attributes(self, data, name, value):
        assert data['objects'][0]['bank_status'][name] == value
