from ..postprocessors.customers import (
    get_customer_response_postprocessor,
    customer_list_response_postprocessor,
)
from .base import Response


class CustomerListResponse(Response):
    postprocessor = customer_list_response_postprocessor


class GetCustomerResponse(Response):
    postprocessor = get_customer_response_postprocessor
