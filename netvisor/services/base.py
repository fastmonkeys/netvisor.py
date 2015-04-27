# -*- coding: utf-8 -*-
"""
    netvisor.services.base
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""


class Service(object):
    def __init__(self, client):
        self.client = client
