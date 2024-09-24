import pytest
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.orders_helpers import OrdersHelper
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
import pdb


pytestmark = [pytest.mark.orders, pytest.mark.smoke]


@pytest.fixture(scope='module')
def orders_smoke_setup():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # get a product from db
    random_product = product_dao.get_random_product_from_db(1)
    product_id = random_product[0]['ID']

    info = {
        'product_id': product_id,
        'order_helper': order_helper
    }

    return info


@pytest.mark.tcid48
def test_create_paid_order_guest_user(orders_smoke_setup):

    order_helper = orders_smoke_setup['order_helper']
    customer_id = 0
    product_id = orders_smoke_setup['product_id']

    # make api call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }      
    ]}
    
    order_json = order_helper.create_order(additional_args=info)
    
    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(orders_smoke_setup):

    # create helper objects
    order_helper = orders_smoke_setup['order_helper']
    customer_helper = CustomerHelper()

    # make api call
    customer_info = customer_helper.create_customer()
    customer_id = customer_info['id']
    product_id = orders_smoke_setup['product_id']

    info = {"line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }      
        ],
        "customer_id": customer_id
    }
    
    order_json = order_helper.create_order(additional_args=info)
    
    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)
   