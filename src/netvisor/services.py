from .exc import InvalidData
from .responses.companies import GetCompanyInformationResponse, CompanyListResponse
from .responses.customers import GetCustomerResponse, CustomerListResponse
from .responses.products import GetProductResponse, ProductListResponse
from .responses.sales_invoices import GetSalesInvoiceResponse, SalesInvoiceListResponse
from .responses.sales_payments import SalesPaymentListResponse


class Service(object):
    def __init__(self, client):
        self.client = client


class CompanyService(Service):
    def get(self, business_code):
        params = {'OrganizationIdentifier': business_code}
        response = self.client.get('GetCompanyInformation.nv', params=params)
        response = GetCompanyInformationResponse(response)
        return response.data['root']['company']

    def list(self, query):
        params = {'QueryTerm': query}
        response = self.client.get('CompanyList.nv', params=params)
        response = CompanyListResponse(response)
        return response.data['root']['company_list']


class CustomerService(Service):
    def get(self, id):
        response = self.client.get('GetCustomer.nv', params={'id': id})
        response = GetCustomerResponse(response)
        return response.data['root']['customer']

    def list(self, query=None):
        response = self.client.get('CustomerList.nv', params={'Keyword': query})
        response = CustomerListResponse(response)
        return response.data['root']['customer_list']


class ProductService(Service):
    def get(self, id):
        response = self.client.get('GetProduct.nv', params={'id': id})
        response = GetProductResponse(response)
        if not response.data['root']['product']:
            raise InvalidData(
                'Data form incorrect:. '
                'Customer not found with Netvisor identifier: {0}'.format(id)
            )
        return response.data['root']['product']

    def list(self):
        response = self.client.get('ProductList.nv')
        response = ProductListResponse(response)
        return response.data['root']['product_list']


class SalesInvoiceService(Service):

    def get(self, id):
        response = self.client.get('GetSalesInvoice.nv', params={'NetvisorKey': id})
        response = GetSalesInvoiceResponse(response)
        return response.data['root']['sales_invoice']

    def list(self):
        response = self.client.get('SalesInvoiceList.nv')
        response = SalesInvoiceListResponse(response)
        return response.data['root']['sales_invoice_list']


class OrderService(Service):
    def list(self):
        response = self.client.get('SalesInvoiceList.nv', params={'ListType': 'preinvoice'})
        response = SalesInvoiceListResponse(response)
        return response.data['root']['sales_invoice_list']


class SalesPaymentService(Service):
    def list(self):
        response = self.client.get('SalesPaymentList.nv')
        response = SalesPaymentListResponse(response)
        return response.data['root']['sales_payment_list']
