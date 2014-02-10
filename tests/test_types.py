from decimal import Decimal

import pytest
from schematics.exceptions import ConversionError

from netvisor import types


class TestCommaSeparatedDecimalType(object):
    @pytest.fixture
    def type_(self):
        return types.CommaSeparatedDecimalType()

    def test_to_primitive(self, type_):
        assert type_.to_primitive(Decimal('1.23')) == '1,23'

    def test_to_native_with_decimal_value(self, type_):
        assert type_.to_native(Decimal('1.23')) == Decimal('1.23')

    def test_to_native_with_int_value(self, type_):
        assert type_.to_native(1) == Decimal(1)

    def test_to_native_with_invalid_value(self, type_):
        with pytest.raises(ConversionError) as excinfo:
            type_.to_native('1;23')
        assert excinfo.value.messages == [type_.messages['number_coerce']]
