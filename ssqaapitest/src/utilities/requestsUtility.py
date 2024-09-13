import requests
import os
import json
from ssqaapitest.src.configs.hosts_config import API_HOSTS


class RequestsUtility:

    def __init__(self):

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]


    def post(self, endpoint, payload=None, headers=None):
        
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = self.base_url + endpoint

        response = requests.post(url=url, data=json.dumps(payload), headers=headers)
        import pdb; pdb.set_trace()

    def get(self):
        pass