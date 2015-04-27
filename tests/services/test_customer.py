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
            'customer_base_information': {
                'internal_identifier': u'MM',
                'external_identifier': u'1234567-8',
                'customer_group_netvisor_key': 1,
                'customer_group_name': u'Asiakasryhm\xe4 1',
                'name': u'Maija Mallikas',
                'name_extension': u'toimitusjohtaja',
                'street_address': u'Pajukuja 2',
                'city': u'Lappeenranta',
                'post_number': u'53100',
                'country': u'FI',
                'phone_number': u'040 12157 988',
                'fax_number': u'(015) 123 4567',
                'email': u'maija.mallikas@netvisor.fi',
                'home_page_uri': u'www.netvisor.fi',
                'is_active': True,
            },
            'customer_finvoice_details': {
                'finvoice_address': u'FI002316574613249',
                'finvoice_router_code':  'PSPBFIHH',
            },
            'customer_delivery_details': {
                'delivery_name': u'Matti',
                'delivery_street_address': u'Pajukuja 90',
                'delivery_post_number': u'53100',
                'delivery_city': u'Lappeenranta',
            },
            'customer_contact_details': {
                'contact_person': u'Perttu',
                'contact_person_email': u'perttu@netvisor.fi',
                'contact_person_phone': u'040 21578 999',
            },
            'customer_additional_information': {
                'comment': u'Great customer!',
                'reference_number': u'1070',
                'balance_limit': decimal.Decimal('200.3'),
            }
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
            'customer_base_information': {
                'internal_identifier': None,
                'external_identifier': None,
                'customer_group_netvisor_key': 1,
                'customer_group_name': u'Asiakasryhm\xe4 1',
                'name': u'Maija Mallikas',
                'name_extension': None,
                'street_address': None,
                'city': None,
                'post_number': None,
                'country': u'FI',
                'phone_number': None,
                'fax_number': None,
                'email': None,
                'home_page_uri': None,
                'is_active': False,
            },
            'customer_finvoice_details': {
                'finvoice_address': None,
                'finvoice_router_code': None,
            },
            'customer_delivery_details': {
                'delivery_name': None,
                'delivery_street_address': None,
                'delivery_post_number': None,
                'delivery_city': None,
            },
            'customer_contact_details': {
                'contact_person': None,
                'contact_person_email': None,
                'contact_person_phone': None,
            },
            'customer_additional_information': {
                'comment': None,
                'reference_number': None,
                'balance_limit': None,
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
                'netvisor_key': 165,
                'name': u'Anni Asiakas',
                'code': u'AA',
                'organisation_identifier': u'12345678-9',
            },
            {
                'netvisor_key': 166,
                'name': u'Matti Mallikas',
                'code': None,
                'organisation_identifier': None,
            }
        ]

    def test_list_with_zero_customers(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/CustomerList.nv',
            body=get_response_content('CustomerListMinimal.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        customers = netvisor.customers.list()
        assert customers == []

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
                'netvisor_key': 165,
                'name': u'Anni Asiakas',
                'code': u'AA',
                'organisation_identifier': u'12345678-9',
            },
            {
                'netvisor_key': 166,
                'name': u'Matti Mallikas',
                'code': None,
                'organisation_identifier': None,
            }
        ]
