# -*- coding: utf-8 -*-
import decimal

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
                'name': u'',
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
                'country': u'',
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
                'code': u'',
                'business_code': u'',
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
                'code': u'',
                'business_code': u'',
            }
        ]
