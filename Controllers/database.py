import mysql.connector 

import sys

def connect():

    connexion = None
    try :
        connexion = mysql.connector.Connect(
            host='localhost',
            user='arsene',
            password="nelson",
            database='balancemaster',
         )
        print("Connected")
    except:
        print("Error : ", sys.exc_info())
    finally:
        return connexion
    

connect()