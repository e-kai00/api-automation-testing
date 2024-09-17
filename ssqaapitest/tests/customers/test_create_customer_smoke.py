import pytest
import logging as logger
import pdb
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.dao.customers_dao import CustomerDAO


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info('TEST: cteate new customer with email and password only.')

    random_info = generate_random_email_and_password()
    email = random_info['email']
    password = random_info['password']

    # create payload
    # payload = {'email': email, 'password': password}

    # make the api call
    customer_obj = CustomerHelper()
    customer_api_info = customer_obj.create_customer(email=email, password=password)

    # varify email and first nanme in the response
    assert customer_api_info['email'] == email, f'Create Customer API returned wrong emai. Email: {email}'
    assert customer_api_info['first_name'] == '', f'Create Customer API returned value for first_name but it should be empty.'

    # varify customer is created in DB
    customer_dao = CustomerDAO()
    customer_info = customer_dao.get_customer_by_email(email)

    id_in_api = customer_api_info['id']
    id_in_db = customer_info[0]['ID']

    assert id_in_api == id_in_db, f'Create Customer response "id" is not the same as "ID" in database. Email: {email}'
