from ..transformers.sales_invoices import (
    get_sales_invoice_response_transformer,
    sales_invoice_list_response_transformer,
)
from .base import Response


class SalesInvoiceListResponse(Response):
    transformer = sales_invoice_list_response_transformer


class GetSalesInvoiceResponse(Response):
    transformer = get_sales_invoice_response_transformer
