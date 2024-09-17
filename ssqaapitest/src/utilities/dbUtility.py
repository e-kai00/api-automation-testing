import pymysql
from pymysql.cursors import DictCursor
import logging as logger
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility:

    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()
        self.host = 'localhost'


    def create_connection(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.creds['db_user'],
            password=self.creds['db_password'],
            port=3306
        )

        return connection
    

    def execute_select(self, sql):
        connection = self.create_connection()

        try:
            logger.debug(f'Executing: {sql}')
            cur = connection.cursor(DictCursor)
            cur.execute(sql)
            response_dict = cur.fetchall()
            cur.close()

        except Exception as e:
            raise Exception(f'Failed running {sql} \n Error: {str(e)}')
        
        finally:
            connection.close()

        return response_dict
            


    def execute_sql(self, sql):
        pass
