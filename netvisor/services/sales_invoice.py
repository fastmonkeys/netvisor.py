# -*- coding: utf-8 -*-
"""
    netvisor.services.sales_invoice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.sales_invoice import (
    GetSalesInvoiceRequest,
    SalesInvoiceListRequest
)


class SalesInvoiceService(Service):
    def get(self, id):
        request = GetSalesInvoiceRequest(
            self.client,
            params={'NetvisorKey': id}
        )
        return request.make_request()

    def list(self, above_id=None, invoice_number=None):
        request = SalesInvoiceListRequest(
            self.client,
            params={
                'InvoicesAboveNetvisorKey': above_id,
                'InvoiceNumber': invoice_number
            }
        )
        return request.make_request()
