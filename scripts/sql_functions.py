import pymysql

def sql_connection(hostname, username, password, db):
    cnx = pymysql.connect(
        host=hostname
    )
