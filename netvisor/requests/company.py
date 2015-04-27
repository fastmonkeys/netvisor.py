# -*- coding: utf-8 -*-
"""
    netvisor.requests.company
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from .base import Request
from ..responses.companies import (
    CompanyListResponse,
    GetCompanyInformationResponse,
)


class GetCompanyInformationRequest(Request):
    method = 'GET'
    uri = 'GetCompanyInformation.nv'
    response_cls = GetCompanyInformationResponse
    resource_key = 'company'


class CompanyListRequest(Request):
    method = 'GET'
    uri = 'CompanyList.nv'
    response_cls = CompanyListResponse
    resource_key = 'company_list'
