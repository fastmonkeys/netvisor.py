# -*- coding: utf-8 -*-
"""
    netvisor.responses.sales_payments
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..postprocessors import (
    Boolean,
    Chain,
    Decimal,
    ExtractAttribute,
    FinnishDate,
    Flatten,
    Integer,
    Listify,
    Nest,
    Rename,
    Underscore,
)
from .base import Response


class SalesPaymentListResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Listify('sales_payment_list', 'sales_payment'),
        Rename('netvisor_key', 'id'),
        Rename('sum', 'amount'),
        Rename('bank_status', 'is_ok'),
        Boolean('is_ok', true=[u'OK'], false=[u'FAILED']),
        Decimal('amount'),
        FinnishDate('date'),
        Integer('id'),
        Integer('invoice_number'),
        ExtractAttribute(
            key='bank_status_error_description',
            attr='code',
            attr_key='error_code',
            cdata_key='error_description'
        ),
        Flatten('bank_status_error_description'),
        Nest(
            'bank_status', {
                'is_ok': 'is_ok',
                'error_code': 'error_code',
                'error_description': 'error_description',
            }
        )
    ])
