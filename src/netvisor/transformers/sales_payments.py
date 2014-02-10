from .primitives import (
    Chain,
    Context,
    Flatten,
    Listify,
    Nest,
    Rename,
    Remove,
    Underscore,
)


sales_payment_list_response_transformer = Chain([
    Underscore(),
    Flatten('root'),                 # REMOVE?
    Remove('response_status'),       # REMOVE?
    Flatten('sales_payment_list'),   # REMOVE?
    Rename('sales_payment', 'sales_payments'),
    Listify('sales_payments'),
    Context(
        'sales_payments',
        Chain([
            Rename('sum', 'amount'),
            Context(
                'bank_status_error_description',
                Chain([
                    Rename('@code', 'error_code'),
                    Rename('#text', 'error_description'),
                ])
            ),
            Flatten('bank_status_error_description'),
            Rename('bank_status', 'status'),
            Nest(
                'bank_status',
                ['status', 'error_code', 'error_description']
            )
        ])
    )
])
