# -*- coding: utf-8 -*-
from datetime import date
import decimal
import io
import os

import pytest

from netvisor import models, responses


class ModelFromResponseTestCase(object):
    @pytest.fixture
    def xml(self, responses_dir):
        filename = os.path.join(responses_dir, self.response_filename)
        with io.open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    @pytest.fixture
    def data(self, xml):
        response = self.response_cls(xml)
        return response.parse()


class TestCompanyFromGetCompanyInformationResponse(ModelFromResponseTestCase):
    response_cls = responses.GetCompanyInformationResponse
    response_filename = 'GetCompanyInformation.xml'

    @pytest.fixture
    def company(self, data):
        company = models.Company()
        company.import_data(data)
        return company

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
            ('current_special_status', None),
            ('domicile', u'Helsinki'),
            ('activity_description', u'Kebab'),
            ('email', u'info@generalmotors.fi'),
            ('phone', u'020 1234567'),
            ('fax', u'(09) 5551234'),
        ]
    )
    def test_company_attributes(self, company, name, value):
        assert getattr(company, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', u'Esimerkkikatu 123'),
            ('postal_code', u'00100'),
            ('post_office', u'Helsinki'),
        ]
    )
    def test_company_street_address_attributes(self, company, name, value):
        assert getattr(company.street_address, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', None),
            ('postal_code', u'00002'),
            ('post_office', u'Helsinki'),
        ]
    )
    def test_company_postal_address_attributes(self, company, name, value):
        assert getattr(company.postal_address, name) == value

    def test_number_of_registered_names(self, company):
        assert len(company.registered_names) == 1

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
    def test_registered_name_attributes(self, company, name, value):
        assert getattr(company.registered_names[0], name) == value

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
    def test_company_stats_attributes(self, company, name, value):
        assert getattr(company.stats, name) == value

    def test_number_of_registered_person_roles(self, company):
        assert len(company.registered_person_roles) == 1

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
    def test_registered_person_role_attributes(self, company, name, value):
        assert getattr(company.registered_person_roles[0], name) == value


class TestCompanyFromCompanyListResponse(ModelFromResponseTestCase):
    response_cls = responses.CompanyListResponse
    response_filename = 'CompanyList.xml'

    @pytest.fixture
    def company(self, data):
        company = models.Company()
        company.import_data(data['companies'][0])
        return company

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'ACME'),
            ('business_code', u'1234567-8'),
            ('is_active', True),
        ]
    )
    def test_company_attributes(self, company, name, value):
        assert getattr(company, name) == value


class TestCustomerFromCustomerListResponse(ModelFromResponseTestCase):
    response_cls = responses.CustomerListResponse
    response_filename = 'CustomerList.xml'

    @pytest.fixture
    def customer(self, data):
        customer = models.Customer()
        customer.import_data(data['customers'][0])
        return customer

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('netvisor_key', 165),
            ('name', 'Anni Asiakas'),
            ('code', 'AA'),
            ('business_code', '12345678-9'),
        ]
    )
    def test_customer_attributes(self, customer, name, value):
        assert getattr(customer, name) == value


class TestCustomerFromGetCustomerResponse(ModelFromResponseTestCase):
    response_cls = responses.GetCustomerResponse
    response_filename = 'GetCustomer.xml'

    @pytest.fixture
    def customer(self, data):
        customer = models.Customer()
        customer.import_data(data)
        return customer

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('code', u'MM'),
            ('business_code', None),
            ('name', u'Maija Mallikas'),
            ('name_extension', None),
            ('phone', u'040 12157 988'),
            ('fax', None),
            ('email', u'maija.mallikas@netvisor.fi'),
            ('homepage', u'www.netvisor.fi'),
            ('comment', None),
            ('reference_number', u'1070'),
        ]
    )
    def test_customer_attributes(self, customer, name, value):
        assert getattr(customer, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('street', u'Pajukuja 2'),
            ('postal_code', u'53100'),
            ('post_office', u'Lappeenranta'),
            ('country', u'AF'),
        ]
    )
    def test_customer_street_address_attributes(self, customer, name, value):
        assert getattr(customer.street_address, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Matti'),
            ('street', u'Pajukuja 90'),
            ('postal_code', u'53100'),
            ('post_office', u'Lappeenranta'),
        ]
    )
    def test_customer_delivery_address_attributes(self, customer, name, value):
        assert getattr(customer.delivery_address, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('address', u'FI002316574613249'),
            ('router_code', 'PSPBFIHH'),
        ]
    )
    def test_customer_finvoice_attributes(self, customer, name, value):
        assert getattr(customer.finvoice, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Perttu'),
            ('email', None),
            ('phone', u'040 21578 999'),
        ]
    )
    def test_customer_contact_person_attributes(self, customer, name, value):
        assert getattr(customer.contact_person, name) == value


class TestProductFromGetProductResponse(ModelFromResponseTestCase):
    response_cls = responses.GetProductResponse
    response_filename = 'GetProduct.xml'

    @pytest.fixture
    def product(self, data):
        product = models.Product()
        product.import_data(data)

        return product

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('netvisor_key', 165),
            ('code', u'CC'),
            ('group', u'Kirjat'),
            ('name', u'Code Complete'),
            ('description', u'Toinen painos'),
            ('unit_price', decimal.Decimal('42.5')),
            ('unit_price_type', u'brutto'),
            ('unit', u'kpl'),
            ('unit_weight', decimal.Decimal('1')),
            ('purchase_price', decimal.Decimal('25')),
            ('tariff_heading', u'Code Complete'),
            ('commission_percentage', decimal.Decimal('11')),
            ('is_active', True),
            ('is_sales_product', False),
            ('default_vat_percentage', decimal.Decimal('22')),
            ('default_domestic_account_number', None),
            ('default_eu_account_number', None),
            ('default_outside_eu_account_number', None),
        ]
    )
    def test_product_attributes(self, product, name, value):
        assert getattr(product, name) == value


class TestProductFromProductListResponse(ModelFromResponseTestCase):
    response_cls = responses.ProductListResponse
    response_filename = 'ProductList.xml'

    @pytest.fixture
    def product(self, data):
        product = models.Product()
        product.import_data(data['products'][0])

        return product

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('netvisor_key', 165),
            ('code', u'TT'),
            ('name', u'Testituote'),
            ('unit_price', decimal.Decimal('1.96')),
            ('unit_price_type', u'netto'),
        ]
    )
    def test_product_attributes(self, product, name, value):
        assert getattr(product, name) == value


class TestSalesInvoiceFromGetSalesInvoiceResponse(ModelFromResponseTestCase):
    response_cls = responses.GetSalesInvoiceResponse
    response_filename = 'GetSalesInvoice.xml'

    @pytest.fixture
    def sales_invoice(self, data):
        sales_invoice = models.SalesInvoice()
        sales_invoice.import_data(data)
        return sales_invoice

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('number', 3),
            ('date', date(2012, 1, 27)),
            ('delivery_date', date(2012, 1, 27)),
            ('due_date', date(2012, 2, 11)),
            ('reference_number', u'1070'),
            ('amount', decimal.Decimal('244.00')),
            ('seller', u'Jarmo'),
            ('status', u'Unsent'),
            ('free_text_before_lines', None),
            ('free_text_after_lines', None),
            ('our_reference', None),
            ('your_reference', None),
            ('private_comment', None),
            ('match_partial_payments_by_default', False),
            ('delivery_method', None),
            ('delivery_term', None),
            ('payment_term_net_days', 14),
            ('payment_term_cash_discount_days', 5),
            ('payment_term_cash_discount', decimal.Decimal(9)),
        ]
    )
    def test_sales_invoice_attributes(self, sales_invoice, name, value):
        assert getattr(sales_invoice, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Matti Mallikas'),
            ('street', u'Pajukuja 1'),
            ('postal_code', u'53100'),
            ('post_office', u'Lappeenranta'),
            ('country', u'FINLAND'),
        ]
    )
    def test_sales_invoice_billing_address_attributes(
        self, sales_invoice, name, value
    ):
        assert getattr(sales_invoice.billing_address, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('name', u'Netvisor Oy'),
            ('street', u'Snelmanninkatu 12'),
            ('postal_code', u'53100'),
            ('post_office', u'LPR'),
            ('country', u'FINLAND'),
        ]
    )
    def test_sales_invoice_delivery_address_attributes(
        self, sales_invoice, name, value
    ):
        assert getattr(sales_invoice.delivery_address, name) == value

    def test_number_of_lines(self, sales_invoice):
        assert len(sales_invoice.lines) == 1

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('product_code', u'PELSU'),
            ('name', u'Omena'),
            ('free_text', None),
            ('quantity', decimal.Decimal('2')),
            ('unit_price', decimal.Decimal('6.9000')),
            ('discount_percentage', decimal.Decimal('0')),
            ('vat_percentage', decimal.Decimal('22')),
            ('vat_code', u'KOMY'),
            ('vat_amount', decimal.Decimal('3.04')),
            ('amount', decimal.Decimal('16.84')),
            ('accounting_suggestion', u'551'),
        ]
    )
    def test_sales_invoice_line_attributes(self, sales_invoice, name, value):
        assert getattr(sales_invoice.lines[0], name) == value


class TestSalesInvoiceFromSalesInvoiceListResponse(ModelFromResponseTestCase):
    response_cls = responses.SalesInvoiceListResponse
    response_filename = 'SalesInvoiceList.xml'

    @pytest.fixture
    def sales_invoice(self, data):
        sales_invoice = models.SalesInvoice()
        sales_invoice.import_data(data['sales_invoices'][0])
        return sales_invoice

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('netvisor_key', 165),
            ('number', 5),
            ('date', date(2013, 11, 9)),
            ('status', u'open'),
            ('substatus', u'overdue'),
            ('reference_number', u'1070'),
            ('amount', decimal.Decimal('123.45')),
            ('open_amount', decimal.Decimal('45.67')),
        ]
    )
    def test_sales_invoice_attributes(self, sales_invoice, name, value):
        assert getattr(sales_invoice, name) == value


class TestSalesPaymentFromSalesPaymentListResponse(ModelFromResponseTestCase):
    response_cls = responses.SalesPaymentListResponse
    response_filename = 'SalesPaymentList.xml'

    @pytest.fixture
    def sales_payment(self, data):
        sales_payment = models.SalesPayment()
        sales_payment.import_data(data['sales_payments'][0])

        return sales_payment

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('netvisor_key', 165),
            ('name', u'Matti Mallikas'),
            ('date', date(2014, 2, 7)),
            ('amount', decimal.Decimal('250')),
            ('foreign_currency_amount', None),
            ('reference_number', u'1094'),
            ('invoice_number', 1),
        ]
    )
    def test_sales_payment_attributes(self, sales_payment, name, value):
        assert getattr(sales_payment, name) == value

    @pytest.mark.parametrize(
        ('name', 'value'),
        [
            ('is_ok', False),
            ('error_code', u'ERROR_IN_DUE_DATE'),
            ('error_description', u'Eräpäivä virheellinen'),
        ]
    )
    def test_sales_payment_bank_status_attributes(
        self, sales_payment, name, value
    ):
        assert getattr(sales_payment.bank_status, name) == value
