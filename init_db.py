from utils import *

if __name__ == '__main__':
    con = sql_connect()
    sql_create_table(con)
    con.close()