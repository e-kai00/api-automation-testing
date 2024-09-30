import pytest
from ssqaapitest.src.helpers.orders_helpers import OrdersHelper
import pdb


@pytest.mark.regression
@pytest.mark.parametrize("new_status", [
    pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
    pytest.param('completed', marks=pytest.mark.tcid56),
    pytest.param('on-hold', marks=pytest.mark.tcid57),
])
def test_update_order_status(new_status):

    order_helper = OrdersHelper()

    pdb.set_trace()

    # create a new order
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
