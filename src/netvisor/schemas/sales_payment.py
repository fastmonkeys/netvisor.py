# -*- coding: utf-8 -*-
import colander

from .types import FinnishDate


class BankStatusSchema(colander.Schema):
    is_ok = colander.SchemaNode(colander.Boolean())
    error_code = colander.SchemaNode(colander.String(), missing=u'')
    error_description = colander.SchemaNode(colander.String(), missing=u'')


class SalesPaymentListSalesPaymentSchema(colander.Schema):
    id = colander.SchemaNode(colander.Int())
    name = colander.SchemaNode(colander.String())
    date = colander.SchemaNode(FinnishDate())
    amount = colander.SchemaNode(colander.Decimal())
    foreign_currency_amount = colander.SchemaNode(
        colander.Decimal(),
        missing=None
    )
    reference_number = colander.SchemaNode(colander.String())
    invoice_number = colander.SchemaNode(colander.Int())
    bank_status = BankStatusSchema()


class SalesPaymentListSalesPaymentsSchema(colander.SequenceSchema):
    sales_payment = SalesPaymentListSalesPaymentSchema()


class SalesPaymentListSchema(colander.Schema):
    objects = SalesPaymentListSalesPaymentsSchema()
