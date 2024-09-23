import pytest
from datetime import datetime, timedelta
from ssqaapitest.src.helpers.products_helper import ProductHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO
import pdb


@pytest.mark.regression
class TestProductsWithFilter:

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        
        # create data
        x_day_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_day_from_today)
        after_created_date = _after_created_date.isoformat()

        # tmp_date = datetime.now() - timedelta(days=x_day_from_today)
        # after_created_day = tmp_date.strftime('%Y-%m-%dT%H:%M:%S')

        # make the call
        payload = {
            'after': after_created_date,            
        }       
        response = ProductHelper().call_list_products(payload)

        assert response, f'Empty response for "list products with filter".'

        # get data from db
        db_products = ProductsDAO().get_products_after_given_date(after_created_date)

        # verify API response match db
        assert len(response) == len(db_products), (
            f'List products with filter "after" returned unexpected number of products'
            f'Exptected: {len(db_products)}. Actual: {len(response)}.'
        )

        ids_in_response_api = [i['id'] for i in response]
        ids_in_db = [i['ID'] for i in db_products]
        ids_diff = list(set(ids_in_response_api) -  set(ids_in_db))

        assert not ids_diff, f'List products with filter. Product ids in response mismatch in db.'

        # pdb.set_trace()
