# -*- coding: utf-8 -*-
"""
    netvisor.responses.sales_invoices
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import GetSalesInvoiceSchema, SalesInvoiceListSchema
from .base import Response


class SalesInvoiceListResponse(Response):
    schema_cls = SalesInvoiceListSchema
    tag_name = 'sales_invoice_list'


class GetSalesInvoiceResponse(Response):
    schema_cls = GetSalesInvoiceSchema
    tag_name = 'sales_invoice'
