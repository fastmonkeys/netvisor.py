# -*- coding: utf-8 -*-
"""
    netvisor.requests.sales_payment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..responses.sales_payments import SalesPaymentListResponse
from .base import Request


class SalesPaymentListRequest(Request):
    method = 'GET'
    uri = 'SalesPaymentList.nv'
    response_cls = SalesPaymentListResponse
