# -*- coding: utf-8 -*-
from datetime import date
import decimal

from ..utils import get_response_content


class TestOrderService(object):
    def test_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url=(
                'http://koulutus.netvisor.fi/SalesInvoiceList.nv?'
                'ListType=preinvoice'
            ),
            body=get_response_content('SalesInvoiceListPreinvoice.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        orders = netvisor.orders.list()
        assert orders == [
            {
                'id': 165,
                'number': 5,
                'date': date(2013, 11, 9),
                'status': u'open',
                'substatus': None,
                'reference_number': u'1070',
                'amount': decimal.Decimal('123.45'),
                'open_amount': decimal.Decimal('45.67'),
            }
        ]
