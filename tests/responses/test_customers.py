# -*- coding: utf-8 -*-
from netvisor.responses.customers import (
    CustomerListResponse,
    GetCustomerResponse,
)
from ..utils import get_response_text


def test_customer_list_response():
    xml = get_response_text('CustomerList.xml')
    response = CustomerListResponse(xml)

    assert response.parse() == {
        'objects': [
            {
                'id': u'165',
                'name': u'Anni Asiakas',
                'code': u'AA',
                'business_code': u'12345678-9',
            }
        ]
    }


def test_get_customer_response():
    xml = get_response_text('GetCustomer.xml')
    response = GetCustomerResponse(xml)
    assert response.parse() == {
        'code': u'MM',
        'business_code': None,
        'name': u'Maija Mallikas',
        'name_extension': None,
        'street_address': {
            'street': u'Pajukuja 2',
            'postal_code': u'53100',
            'post_office': u'Lappeenranta',
            'country': u'AF',
        },
        'phone': u'040 12157 988',
        'fax': None,
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
            'email': None,
            'phone': u'040 21578 999',
        },
        'comment': None,
        'reference_number': u'1070'
    }
