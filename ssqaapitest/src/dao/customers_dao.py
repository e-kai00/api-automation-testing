from ssqaapitest.src.utilities.dbUtility import DBUtility
import pdb
import random


class CustomerDAO:

    def __init__(self):
        self.db_helper = DBUtility()


    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM wordpress.wp_users WHERE user_email = '{email}';"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql
    

    def get_random_customer_from_db(self, qty=1):

        sql = 'SELECT * FROM wordpress.wp_users ORDER BY id DESC LIMIT 500;'
        response_sql = self.db_helper.execute_select(sql)

        return random.sample(response_sql, int(qty))
    