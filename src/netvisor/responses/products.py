from ..postprocessors.products import (
    get_product_response_postprocessor,
    product_list_response_postprocessor,
)
from .base import Response


class ProductListResponse(Response):
    postprocessor = product_list_response_postprocessor


class GetProductResponse(Response):
    postprocessor = get_product_response_postprocessor
