from .exc import InvalidData
from .schemas.company import GetCompanyInformationSchema, CompanyListSchema
from .schemas.customer import CustomerListSchema, GetCustomerSchema
from .schemas.product import GetProductSchema, ProductListSchema
from .schemas.sales_invoice import (
    GetSalesInvoiceSchema,
    SalesInvoiceListSchema,
)
from .schemas.sales_payment import SalesPaymentListSchema
from .transformers.companies import (
    company_list_response_transformer,
    get_company_information_response_transformer,
)
from .transformers.customers import (
    customer_list_response_transformer,
    get_customer_response_transformer,
)
from .transformers.products import (
    get_product_response_transformer,
    product_list_response_transformer,
)
from .transformers.sales_invoices import (
    get_sales_invoice_response_transformer,
    sales_invoice_list_response_transformer,
)
from .transformers.sales_payments import (
    sales_payment_list_response_transformer,
)


class Service(object):

    def __init__(self, client):
        self.client = client


class CompanyService(Service):

    def get(self, business_code):
        params = {'OrganizationIdentifier': business_code}
        response = self.client.get('GetCompanyInformation.nv', params=params)
        data = get_company_information_response_transformer.transform(response.data)
        schema = GetCompanyInformationSchema()
        return schema.deserialize(data)

    def list(self, query):
        params = {'QueryTerm': query}
        response = self.client.get('CompanyList.nv', params=params)
        data = company_list_response_transformer.transform(response.data)
        schema = CompanyListSchema()
        return schema.deserialize(data)['objects']


class CustomerService(Service):

    def get(self, id):
        response = self.client.get('GetCustomer.nv', params={'id': id})
        data = get_customer_response_transformer.transform(response.data)
        schema = GetCustomerSchema()
        return schema.deserialize(data)

    def list(self, query=None):
        response = self.client.get('CustomerList.nv', params={'Keyword': query})
        data = customer_list_response_transformer.transform(response.data)
        schema = CustomerListSchema()
        return schema.deserialize(data)['objects']


class ProductService(Service):

    def get(self, id):
        response = self.client.get('GetProduct.nv', params={'id': id})
        if not response.data['Root']['Product']:
            raise InvalidData(
                'Data form incorrect:. '
                'Customer not found with Netvisor identifier: {0}'.format(id)
            )
        data = get_product_response_transformer.transform(response.data)
        schema = GetProductSchema()
        return schema.deserialize(data)

    def list(self):
        response = self.client.get('ProductList.nv')
        data = product_list_response_transformer.transform(response.data)
        schema = ProductListSchema()
        return schema.deserialize(data)['objects']


class SalesInvoiceService(Service):

    def get(self, id):
        response = self.client.get('GetSalesInvoice.nv', params={'NetvisorKey': id})
        data = get_sales_invoice_response_transformer.transform(response.data)
        schema = GetSalesInvoiceSchema()
        return schema.deserialize(data)

    def list(self):
        response = self.client.get('SalesInvoiceList.nv')
        data = sales_invoice_list_response_transformer.transform(response.data)
        schema = SalesInvoiceListSchema()
        return schema.deserialize(data)['objects']


class OrderService(Service):
    def list(self):
        response = self.client.get('SalesInvoiceList.nv', params={'ListType': 'preinvoice'})
        data = sales_invoice_list_response_transformer.transform(response.data)
        schema = SalesInvoiceListSchema()
        return schema.deserialize(data)['objects']


class SalesPaymentService(Service):
    def list(self):
        response = self.client.get('SalesPaymentList.nv')
        data = sales_payment_list_response_transformer.transform(response.data)
        schema = SalesPaymentListSchema()
        return schema.deserialize(data)['objects']
