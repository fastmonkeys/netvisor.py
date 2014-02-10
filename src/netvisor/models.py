# -*- coding: utf-8 -*-
from schematics.models import Model
from schematics.types.base import BooleanType, DateType, IntType, StringType
from schematics.types.compound import ListType, ModelType

from .types import (
    ActivityStatusType,
    BankStatusType,
    CommaSeparatedDecimalType,
    FinnishDateType,
    YesNoBooleanType,
)


class Address(Model):
    name = StringType()
    street = StringType()
    postal_code = StringType()
    post_office = StringType()
    country = StringType()


class Finvoice(Model):
    router_code = StringType()
    address = StringType()


class ContactPerson(Model):
    name = StringType()
    email = StringType()
    phone = StringType()


class CompanyStats(Model):
    employer_register_status = StringType()
    revenue_size = StringType()
    staff_size = StringType()
    standard_industrial_classification2008 = StringType()
    tax_prepayment_register_status = StringType()
    vat_register_status = StringType()


class RegisteredName(Model):
    name = StringType()
    type = StringType()
    is_active = ActivityStatusType(deserialize_from='current_activity_status')
    established_date = DateType()
    terminated_date = DateType()


class RegisteredPersonRole(Model):
    nationality = StringType()
    identifier = StringType()
    type = StringType()
    established_date = DateType()
    name = StringType()


class Company(Model):
    name = StringType()
    type = StringType()
    responsible_person_authorization_rule = StringType()
    established_date = DateType()
    terminated_date = DateType()
    most_recent_change_date = DateType()
    is_active = ActivityStatusType(deserialize_from='current_activity_status')
    current_special_status = StringType()
    domicile = StringType()
    activity_description = StringType()
    email = StringType()
    phone = StringType()
    fax = StringType()
    registered_names = ListType(ModelType(RegisteredName))
    registered_person_roles = ListType(ModelType(RegisteredPersonRole))
    business_code = StringType()
    street_address = ModelType(Address)
    postal_address = ModelType(Address)
    stats = ModelType(CompanyStats)


class Customer(Model):
    netvisor_key = IntType()
    name = StringType()
    name_extension = StringType()
    code = StringType()
    business_code = StringType()
    phone = StringType()
    fax = StringType()
    email = StringType()
    homepage = StringType()
    comment = StringType()
    reference_number = StringType()
    street_address = ModelType(Address)
    delivery_address = ModelType(Address)
    finvoice = ModelType(Finvoice)
    contact_person = ModelType(ContactPerson)


class Product(Model):
    netvisor_key = IntType()
    code = StringType()
    group = StringType()
    name = StringType()
    description = StringType()
    unit_price = CommaSeparatedDecimalType()
    unit_price_type = StringType(default=u'netto')
    unit = StringType()
    unit_weight = CommaSeparatedDecimalType()
    purchase_price = CommaSeparatedDecimalType()
    tariff_heading = StringType()
    commission_percentage = CommaSeparatedDecimalType()
    is_active = BooleanType()
    is_sales_product = BooleanType()
    default_vat_percentage = CommaSeparatedDecimalType()
    default_domestic_account_number = StringType()
    default_eu_account_number = StringType()
    default_outside_eu_account_number = StringType()


class BankStatus(Model):
    is_ok = BankStatusType(deserialize_from='status')
    error_code = StringType()
    error_description = StringType()


class SalesInvoiceLine(Model):
    product_code = StringType()
    name = StringType()
    free_text = StringType()
    quantity = CommaSeparatedDecimalType()
    unit_price = CommaSeparatedDecimalType()
    discount_percentage = CommaSeparatedDecimalType()
    vat_percentage = CommaSeparatedDecimalType()
    vat_code = StringType()
    vat_amount = CommaSeparatedDecimalType()
    amount = CommaSeparatedDecimalType()
    accounting_suggestion = StringType()


class SalesInvoice(Model):
    netvisor_key = IntType()
    number = IntType()
    date = DateType()
    delivery_date = DateType()
    due_date = DateType()
    reference_number = StringType()
    amount = CommaSeparatedDecimalType()
    open_amount = CommaSeparatedDecimalType()
    seller = StringType()
    status = StringType()
    substatus = StringType()
    free_text_before_lines = StringType()
    free_text_after_lines = StringType()
    our_reference = StringType()
    your_reference = StringType()
    private_comment = StringType()
    match_partial_payments_by_default = YesNoBooleanType()
    delivery_method = StringType()
    delivery_term = StringType()
    payment_term_net_days = IntType()
    payment_term_cash_discount_days = IntType()
    payment_term_cash_discount = CommaSeparatedDecimalType()
    billing_address = ModelType(Address)
    delivery_address = ModelType(Address)
    lines = ListType(ModelType(SalesInvoiceLine))


class SalesPayment(Model):
    netvisor_key = IntType()
    name = StringType()
    date = FinnishDateType()
    amount = CommaSeparatedDecimalType()
    foreign_currency_amount = CommaSeparatedDecimalType()
    reference_number = StringType()
    invoice_number = IntType()
    bank_status = ModelType(BankStatus)
