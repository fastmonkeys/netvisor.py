import xmltodict

from . import transformers as tf


class FlattenText(tf.Chain):
    def __init__(self, key):
        super(FlattenText, self).__init__([
            tf.Context(
                key,
                tf.Chain([
                    tf.Rename('#text', key),
                    tf.Remove('@format'),
                    tf.Remove('@type'),
                ])
            ),
            tf.Flatten(key),
        ])


class Response(object):
    transformer = None

    def __init__(self, content):
        self.content = content

    def parse(self):
        data = xmltodict.parse(self.content)
        return self.transformer.transform(data)


class CompanyListResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),               # REMOVE?
        tf.Flatten('company_list'),       # REMOVE?
        tf.Remove('response_status'),     # REMOVE?
        tf.Rename('company', 'companies'),
        tf.Listify('companies'),
        tf.Context(
            'companies',
            tf.Rename('finnish_organization_identifier', 'business_code')
        ),
        tf.Remove('is_more'),
    ])


class CustomerListResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),               # REMOVE?
        tf.Flatten('customer_list'),      # REMOVE?
        tf.Remove('response_status'),     # REMOVE?
        tf.Rename('customer', 'customers'),
        tf.Listify('customers'),
        tf.Context(
            'customers',
            tf.Chain([
                tf.Remove('uri'),
                tf.Rename('organisation_identifier', 'business_code')
            ])
        ),
    ])


class GetCompanyInformationResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),                   # REMOVE?
        tf.Flatten('company_information'),    # REMOVE?
        tf.Remove('netvisor_disclaimer'),     # REMOVE?
        tf.Flatten('company'),                # REMOVE?
        tf.Rename('finnish_organization_identifier', 'business_code'),
        FlattenText('established_date'),
        FlattenText('terminated_date'),
        FlattenText('most_recent_change_date'),
        tf.Context(
            'registered_names',
            tf.Chain([
                tf.Context(
                    'registered_name',
                    tf.Chain([
                        FlattenText('established_date'),
                        FlattenText('terminated_date'),
                    ])
                ),
                tf.Rename('registered_name', 'registered_names'),
                tf.Listify('registered_names'),
            ])
        ),
        tf.Flatten('registered_names'),
        tf.Context(
            'registered_person_roles',
            tf.Chain([
                tf.Context(
                    'role',
                    tf.Chain([
                        FlattenText('established_date'),
                        FlattenText('nationality')
                    ])
                ),
                tf.Listify('role'),
                tf.Rename('role', 'registered_person_roles'),
            ])
        ),
        tf.Flatten('registered_person_roles'),
    ])


class GetCustomerResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),               # REMOVE?
        tf.Remove('response_status'),     # REMOVE?
        tf.Flatten('customer'),           # REMOVE?
        tf.Flatten('customer_base_information'),
        tf.Rename('internal_identifier', 'code'),
        tf.Rename('external_identifier', 'business_code'),
        tf.Rename('fax_number', 'fax'),
        tf.Rename('home_page_uri', 'homepage'),
        tf.Rename('phone_number', 'phone'),
        tf.Rename('street_address', 'street'),
        tf.Rename('post_number', 'postal_code'),
        tf.Rename('city', 'post_office'),
        FlattenText('country'),
        tf.Nest(
            'street_address',
            [
                'street',
                'postal_code',
                'post_office',
                'country'
            ]
        ),
        tf.Rename('customer_finvoice_details', 'finvoice'),
        tf.Context(
            'finvoice',
            tf.Chain([
                tf.Rename('finvoice_address', 'address'),
                tf.Rename('finvoice_router_code', 'router_code'),
            ])
        ),
        tf.Rename('customer_delivery_details', 'delivery_address'),
        tf.Context(
            'delivery_address',
            tf.Chain([
                tf.Rename('delivery_name', 'name'),
                tf.Rename('delivery_street_address', 'street'),
                tf.Rename('delivery_post_number', 'postal_code'),
                tf.Rename('delivery_city', 'post_office'),
            ])
        ),
        tf.Rename('customer_contact_details', 'contact_person'),
        tf.Context(
            'contact_person',
            tf.Chain([
                tf.Rename('contact_person', 'name'),
                tf.Rename('contact_person_email', 'email'),
                tf.Rename('contact_person_phone', 'phone'),
            ])
        ),
        tf.Flatten('customer_additional_information'),
    ])


class GetProductResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),               # REMOVE?
        tf.Remove('response_status'),     # REMOVE?
        tf.Flatten('product'),            # REMOVE?
        tf.Flatten('product_base_information'),
        tf.Flatten('product_book_keeping_details'),
        tf.Rename('product_code', 'code'),
        tf.Rename('product_group', 'group'),
        tf.Context(
            'unit_price',
            tf.Chain([
                tf.Rename('#text', 'unit_price'),
                tf.Rename('@type', 'unit_price_type'),
            ])
        ),
        tf.Flatten('unit_price'),
        tf.Rename('comission_percentage', 'commission_percentage'),
        tf.Rename('product_inventory_details', 'inventory'),
        tf.Context(
            'inventory',
            tf.Chain([
                tf.Rename('inventory_amount', 'amount'),
                tf.Rename('inventory_mid_price', 'mid_price'),
                tf.Rename('inventory_value', 'value'),
                tf.Rename('inventory_reserved_amount', 'reserved_amount'),
                tf.Rename('inventory_ordered_amount', 'ordered_amount'),
            ])
        )
    ])


class GetSalesInvoiceResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),               # REMOVE?
        tf.Remove('response_status'),     # REMOVE?
        tf.Flatten('sales_invoice'),      # REMOVE?
        tf.Rename('sales_invoice_date', 'date'),
        tf.Rename('sales_invoice_delivery_date', 'delivery_date'),
        tf.Rename('sales_invoice_due_date', 'due_date'),
        FlattenText('date'),
        FlattenText('delivery_date'),
        FlattenText('due_date'),
        tf.Rename('sales_invoice_number', 'number'),
        tf.Rename('sales_invoice_our_reference', 'our_reference'),
        tf.Rename('sales_invoice_your_reference', 'your_reference'),
        tf.Nest(
            'delivery_address',
            [
                'delivery_address_name',
                'delivery_address_line',
                'delivery_address_postnumber',
                'delivery_address_town',
                'delivery_address_country_code',
            ]
        ),
        tf.Context(
            'delivery_address',
            tf.Chain([
                tf.Rename('delivery_address_name', 'name'),
                tf.Rename('delivery_address_line', 'street'),
                tf.Rename('delivery_address_postnumber', 'postal_code'),
                tf.Rename('delivery_address_town', 'post_office'),
                tf.Rename('delivery_address_country_code', 'country'),
            ])
        ),
        tf.Nest(
            'billing_address',
            [
                'invoicing_customer_name',
                'invoicing_customer_addressline',
                'invoicing_customer_postnumber',
                'invoicing_customer_town',
                'invoicing_customer_country_code',
            ]
        ),
        tf.Context(
            'billing_address',
            tf.Chain([
                tf.Rename('invoicing_customer_name', 'name'),
                tf.Rename('invoicing_customer_addressline', 'street'),
                tf.Rename('invoicing_customer_postnumber', 'postal_code'),
                tf.Rename('invoicing_customer_town', 'post_office'),
                tf.Rename('invoicing_customer_country_code', 'country'),
            ])
        ),
        tf.Rename('sales_invoice_referencenumber', 'reference_number'),
        tf.Rename('sales_invoice_amount', 'amount'),
        tf.Rename(
            'sales_invoice_free_text_after_lines',
            'free_text_after_lines'
        ),
        tf.Rename(
            'sales_invoice_free_text_before_lines',
            'free_text_before_lines'
        ),
        tf.Rename('sales_invoice_private_comment', 'private_comment'),
        tf.Rename('seller_identifier', 'seller_id'),
        FlattenText('seller_id'),
        FlattenText('payment_term_cash_discount'),
        tf.Rename('invoice_status', 'status'),
        tf.Flatten('invoice_lines'),
        tf.Flatten('invoice_line'),
        tf.Rename('sales_invoice_product_line', 'lines'),
        tf.Listify('lines'),
        tf.Context(
            'lines',
            tf.Chain([
                tf.Rename('productidentifier', 'product_code'),
                FlattenText('product_code'),
                tf.Rename('product_name', 'name'),
                tf.Rename('product_unit_price', 'unit_price'),
                tf.Rename('product_vat_percentage', 'vat_percentage'),
                tf.Context(
                    'vat_percentage',
                    tf.Chain([
                        tf.Rename('@vatcode', 'vat_code'),
                        tf.Rename('#text', 'vat_percentage'),
                    ])
                ),
                tf.Flatten('vat_percentage'),
                tf.Rename(
                    'sales_invoice_product_line_discount_percentage',
                    'discount_percentage'
                ),
                tf.Rename('sales_invoice_product_line_quantity', 'quantity'),
                tf.Rename('sales_invoice_product_line_free_text', 'free_text'),
                tf.Rename('sales_invoice_product_line_vat_sum', 'vat_amount'),
                tf.Rename('sales_invoice_product_line_sum', 'amount'),

                tf.Rename(
                    'accounting_account_suggestion',
                    'accounting_suggestion'
                )
            ])
        )
    ])


class ProductListResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),               # REMOVE?
        tf.Flatten('product_list'),       # REMOVE?
        tf.Remove('response_status'),     # REMOVE?
        tf.Rename('product', 'products'),
        tf.Listify('products'),
        tf.Context(
            'products',
            tf.Chain([
                tf.Remove('uri'),
                tf.Rename('product_code', 'code')
            ])
        ),
    ])


class SalesInvoiceListResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),                 # REMOVE?
        tf.Remove('response_status'),       # REMOVE?
        tf.Flatten('sales_invoice_list'),   # REMOVE?
        tf.Rename('sales_invoice', 'sales_invoices'),
        tf.Listify('sales_invoices'),
        tf.Context(
            'sales_invoices',
            tf.Chain([
                tf.Rename('invoice_number', 'number'),
                tf.Rename('invoice_date', 'date'),
                tf.Rename('invoice_sum', 'amount'),
                tf.Rename('open_sum', 'open_amount'),
                tf.Remove('customer_code'),
                tf.Remove('customer_name'),
                tf.Remove('uri'),
                FlattenText('date'),
                tf.Context(
                    'invoice_status',
                    tf.Chain([
                        tf.Rename('#text', 'status'),
                        tf.Rename('@substatus', 'substatus')
                    ])
                ),
                tf.Flatten('invoice_status'),
            ])
        )
    ])


class SalesPaymentListResponse(Response):
    transformer = tf.Chain([
        tf.Underscore(),
        tf.Flatten('root'),                 # REMOVE?
        tf.Remove('response_status'),       # REMOVE?
        tf.Flatten('sales_payment_list'),   # REMOVE?
        tf.Rename('sales_payment', 'sales_payments'),
        tf.Listify('sales_payments'),
        tf.Context(
            'sales_payments',
            tf.Chain([
                tf.Rename('sum', 'amount'),
                tf.Rename(
                    'bank_status_error_description',
                    'bank_status_error'
                ),
                tf.Context(
                    'bank_status_error',
                    tf.Chain([
                        tf.Rename('@code', 'code'),
                        tf.Rename('#text', 'description'),
                    ])
                )
            ])
        )
    ])
