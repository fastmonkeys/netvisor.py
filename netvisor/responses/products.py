# -*- coding: utf-8 -*-
"""
    netvisor.responses.products
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..postprocessors import (
    Boolean,
    Chain,
    Decimal,
    ExtractAttribute,
    Flatten,
    Integer,
    Listify,
    Remove,
    Rename,
    Underscore,
)
from .base import Response


class ProductListResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Listify('product_list', 'product'),
        Rename('netvisor_key', 'id'),
        Rename('product_code', 'code'),
        Remove('uri'),
        Integer('id'),
        Decimal('unit_price'),
        ExtractAttribute(
            key='unit_price',
            attr='Type',
            attr_key='unit_price_type',
            attr_default='netto',
            cdata_key='unit_price'
        ),
        Flatten('unit_price')
    ])


class GetProductResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Flatten('product_base_information'),
        Flatten('product_book_keeping_details'),
        Rename('comission_percentage', 'commission_percentage'),
        Rename('default_vat_percent', 'default_vat_percentage'),
        Rename('inventory_amount', 'amount'),
        Rename('inventory_mid_price', 'mid_price'),
        Rename('inventory_ordered_amount', 'ordered_amount'),
        Rename('inventory_reserved_amount', 'reserved_amount'),
        Rename('inventory_value', 'value'),
        Rename('netvisor_key', 'id'),
        Rename('product_code', 'code'),
        Rename('product_group', 'group'),
        Rename('product_inventory_details', 'inventory'),
        Integer('id'),
        Decimal('unit_price'),
        ExtractAttribute(
            key='unit_price',
            attr='Type',
            attr_key='unit_price_type',
            attr_default='netto',
            cdata_key='unit_price'
        ),
        Flatten('unit_price'),
        Decimal('amount'),
        Decimal('commission_percentage'),
        Decimal('default_vat_percentage'),
        Decimal('mid_price'),
        Decimal('ordered_amount'),
        Decimal('purchase_price'),
        Decimal('reserved_amount'),
        Decimal('unit_weight'),
        Decimal('value'),
        Boolean('is_active'),
        Boolean('is_sales_product')
    ])
