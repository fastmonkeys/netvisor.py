# -*- coding: utf-8 -*-
"""
    netvisor.schemas.replies
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load


class RepliesSchema(Schema):
    inserted_data_identifier = fields.Integer()

    @post_load
    def preprocess_replies(self, input_data):
        return input_data['inserted_data_identifier']
