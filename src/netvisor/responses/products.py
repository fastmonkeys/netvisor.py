from ..transformers.products import (
    get_product_response_transformer,
    product_list_response_transformer,
)
from .base import Response


class ProductListResponse(Response):
    transformer = product_list_response_transformer


class GetProductResponse(Response):
    transformer = get_product_response_transformer
