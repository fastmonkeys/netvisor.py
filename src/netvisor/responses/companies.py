from ..transformers.companies import (
    get_company_information_response_transformer,
    company_list_response_transformer,
)
from .base import Response


class CompanyListResponse(Response):
    transformer = company_list_response_transformer


class GetCompanyInformationResponse(Response):
    transformer = get_company_information_response_transformer
