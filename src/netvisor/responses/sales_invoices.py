from ..postprocessors.sales_invoices import (
    get_sales_invoice_response_postprocessor,
    sales_invoice_list_response_postprocessor,
)
from .base import Response


class SalesInvoiceListResponse(Response):
    postprocessor = sales_invoice_list_response_postprocessor


class GetSalesInvoiceResponse(Response):
    postprocessor = get_sales_invoice_response_postprocessor
