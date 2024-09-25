import pytest
from ssqaapitest.src.helpers.orders_helpers import OrdersHelper
import pdb


@pytest.mark.tcid55
def test_update_order_status():

    new_status = 'cancelled'
    order_helper = OrdersHelper()

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
    rs_update = order_helper.call_update_order(order_id, payload)

    pdb.set_trace()

    # get order info

    # verify updated order status