import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():


        conn = pymysql.connect(
            user= "admin",
            password="whr19970319.",
            host="e61561.cqwxd1xpxdgk.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

