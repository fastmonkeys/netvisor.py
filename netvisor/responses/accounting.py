# -*- coding: utf-8 -*-
"""
    netvisor.responses.accounting
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import AccountingListSchema
from .base import Response


class AccountingListResponse(Response):
    schema_cls = AccountingListSchema
    tag_name = 'vouchers'
