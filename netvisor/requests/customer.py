# -*- coding: utf-8 -*-
"""
    netvisor.requests.customer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from .base import Request
from ..responses.customers import CustomerListResponse, GetCustomerResponse


class GetCustomerRequest(Request):
    method = 'GET'
    uri = 'GetCustomer.nv'
    response_cls = GetCustomerResponse
    resource_key = 'customer'


class CustomerListRequest(Request):
    method = 'GET'
    uri = 'CustomerList.nv'
    response_cls = CustomerListResponse
    resource_key = 'customer_list'
