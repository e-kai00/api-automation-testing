import pytest
import pdb
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
     
    request_helper = RequestsUtility()
    response = request_helper.get(endpoint='products')

    assert response, f'Response of list all products is emtpy.'

    # pdb.set_trace()


@pytest.mark.tcid25
def test_get_product_by_id():

    # get a product (test data) from db
    random_product = ProductsDAO().get_random_product_from_db(1)
    random_product_id = random_product[0]['ID']
    db_name = random_product[0]['post_title']


    # make the call
    product_helper = ProductHelper()
    response = product_helper.get_product_by_id(random_product_id)
    response_api_name = response['name']


    # varify the response
    assert db_name == response_api_name, (
        f'Get product by id returned wrong product.'
        f'Id: {random_product_id}. DB name: {db_name}, API name: {response_api_name}'
    )
    