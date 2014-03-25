# -*- coding: utf-8 -*-
"""
    netvisor.responses.sales_invoices
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..postprocessors import (
    Boolean,
    Chain,
    Context,
    Date,
    Decimal,
    ExtractAttribute,
    Flatten,
    Integer,
    Listify,
    Nest,
    Remove,
    Rename,
    Underscore,
)
from .base import Response


class SalesInvoiceListResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Listify('sales_invoice_list', 'sales_invoice'),
        Rename('netvisor_key', 'id'),
        Rename('invoice_number', 'number'),
        Rename('invoicedate', 'date'),
        Rename('invoice_sum', 'amount'),
        Rename('open_sum', 'open_amount'),
        Remove('uri'),
        Rename('invoice_status', 'status'),
        Nest(
            'customer',
            {
                'name': 'customer_name',
                'code': 'customer_code'
            }
        ),
        Context(
            ['Root', 'SalesInvoiceList', 'SalesInvoice', 'InvoiceStatus'],
            ExtractAttribute(
                key='status',
                attr='substatus',
                cdata_key='status'
            )
        ),
        Flatten('status'),
        Date('date'),
        Decimal('amount'),
        Decimal('open_amount'),
        Integer('id'),
        Integer('number'),
    ])


class GetSalesInvoiceResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Rename('sales_invoice_date', 'date'),
        Rename('sales_invoice_delivery_date', 'delivery_date'),
        Rename('sales_invoice_due_date', 'due_date'),
        Rename('sales_invoice_number', 'number'),
        Rename('sales_invoice_our_reference', 'our_reference'),
        Rename('sales_invoice_your_reference', 'your_reference'),
        Nest(
            'delivery_address',
            {
                'name': 'delivery_address_name',
                'street': 'delivery_address_line',
                'postal_code': 'delivery_address_postnumber',
                'post_office': 'delivery_address_town',
                'country': 'delivery_address_country_code',
            }
        ),
        Nest(
            'billing_address',
            {
                'name': 'invoicing_customer_name',
                'street': 'invoicing_customer_addressline',
                'postal_code': 'invoicing_customer_postnumber',
                'post_office': 'invoicing_customer_town',
                'country': 'invoicing_customer_country_code',
            }
        ),
        Rename('sales_invoice_referencenumber', 'reference_number'),
        Rename('sales_invoice_amount', 'amount'),
        Rename('sales_invoice_free_text_after_lines', 'free_text_after_lines'),
        Rename(
            'sales_invoice_free_text_before_lines',
            'free_text_before_lines'
        ),
        Rename('sales_invoice_private_comment', 'private_comment'),
        Rename('seller_identifier', 'seller'),
        Rename('invoice_status', 'status'),
        Rename('productidentifier', 'product_code'),
        Rename('product_name', 'name'),
        Rename('product_unit_price', 'unit_price'),
        Rename('sales_invoice_product_line_quantity', 'quantity'),
        Rename('sales_invoice_product_line_free_text', 'free_text'),
        Rename('sales_invoice_product_line_sum', 'amount'),
        Rename('accounting_account_suggestion', 'accounting_suggestion'),
        Rename(
            'sales_invoice_product_line_discount_percentage',
            'discount_percentage'
        ),
        Boolean(
            'match_partial_payments_by_default',
            true=[u'Yes', u'Kyllä'],
            false=[u'No', u'Ei']
        ),
        Date('date'),
        Date('delivery_date'),
        Date('due_date'),
        Decimal('amount'),
        Decimal('discount_percentage'),
        Decimal('payment_term_cash_discount'),
        Decimal('product_vat_percentage'),
        Decimal('quantity'),
        Decimal('sales_invoice_product_line_vat_sum'),
        Decimal('unit_price'),
        Integer('number'),
        Integer('payment_term_cash_discount_days'),
        Integer('payment_term_net_days'),
        Listify('invoice_lines', 'invoice_line'),
        Rename('invoice_lines', 'lines'),
        Flatten('sales_invoice_product_line'),
        ExtractAttribute(
            key='product_vat_percentage',
            attr='vatcode',
            attr_key='code',
            cdata_key='percentage'
        ),
        Rename('product_vat_percentage', 'vat'),
        Nest('vat', {'amount': 'sales_invoice_product_line_vat_sum'}),
    ])
