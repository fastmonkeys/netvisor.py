import pytest

from netvisor import transformers


class _TestTransformer(object):
    def test_transforms_data_correctly(self, transformer, data, expected):
        assert transformer.transform(data) == expected

    def test_transforming_transformed_data(self, transformer, expected):
        assert transformer.transform(expected) == expected

    def test_tranforming_returns_a_new_object(self, transformer, data):
        assert id(transformer.transform(data)) != id(data)


class TestRename(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Rename('product_code', 'code')

    @pytest.fixture
    def data(self):
        return {
            "product_code": "CC",
            "product_group": "Kirjat"
        }

    @pytest.fixture
    def expected(self):
        return {
            "code": "CC",
            "product_group": "Kirjat"
        }


class TestAdd(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Add('product_group', 'Kirjat')

    @pytest.fixture
    def data(self):
        return {
            "product_code": "CC",
        }

    @pytest.fixture
    def expected(self):
        return {
            "product_code": "CC",
            "product_group": "Kirjat",
        }


class TestRemove(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Remove('uri')

    @pytest.fixture
    def data(self):
        return {
            "product_code": "CC",
            "product_group": "Kirjat",
            "uri": "http://koulutus.netvisor.fi/getproduct.nv?id=165"
        }

    @pytest.fixture
    def expected(self):
        return {
            "product_code": "CC",
            "product_group": "Kirjat",
        }


class TestFlatten(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Flatten('customer_base_information')

    @pytest.fixture
    def data(self):
        return {
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

    @pytest.fixture
    def expected(self):
        return {
            "name": "John Smith",
            "email": "john@smith.net",
            "customer_delivery_details": {
                "delivery_street_address": "Pajukuja 90",
                "delivery_city": "Lappeenranta",
                "delivery_post_number": "53100",
            }
        }


class TestNest(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Nest(
            'street_address',
            [
                'street',
                'postal_code',
                'postal_office',
            ]
        )

    @pytest.fixture
    def data(self):
        return {
            'business_code': '1234567-8',
            'name': 'ACME',
            'street': 'Esimerkkikatu 123',
            'postal_code': '00100',
            'postal_office': 'Helsinki',
        }

    @pytest.fixture
    def expected(self):
        return {
            'business_code': '1234567-8',
            'name': 'ACME',
            'street_address': {
                'street': 'Esimerkkikatu 123',
                'postal_code': '00100',
                'postal_office': 'Helsinki',
            }
        }


class TestNestAddsToExistingDict(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Nest(
            'street_address',
            [
                'street',
                'postal_code',
                'postal_office',
            ]
        )

    @pytest.fixture
    def data(self):
        return {
            'street': 'Esimerkkikatu 123',
            'postal_code': '00100',
            'postal_office': 'Helsinki',
            'street_address': {
                'country': 'FI'
            }
        }

    @pytest.fixture
    def expected(self):
        return {
            'street_address': {
                'street': 'Esimerkkikatu 123',
                'postal_code': '00100',
                'postal_office': 'Helsinki',
                'country': 'FI'
            }
        }


class TestNestCanNestKeyWithSameNameAsParent(object):
    @pytest.fixture
    def transformer(self):
        return transformers.Nest('street_address', ['street_address'])

    @pytest.fixture
    def data(self):
        return {
            'street_address': 'Esimerkkikatu 123'
        }

    @pytest.fixture
    def expected(self):
        return {
            'street_address': {
                'street_address': 'Esimerkkikatu 123'
            }
        }

    def test_transforms_data_correctly(self, transformer, data, expected):
        assert transformer.transform(data) == expected


class TestListify(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Listify('products')

    @pytest.fixture
    def data(self):
        return {
            "products": {
                "code": "TT",
                "name": "Testituote"
            }
        }

    @pytest.fixture
    def expected(self):
        return {
            "products": [
                {
                    "code": "TT",
                    "name": "Testituote"
                }
            ]
        }


class TestListifyWithNonExistingKey(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Listify('products')

    @pytest.fixture
    def data(self):
        return {}

    @pytest.fixture
    def expected(self):
        return {}


class TestUnderscore(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Underscore()

    @pytest.fixture
    def data(self):
        return {
            "ProductList": {
                "Product": [
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
        }

    @pytest.fixture
    def expected(self):
        return {
            "product_list": {
                "product": [
                    {
                        "product_code": "CC",
                        "product_group": "Kirjat"
                    },
                    {
                        "product_code": "DH",
                        "product_group": "Kirjat"
                    }
                ]
            }
        }


class TestCamelize(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Camelize()

    @pytest.fixture
    def data(self):
        return {
            "product_list": {
                "product": [
                    {
                        "product_code": "CC",
                        "product_group": "Kirjat"
                    },
                    {
                        "product_code": "DH",
                        "product_group": "Kirjat"
                    }
                ]
            }
        }

    @pytest.fixture
    def expected(self):
        return {
            "ProductList": {
                "Product": [
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
        }


class TestChain(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Chain([
            transformers.Rename('product_code', 'code'),
            transformers.Rename('product_group', 'group'),
            transformers.Remove('product_group'),
        ])

    @pytest.fixture
    def data(self):
        return {
            "product_code": "CC",
            "product_group": "Kirjat"
        }

    @pytest.fixture
    def expected(self):
        return {
            "code": "CC",
            "group": "Kirjat"
        }


class TestContextWithDicts(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Context(
            'product',
            transformers.Rename('product_code', 'code')
        )

    @pytest.fixture
    def data(self):
        return {
            "product": {
                "product_code": "CC",
                "product_group": "Kirjat"
            }
        }

    @pytest.fixture
    def expected(self):
        return {
            "product": {
                "code": "CC",
                "product_group": "Kirjat"
            }
        }


class TestContextWithLists(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Context(
            'products',
            transformers.Rename('product_code', 'code')
        )

    @pytest.fixture
    def data(self):
        return {
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

    @pytest.fixture
    def expected(self):
        return {
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


class TestContextWithNonExistingKey(_TestTransformer):
    @pytest.fixture
    def transformer(self):
        return transformers.Context(
            'product',
            transformers.Rename('product_code', 'code')
        )

    @pytest.fixture
    def data(self):
        return {}

    @pytest.fixture
    def expected(self):
        return {}
