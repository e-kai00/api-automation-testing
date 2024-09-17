import pytest
from ssqaapitest.src.utilities.genericUtilities import generate_random_string
from ssqaapitest.src.helpers.products_helper import ProductHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO
import pdb


@pytest.mark.products
@pytest.mark.tcid26
def test_create_1_simple_product():

    # genetate product data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'


    # make the api call
    product_response = ProductHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_response, f'Create product api response is empty. Payload: {payload}'
    assert product_response['name'] == payload['name'], (
        f'Create product api call response has unexpected name.'
        f'Expected: {payload["name"]}. Actual: {product_response["name"]}.'
    )

    # verify product exist in db
    product_id = product_response['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], (
        f'Create product, title in db does not match title in api.'
        f'DB: {db_product[0]["post_title"]}. API: {payload["name"]}'
    )
