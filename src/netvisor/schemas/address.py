# -*- coding: utf-8 -*-
import colander


class AddressSchema(colander.Schema):
    name = colander.SchemaNode(colander.String(), missing=u'')
    street = colander.SchemaNode(colander.String(), missing=u'')
    postal_code = colander.SchemaNode(colander.String(), missing=u'')
    post_office = colander.SchemaNode(colander.String(), missing=u'')
    country = colander.SchemaNode(colander.String(), missing=u'')
