# -*- coding: utf-8 -*-
"""
    netvisor.services.sales_invoice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.sales_invoice import (
    GetSalesInvoiceRequest,
    SalesInvoiceListRequest
)


class SalesInvoiceService(Service):
    def get(self, id):
        request = GetSalesInvoiceRequest(self.client, NetvisorKey=id)
        return request.make_request()

    def list(self, above_id=None):
        request = SalesInvoiceListRequest(
            self.client,
            InvoicesAboveNetvisorKey=above_id
        )
        return request.make_request()
