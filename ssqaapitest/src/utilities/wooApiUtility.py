import os
import logging as logger
from woocommerce import API
from ssqaapitest.src.configs.hosts_config import WOO_API_HOSTS
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility
import pdb


class WooApiUtility:

    def __init__(self):

        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]

        self.wcapi = API(
        url=self.base_url,
        consumer_key=wc_creds['wc_key'],
        consumer_secret=wc_creds["wc_secret"],
        version="wc/v3",
        timeout=20
    )   
        

    def assert_status_code(self):

        assert self.status_code == self.expected_status_code, (
            f'Bad Status Code. Expected {self.expected_status_code}. Actual status code: {self.status_code} '
            f'URL: {self.wc_endpoint}. Response JSON: {self.response_json}'
        )

    
    def get(self, wc_endpoint, params=None, expected_status_code=200):

        response = self.wcapi.get(wc_endpoint, params=params)

        self.status_code = response.status_code
        self.expected_status_code = expected_status_code
        self.response_json = response.json()
        self.wc_endpoint = wc_endpoint

        self.assert_status_code()

        logger.debug(f'API GET response: {self.response_json}')

        return self.response_json
    

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        response = self.wcapi.post(wc_endpoint, data=params)

        self.status_code = response.status_code
        self.expected_status_code = expected_status_code
        self.response_json = response.json()
        self.wc_endpoint = wc_endpoint

        self.assert_status_code()

        logger.debug(f'API POST response: {self.response_json}')

        return self.response_json
    

    def put(self, wc_endpoint, params=None, expected_status_code=200):

        response = self.wcapi.put(wc_endpoint, data=params)

        self.status_code = response.status_code
        self.expected_status_code = expected_status_code
        self.response_json = response.json()
        self.wc_endpoint = wc_endpoint

        self.assert_status_code()

        logger.debug(f'API PUT response: {self.response_json}')

        return self.response_json



if __name__ == '__main__':

    obj = WooApiUtility()
    rs_api = obj.get('products')
    print(rs_api)
    import pdb; pdb.set_trace()