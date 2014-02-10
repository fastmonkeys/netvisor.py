from ..transformers.sales_payments import (
    sales_payment_list_response_transformer,
)
from .base import Response


class SalesPaymentListResponse(Response):
    transformer = sales_payment_list_response_transformer
