import requests
import os
import json
import pdb
import logging as logger
from requests_oauthlib import OAuth1
from ssqaapitest.src.configs.hosts_config import API_HOSTS
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility


class RequestsUtility:

    def __init__(self):

        wc_creds = CredentialsUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])


    def assert_status_code(self):

        assert self.status_code == self.expected_status_code, (
            f'Bad Status Code. Expected {self.expected_status_code}. Actual status code: {self.status_code}'
            f'URL: {self.url}. Response JSON: {self.response_json}'
        )


    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {'Content-Type': 'application/json'}
        self.url = self.base_url + endpoint

        response = requests.post(
            url=self.url, 
            data=json.dumps(payload),
            headers=headers,
            auth=self.auth,
        )
        self.status_code = response.status_code
        self.expected_status_code = expected_status_code
        self.response_json = response.json()

        self.assert_status_code()

        logger.debug(f'API response: {self.response_json}')

        return self.response_json


    def get(self):
        pass