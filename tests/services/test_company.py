# -*- coding: utf-8 -*-
from datetime import date

from ..utils import get_response_content


class TestCompanyService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url=(
                'http://koulutus.netvisor.fi/GetCompanyInformation.nv?'
                'OrganizationIdentifier=1234567-8'
            ),
            body=get_response_content('GetCompanyInformation.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        company = netvisor.companies.get('1234567-8')
        assert company == {
            'name': u'General Motors Finland',
            'business_code': u'1234567-8',
            'type': u'Osakeyhtiö',
            'responsible_person_authorization_rule': (
                u'Yhteisösääntöjen mukaan toiminimen kirjoittavat hallituksen '
                u'puheenjohtaja, toimitusjohtaja ja toimitusjohtajan sijainen '
                u'kukin yksin.'
            ),
            'established_date': date(2009, 12, 31),
            'terminated_date': date(2009, 12, 31),
            'most_recent_change_date': date(2009, 12, 31),
            'is_active': True,
            'current_special_status': u'',
            'domicile': u'Helsinki',
            'activity_description': u'Kebab',
            'street_address': {
                'name': u'',
                'street': u'Esimerkkikatu 123',
                'postal_code': u'00100',
                'post_office': u'Helsinki',
                'country': u'',
            },
            'postal_address': {
                'name': u'',
                'street': u'',
                'postal_code': u'00002',
                'post_office': u'Helsinki',
                'country': u'',
            },
            'email': u'info@generalmotors.fi',
            'phone': u'020 1234567',
            'fax': u'(09) 5551234',
            'registered_person_roles': [
                {
                    'nationality': u'FI',
                    'identifier': u'Toimitusjohtaja',
                    'type': u'Yhtiön muu johto',
                    'established_date': date(2009, 12, 31),
                    'name': u'Gunnar Peterson',
                }
            ],
            'registered_names': [
                {
                    'established_date': date(2009, 12, 31),
                    'terminated_date': date(2009, 12, 31),
                    'type': u'Päätoiminimi',
                    'name': u'Pekan yritys Oy',
                    'is_active': True
                }
            ],
            'stats': {
                'employer_register_status': u'never_registered',
                'revenue_size': u'100-200',
                'staff_size': u'4-9',
                'vat_register_status': u'currently_registered',
                'standard_industrial_classification2008': u'Kaivostoiminta',
                'tax_prepayment_register_status': u'previously_registered',
            }
        }

    def test_list_with_query(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/CompanyList.nv?QueryTerm=acme',
            body=get_response_content('CompanyList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        companies = netvisor.companies.list(query=u'acme')
        assert companies == [
            {
                'is_active': True,
                'name': u'ACME',
                'business_code': u'1234567-8'
            }
        ]
