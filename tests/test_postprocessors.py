import decimal
from datetime import date

import pytest
import xmltodict

from netvisor.postprocessors import (
    Boolean,
    Chain,
    Context,
    Date,
    Decimal,
    ExtractAttribute,
    Flatten,
    Integer,
    Listify,
    Nest,
    Remove,
    Rename,
    Underscore
)


class _TestPostProcessor(object):
    def test_processes_xml_correctly(self, postprocessor, xml, expected):
        data = xmltodict.parse(
            xml,
            postprocessor=postprocessor,
            dict_constructor=dict,
            xml_attribs=False
        )
        assert data == expected


class TestRename(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Rename('product_code', 'code')

    @pytest.fixture
    def xml(self):
        return '''
            <product>
                <product_code>CC</product_code>
                <product_group>Kirjat</product_group>
            </product>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product": {
                "code": "CC",
                "product_group": "Kirjat"
            }
        }


class TestRemove(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Remove('uri')

    @pytest.fixture
    def xml(self):
        return '''
            <product>
                <product_code>CC</product_code>
                <product_group>Kirjat</product_group>
                <uri>http://koulutus.netvisor.fi/getproduct.nv?id=165</uri>
            </product>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product": {
                "product_code": "CC",
                "product_group": "Kirjat",
            }
        }


class TestFlatten(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Flatten('customer_base_information')

    @pytest.fixture
    def xml(self):
        return '''
            <customer>
                <customer_base_information>
                    <name>John Smith</name>
                    <email>john@smith.net</email>
                </customer_base_information>
                <customer_delivery_details>
                    <delivery_street_address>
                        Pajukuja 90
                    </delivery_street_address>
                    <delivery_city>Lappeenranta</delivery_city>
                    <delivery_post_number>53100</delivery_post_number>
                </customer_delivery_details>
            </customer>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "customer": {
                "name": "John Smith",
                "email": "john@smith.net",
                "customer_delivery_details": {
                    "delivery_street_address": "Pajukuja 90",
                    "delivery_city": "Lappeenranta",
                    "delivery_post_number": "53100",
                }
            }
        }


class TestFlattenString(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Flatten('status')

    @pytest.fixture
    def xml(self):
        return '''
            <company>
                <status>open</status>
            </company>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "company": {
                "status": "open"
            }
        }


class TestNest(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Nest(
            'street_address',
            {
                'street': 'street',
                'postal_code': 'postal_code',
                'postal_office': 'postal_office',
            }
        )

    @pytest.fixture
    def xml(self):
        return '''
            <company>
                <business_code>1234567-8</business_code>
                <name>ACME</name>
                <street>Esimerkkikatu 123</street>
                <postal_code>00100</postal_code>
                <postal_office>Helsinki</postal_office>
            </company>
        '''

    @pytest.fixture
    def expected(self):
        return {
            'company': {
                'business_code': '1234567-8',
                'name': 'ACME',
                'street_address': {
                    'street': 'Esimerkkikatu 123',
                    'postal_code': '00100',
                    'postal_office': 'Helsinki',
                }
            }
        }


class TestNestAddsToExistingDict(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Nest(
            'street_address',
            {
                'street': 'street',
                'postal_code': 'postal_code',
                'postal_office': 'postal_office',
            }
        )

    @pytest.fixture
    def xml(self):
        return '''
            <company>
                <street>Esimerkkikatu 123</street>
                <postal_code>00100</postal_code>
                <postal_office>Helsinki</postal_office>
                <street_address>
                    <country>FI</country>
                </street_address>
            </company>
        '''

    @pytest.fixture
    def expected(self):
        return {
            'company': {
                'street_address': {
                    'street': 'Esimerkkikatu 123',
                    'postal_code': '00100',
                    'postal_office': 'Helsinki',
                    'country': 'FI'
                }
            }
        }


class TestNestCanNestKeyWithSameNameAsParent(object):
    @pytest.fixture
    def postprocessor(self):
        return Nest(
            'street_address',
            {
                'street': 'street_address',
                'postal_code': 'post_number',
                'postal_office': 'city',
            }
        )

    @pytest.fixture
    def xml(self):
        return '''
            <company>
              <street_address>Pajukuja 2</street_address>
              <city>Lappeenranta</city>
              <post_number>53100</post_number>
            </company>
        '''

    @pytest.fixture
    def expected(self):
        return {
            'company': {
                'street_address': {
                    'street': 'Esimerkkikatu 123',
                    'post_office': 'Lappeenrata',
                    'postal_code': '53100'
                }
            }
        }


class TestListifyEmptyList(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Listify('product_list', 'product')

    @pytest.fixture
    def xml(self):
        return '''
            <product_list/>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product_list": []
        }


class TestListifyListWithOneItem(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Listify('product_list', 'product')

    @pytest.fixture
    def xml(self):
        return '''
            <product_list>
                <product>
                    <name>Testituote</name>
                    <code>TT</code>
                </product>
            </product_list>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product_list": [
                {
                    "code": "TT",
                    "name": "Testituote"
                }
            ]
        }


class TestListifyListWithTwoItems(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Listify('product_list', 'product')

    @pytest.fixture
    def xml(self):
        return '''
            <product_list>
                <product>
                    <name>Testituote</name>
                    <code>TT</code>
                </product>
                <product>
                    <name>Demotuote</name>
                    <code>DT</code>
                </product>
            </product_list>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product_list": [
                {
                    "code": "TT",
                    "name": "Testituote"
                },
                {
                    "code": "DT",
                    "name": "Demotuote"
                }
            ]
        }


class TestUnderscore(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Underscore()

    @pytest.fixture
    def xml(self):
        return '''
            <ProductList>
                <Product>
                    <ProductCode>CC</ProductCode>
                    <ProductGroup>Kirjat</ProductGroup>
                </Product>
                <Product>
                    <ProductCode>DH</ProductCode>
                    <ProductGroup>Kirjat</ProductGroup>
                </Product>
            </ProductList>
        '''

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


class TestChain(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Chain([
            Remove('netvisor_key'),
            Rename('product_code', 'code'),
            Rename('product_group', 'group'),
            Remove('product_group'),
        ])

    @pytest.fixture
    def xml(self):
        return '''
            <product>
                <netvisor_key>165</netvisor_key>
                <product_code>CC</product_code>
                <product_group>Kirjat</product_group>
            </product>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product": {
                "code": "CC",
                "group": "Kirjat"
            }
        }


class TestContext(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Context(['product', 'group', 'name'], Remove('name'))

    @pytest.fixture
    def xml(self):
        return '''
            <product>
                <name>Code Complete</name>
                <group>
                    <id>123</id>
                    <name>Kirjat</name>
                </group>
            </product>
        '''

    @pytest.fixture
    def expected(self):
        return {
            "product": {
                "name": "Code Complete",
                "group": {
                    "id": '123'
                }
            }
        }


class TestIntegerWithEmptyValue(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Integer('netvisor_key')

    @pytest.fixture
    def xml(self):
        return '<netvisor_key/>'

    @pytest.fixture
    def expected(self):
        return {'netvisor_key': None}


class TestIntegerWithIntegerNumber(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Integer('netvisor_key')

    @pytest.fixture
    def xml(self):
        return '<netvisor_key>165</netvisor_key>'

    @pytest.fixture
    def expected(self):
        return {'netvisor_key': 165}


class TestBooleanWithEmptyValue(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Boolean('is_active')

    @pytest.fixture
    def xml(self):
        return '<is_active/>'

    @pytest.fixture
    def expected(self):
        return {'is_active': None}


class TestBooleanWithZeroesAndOnes(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Chain([
            Boolean('is_active'),
            Boolean('is_passive')
        ])

    @pytest.fixture
    def xml(self):
        return '''
            <booleans>
                <is_active>1</is_active>
                <is_passive>0</is_passive>
            </booleans>
        '''

    @pytest.fixture
    def expected(self):
        return {
            'booleans': {
                'is_active': True,
                'is_passive': False,
            }
        }


class TestBooleanWithCustomTrueAndFalseValues(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Chain([
            Boolean('is_active', true=['Yes'], false=['No']),
            Boolean('is_passive', true=['Yes'], false=['No'])
        ])

    @pytest.fixture
    def xml(self):
        return '''
            <booleans>
                <is_active>Yes</is_active>
                <is_passive>No</is_passive>
            </booleans>
        '''

    @pytest.fixture
    def expected(self):
        return {
            'booleans': {
                'is_active': True,
                'is_passive': False,
            }
        }


class TestDateWithEmptyValue(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Date('date')

    @pytest.fixture
    def xml(self):
        return '<date/>'

    @pytest.fixture
    def expected(self):
        return {'date': None}


class TestDateWithDateNumber(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Date('date')

    @pytest.fixture
    def xml(self):
        return '<date>2014-05-12</date>'

    @pytest.fixture
    def expected(self):
        return {'date': date(2014, 5, 12)}


class TestDecimalWithEmptyValue(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Decimal('unit_price')

    @pytest.fixture
    def xml(self):
        return '<unit_price/>'

    @pytest.fixture
    def expected(self):
        return {'unit_price': None}


class TestDecimalWithDecimalNumber(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return Decimal('unit_price')

    @pytest.fixture
    def xml(self):
        return '<unit_price>1,96</unit_price>'

    @pytest.fixture
    def expected(self):
        return {'unit_price': decimal.Decimal('1.96')}


class TestExtractAttribute(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return ExtractAttribute(
            key='unit_price',
            attr='Type',
            attr_key='type',
            cdata_key='price'
        )

    @pytest.fixture
    def xml(self):
        return '<unit_price Type="brutto">1,96</unit_price>'

    @pytest.fixture
    def expected(self):
        return {
            'unit_price': {
                'price': '1,96',
                'type': 'brutto'
            }
        }


class TestExtractAttributeWhenAttributeMissing(_TestPostProcessor):
    @pytest.fixture
    def postprocessor(self):
        return ExtractAttribute(
            key='unit_price',
            attr='Type',
            attr_key='type',
            attr_default='netto',
            cdata_key='price',
        )

    @pytest.fixture
    def xml(self):
        return '<unit_price>1,96</unit_price>'

    @pytest.fixture
    def expected(self):
        return {
            'unit_price': {
                'price': '1,96',
                'type': 'netto'
            }
        }
