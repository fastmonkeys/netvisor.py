from .primitives import (
    Chain,
    Context,
    Flatten,
    FlattenText,
    Listify,
    Nest,
    NormalizeDecimalPoint,
    NormalizeYesNoBoolean,
    Rename,
    Remove,
    Underscore,
)


sales_invoice_list_response_transformer = Chain([
    Underscore(),
    Flatten('root'),                 # REMOVE?
    Remove('response_status'),       # REMOVE?
    Flatten('sales_invoice_list'),   # REMOVE?
    Rename('sales_invoice', 'objects'),
    Listify('objects'),
    Context(
        'objects',
        Chain([
            Rename('netvisor_key', 'id'),
            Rename('invoice_number', 'number'),
            Rename('invoicedate', 'date'),
            Rename('invoice_sum', 'amount'),
            Rename('open_sum', 'open_amount'),
            Remove('customer_code'),
            Remove('customer_name'),
            Remove('uri'),
            FlattenText('date'),
            Rename('invoice_status', 'status'),
            Context(
                'status',
                Chain([
                    Rename('#text', 'status'),
                    Rename('@substatus', 'substatus')
                ])
            ),
            Flatten('status'),
            NormalizeDecimalPoint('amount'),
            NormalizeDecimalPoint('open_amount'),
        ])
    )
])


get_sales_invoice_response_transformer = Chain([
    Underscore(),
    Flatten('root'),               # REMOVE?
    Remove('response_status'),     # REMOVE?
    Flatten('sales_invoice'),      # REMOVE?
    Rename('sales_invoice_date', 'date'),
    Rename('sales_invoice_delivery_date', 'delivery_date'),
    Rename('sales_invoice_due_date', 'due_date'),
    FlattenText('date'),
    FlattenText('delivery_date'),
    FlattenText('due_date'),
    Rename('sales_invoice_number', 'number'),
    Rename('sales_invoice_our_reference', 'our_reference'),
    Rename('sales_invoice_your_reference', 'your_reference'),
    Nest(
        'delivery_address',
        [
            'delivery_address_name',
            'delivery_address_line',
            'delivery_address_postnumber',
            'delivery_address_town',
            'delivery_address_country_code',
        ]
    ),
    Context(
        'delivery_address',
        Chain([
            Rename('delivery_address_name', 'name'),
            Rename('delivery_address_line', 'street'),
            Rename('delivery_address_postnumber', 'postal_code'),
            Rename('delivery_address_town', 'post_office'),
            Rename('delivery_address_country_code', 'country'),
        ])
    ),
    Nest(
        'billing_address',
        [
            'invoicing_customer_name',
            'invoicing_customer_addressline',
            'invoicing_customer_postnumber',
            'invoicing_customer_town',
            'invoicing_customer_country_code',
        ]
    ),
    Context(
        'billing_address',
        Chain([
            Rename('invoicing_customer_name', 'name'),
            Rename('invoicing_customer_addressline', 'street'),
            Rename('invoicing_customer_postnumber', 'postal_code'),
            Rename('invoicing_customer_town', 'post_office'),
            Rename('invoicing_customer_country_code', 'country'),
        ])
    ),
    Rename('sales_invoice_referencenumber', 'reference_number'),
    Rename('sales_invoice_amount', 'amount'),
    NormalizeDecimalPoint('amount'),
    Rename(
        'sales_invoice_free_text_after_lines',
        'free_text_after_lines'
    ),
    Rename(
        'sales_invoice_free_text_before_lines',
        'free_text_before_lines'
    ),
    Rename('sales_invoice_private_comment', 'private_comment'),
    Rename('seller_identifier', 'seller'),
    FlattenText('seller'),
    FlattenText('payment_term_cash_discount'),
    Rename('invoice_status', 'status'),
    NormalizeYesNoBoolean('match_partial_payments_by_default'),
    Flatten('invoice_lines'),
    Flatten('invoice_line'),
    Rename('sales_invoice_product_line', 'lines'),
    Listify('lines'),
    Context(
        'lines',
        Chain([
            Rename('productidentifier', 'product_code'),
            FlattenText('product_code'),
            Rename('product_name', 'name'),
            Rename('product_unit_price', 'unit_price'),
            Rename('product_vat_percentage', 'vat_percentage'),
            Context(
                'vat_percentage',
                Chain([
                    Rename('@vatcode', 'vat_code'),
                    Rename('#text', 'vat_percentage'),
                ])
            ),
            Flatten('vat_percentage'),
            Rename(
                'sales_invoice_product_line_discount_percentage',
                'discount_percentage'
            ),
            Rename('sales_invoice_product_line_quantity', 'quantity'),
            Rename('sales_invoice_product_line_free_text', 'free_text'),
            Rename('sales_invoice_product_line_vat_sum', 'vat_amount'),
            Rename('sales_invoice_product_line_sum', 'amount'),
            NormalizeDecimalPoint('quantity'),
            NormalizeDecimalPoint('vat_amount'),
            NormalizeDecimalPoint('amount'),
            NormalizeDecimalPoint('vat_percentage'),
            NormalizeDecimalPoint('unit_price'),
            Rename(
                'accounting_account_suggestion',
                'accounting_suggestion'
            )
        ])
    )
])
