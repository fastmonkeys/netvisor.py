from ..postprocessors.companies import (
    get_company_information_response_postprocessor,
    company_list_response_postprocessor,
)
from .base import Response


class CompanyListResponse(Response):
    postprocessor = company_list_response_postprocessor


class GetCompanyInformationResponse(Response):
    postprocessor = get_company_information_response_postprocessor
