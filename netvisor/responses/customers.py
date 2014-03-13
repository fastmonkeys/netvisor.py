# -*- coding: utf-8 -*-
"""
    netvisor.responses.customers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2014 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..postprocessors import (
    Boolean,
    Chain,
    Context,
    Decimal,
    Flatten,
    Integer,
    Listify,
    Nest,
    Remove,
    Rename,
    Underscore,
)
from .base import Response


class CustomerListResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Rename('customerlist', 'customer_list'),
        Listify('customer_list', 'customer'),
        Chain([
            Rename('netvisorkey', 'id'),
            Rename('organisation_identifier', 'business_code'),
            Remove('uri'),
            Integer('id')
        ])
    ])


class GetCustomerResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Flatten('customer_base_information'),
        Rename('internal_identifier', 'code'),
        Rename('external_identifier', 'business_code'),
        Rename('fax_number', 'fax'),
        Rename('home_page_uri', 'homepage'),
        Rename('phone_number', 'phone'),
        Rename('customer_finvoice_details', 'finvoice'),
        Rename('finvoice_address', 'address'),
        Rename('finvoice_router_code', 'router_code'),
        Rename('customer_delivery_details', 'delivery_address'),
        Rename('delivery_name', 'name'),
        Rename('delivery_street_address', 'street'),
        Rename('delivery_post_number', 'postal_code'),
        Rename('delivery_city', 'post_office'),
        Rename('contact_person', 'name'),
        Rename('contact_person_email', 'email'),
        Rename('contact_person_phone', 'phone'),
        Rename('customer_contact_details', 'contact_person'),
        Boolean('is_active'),
        Decimal('balance_limit'),
        Integer('customer_group_netvisor_key'),
        Nest(
            'group',
            {
                'id': 'customer_group_netvisor_key',
                'name': 'customer_group_name',
            }
        ),
        Context(
            ['Root', 'Customer'],
            Nest(
                'street_address',
                {
                    'street': 'street_address',
                    'postal_code': 'post_number',
                    'post_office': 'city',
                    'country': 'country',
                }
            )
        ),
        Flatten('customer_additional_information'),
    ])
