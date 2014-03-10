from .primitives import (
    Chain,
    Context,
    Flatten,
    Listify,
    Nest,
    NormalizeBankStatus,
    NormalizeDecimalPoint,
    Rename,
    Remove,
    Underscore,
)


sales_payment_list_response_transformer = Chain([
    Underscore(),
    Flatten('root'),                 # REMOVE?
    Remove('response_status'),       # REMOVE?
    Flatten('sales_payment_list'),   # REMOVE?
    Rename('sales_payment', 'objects'),
    Listify('objects'),
    Context(
        'objects',
        Chain([
            Rename('netvisor_key', 'id'),
            Rename('sum', 'amount'),
            NormalizeDecimalPoint('amount'),
            Context(
                'bank_status_error_description',
                Chain([
                    Rename('@code', 'error_code'),
                    Rename('#text', 'error_description'),
                ])
            ),
            Flatten('bank_status_error_description'),
            NormalizeBankStatus('bank_status'),
            Rename('bank_status', 'is_ok'),
            Nest(
                'bank_status',
                ['is_ok', 'error_code', 'error_description']
            )
        ])
    )
])
