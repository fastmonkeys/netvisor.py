# -*- coding: utf-8 -*-
"""
    netvisor.services.sales_payment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.sales_payment import SalesPaymentListRequest


class SalesPaymentService(Service):
    def list(self):
        request = SalesPaymentListRequest(self.client)
        return request.make_request()
