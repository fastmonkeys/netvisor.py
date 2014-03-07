# -*- coding: utf-8 -*-
import io
import os

from netvisor.responses.products import (
    ProductListResponse,
    GetProductResponse,
)


def test_get_product_response(responses_dir):
    filename = os.path.join(responses_dir, 'GetProduct.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = GetProductResponse(xml)
    assert response.parse() == {
        'netvisor_key': u'165',
        'code': u'CC',
        'group': u'Kirjat',
        'name': u'Code Complete',
        'description': u'Toinen painos',
        'unit_price': u'42.5',
        'unit_price_type': u'brutto',
        'unit': u'kpl',
        'unit_weight': u'1',
        'purchase_price': u'25',
        'tariff_heading': u'Code Complete',
        'commission_percentage': u'11',
        'is_active': u'1',
        'is_sales_product': u'0',
        'default_vat_percentage': u'22',
        'default_domestic_account_number': None,
        'default_eu_account_number': None,
        'default_outside_eu_account_number': None,
        'inventory': {
            'amount': u'2.00',
            'mid_price': u'5.00',
            'value': u'10.0000',
            'reserved_amount': u'1.00',
            'ordered_amount': u'0.00',
        }
    }


def test_product_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'ProductList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = ProductListResponse(xml)
    assert response.parse() == {
        'products': [
            {
                'netvisor_key': u'165',
                'code': u'TT',
                'name': u'Testituote',
                'unit_price': u'1.96',
            }
        ]
    }
