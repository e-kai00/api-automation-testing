import os
import json
from ssqaapitest.src.utilities.wooApiUtility import WooApiUtility
from ssqaapitest.src.dao.orders_dao import OrdersDAO



class OrdersHelper:

    def __init__(self):
        self.current_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooApiUtility()


    def create_order(self, additional_args=None):

        payload_template = os.path.join(self.current_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        # if user adds more info to payload, then update payload
        if additional_args:
            assert isinstance(additional_args, dict), f'Parameter "additional_arg" must be a dictionary but found {type(additional_args)}'
            
            payload.update(additional_args)

        response = self.woo_helper.post('orders', params=payload, expected_status_code=201)

        return response
    

    @staticmethod
    def verify_order_is_created(order_json, expected_customer_id, expected_products):

        orders_dao = OrdersDAO()

        # verify response
        assert order_json, f'Create order response is empty.'
        assert order_json['customer_id'] == expected_customer_id, (
            f"Create order with given customer id returned bas customer id. "
            f"Expected: {expected_customer_id} but got: {order_json['customer_id']}"
        )
        assert len(order_json['line_items']) == len(expected_products), (
            f"Expected only {len(expected_products)} item"
            f"but found: {len(order_json['line_items'])}."
            f"Order id: {order_json['id']}."
        )

        # verify db
        order_id = order_json['id']
        line_info = orders_dao.get_order_lines_by_order_id(order_id)

        assert line_info, f"Create order, line item not found in DB. Order id: {order_id}"

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']

        assert len(line_items) == 1, f"Expected 1 line item but found {len(line_items)}. Order id {order_id}."

        # get list of product IDs in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in expected_products:
            assert product['product_id'] in api_product_ids, (
                f"Create order does not have at least 1 expected product in DB. "
                f"Product id: {product['product_id']}. Order id: {order_id}."
            )


    def call_update_order(self, order_id, payload):
        return self.woo_helper.put(f'orders/{order_id}', params=payload)