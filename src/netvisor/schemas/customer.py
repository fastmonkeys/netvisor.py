# -*- coding: utf-8 -*-
import colander

from .address import AddressSchema


class CustomerGroup(colander.Schema):
    id = colander.SchemaNode(colander.Int())
    name = colander.SchemaNode(colander.String())


class FinvoiceSchema(colander.Schema):
    router_code = colander.SchemaNode(colander.String(), missing=u'')
    address = colander.SchemaNode(colander.String(), missing=u'')


class ContactPersonSchema(colander.Schema):
    name = colander.SchemaNode(colander.String(), missing=u'')
    email = colander.SchemaNode(colander.String(), missing=u'')
    phone = colander.SchemaNode(colander.String(), missing=u'')


class CustomerListCustomerSchema(colander.Schema):
    id = colander.SchemaNode(colander.Int())
    name = colander.SchemaNode(colander.String())
    code = colander.SchemaNode(colander.String(), missing=u'')
    business_code = colander.SchemaNode(colander.String(), missing=u'')


class CustomerListCustomersSchema(colander.SequenceSchema):
    customer = CustomerListCustomerSchema()


class CustomerListSchema(colander.Schema):
    objects = CustomerListCustomersSchema()


class GetCustomerSchema(colander.Schema):
    name = colander.SchemaNode(colander.String())
    name_extension = colander.SchemaNode(colander.String(), missing=u'')
    group = CustomerGroup()
    code = colander.SchemaNode(colander.String(), missing=u'')
    business_code = colander.SchemaNode(colander.String(), missing=u'')
    phone = colander.SchemaNode(colander.String(), missing=u'')
    fax = colander.SchemaNode(colander.String(), missing=u'')
    email = colander.SchemaNode(colander.String(), missing=u'')
    homepage = colander.SchemaNode(colander.String(), missing=u'')
    comment = colander.SchemaNode(colander.String(), missing=u'')
    reference_number = colander.SchemaNode(colander.String(), missing=u'')
    street_address = AddressSchema()
    delivery_address = AddressSchema()
    finvoice = FinvoiceSchema()
    contact_person = ContactPersonSchema()
    is_active = colander.SchemaNode(colander.Boolean())
    balance_limit = colander.SchemaNode(colander.Decimal(), missing=None)
