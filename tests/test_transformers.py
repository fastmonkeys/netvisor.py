from netvisor import transformers


class TestRename(object):
    def test_renames_matching_key(self):
        data = {
            "product_code": "CC",
            "product_group": "Kirjat"
        }
        transformer = transformers.Rename('product_code', 'code')
        assert transformer.transform(data) == {
            "code": "CC",
            "product_group": "Kirjat"
        }


class TestRemove(object):
    def test_removes_matching_key(self):
        data = {
            "product_code": "CC",
            "product_group": "Kirjat",
            "uri": "http://koulutus.netvisor.fi/getproduct.nv?id=165"
        }
        transformer = transformers.Remove('uri')
        assert transformer.transform(data) == {
            "product_code": "CC",
            "product_group": "Kirjat",
        }


class TestFlatten(object):
    def test_flattens_matching_key(self):
        data = {
            "customer_base_information": {
                "name": "John Smith",
                "email": "john@smith.net",
            },
            "customer_delivery_details": {
                "delivery_street_address": "Pajukuja 90",
                "delivery_city": "Lappeenranta",
                "delivery_post_number": "53100",
            }
        }
        transformer = transformers.Flatten(
            'customer_base_information'
        )
        assert transformer.transform(data) == {
            "name": "John Smith",
            "email": "john@smith.net",
            "customer_delivery_details": {
                "delivery_street_address": "Pajukuja 90",
                "delivery_city": "Lappeenranta",
                "delivery_post_number": "53100",
            }
        }


class TestListify(object):
    def test_makes_matching_keys_value_a_list(self):
        data = {
            "products": {
                "code": "TT",
                "name": "Testituote"
            }
        }
        transformer = transformers.Listify('products')
        assert transformer.transform(data) == {
            "products": [
                {
                    "code": "TT",
                    "name": "Testituote"
                }
            ]
        }

    def test_doesnt_touch_values_that_are_already_lists(self):
        data = {
            "products": [
                {
                    "code": "TT",
                    "name": "Testituote"
                }
            ]
        }
        transformer = transformers.Listify('products')
        assert transformer.transform(data) == {
            "products": [
                {
                    "code": "TT",
                    "name": "Testituote"
                }
            ]
        }


class TestUnderscore(object):
    def test_underscorifies_all_keys(self):
        data = {
            "ProductCode": "CC",
            "ProductGroup": "Kirjat"
        }
        transformer = transformers.Underscore()
        assert transformer.transform(data) == {
            "product_code": "CC",
            "product_group": "Kirjat",
        }

    def test_undescorifies_nested_dicts(self):
        data = {
            "Product": {
                "ProductCode": "CC",
                "ProductGroup": "Kirjat"
            }
        }
        transformer = transformers.Underscore()
        assert transformer.transform(data) == {
            "product": {
                "product_code": "CC",
                "product_group": "Kirjat",
            }
        }

    def test_undescorifies_listed_dicts(self):
        data = {
            "Products": [
                {
                    "ProductCode": "CC",
                    "ProductGroup": "Kirjat"
                },
                {
                    "ProductCode": "DH",
                    "ProductGroup": "Kirjat"
                }
            ]
        }
        transformer = transformers.Underscore()
        assert transformer.transform(data) == {
            "products": [
                {
                    "product_code": "CC",
                    "product_group": "Kirjat",
                },
                {
                    "product_code": "DH",
                    "product_group": "Kirjat",
                }
            ]
        }


class TestCamelize(object):
    def test_camelizes_all_keys(self):
        data = {
            "product_code": "CC",
            "product_group": "Kirjat"
        }
        transformer = transformers.Camelize()
        assert transformer.transform(data) == {
            "ProductCode": "CC",
            "ProductGroup": "Kirjat"
        }


class TestChain(object):
    def test_applies_given_transformers_in_order(self):
        data = {
            "product_code": "CC",
            "product_group": "Kirjat"
        }
        transformer = transformers.Chain([
            transformers.Rename('product_code', 'code'),
            transformers.Rename('product_group', 'group'),
            transformers.Remove('product_group'),
        ])
        assert transformer.transform(data) == {
            "code": "CC",
            "group": "Kirjat"
        }


class TestKey(object):
    def test_applies_transformer_to_given_keys_value(self):
        data = {
            "product": {
                "product_code": "CC",
                "product_group": "Kirjat"
            }
        }
        transformer = transformers.Key(
            'product',
            transformers.Rename(
                old_key='product_code',
                new_key='code'
            )
        )
        assert transformer.transform(data) == {
            "product": {
                "code": "CC",
                "product_group": "Kirjat"
            }
        }

    def test_applies_transformer_to_all_list_elements(self):
        data = {
            "products": [
                {
                    "product_code": "CC",
                    "product_group": "Kirjat"
                },
                {
                    "product_code": "DH",
                    "product_group": "Kirjat"
                },
            ]
        }
        transformer = transformers.Key(
            'products',
            transformers.Rename('product_code', 'code')
        )
        assert transformer.transform(data) == {
            "products": [
                {
                    "code": "CC",
                    "product_group": "Kirjat"
                },
                {
                    "code": "DH",
                    "product_group": "Kirjat"
                },
            ]
        }
