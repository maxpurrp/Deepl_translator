import pymysql


class Database:

    database_cred = {

        "host": "localhost",

        "user": "max",

        "password": "1234",

        "database": "Users",

        "autocommit": True,  # making sure updated, inserts, deletions are commited for every query

        "cursorclass": pymysql.cursors.DictCursor,

    }

    def __init__(self):
        db_exists = False
        self.conn = pymysql.connect(host=self.database_cred['host'],
                                    user=self.database_cred['user'],
                                    password=self.database_cred['password'])
        cursor = self.conn.cursor()
        cursor.execute('show databases')
        res = cursor.fetchall()
        for elem in res:
            if self.database_cred['database'] in elem:
                db_exists = True
        if not db_exists:
            cursor.execute('create database Users')
            cursor.execute('use Users')
            cursor.execute('create table translations (name varchar(255) not null, original_text varchar(255) not null, translate varchar(255) not null)')

        cursor.execute('use Users')

    def add_info(self, user, dest, src):

        # to check DB Connection pin the instance
        try:
            self.conn.ping()

            with self.conn.cursor() as cursor:

                cursor.execute('insert into translations values (%s, %s, %s)', (user, dest, src))

                self.conn.commit()

                result = cursor.fetchall()

        except pymysql.Error as e:
            print(e)

        return result

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
