Changelog
---------

Here you can see the full list of changes between each Unistorage release.


0.3.1 (April 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed `netvisor.schemas` package missing from the source distribution.

0.3.0 (April 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Added official Python 3.4 support.
- Added creating and updating of customers and sales invoices.
- Changed response parsing not to rename and restructure the responses to keep
  the Python API implementation simpler and more consistent with the Netvisor
  API's XML responses.
- Changed response parsing to use Marshmallow.
- Changed `Request` to take `params` as a single keyword argument instead of
  as named variable-length arguments.
- Fixed tests to work with responses 0.3.0.

0.2.0 (April 8th, 2014)
^^^^^^^^^^^^^^^^^^^^^^^

- Added support for InvoiceNumber and InvoicesAboveNetvisorKey parameters to
  sales invoice listing.
- Changed xmltodict's dict constructor from `OrderedDict` to to `dict`.
- Fixed parsing of sales invoice with multiple lines.

0.1.0 (March 26th, 2014)
^^^^^^^^^^^^^^^^^^^^^^^^

- Initial public release.
