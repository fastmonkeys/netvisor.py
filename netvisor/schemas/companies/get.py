# -*- coding: utf-8 -*-
"""
    netvisor.schemas.companies.get
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..common import DateSchema, StringSchema


class Address(Schema):
    street = fields.String(allow_none=True)
    postal_code = fields.String()
    postal_office = fields.String()


class RegisteredName(Schema):
    type = fields.String()
    name = fields.String()
    current_activity_status = fields.String()
    established_date = fields.Nested(DateSchema)
    terminated_date = fields.Nested(DateSchema)


class RegisteredNames(Schema):
    registered_name = fields.List(fields.Nested(RegisteredName))


@RegisteredNames.preprocessor
def preprocess_registered_names(schema, input_data):
    return input_data['registered_name'] if input_data else []


class RegisteredPersonRole(Schema):
    type = fields.String()
    identifier = fields.String()
    established_date = fields.Nested(DateSchema)
    name = fields.String()
    nationality = fields.Nested(StringSchema)


class RegisteredPersonRoles(Schema):
    role = fields.List(fields.Nested(RegisteredPersonRole))


@RegisteredPersonRoles.preprocessor
def preprocess_registered_person_roles(schema, input_data):
    return input_data['role'] if input_data else []


class CompanySchema(Schema):
    name = fields.String()
    finnish_organization_identifier = fields.String()
    type = fields.String()
    responsible_person_authorization_rule = fields.String()
    established_date = fields.Nested(DateSchema)
    terminated_date = fields.Nested(DateSchema)
    most_recent_change_date = fields.Nested(DateSchema)
    current_activity_status = fields.String()
    current_special_status = fields.String(allow_none=True)
    domicile = fields.String()
    activity_description = fields.String()
    street_address = fields.Nested(Address)
    postal_address = fields.Nested(Address)
    email = fields.String()
    phone = fields.String()
    fax = fields.String()
    registered_person_roles = fields.Nested(RegisteredPersonRoles)
    registered_names = fields.Nested(RegisteredNames)
    stat_employer_register_status = fields.String()
    stat_revenue_size = fields.String()
    stat_staff_size = fields.String()
    stat_vat_register_status = fields.String()
    stat_standard_industrial_classification2008 = fields.String()
    stat_tax_prepayment_register_status = fields.String()


class GetCompanyInformationSchema(Schema):
    company = fields.Nested(CompanySchema)


@GetCompanyInformationSchema.preprocessor
def preprocess_customer(schema, input_data):
    return input_data['company']
