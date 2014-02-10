# -*- coding: utf-8 -*-
import io
import os

from netvisor.responses.sales_payments import SalesPaymentListResponse


def test_sales_payment_list_response(responses_dir):
    filename = os.path.join(responses_dir, 'SalesPaymentList.xml')
    with io.open(filename, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = SalesPaymentListResponse(xml)

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
