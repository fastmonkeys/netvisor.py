# -*- coding: utf-8 -*-
import decimal

import pytest

from netvisor.exc import InvalidData
from ..utils import get_response_content


class TestCustomerService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetCustomer.nv?id=5',
            body=get_response_content('GetCustomer.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        customer = netvisor.customers.get(5)
        assert customer == {
            'code': u'MM',
            'business_code': u'1234567-8',
            'name': u'Maija Mallikas',
            'name_extension': u'toimitusjohtaja',
            'group': {
                'id': 1,
                'name': u'Asiakasryhm\xe4 1'
            },
            'street_address': {
                'street': u'Pajukuja 2',
                'postal_code': u'53100',
                'post_office': u'Lappeenranta',
                'country': u'FI',
            },
            'phone': u'040 12157 988',
            'fax': u'(015) 123 4567',
            'email': u'maija.mallikas@netvisor.fi',
            'homepage': u'www.netvisor.fi',
            'finvoice': {
                'address': u'FI002316574613249',
                'router_code':  'PSPBFIHH'
            },
            'delivery_address': {
                'name': u'Matti',
                'street': u'Pajukuja 90',
                'postal_code': u'53100',
                'post_office': u'Lappeenranta',
            },
            'contact_person': {
                'name': u'Perttu',
                'email': u'perttu@netvisor.fi',
                'phone': u'040 21578 999',
            },
            'balance_limit': decimal.Decimal('200.3'),
            'is_active': True,
            'comment': u'Great customer!',
            'reference_number': u'1070'
        }

    def test_get_with_minimal_customer(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetCustomer.nv?id=5',
            body=get_response_content('GetCustomerMinimal.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        customer = netvisor.customers.get(5)
        assert customer == {
            'code': None,
            'business_code': None,
            'name': u'Maija Mallikas',
            'name_extension': None,
            'group': {
                'id': 1,
                'name': u'Asiakasryhm\xe4 1'
            },
            'phone': None,
            'fax': None,
            'email': None,
            'homepage': None,
            'comment': None,
            'reference_number': None,
            'is_active': False,
            'balance_limit': None,
            'street_address': {
                'street': None,
                'postal_code': None,
                'post_office': None,
                'country': u'FI',
            },
            'delivery_address': {
                'name': None,
                'street': None,
                'postal_code': None,
                'post_office': None,
            },
            'finvoice': {
                'address': None,
                'router_code': None,
            },
            'contact_person': {
                'name': None,
                'email': None,
                'phone': None,
            }
        }

    def test_get_raises_error_if_customer_not_found(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetCustomer.nv?id=123',
            body=get_response_content('GetCustomerNotFound.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.customers.get(123)

        assert str(excinfo.value) == (
            'Data form incorrect:. '
            'Customer not found with Netvisor identifier: 123'
        )

    def test_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/CustomerList.nv',
            body=get_response_content('CustomerList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        customers = netvisor.customers.list()
        assert customers == [
            {
                'id': 165,
                'name': u'Anni Asiakas',
                'code': u'AA',
                'business_code': u'12345678-9',
            },
            {
                'id': 166,
                'name': u'Matti Mallikas',
                'code': None,
                'business_code': None,
            }
        ]

    def test_list_with_query(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/CustomerList.nv?Keyword=anni',
            body=get_response_content('CustomerList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        customers = netvisor.customers.list(query=u'anni')
        assert customers == [
            {
                'id': 165,
                'name': u'Anni Asiakas',
                'code': u'AA',
                'business_code': u'12345678-9',
            },
            {
                'id': 166,
                'name': u'Matti Mallikas',
                'code': None,
                'business_code': None,
            }
        ]
