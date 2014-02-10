# -*- coding: utf-8 -*-
import io
import os

from netvisor.responses.sales_invoices import (
    SalesInvoiceListResponse,
    GetSalesInvoiceResponse,
)


def test_get_sales_invoice(responses_dir):
    filename = os.path.join(responses_dir, 'GetSalesInvoice.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = GetSalesInvoiceResponse(xml)

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


def test_sales_invoice_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'SalesInvoiceList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = SalesInvoiceListResponse(xml)

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
