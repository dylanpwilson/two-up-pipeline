import pymysql


def sql_connection(hostname, username, passwrd, db):
    cnx = pymysql.connect(
        host=hostname,
        user=username,
        password=passwrd,
        database=db
    )

    return cnx


def sql_close_connection(connection):
    connection.close()


def sql_insert_data_pt(connection, table, data_pt):

    keys_sorted = sorted([key for key in data_pt.keys()])
    var_str = str(tuple(keys_sorted)).replace('\'', '"')
    val_str = '%s, ' * len()
    val_str = val_str[:len(val_str)-2]

    sql_statement = f'INSERT INTO {table} {var_str} VALUES ({val_str});'
    values = tuple([data_pt[key] for key in keys_sorted])
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql_statement, values)

    connection.commit()



