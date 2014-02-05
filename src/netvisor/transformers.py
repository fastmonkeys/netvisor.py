import inflection


class Transformer(object):
    def transform(self, obj):
        return {key: value for key, value in self._new_items(obj)}

    def _new_items(self, obj):
        for key, value in self._filtered_items(obj):
            for item in self.transform_item(key, value):
                yield item

    def _filtered_items(self, obj):
        for key, value in obj.iteritems():
            if self.filter(key, value):
                yield key, value

    def transform_item(self, key, value):
        yield self.transform_key(key, value), self.transform_value(key, value)

    def transform_key(self, key, value):
        return key

    def transform_value(self, key, value):
        return value

    def filter(self, key, value):
        return True


class DeepTransformer(Transformer):
    def transform_value(self, key, value):
        if isinstance(value, list):
            return [self.transform(element) for element in value]
        if isinstance(value, dict):
            return self.transform(value)
        else:
            return value


class Flatten(Transformer):
    def __init__(self, key_to_flatten):
        self.key_to_flatten = key_to_flatten

    def transform_item(self, key, value):
        if key == self.key_to_flatten:
            for item in value.iteritems():
                yield item
        else:
            yield key, value


class Listify(Transformer):
    def __init__(self, key_to_listify):
        self.key_to_listify = key_to_listify

    def transform_value(self, key, value):
        if key == self.key_to_listify and not isinstance(value, list):
            return [value]
        else:
            return value


class Rename(Transformer):
    def __init__(self, old_key, new_key):
        self.old_key = old_key
        self.new_key = new_key

    def transform_key(self, key, value):
        if key == self.old_key:
            return self.new_key
        else:
            return key


class Remove(Transformer):
    def __init__(self, key_to_remove):
        self.key_to_remove = key_to_remove

    def filter(self, key, value):
        return key != self.key_to_remove


class Underscore(DeepTransformer):
    def transform_key(self, key, value):
        return inflection.underscore(key)


class Camelize(Transformer):
    def transform_key(self, key, value):
        return inflection.camelize(key)


class Key(Transformer):
    def __init__(self, key_to_transform, transformer):
        self.key_to_transform = key_to_transform
        self.transformer = transformer

    def transform_value(self, key, value):
        if key == self.key_to_transform:
            if isinstance(value, list):
                return [
                    self.transformer.transform(element)
                    for element in value
                ]
            else:
                return self.transformer.transform(value)
        else:
            return value


class Chain(Transformer):
    def __init__(self, transformers):
        self.transformers = transformers

    def transform(self, obj):
        for transformer in self.transformers:
            obj = transformer.transform(obj)
        return obj
