import pymysql
from pymysql.cursors import DictCursor
import logging as logger
import os
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility
from ssqaapitest.src.configs.hosts_config import DB_HOST


class DBUtility:

    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()

        self.machine = os.environ.get('MACHINE')
        assert self.machine, f'Environment variable "MACHINE" should be set.'

        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, f'Environment variable "WP_HOST" should be set.'

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f'Can not run test in docker if WP_HOST=local')

        self.env = os.environ.get('ENV', 'test')

        # self.host = 'localhost'
        self.host = DB_HOST[self.machine][self.env]['host']
        self.port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']


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
