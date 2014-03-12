# -*- coding: utf-8 -*-
import pytest

from ..utils import get_response_text


class SchemaTestCase(object):
    response_filename = None
    response_cls = None
    schema_cls = None

    @pytest.fixture(scope='class')
    def raw_data(self):
        xml = get_response_text(self.__class__.response_filename)
        response = self.__class__.response_cls(xml)
        return response.parse()

    @pytest.fixture(scope='class')
    def data(self, raw_data):
        schema = self.__class__.schema_cls()
        return schema.deserialize(raw_data)
