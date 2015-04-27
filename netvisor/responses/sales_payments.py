# -*- coding: utf-8 -*-
"""
    netvisor.responses.sales_payments
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import SalesPaymentListSchema
from .base import Response


class SalesPaymentListResponse(Response):
    schema_cls = SalesPaymentListSchema
    tag_name = 'sales_payment_list'
