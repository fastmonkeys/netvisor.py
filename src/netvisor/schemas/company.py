# -*- coding: utf-8 -*-
import colander

from .address import AddressSchema


class CompanyStatsSchema(colander.Schema):
    employer_register_status = colander.SchemaNode(colander.String())
    revenue_size = colander.SchemaNode(colander.String())
    staff_size = colander.SchemaNode(colander.String())
    standard_industrial_classification2008 = colander.SchemaNode(
        colander.String()
    )
    tax_prepayment_register_status = colander.SchemaNode(colander.String())
    vat_register_status = colander.SchemaNode(colander.String())


class RegisteredNameSchema(colander.Schema):
    name = colander.SchemaNode(colander.String())
    type = colander.SchemaNode(colander.String())
    is_active = colander.SchemaNode(colander.Boolean())
    established_date = colander.SchemaNode(colander.Date())
    terminated_date = colander.SchemaNode(colander.Date())


class RegisteredNamesSchema(colander.SequenceSchema):
    registered_name = RegisteredNameSchema()


class RegisteredPersonRoleSchema(colander.Schema):
    nationality = colander.SchemaNode(colander.String())
    identifier = colander.SchemaNode(colander.String())
    type = colander.SchemaNode(colander.String())
    established_date = colander.SchemaNode(colander.Date())
    name = colander.SchemaNode(colander.String())


class RegisteredPersonRolesSchema(colander.SequenceSchema):
    registered_person_roles = RegisteredPersonRoleSchema()


class CompanyListCompanySchema(colander.Schema):
    name = colander.SchemaNode(colander.String())
    business_code = colander.SchemaNode(colander.String())
    is_active = colander.SchemaNode(colander.Boolean())


class CompanyListCompaniesSchema(colander.SequenceSchema):
    company = CompanyListCompanySchema()


class CompanyListSchema(colander.Schema):
    objects = CompanyListCompaniesSchema()


class GetCompanyInformationSchema(CompanyListCompanySchema):
    type = colander.SchemaNode(colander.String())
    responsible_person_authorization_rule = colander.SchemaNode(
        colander.String()
    )
    established_date = colander.SchemaNode(colander.Date())
    terminated_date = colander.SchemaNode(colander.Date())
    most_recent_change_date = colander.SchemaNode(colander.Date())
    current_special_status = colander.SchemaNode(
        colander.String(),
        missing=u''
    )
    domicile = colander.SchemaNode(colander.String())
    activity_description = colander.SchemaNode(colander.String())
    email = colander.SchemaNode(colander.String())
    phone = colander.SchemaNode(colander.String())
    fax = colander.SchemaNode(colander.String())
    registered_names = RegisteredNamesSchema()
    registered_person_roles = RegisteredPersonRolesSchema()
    street_address = AddressSchema()
    postal_address = AddressSchema()
    stats = CompanyStatsSchema()
