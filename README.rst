Netvisor: Python API wrapper
============================

.. image:: https://secure.travis-ci.org/fastmonkeys/netvisor.py.png?branch=master
   :target: http://travis-ci.org/fastmonkeys/netvisor.py

This is a Python wrapper for the Netvisor API.

Installation
------------

You can install netvisor with pip::

    $ pip install netvisor

Usage
-----

Creating a Netvisor client::

    >>> netvisor = Netvisor(
    ...     host='http://koulutus.netvisor.fi'
    ...     sender='Test client',
    ...     partner_id='xxx_yyy',
    ...     partner_key='E2CEBB1966C7016730C70CA92CBB93DD',
    ...     customer_id='xx_yyyy_zz',
    ...     customer_key='7767899D6F5FB333784A2520771E5871',
    ...     organization_id='1967543-8',
    ...     language='EN'
    ... )


Resources
---------

* `Bug Tracker <http://github.com/fastmonkeys/netvisor.py/issues>`_
* `Code <http://github.com/fastmonkeys/netvisor.py>`_
* `Development Version <http://github.com/fastmonkeys/netvisor.py/zipball/master#egg=netvisor-dev>`_
