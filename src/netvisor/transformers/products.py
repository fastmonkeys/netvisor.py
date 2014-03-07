from .primitives import (
    Chain,
    Context,
    Flatten,
    Listify,
    NormalizeDecimalPoint,
    Rename,
    Remove,
    Underscore,
)


product_list_response_transformer = Chain([
    Underscore(),
    Flatten('root'),               # REMOVE?
    Flatten('product_list'),       # REMOVE?
    Remove('response_status'),     # REMOVE?
    Rename('product', 'products'),
    Listify('products'),
    Context(
        'products',
        Chain([
            Remove('uri'),
            NormalizeDecimalPoint('unit_price'),
            Rename('product_code', 'code')
        ])
    ),
])


get_product_response_transformer = Chain([
    Underscore(),
    Flatten('root'),               # REMOVE?
    Remove('response_status'),     # REMOVE?
    Flatten('product'),            # REMOVE?
    Flatten('product_base_information'),
    Flatten('product_book_keeping_details'),
    Rename('product_code', 'code'),
    Rename('product_group', 'group'),
    Context(
        'unit_price',
        Chain([
            Rename('#text', 'unit_price'),
            Rename('@type', 'unit_price_type'),
        ])
    ),
    Flatten('unit_price'),
    Rename('comission_percentage', 'commission_percentage'),
    Rename('product_inventory_details', 'inventory'),
    Rename('default_vat_percent', 'default_vat_percentage'),
    NormalizeDecimalPoint('unit_price'),
    Context(
        'inventory',
        Chain([
            Rename('inventory_amount', 'amount'),
            Rename('inventory_mid_price', 'mid_price'),
            Rename('inventory_value', 'value'),
            Rename('inventory_reserved_amount', 'reserved_amount'),
            Rename('inventory_ordered_amount', 'ordered_amount'),
            NormalizeDecimalPoint('amount'),
            NormalizeDecimalPoint('mid_price'),
            NormalizeDecimalPoint('value'),
            NormalizeDecimalPoint('reserved_amount'),
            NormalizeDecimalPoint('ordered_amount'),
        ])
    )
])
