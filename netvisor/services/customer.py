from .base import Service
from ..requests.customer import GetCustomerRequest, CustomerListRequest


class CustomerService(Service):
    def get(self, id):
        request = GetCustomerRequest(self.client, id=id)
        return request.make_request()

    def list(self, query=None):
        request = CustomerListRequest(self.client, Keyword=query)
        return request.make_request()
