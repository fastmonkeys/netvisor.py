# -*- coding: utf-8 -*-
import decimal

import pytest

from netvisor.schemas.customer import CustomerListSchema, GetCustomerSchema
from netvisor.responses.customers import (
    CustomerListResponse,
    GetCustomerResponse,
)
from .base import SchemaTestCase


class TestCustomerFromCustomerListResponse(SchemaTestCase):
    response_filename = 'CustomerList.xml'
    response_cls = CustomerListResponse
    schema_cls = CustomerListSchema

    def test_has_one_customer(self, data):
        assert len(data['objects']) == 2

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 165),
            ('name', 'Anni Asiakas'),
            ('code', 'AA'),
            ('business_code', '12345678-9'),
        ]
    )
    def test_customer_attributes(self, data, name, value):
        assert data['objects'][0][name] == value


class TestCustomerFromGetCustomerResponse(SchemaTestCase):
    response_filename = 'GetCustomer.xml'
    response_cls = GetCustomerResponse
    schema_cls = GetCustomerSchema

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('code', u'MM'),
            ('business_code', u'1234567-8'),
            ('name', u'Maija Mallikas'),
            ('name_extension', u'toimitusjohtaja'),
            ('phone', u'040 12157 988'),
            ('fax', u'(015) 123 4567'),
            ('email', u'maija.mallikas@netvisor.fi'),
            ('homepage', u'www.netvisor.fi'),
            ('comment', u'Great customer!'),
            ('reference_number', u'1070'),
            ('is_active', True),
            ('balance_limit', decimal.Decimal('200.3')),
        ]
    )
    def test_customer_attributes(self, data, name, value):
        assert data[name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', u'Pajukuja 2'),
            ('postal_code', u'53100'),
            ('post_office', u'Lappeenranta'),
            ('country', u'FI'),
        ]
    )
    def test_customer_street_address_attributes(self, data, name, value):
        assert data['street_address'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Matti'),
            ('street', u'Pajukuja 90'),
            ('postal_code', u'53100'),
            ('post_office', u'Lappeenranta'),
        ]
    )
    def test_customer_delivery_address_attributes(self, data, name, value):
        assert data['delivery_address'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('address', u'FI002316574613249'),
            ('router_code', 'PSPBFIHH'),
        ]
    )
    def test_customer_finvoice_attributes(self, data, name, value):
        assert data['finvoice'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Perttu'),
            ('email', u'perttu@netvisor.fi'),
            ('phone', u'040 21578 999'),
        ]
    )
    def test_customer_contact_person_attributes(self, data, name, value):
        assert data['contact_person'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('id', 1),
            ('name', u'Asiakasryhmä 1'),
        ]
    )
    def test_customer_group_attributes(self, data, name, value):
        assert data['group'][name] == value


class TestMinimalCustomerFromGetCustomerResponse(SchemaTestCase):
    response_filename = 'GetCustomerMinimal.xml'
    response_cls = GetCustomerResponse
    schema_cls = GetCustomerSchema

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('code', u''),
            ('business_code', u''),
            ('name', u'Maija Mallikas'),
            ('name_extension', u''),
            ('phone', u''),
            ('fax', u''),
            ('email', u''),
            ('homepage', u''),
            ('comment', u''),
            ('reference_number', u''),
            ('is_active', False),
            ('balance_limit', None),
        ]
    )
    def test_customer_attributes(self, data, name, value):
        assert data[name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', u''),
            ('postal_code', u''),
            ('post_office', u''),
            ('country', u'FI'),
        ]
    )
    def test_customer_street_address_attributes(self, data, name, value):
        assert data['street_address'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u''),
            ('street', u''),
            ('postal_code', u''),
            ('post_office', u''),
        ]
    )
    def test_customer_delivery_address_attributes(self, data, name, value):
        assert data['delivery_address'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('address', u''),
            ('router_code', u''),
        ]
    )
    def test_customer_finvoice_attributes(self, data, name, value):
        assert data['finvoice'][name] == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u''),
            ('email', u''),
            ('phone', u''),
        ]
    )
    def test_customer_contact_person_attributes(self, data, name, value):
        assert data['contact_person'][name] == value
