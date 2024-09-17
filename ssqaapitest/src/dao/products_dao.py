import random
from ssqaapitest.src.utilities.dbUtility import DBUtility


class ProductsDAO:

    def __init__(self):
        self.db_helper= DBUtility()


    def get_random_product_from_db(self, qty=1):
        
        sql = 'SELECT * FROM wordpress.wp_posts WHERE post_type = "product" LIMIT 500;'
        response_sql = self.db_helper.execute_select(sql)

        return random.sample(response_sql, int(qty))
    

    def get_product_by_id(self, product_id):
        
        sql = f'SELECT * FROM wordpress.wp_posts WHERE ID = {product_id};'
        
        return self.db_helper.execute_select(sql)