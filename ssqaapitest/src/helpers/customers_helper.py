from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper:

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        self.request_utility.post('customers', payload=payload)

        return True