# -*- coding: utf-8 -*-
"""
    netvisor.postprocessors
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from datetime import datetime
import decimal

import inflection


class Remove(object):
    def __init__(self, key):
        self.key = key

    def __call__(self, path, key, data):
        if key != self.key:
            return key, data


class Rename(object):
    def __init__(self, old_key, new_key):
        self.old_key = old_key
        self.new_key = new_key

    def __call__(self, path, key, data):
        if key == self.old_key:
            key = self.new_key
        return key, data


class Flatten(object):
    def __init__(self, key_to_flatten):
        self.key_to_flatten = key_to_flatten

    def _flatten(self, data):
        dict_to_flatten = data.pop(self.key_to_flatten)
        for key, value in dict_to_flatten.items():
            data[key] = value

    def _can_flatten(self, data):
        return (
            isinstance(data, dict) and
            self.key_to_flatten in data and
            isinstance(data[self.key_to_flatten], dict)
        )

    def __call__(self, path, key, data):
        if self._can_flatten(data):
            self._flatten(data)
        return key, data


class Nest(object):
    def __init__(self, parent_key, keys_to_nest):
        self.parent_key = parent_key
        self.keys_to_nest = keys_to_nest

    def _nest(self, data):
        nested_obj = {
            key: data.pop(value)
            for key, value in self.keys_to_nest.items()
            if value in data
        }
        if nested_obj:
            should_update = (
                self.parent_key in data and
                isinstance(data[self.parent_key], dict)
            )
            if should_update:
                data[self.parent_key].update(nested_obj)
            else:
                data[self.parent_key] = nested_obj

    def _can_nest(self, data):
        return isinstance(data, dict)

    def __call__(self, path, key, data):
        if self._can_nest(data):
            self._nest(data)
        return key, data


class Listify(object):
    def __init__(self, parent_key, child_key):
        self.parent_key = parent_key
        self.child_key = child_key

    def __call__(self, path, key, data):
        if key == self.parent_key:
            if data is None:
                data = []
            elif not isinstance(data[self.child_key], list):
                data = [data[self.child_key]]
            else:
                data = data[self.child_key]
        return key, data


class Chain(object):
    def __init__(self, postprocessors):
        self.postprocessors = postprocessors

    def __call__(self, path, key, data):
        for postprocess in self.postprocessors:
            result = postprocess(path, key, data)
            if result is None:
                return
            else:
                key, data = result
        return key, data


class Context(object):
    def __init__(self, path, postprocessor):
        self.path = path
        self.postprocessor = postprocessor

    def remove_attributes_from_path(self, path):
        return [element for element, _ in path]

    def __call__(self, path, key, data):
        element_path = self.remove_attributes_from_path(path)
        if element_path == self.path:
            return self.postprocessor(path, key, data)
        else:
            return key, data


class Underscore(object):
    def __call__(self, path, key, data):
        return inflection.underscore(key), data


class Decimal(object):
    def __init__(self, key):
        self.key = key

    def __call__(self, path, key, data):
        if key == self.key and data:
            data = data.replace(',', '.')
            data = decimal.Decimal(data)
        return key, data


class Integer(object):
    def __init__(self, key):
        self.key = key

    def __call__(self, path, key, data):
        if key == self.key and data:
            data = int(data)
        return key, data


class Boolean(object):
    def __init__(self, key, true=None, false=None):
        self.key = key
        self.true = ['1'] if true is None else true
        self.false = ['0'] if false is None else false

    def __call__(self, path, key, data):
        if key == self.key and data:
            if data in self.true:
                data = True
            elif data in self.false:
                data = False
        return key, data


class Date(object):
    date_format = '%Y-%m-%d'

    def __init__(self, key):
        self.key = key

    def __call__(self, path, key, data):
        if key == self.key and data:
            data = datetime.strptime(data, self.date_format).date()
        return key, data


class FinnishDate(Date):
    date_format = '%d.%m.%Y'


class ExtractAttribute(object):
    def __init__(
        self, key, attr, attr_key=None, attr_default=None, cdata_key='#text'
    ):
        self.key = key
        self.attr = attr
        self.attr_key = attr_key or attr
        self.attr_default = attr_default
        self.cdata_key = cdata_key

    def __call__(self, path, key, data):
        if key == self.key:
            _, attrs = path[-1]
            if attrs is None:
                attrs = {}
            data = {
                self.cdata_key: data,
                self.attr_key: attrs.get(self.attr, self.attr_default)
            }
        return key, data
