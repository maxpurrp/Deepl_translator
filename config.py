import pymysql
TOKEN = '6352600603:AAFivWTSkbcWoOs51CrmusgxDTxHG0KqNE0'

database_cred = {

        "host": "host.docker.internal",

        "user": "user",

        "password": "password",

        "database": "Users",

        "autocommit": True,

        "cursorclass": pymysql.cursors.DictCursor,

    }