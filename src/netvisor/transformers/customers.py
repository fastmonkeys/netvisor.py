from .primitives import (
    Chain,
    Context,
    Flatten,
    FlattenText,
    Listify,
    Nest,
    Rename,
    Remove,
    Underscore,
)


customer_list_response_transformer = Chain([
    Underscore(),
    Flatten('root'),               # REMOVE?
    Flatten('customer_list'),      # REMOVE?
    Remove('response_status'),     # REMOVE?
    Rename('customer', 'objects'),
    Listify('objects'),
    Context(
        'objects',
        Chain([
            Rename('netvisor_key', 'id'),
            Rename('organisation_identifier', 'business_code'),
            Remove('uri'),
        ])
    ),
])


get_customer_response_transformer = Chain([
    Underscore(),
    Flatten('root'),               # REMOVE?
    Remove('response_status'),     # REMOVE?
    Flatten('customer'),           # REMOVE?
    Flatten('customer_base_information'),
    Rename('internal_identifier', 'code'),
    Rename('external_identifier', 'business_code'),
    Rename('fax_number', 'fax'),
    Rename('home_page_uri', 'homepage'),
    Rename('phone_number', 'phone'),
    Rename('street_address', 'street'),
    Rename('post_number', 'postal_code'),
    Rename('city', 'post_office'),
    FlattenText('country'),
    Nest(
        'street_address',
        [
            'street',
            'postal_code',
            'post_office',
            'country'
        ]
    ),
    Rename('customer_finvoice_details', 'finvoice'),
    Context(
        'finvoice',
        Chain([
            Rename('finvoice_address', 'address'),
            Rename('finvoice_router_code', 'router_code'),
        ])
    ),
    Rename('customer_delivery_details', 'delivery_address'),
    Context(
        'delivery_address',
        Chain([
            Rename('delivery_name', 'name'),
            Rename('delivery_street_address', 'street'),
            Rename('delivery_post_number', 'postal_code'),
            Rename('delivery_city', 'post_office'),
        ])
    ),
    Rename('customer_contact_details', 'contact_person'),
    Context(
        'contact_person',
        Chain([
            Rename('contact_person', 'name'),
            Rename('contact_person_email', 'email'),
            Rename('contact_person_phone', 'phone'),
        ])
    ),
    Flatten('customer_additional_information'),
])
