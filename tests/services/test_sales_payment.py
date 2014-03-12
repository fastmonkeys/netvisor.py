# -*- coding: utf-8 -*-
from datetime import date
import decimal

from ..utils import get_response_content


class TestSalesPaymentService(object):
    def test_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/SalesPaymentList.nv',
            body=get_response_content('SalesPaymentList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        sales_payments = netvisor.sales_payments.list()
        assert sales_payments == [
            {
                'id': 165,
                'name': u'Matti Mallikas',
                'date': date(2014, 2, 7),
                'amount': decimal.Decimal('249.90'),
                'foreign_currency_amount': None,
                'reference_number': u'1094',
                'invoice_number': 1,
                'bank_status': {
                    'is_ok': False,
                    'error_code': u'ERROR_IN_DUE_DATE',
                    'error_description': u'Eräpäivä virheellinen'
                }
            },
            {
                'id': 166,
                'name': u'Assi Asiakas',
                'date': date(2014, 3, 10),
                'amount': decimal.Decimal('200'),
                'foreign_currency_amount': None,
                'reference_number': u'1106',
                'invoice_number': 2,
                'bank_status': {
                    'is_ok': True,
                    'error_code': u'',
                    'error_description': u'',
                }
            }
        ]
