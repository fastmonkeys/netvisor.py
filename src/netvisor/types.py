# -*- coding: utf-8 -*-
from schematics.types.base import BooleanType, DateType, DecimalType


class ActivityStatusType(BooleanType):
    TRUE_VALUES = ('1', 'active',)
    FALSE_VALUES = ('0', 'inactive',)


class BankStatusType(BooleanType):
    TRUE_VALUES = ('OK',)
    FALSE_VALUES = ('FAILED',)


class YesNoBooleanType(BooleanType):
    TRUE_VALUES = (u'Kyllä', u'Yes',)
    FALSE_VALUES = (u'Ei', u'No',)


class CommaSeparatedDecimalType(DecimalType):
    def to_primitive(self, value):
        value = super(CommaSeparatedDecimalType, self).to_primitive(value)
        return value.replace('.', ',')

    def to_native(self, value):
        if isinstance(value, basestring):
            value = value.replace(',', '.')
        return super(CommaSeparatedDecimalType, self).to_native(value)


class FinnishDateType(DateType):
    SERIALIZED_FORMAT = '%d.%m.%Y'
    MESSAGES = {
        'parse': u'Could not parse {0}. Should be DD.MM.YYYY).',
    }
