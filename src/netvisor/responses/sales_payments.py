from ..postprocessors.sales_payments import (
    sales_payment_list_response_postprocessor,
)
from .base import Response


class SalesPaymentListResponse(Response):
    postprocessor = sales_payment_list_response_postprocessor
