import pytest
import logging as logger
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info('TEST: cteate new customer with email and password only.')

    random_info = generate_random_email_and_password()
    email = random_info['email']
    password = random_info['password']

    # create payload
    # payload = {'email': email, 'password': password}

    # make call
    customer_obj = CustomerHelper()
    customer_api_info = customer_obj.create_customer(email=email, password=password)

    import pdb; pdb.set_trace()

    # varify status code of the call

    # varify email in the response

    # varify customer is created in DB