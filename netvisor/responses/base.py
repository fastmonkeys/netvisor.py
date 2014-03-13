# -*- coding: utf-8 -*-
"""
    netvisor.responses.base
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
import xmltodict

from ..exc import NetvisorError


class Response(object):
    postprocessor = None

    def __init__(self, response):
        self.response = response
        self.data = self.parse()

    def parse(self):
        return xmltodict.parse(
            self.response.text,
            postprocessor=self.postprocessor,
            xml_attribs=False
        )

    def raise_for_failure(self):
        if not self.is_ok:
            raise NetvisorError.from_status(self.statuses[1])

    @property
    def statuses(self):
        return self.data['root']['response_status']['status']

    @property
    def is_ok(self):
        return self.statuses == 'OK'
