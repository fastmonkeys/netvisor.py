# -*- coding: utf-8 -*-
import datetime

import colander


class FinnishDate(colander.SchemaType):
    err_template = colander._('Invalid date')
    date_format = '%d.%m.%Y'

    def serialize(self, node, appstruct):
        if not appstruct:
            return colander.null

        if not isinstance(appstruct, datetime.date):
            raise colander.Invalid(
                node,
                colander._(
                    '"${val}" is not a date object',
                    mapping={'val': appstruct}
                )
            )

        return appstruct.strftime(self.date_format)

    def deserialize(self, node, cstruct):
        if not cstruct:
            return colander.null

        try:
            return datetime.datetime.strptime(cstruct, self.date_format).date()
        except ValueError as e:
            raise colander.Invalid(
                node,
                colander._(
                    self.err_template,
                    mapping={'val': cstruct, 'err': e}
                )
            )
