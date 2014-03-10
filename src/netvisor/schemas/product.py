# -*- coding: utf-8 -*-
import colander


class InventorySchema(colander.Schema):
    mid_price = colander.SchemaNode(colander.Decimal())
    amount = colander.SchemaNode(colander.Decimal())
    ordered_amount = colander.SchemaNode(colander.Decimal())
    value = colander.SchemaNode(colander.Decimal())
    reserved_amount = colander.SchemaNode(colander.Decimal())


class ProductListProductSchema(colander.Schema):
    id = colander.SchemaNode(colander.Int())
    code = colander.SchemaNode(colander.String())
    name = colander.SchemaNode(colander.String())
    unit_price = colander.SchemaNode(colander.Decimal())
    unit_price_type = colander.SchemaNode(colander.String(), missing=u'netto')


class ProductListProductsSchema(colander.SequenceSchema):
    product = ProductListProductSchema()


class ProductListSchema(colander.Schema):
    objects = ProductListProductsSchema()


class GetProductSchema(ProductListProductSchema):
    group = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(colander.String())
    unit = colander.SchemaNode(colander.String())
    unit_weight = colander.SchemaNode(colander.Decimal())
    purchase_price = colander.SchemaNode(colander.Decimal())
    tariff_heading = colander.SchemaNode(colander.String())
    commission_percentage = colander.SchemaNode(colander.Decimal())
    is_active = colander.SchemaNode(colander.Boolean())
    is_sales_product = colander.SchemaNode(colander.Boolean())
    default_vat_percentage = colander.SchemaNode(colander.Decimal())
    default_domestic_account_number = colander.SchemaNode(
        colander.String(),
        missing=u''
    )
    default_eu_account_number = colander.SchemaNode(
        colander.String(),
        missing=u''
    )
    default_outside_eu_account_number = colander.SchemaNode(
        colander.String(),
        missing=u''
    )
    inventory = InventorySchema()
