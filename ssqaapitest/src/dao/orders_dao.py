from ssqaapitest.src.utilities.dbUtility import DBUtility


class OrdersDAO:

    def __init__(self):
        self.db_helper= DBUtility()


    def get_order_lines_by_order_id(self, order_id):
        sql = f'SELECT * FROM wordpress.wp_woocommerce_order_items WHERE order_id = {order_id};'
        return self.db_helper.execute_select(sql)
    

    def get_order_items_details(self, order_item__id):
        sql = f'SELECT * FROM wordpress.wp_woocommerce_order_itemmeta WHERE order_item_id = {order_item__id};'
        rs_sql = self.db_helper.execute_select(sql)

        line_details = dict()
        for meta in rs_sql:
            line_details[meta['meta_key']] = meta['meta_value']

        return line_details
