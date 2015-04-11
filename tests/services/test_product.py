# -*- coding: utf-8 -*-
import decimal

import pytest

from netvisor.exc import InvalidData

from ..utils import get_response_content


class TestProductService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetProduct.nv?id=5',
            body=get_response_content('GetProduct.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        product = netvisor.products.get(5)
        assert product == {
            'id': 165,
            'code': u'CC',
            'group': u'Kirjat',
            'name': u'Code Complete',
            'description': u'Toinen painos',
            'unit_price': decimal.Decimal('42.5'),
            'unit_price_type': u'brutto',
            'unit': u'kpl',
            'unit_weight': decimal.Decimal('0.2'),
            'purchase_price': decimal.Decimal('25'),
            'tariff_heading': u'Code Complete',
            'commission_percentage': decimal.Decimal('11'),
            'is_active': True,
            'is_sales_product': False,
            'default_vat_percentage': decimal.Decimal('22'),
            'default_domestic_account_number': u'3000',
            'default_eu_account_number': u'3360',
            'default_outside_eu_account_number': u'3380',
            'inventory': {
                'amount': decimal.Decimal('2.00'),
                'mid_price': decimal.Decimal('5.00'),
                'value': decimal.Decimal('10.0000'),
                'reserved_amount': decimal.Decimal('1.00'),
                'ordered_amount': decimal.Decimal('0.00'),
            }
        }

    def test_get_with_minimal_product(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetProduct.nv?id=165',
            body=get_response_content('GetProductMinimal.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        product = netvisor.products.get(165)
        assert product == {
            'id': 165,
            'code': u'CC',
            'group': u'Kirjat',
            'name': u'Code Complete',
            'description': None,
            'unit_price': decimal.Decimal('0'),
            'unit_price_type': u'brutto',
            'unit': None,
            'unit_weight': None,
            'purchase_price': decimal.Decimal('0'),
            'tariff_heading': None,
            'commission_percentage': decimal.Decimal('0'),
            'is_active': False,
            'is_sales_product': True,
            'default_vat_percentage': decimal.Decimal('0'),
            'default_domestic_account_number': u'3000',
            'default_eu_account_number': u'3360',
            'default_outside_eu_account_number': u'3380',
            'inventory': {
                'amount': decimal.Decimal('0'),
                'mid_price': decimal.Decimal('0'),
                'ordered_amount': decimal.Decimal('0'),
                'reserved_amount': decimal.Decimal('0'),
                'value': decimal.Decimal('0'),
            }
        }

    def test_get_raises_error_if_product_not_found(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetProduct.nv?id=123',
            body=get_response_content('GetProductNotFound.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.products.get(123)

        assert str(excinfo.value) == (
            'Data form incorrect:. '
            'Product not found with Netvisor identifier: 123'
        )

    def test_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/ProductList.nv',
            body=get_response_content('ProductList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        products = netvisor.products.list()
        assert products == [
            {
                'id': 165,
                'code': u'TT',
                'name': u'Testituote',
                'unit_price': decimal.Decimal('1.96'),
                'unit_price_type': u'netto',
            }
        ]
