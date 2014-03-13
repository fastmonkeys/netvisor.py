from .base import Request
from ..responses.sales_payments import SalesPaymentListResponse


class SalesPaymentListRequest(Request):
    method = 'GET'
    uri = 'SalesPaymentList.nv'
    response_cls = SalesPaymentListResponse
    resource_key = 'sales_payment_list'
