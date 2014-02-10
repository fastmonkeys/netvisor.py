from ..transformers.customers import (
    get_customer_response_transformer,
    customer_list_response_transformer,
)
from .base import Response


class CustomerListResponse(Response):
    transformer = customer_list_response_transformer


class GetCustomerResponse(Response):
    transformer = get_customer_response_transformer
