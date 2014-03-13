from .base import Service
from ..requests.company import GetCompanyInformationRequest, CompanyListRequest


class CompanyService(Service):
    def get(self, business_code):
        request = GetCompanyInformationRequest(
            self.client,
            OrganizationIdentifier=business_code
        )
        return request.make_request()

    def list(self, query):
        request = CompanyListRequest(self.client, QueryTerm=query)
        return request.make_request()
