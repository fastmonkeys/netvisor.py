from datetime import date

import colander
from colander.tests.test_colander import DummySchemaNode
import pytest

from netvisor.types import FinnishDate


class TestFinnishDate(object):
    @pytest.fixture
    def node(self):
        return DummySchemaNode(None)

    def test_serialize_null(self, node):
        type_ = FinnishDate()
        assert type_.serialize(node, colander.null) == colander.null

    def test_serialize_none(self, node):
        type_ = FinnishDate()
        assert type_.serialize(node, None) == colander.null

    def test_serialize_with_garbage(self, node):
        type_ = FinnishDate()
        with pytest.raises(colander.Invalid) as excinfo:
            type_.serialize(node, 'garbage')
        msg = excinfo.value.msg.interpolate()
        assert msg == '"garbage" is not a date object'

    def test_serialize_with_date(self, node):
        type_ = FinnishDate()
        assert type_.serialize(node, date(2014, 3, 7)) == '07.03.2014'

    def test_deserialize_with_garbage(self, node):
        type_ = FinnishDate()
        with pytest.raises(colander.Invalid) as excinfo:
            type_.deserialize(node, 'garbage')
        assert 'Invalid' in excinfo.value.msg

    def test_deserialize_null(self, node):
        type_ = FinnishDate()
        assert type_.deserialize(node, colander.null) == colander.null

    def test_deserialize_empty(self, node):
        type_ = FinnishDate()
        assert type_.deserialize(node, '') == colander.null

    def test_deserialize_success_date(self, node):
        type_ = FinnishDate()
        assert type_.deserialize(node, '07.03.2014') == date(2014, 3, 7)
