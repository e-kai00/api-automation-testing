from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger


class ProductHelper:

    def __init__(self):
        self.requests_utility = RequestsUtility()

    
    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f'products/{product_id}')
    

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)
    

    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f'List products page: {i}')

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # add currten page number to the call
            payload['page'] = i
            response = self.requests_utility.get('products', payload=payload)

            # if response is empty (not response), stop the loop
            if not response:
                break
            else:
                all_products.extend(response)

        else:
            raise Exception(f'Unable to find all products after {max_pages} pages.')

        return all_products
    

    def call_retrieve_product(self, product_id):
        return self.requests_utility.get(f'products/{product_id}')
    

    def call_update_product(self, product_id, payload=None):
        return self.requests_utility.put(f'products/{product_id}', payload=payload)