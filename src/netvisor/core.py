# -*- coding: utf-8 -*-
"""
    netvisor.core
    ~~~~~~~~~~~~~

    :copyright: (c) 2013 by Janne Vanhala.
    :license: BSD, see LICENSE for more details.
"""

import requests

from .auth import NetvisorAuth


class Netvisor(object):
    def __init__(self, host, **kwargs):
        self.host = host
        self._session = requests.Session()
        self._session.auth = NetvisorAuth(**kwargs)
