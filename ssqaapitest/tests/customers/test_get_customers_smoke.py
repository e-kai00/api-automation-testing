import pytest
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger
import pdb


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():

    request_helper = RequestsUtility()
    response_api = request_helper.get('customers')
    
    assert response_api, f'Response of list all customers is emtpy.'
    # pdb.set_trace()
    
