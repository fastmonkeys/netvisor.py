# -*- coding: utf-8 -*-
"""
    netvisor.schemas.companies.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..fields import Boolean


class CompanySchema(Schema):
    id = fields.Integer()
    name = fields.String()
    finnish_organization_identifier = fields.String(allow_none=True)
    is_active = Boolean(true='1', false='0')


class CompanyListSchema(Schema):
    companies = fields.List(
        fields.Nested(CompanySchema),
        load_from='company'
    )


@CompanyListSchema.preprocessor
def preprocess_company_list(schema, input_data):
    return input_data['companies'] if input_data else []
