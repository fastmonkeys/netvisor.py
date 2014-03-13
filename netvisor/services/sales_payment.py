from .base import Service
from ..requests.sales_payment import SalesPaymentListRequest


class SalesPaymentService(Service):
    def list(self):
        request = SalesPaymentListRequest(self.client)
        return request.make_request()
