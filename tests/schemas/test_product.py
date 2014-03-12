# -*- coding: utf-8 -*-
import decimal

import pytest

from netvisor.schemas.product import GetProductSchema, ProductListSchema
from netvisor.responses.products import (
    GetProductResponse,
    ProductListResponse,
)
from .base import SchemaTestCase


class TestProductFromGetProductResponse(SchemaTestCase):
    response_filename = 'GetProduct.xml'
    response_cls = GetProductResponse
    schema_cls = GetProductSchema

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 165),
            ('code', u'CC'),
            ('group', u'Kirjat'),
            ('name', u'Code Complete'),
            ('description', u'Toinen painos'),
            ('unit_price', decimal.Decimal('42.5')),
            ('unit_price_type', u'brutto'),
            ('unit', u'kpl'),
            ('unit_weight', decimal.Decimal('0.2')),
            ('purchase_price', decimal.Decimal('25')),
            ('tariff_heading', u'Code Complete'),
            ('commission_percentage', decimal.Decimal('11')),
            ('is_active', True),
            ('is_sales_product', False),
            ('default_vat_percentage', decimal.Decimal('22')),
            ('default_domestic_account_number', u'3000'),
            ('default_eu_account_number', u'3360'),
            ('default_outside_eu_account_number', u'3380'),
        ]
    )
    def test_product_attributes(self, data, name, value):
        assert data[name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('amount', decimal.Decimal('2.00')),
            ('mid_price', decimal.Decimal('5.00')),
            ('ordered_amount', decimal.Decimal('0.00')),
            ('reserved_amount', decimal.Decimal('1.00')),
            ('value', decimal.Decimal('10.0000')),
        ]
    )
    def test_product_inventory_attributes(self, data, name, value):
        assert data['inventory'][name] == value


class TestProductFromMinimalGetProductResponse(SchemaTestCase):
    response_filename = 'GetProductMinimal.xml'
    response_cls = GetProductResponse
    schema_cls = GetProductSchema

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 165),
            ('code', u'CC'),
            ('group', u'Kirjat'),
            ('name', u'Code Complete'),
            ('description', u''),
            ('unit_price', decimal.Decimal('0')),
            ('unit_price_type', u'brutto'),
            ('unit', u''),
            ('unit_weight', None),
            ('purchase_price', decimal.Decimal('0')),
            ('tariff_heading', u''),
            ('commission_percentage', decimal.Decimal('0')),
            ('is_active', False),
            ('is_sales_product', True),
            ('default_vat_percentage', decimal.Decimal('0')),
            ('default_domestic_account_number', u'3000'),
            ('default_eu_account_number', u'3360'),
            ('default_outside_eu_account_number', u'3380'),
        ]
    )
    def test_product_attributes(self, data, name, value):
        assert data[name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('amount', decimal.Decimal('0')),
            ('mid_price', decimal.Decimal('0')),
            ('ordered_amount', decimal.Decimal('0')),
            ('reserved_amount', decimal.Decimal('0')),
            ('value', decimal.Decimal('0')),
        ]
    )
    def test_product_inventory_attributes(self, data, name, value):
        assert data['inventory'][name] == value


class TestProductFromProductListResponse(SchemaTestCase):
    response_filename = 'ProductList.xml'
    response_cls = ProductListResponse
    schema_cls = ProductListSchema

    def test_has_one_product(self, data):
        assert len(data['objects']) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 165),
            ('code', u'TT'),
            ('name', u'Testituote'),
            ('unit_price', decimal.Decimal('1.96')),
            ('unit_price_type', u'netto'),
        ]
    )
    def test_product_attributes(self, data, name, value):
        assert data['objects'][0][name] == value
