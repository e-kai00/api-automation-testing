import pytest
from ssqaapitest.src.helpers.orders_helpers import OrdersHelper
from ssqaapitest.src.utilities.wooApiUtility import WooApiUtility
from ssqaapitest.src.utilities.genericUtilities import generate_random_string
import pdb


pytestmark = [pytest.mark.orders, pytest.mark.regression]

@pytest.mark.parametrize("new_status", [
    pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
    pytest.param('completed', marks=pytest.mark.tcid56),
    pytest.param('on-hold', marks=pytest.mark.tcid57),
])
def test_update_order_status(new_status):

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()

    # get current status of the order
    current_status = order_json['status']
    assert current_status != new_status, (
        f"Current status of the order is already {new_status}. "
        f"Unable to run test."
    )

    # update the status
    order_id = order_json['id']
    payload = {'status': new_status}
    order_helper.call_update_order(order_id, payload)

    # get order info
    new_order_info = order_helper.call_retrieve_order(order_id)
    
    # verify updated order status
    assert new_order_info['status'] == new_status, (
        f"Updated order status to '{new_status}', "
        f"but order is still '{new_order_info['status']}'."
    )


@pytest.mark.tcid58
def test_update_order_status_to_random_string():

    new_status = 'abcdefg'

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()   
    order_id = order_json['id']

    # update the status
    payload = {'status': new_status}
    response_api = WooApiUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)

    assert response_api['code'] == 'rest_invalid_param', (
        f"Update order status to random string did not have correct code in response. "
        f"Expected: 'rest_invalid_param'. Actual: {response_api['code']}."
    )
    assert response_api['message'] == 'Invalid parameter(s): status', (
        f"Update order status to random string did not have correct message in response. "
        f"Expected: 'Invalid parameter(s): status'. Actual: {response_api['message']}."
    )


@pytest.mark.tcid59
def test_update_order_customer_note():

    # create a new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()   
    order_id = order_json['id']

    # update the status
    random_string = generate_random_string(40)
    payload = {'customer_note': random_string}
    order_helper.call_update_order(order_id, payload)

    # get order info
    new_order_info = order_helper.call_retrieve_order(order_id)

    assert new_order_info['customer_note'] == random_string, (
        f"Update order 'customer_note' failed. "
        f"Expected: {random_string}. Actual: {new_order_info['customer_note']}."
    )


