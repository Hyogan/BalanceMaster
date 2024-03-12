from Controllers.database import connect
import sys


# from setuptools import setup, find_packages
# setup(name="Controllers",packages=find_packages())


def login(id):
    conn = None
    sql = "select * from test720 WHERE username=%s AND password=%s"
    values = (id.getUsername(), id.getPassword())
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql, conn
        return result
