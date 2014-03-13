from .base import Service
from ..requests.product import GetProductRequest, ProductListRequest


class ProductService(Service):
    def get(self, id):
        request = GetProductRequest(self.client, id=id)
        return request.make_request()

    def list(self):
        request = ProductListRequest(self.client)
        return request.make_request()
