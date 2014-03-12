from ..postprocessors import (
    Boolean,
    Chain,
    Date,
    Flatten,
    Listify,
    Nest,
    Remove,
    Rename,
    Underscore,
)
from .base import Response


class CompanyListResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Listify('company_list', 'company'),
        Remove('id'),
        Rename('finnish_organization_identifier', 'business_code'),
        Boolean('is_active')
    ])


class GetCompanyInformationResponse(Response):
    postprocessor = Chain([
        Underscore(),
        Flatten('company_information'),
        Rename('finnish_organization_identifier', 'business_code'),
        Rename('current_activity_status', 'is_active'),
        Rename('postal_office', 'post_office'),
        Rename('current_activity_status', 'is_active'),
        Boolean('is_active', true=[u'active'], false=[u'inactive']),
        Date('established_date'),
        Date('most_recent_change_date'),
        Date('terminated_date'),
        Date('prh_data_updated_date'),
        Date('statistics_finland_data_updated_date'),
        Listify('registered_person_roles', 'role'),
        Listify('registered_names', 'registered_name'),
        Nest(
            'stats',
            {
                'employer_register_status': 'stat_employer_register_status',
                'revenue_size': 'stat_revenue_size',
                'staff_size': 'stat_staff_size',
                'vat_register_status': 'stat_vat_register_status',
                'standard_industrial_classification2008': (
                    'stat_standard_industrial_classification2008'
                ),
                'tax_prepayment_register_status': (
                    'stat_tax_prepayment_register_status'
                ),
            }
        )
    ])
