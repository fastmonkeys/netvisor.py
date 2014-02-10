import inflection


class Add(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def transform(self, obj):
        obj = obj.copy()
        obj[self.key] = self.value
        return obj


class Remove(object):
    def __init__(self, key):
        self.key = key

    def transform(self, obj):
        obj = obj.copy()
        obj.pop(self.key, None)
        return obj


class Rename(object):
    def __init__(self, old_key, new_key):
        self.old_key = old_key
        self.new_key = new_key

    def transform(self, obj):
        obj = obj.copy()
        if self.old_key in obj:
            obj[self.new_key] = obj.pop(self.old_key)
        return obj


class Flatten(object):
    def __init__(self, key_to_flatten):
        self.key_to_flatten = key_to_flatten

    def transform(self, obj):
        obj = obj.copy()
        dict_to_flatten = obj.pop(self.key_to_flatten, {})
        for key, value in dict_to_flatten.iteritems():
            obj[key] = value
        return obj


class Nest(object):
    def __init__(self, parent_key, keys_to_nest):
        self.parent_key = parent_key
        self.keys_to_nest = keys_to_nest

    def transform(self, obj):
        obj = obj.copy()
        nested_obj = {
            key: obj.pop(key)
            for key in self.keys_to_nest
            if key in obj
        }
        if self.parent_key in obj and isinstance(obj[self.parent_key], dict):
            obj[self.parent_key].update(nested_obj)
        else:
            obj[self.parent_key] = nested_obj
        return obj


class ValueTransformer(object):
    def __init__(self, key):
        self.key = key

    def transform(self, obj):
        obj = obj.copy()
        if self.key in obj:
            obj[self.key] = self.transform_value(obj[self.key])
        return obj

    def transform_value(self, value):
        return value


class Listify(ValueTransformer):
    def transform_value(self, value):
        if isinstance(value, list):
            return value
        else:
            return [value]


class Chain(object):
    def __init__(self, transformers):
        self.transformers = transformers

    def transform(self, obj):
        for transformer in self.transformers:
            obj = transformer.transform(obj)
        return obj


class Context(ValueTransformer):
    def __init__(self, key, transformer):
        super(Context, self).__init__(key)
        self.transformer = transformer

    def transform_value(self, value):
        if isinstance(value, list):
            return [
                self.transformer.transform(element)
                for element in value
            ]
        else:
            return self.transformer.transform(value)


class DeepKeyTransformer(object):
    def transform(self, obj):
        return {
            self.transform_key(key): self.transform_value(value)
            for key, value in obj.iteritems()
        }

    def transform_key(self, key):
        return key

    def transform_value(self, value):
        if isinstance(value, list):
            return [self.transform(element) for element in value]
        if isinstance(value, dict):
            return self.transform(value)
        else:
            return value


class Underscore(DeepKeyTransformer):
    def transform_key(self, key):
        return inflection.underscore(key)


class Camelize(DeepKeyTransformer):
    def transform_key(self, key):
        return inflection.camelize(key)


class FlattenText(Chain):
    def __init__(self, key):
        super(FlattenText, self).__init__([
            Context(
                key,
                Chain([
                    Rename('#text', key),
                    Remove('@format'),
                    Remove('@type'),
                ])
            ),
            Flatten(key),
        ])
