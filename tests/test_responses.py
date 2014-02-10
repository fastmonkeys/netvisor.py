# -*- coding: utf-8 -*-
import io
import os

from netvisor import responses


def test_company_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'CompanyList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.CompanyListResponse(xml)

    assert response.parse() == {
        'companies': [
            {
                'is_active': u'1',
                'name': u'ACME',
                'business_code': u'1234567-8'
            }
        ]
    }


def test_customer_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'CustomerList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.CustomerListResponse(xml)

    assert response.parse() == {
        'customers': [
            {
                'netvisor_key': u'165',
                'name': u'Anni Asiakas',
                'code': u'AA',
                'business_code': u'12345678-9',
            }
        ]
    }


def test_get_company_information_response(responses_dir):
    filename = os.path.join(responses_dir, 'GetCompanyInformation.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.GetCompanyInformationResponse(xml)

    assert response.parse() == {
        'name': u'General Motors Finland',
        'business_code': u'1234567-8',
        'type': u'Osakeyhtiö',
        'responsible_person_authorization_rule': (
            u'Yhteisösääntöjen mukaan toiminimen kirjoittavat hallituksen '
            u'puheenjohtaja, toimitusjohtaja ja toimitusjohtajan sijainen '
            u'kukin yksin.'
        ),
        'established_date': u'2009-12-31',
        'terminated_date': u'2009-12-31',
        'most_recent_change_date': u'2009-12-31',
        'current_activity_status': u'active',
        'current_special_status': None,
        'domicile': u'Helsinki',
        'activity_description': u'Kebab',
        'street_address': {
            'street': u'Esimerkkikatu 123',
            'postal_code': u'00100',
            'post_office': u'Helsinki',
        },
        'postal_address': {
            'street': None,
            'postal_code': u'00002',
            'post_office': u'Helsinki',
        },
        'email': u'info@generalmotors.fi',
        'phone': u'020 1234567',
        'fax': u'(09) 5551234',
        'registered_person_roles': [
            {
                'nationality': u'FI',
                'identifier': u'Toimitusjohtaja',
                'type': u'Yhtiön muu johto',
                'established_date': u'2009-12-31',
                'name': u'Gunnar Peterson',
            }
        ],
        'registered_names': [
            {
                'established_date': u'2009-12-31',
                'terminated_date': u'2009-12-31',
                'type': u'Päätoiminimi',
                'name': u'Pekan yritys Oy',
                'current_activity_status': u'active'
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


def test_get_customer_response(responses_dir):
    filename = os.path.join(responses_dir, 'GetCustomer.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.GetCustomerResponse(xml)
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


def test_get_product_response(responses_dir):
    filename = os.path.join(responses_dir, 'GetProduct.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.GetProductResponse(xml)
    assert response.parse() == {
        'netvisor_key': u'165',
        'code': u'CC',
        'group': u'Kirjat',
        'name': u'Code Complete',
        'description': u'Toinen painos',
        'unit_price': u'42,5',
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
            'amount': u'2,00',
            'mid_price': u'5,00',
            'value': u'10,0000',
            'reserved_amount': u'1,00',
            'ordered_amount': u'0,00',
        }
    }


def test_get_sales_invoice(responses_dir):
    filename = os.path.join(responses_dir, 'GetSalesInvoice.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.GetSalesInvoiceResponse(xml)

    assert response.parse() == {
        'number': u'3',
        'date': u'2012-01-27',
        'delivery_date': u'2012-01-27',
        'due_date': u'2012-02-11',
        'reference_number': u'1070',
        'amount': u'244,00',
        'seller': u'Jarmo',
        'status': u'Unsent',
        'free_text_before_lines': None,
        'free_text_after_lines': None,
        'our_reference': None,
        'your_reference': None,
        'private_comment': None,
        'billing_address': {
            'name': u'Matti Mallikas',
            'street': u'Pajukuja 1',
            'postal_code': u'53100',
            'post_office': u'Lappeenranta',
            'country': u'FINLAND',
        },
        'match_partial_payments_by_default': u'No',
        'delivery_address': {
            'name': u'Netvisor Oy',
            'street': u'Snelmanninkatu 12',
            'postal_code': u'53100',
            'post_office': u'LPR',
            'country': u'FINLAND',
        },
        'delivery_method': None,
        'delivery_term': None,
        'payment_term_net_days': u'14',
        'payment_term_cash_discount_days': u'5',
        'payment_term_cash_discount': u'9',
        'lines': [
            {
                'product_code': u'PELSU',
                'name': u'Omena',
                'free_text': None,
                'quantity': u'2',
                'unit_price': u'6,9000',
                'discount_percentage': u'0',
                'vat_percentage': u'22',
                'vat_code': u'KOMY',
                'vat_amount': u'3,04',
                'amount': u'16,84',
                'accounting_suggestion': u'551',
            },
        ]
    }


def test_product_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'ProductList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.ProductListResponse(xml)
    assert response.parse() == {
        'products': [
            {
                'netvisor_key': u'165',
                'code': u'TT',
                'name': u'Testituote',
                'unit_price': u'1,96',
            }
        ]
    }


def test_sales_invoice_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'SalesInvoiceList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.SalesInvoiceListResponse(xml)

    assert response.parse() == {
        'sales_invoices': [
            {
                'netvisor_key': u'165',
                'number': u'5',
                'date': u'2013-11-09',
                'status': u'open',
                'substatus': u'overdue',
                'reference_number': u'1070',
                'amount': u'123,45',
                'open_amount': u'45,67',
            }
        ]
    }


def test_sales_payment_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'SalesPaymentList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = responses.SalesPaymentListResponse(xml)

    assert response.parse() == {
        'sales_payments': [
            {
                'netvisor_key': u'165',
                'name': u'Matti Mallikas',
                'date': u'7.2.2014',
                'amount': u'250',
                'foreign_currency_amount': None,
                'reference_number': u'1094',
                'invoice_number': u'1',
                'bank_status': {
                    'status': 'FAILED',
                    'error_code': u'ERROR_IN_DUE_DATE',
                    'error_description': u'Eräpäivä virheellinen'
                }
            }
        ]
    }
