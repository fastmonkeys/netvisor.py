# -*- coding: utf-8 -*-
"""
    netvisor.schemas.replies
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields


class RepliesSchema(Schema):
    inserted_data_identifier = fields.Integer()


@RepliesSchema.preprocessor
def preprocess_replies(schema, input_data):
    return input_data['inserted_data_identifier']
