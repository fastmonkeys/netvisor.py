# -*- coding: utf-8 -*-
"""
    netvisor.requests.customer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..responses.customers import CustomerListResponse, GetCustomerResponse
from .base import Request


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
