# -*- coding: utf-8 -*-
from datetime import date

import pytest

from netvisor.schemas.company import (
    CompanyListSchema,
    GetCompanyInformationSchema,
)
from netvisor.responses.companies import (
    CompanyListResponse,
    GetCompanyInformationResponse,
)
from .base import SchemaTestCase


class TestCompanyFromGetCompanyInformationResponse(SchemaTestCase):
    response_filename = 'GetCompanyInformation.xml'
    response_cls = GetCompanyInformationResponse
    schema_cls = GetCompanyInformationSchema

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'General Motors Finland'),
            ('business_code', u'1234567-8'),
            ('type', u'Osakeyhtiö'),
            (
                'responsible_person_authorization_rule',
                u'Yhteisösääntöjen mukaan toiminimen kirjoittavat hallituksen '
                u'puheenjohtaja, toimitusjohtaja ja toimitusjohtajan sijainen '
                u'kukin yksin.'
            ),
            ('established_date', date(2009, 12, 31)),
            ('terminated_date', date(2009, 12, 31)),
            ('most_recent_change_date', date(2009, 12, 31)),
            ('is_active', True),
            ('current_special_status', u''),
            ('domicile', u'Helsinki'),
            ('activity_description', u'Kebab'),
            ('email', u'info@generalmotors.fi'),
            ('phone', u'020 1234567'),
            ('fax', u'(09) 5551234'),
        ]
    )
    def test_company_attributes(self, data, name, value):
        assert data[name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', u'Esimerkkikatu 123'),
            ('postal_code', u'00100'),
            ('post_office', u'Helsinki'),
        ]
    )
    def test_company_street_address_attributes(self, data, name, value):
        assert data['street_address'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', u''),
            ('postal_code', u'00002'),
            ('post_office', u'Helsinki'),
        ]
    )
    def test_company_postal_address_attributes(self, data, name, value):
        assert data['postal_address'][name] == value

    def test_number_of_registered_names(self, data):
        assert len(data['registered_names']) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('established_date', date(2009, 12, 31)),
            ('terminated_date', date(2009, 12, 31)),
            ('type', u'Päätoiminimi'),
            ('name', u'Pekan yritys Oy'),
            ('is_active', True),
        ]
    )
    def test_registered_name_attributes(self, data, name, value):
        assert data['registered_names'][0][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('employer_register_status', u'never_registered'),
            ('revenue_size', u'100-200'),
            ('staff_size', u'4-9'),
            ('vat_register_status', u'currently_registered'),
            ('standard_industrial_classification2008', u'Kaivostoiminta'),
            ('tax_prepayment_register_status', u'previously_registered'),
        ]
    )
    def test_company_stats_attributes(self, data, name, value):
        assert data['stats'][name] == value

    def test_number_of_registered_person_roles(self, data):
        assert len(data['registered_person_roles']) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('nationality', u'FI'),
            ('identifier', u'Toimitusjohtaja'),
            ('type', u'Yhtiön muu johto'),
            ('established_date', date(2009, 12, 31)),
            ('name', u'Gunnar Peterson'),
        ]
    )
    def test_registered_person_role_attributes(self, data, name, value):
        assert data['registered_person_roles'][0][name] == value


class TestCompanyFromCompanyListResponse(SchemaTestCase):
    response_filename = 'CompanyList.xml'
    response_cls = CompanyListResponse
    schema_cls = CompanyListSchema

    def test_has_one_company(self, data):
        assert len(data['objects']) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'ACME'),
            ('business_code', u'1234567-8'),
            ('is_active', True),
        ]
    )
    def test_company_attributes(self, data, name, value):
        assert data['objects'][0][name] == value
