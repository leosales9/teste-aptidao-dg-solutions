from sys import exit
from os import environ
from psycopg2 import connect


class PostgresConnection:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def get_connection(self):
        try:
            return connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                dbname=self.__database
            )
        except Exception as e:
            print(e)
            exit(1)
