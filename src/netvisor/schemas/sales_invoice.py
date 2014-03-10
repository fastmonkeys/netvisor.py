# -*- coding: utf-8 -*-
import colander

from .address import AddressSchema


class SalesInvoiceLineSchema(colander.Schema):
    product_code = colander.SchemaNode(colander.String())
    name = colander.SchemaNode(colander.String())
    free_text = colander.SchemaNode(colander.String(), missing=u'')
    quantity = colander.SchemaNode(colander.Decimal())
    unit_price = colander.SchemaNode(colander.Decimal())
    discount_percentage = colander.SchemaNode(colander.Decimal())
    vat_percentage = colander.SchemaNode(colander.Decimal())
    vat_code = colander.SchemaNode(colander.String())
    vat_amount = colander.SchemaNode(colander.Decimal())
    amount = colander.SchemaNode(colander.Decimal())
    accounting_suggestion = colander.SchemaNode(colander.String())


class SalesInvoiceLinesSchema(colander.SequenceSchema):
    sales_invoice_line = SalesInvoiceLineSchema()


class SalesInvoiceListSalesInvoiceSchema(colander.Schema):
    id = colander.SchemaNode(colander.Int())
    number = colander.SchemaNode(colander.Int())
    date = colander.SchemaNode(colander.Date())
    status = colander.SchemaNode(colander.String())
    substatus = colander.SchemaNode(colander.String())
    reference_number = colander.SchemaNode(colander.String())
    amount = colander.SchemaNode(colander.Decimal())
    open_amount = colander.SchemaNode(colander.Decimal())


class SalesInvoiceListSalesInvoicesSchema(colander.SequenceSchema):
    sales_invoice = SalesInvoiceListSalesInvoiceSchema()


class SalesInvoiceListSchema(colander.Schema):
    objects = SalesInvoiceListSalesInvoicesSchema()


class GetSalesInvoiceSchema(colander.Schema):
    number = colander.SchemaNode(colander.Int())
    date = colander.SchemaNode(colander.Date())
    delivery_date = colander.SchemaNode(colander.Date())
    due_date = colander.SchemaNode(colander.Date())
    reference_number = colander.SchemaNode(colander.String())
    amount = colander.SchemaNode(colander.Decimal())
    seller = colander.SchemaNode(colander.String())
    status = colander.SchemaNode(colander.String())
    free_text_before_lines = colander.SchemaNode(colander.String(), missing=u'')
    free_text_after_lines = colander.SchemaNode(colander.String(), missing=u'')
    our_reference = colander.SchemaNode(colander.String(), missing=u'')
    your_reference = colander.SchemaNode(colander.String(), missing=u'')
    private_comment = colander.SchemaNode(colander.String(), missing=u'')
    match_partial_payments_by_default = colander.SchemaNode(colander.Boolean())
    delivery_method = colander.SchemaNode(colander.String(), missing=u'')
    delivery_term = colander.SchemaNode(colander.String(), missing=u'')
    payment_term_net_days = colander.SchemaNode(colander.Int())
    payment_term_cash_discount_days = colander.SchemaNode(colander.Int())
    payment_term_cash_discount = colander.SchemaNode(colander.Decimal())
    billing_address = AddressSchema()
    delivery_address = AddressSchema()
    lines = SalesInvoiceLinesSchema()
