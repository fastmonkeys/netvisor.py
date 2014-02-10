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


company_list_response_transformer = Chain([
    Underscore(),
    Flatten('root'),               # REMOVE?
    Flatten('company_list'),       # REMOVE?
    Remove('response_status'),     # REMOVE?
    Rename('company', 'companies'),
    Listify('companies'),
    Context(
        'companies',
        Chain([
            Remove('id'),
            Rename('finnish_organization_identifier', 'business_code'),
        ])
    ),
    Remove('is_more'),
])


get_company_information_response_transformer = Chain([
    Underscore(),
    Flatten('root'),                   # REMOVE?
    Flatten('company_information'),    # REMOVE?
    Remove('netvisor_disclaimer'),     # REMOVE?
    Flatten('company'),                # REMOVE?
    Rename('finnish_organization_identifier', 'business_code'),
    FlattenText('established_date'),
    FlattenText('terminated_date'),
    FlattenText('most_recent_change_date'),
    Context(
        'street_address',
        Rename('postal_office', 'post_office')
    ),
    Context(
        'postal_address',
        Rename('postal_office', 'post_office')
    ),
    Context(
        'registered_names',
        Chain([
            Context(
                'registered_name',
                Chain([
                    FlattenText('established_date'),
                    FlattenText('terminated_date'),
                ])
            ),
            Rename('registered_name', 'registered_names'),
            Listify('registered_names'),
        ])
    ),
    Flatten('registered_names'),
    Context(
        'registered_person_roles',
        Chain([
            Context(
                'role',
                Chain([
                    FlattenText('established_date'),
                    FlattenText('nationality')
                ])
            ),
            Listify('role'),
            Rename('role', 'registered_person_roles'),
        ])
    ),
    Flatten('registered_person_roles'),
    Rename('stat_employer_register_status', 'employer_register_status'),
    Rename('stat_revenue_size', 'revenue_size'),
    Rename('stat_staff_size', 'staff_size'),
    Rename('stat_vat_register_status', 'vat_register_status'),
    Rename(
        'stat_standard_industrial_classification2008',
        'standard_industrial_classification2008'
    ),
    Rename(
        'stat_tax_prepayment_register_status',
        'tax_prepayment_register_status'
    ),
    Nest(
        'stats',
        [
            'employer_register_status',
            'revenue_size',
            'staff_size',
            'vat_register_status',
            'standard_industrial_classification2008',
            'tax_prepayment_register_status',
        ]
    )
])
