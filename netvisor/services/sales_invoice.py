from .base import Service
from ..requests.sales_invoice import (
    GetSalesInvoiceRequest,
    SalesInvoiceListRequest
)


class SalesInvoiceService(Service):
    def get(self, id):
        request = GetSalesInvoiceRequest(self.client, NetvisorKey=id)
        return request.make_request()

    def list(self):
        request = SalesInvoiceListRequest(self.client)
        return request.make_request()
