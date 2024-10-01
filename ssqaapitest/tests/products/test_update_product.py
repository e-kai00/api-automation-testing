import pytest
import random
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductHelper
from ssqaapitest.src.utilities.genericUtilities import generate_random_string
import pdb


pytestmark = [pytest.mark.products]


@pytest.mark.tcid61
def test_update_procuct_regular_price():

    product_helper = ProductHelper()
    product_dao = ProductsDAO()

    # retrive product
    random_product = product_dao.get_random_product_from_db(1)
    product_id = random_product[0]['ID']

    # if product on sale, remove sale_price otherwise price won't update
    product_data = product_helper.call_retrieve_product(product_id)
    if product_data['on_sale']:
        product_helper.call_update_product(product_id, {'sale_price': ''})    

    # update price
    new_price = str(random.randint(10, 99)) + '.' + str(random.randint(10, 99))
    payload = {
        'regular_price': new_price
    }
    response = product_helper.call_update_product(product_id, payload=payload)

    # verify updated price
    assert response['price'] == new_price, (
        f"Update product api call response. "
        f"Updating the 'reqular_price' did not update 'price' field. "
        f"Expected value: {new_price}. Actual value: {response['price']}."
    )

    assert response['regular_price'] == new_price, (
        f"Update product api call response. "
        f"Updating the 'reqular_price' did not update in the response. "
        f"Expected value: {new_price}. Actual value: {response['regular_price']}."
    )
    

@pytest.mark.tcid63
@pytest.mark.tcid64
def test_update_product_on_sale_field():
    
    product_helper = ProductHelper()

    regular_price = str(random.randint(10, 99)) + '.' + str(random.randint(10, 99))
    sale_price = float(regular_price) * .75

    # create product
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = regular_price

    new_product = product_helper.call_create_product(payload=payload)

    assert new_product['sale_price'] == '', (
        f"Sale_price in api response has unexpected value. "
        f"Expected value: ''. Actual value: {new_product['sale_price']}. Product id: {product_id}"
    )
    assert not new_product['on_sale'], (
        f"On_sale field is expected to be False, but got: {new_product['on_sale']}"
    )

    # (tcid63) update sale price > 0 and veryfy on_sale set to True
    product_id = new_product['id']
    payload = {'sale_price': str(sale_price)}
    response_api = product_helper.call_update_product(product_id, payload=payload)

    assert response_api['on_sale'], (
        f"Update sale_price did not set on_sale to True. "
    )
    assert response_api['sale_price'] == str(sale_price), (
        f"Update sale_price did not update the field. "
        f"Expected sale_price: {sale_price}. Actual sale_price: {response_api['sale_price']}"
    )

     # (tcid64) update sale_price to empty string and veryfy on_sale set to False
    payload = {'sale_price': ''}
    response_api = product_helper.call_update_product(product_id, payload=payload)

    assert not response_api['on_sale'], (
        f"Updated sale_price='', but the on_sale did not set to False. "
        f"Product id: {product_id}"
    )
    assert not response_api['sale_price'], (
        f"Updated sale_price='', but sale_price in the api response: {response_api['sale_price']} "
        f"Product id: {product_id}"
    )