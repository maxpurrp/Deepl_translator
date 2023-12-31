import pymysql
from config import database_cred

class Database:

    def __init__(self):
        self.conn = pymysql.connect(host=database_cred['host'],
                                    user=database_cred['user'],
                                    password=database_cred['password'])
        with self.conn.cursor() as cursor:
            cursor.execute('use Users')
            cursor.execute('create table if not exists translations (name varchar(255) not null, original_text varchar(255) not null, translate varchar(255) not null)')

    def add_info(self, user, dest, src):

        try:

            with self.conn.cursor() as cursor:

                cursor.execute('insert into translations values (%s, %s, %s)', (user, dest, src))

                self.conn.commit()

        except pymysql.Error as e:
            print(e)

    def get_users(self):
        try:
            self.conn.ping()

            with self.conn.cursor() as cursor:

                cursor.execute('select DISTINCT name from translations')

                self.conn.commit()

                result = cursor.fetchall()

                return result

        except pymysql.Error as e:
            print(e)

    def get_info_about_user(self, name):

        self.conn.ping()

        with self.conn.cursor() as cursor:

            cursor.execute('select * from translations where name=%s', name)

            self.conn.commit()

            result = cursor.fetchall()

            return result
