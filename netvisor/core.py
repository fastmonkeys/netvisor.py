from .auth import NetvisorAuth
from .client import Client
from .services import (
    CompanyService,
    CustomerService,
    OrderService,
    ProductService,
    SalesInvoiceService,
    SalesPaymentService,
)


class Netvisor(object):
    def __init__(self, host, **kwargs):
        self._client = self._make_client(host, **kwargs)
        self._init_services()

    def _make_client(self, host, **kwargs):
        auth = NetvisorAuth(**kwargs)
        return Client(host, auth)

    def _init_services(self):
        self.companies = CompanyService(self._client)
        self.customers = CustomerService(self._client)
        self.orders = OrderService(self._client)
        self.products = ProductService(self._client)
        self.sales_invoices = SalesInvoiceService(self._client)
        self.sales_payments = SalesPaymentService(self._client)
