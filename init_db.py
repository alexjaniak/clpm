from utils import sqllite_connect

def sql_create_table(con):
    """creates accounts table"""
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account VARCHAR(255) NOT NULL,
        username VARCHAR(255),
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        tag VARCHAR(50) DEFAULT 'NONE'
    )""")
    con.commit()

def sql_reset_table(con):
    """resets accounts table"""
    cursor = con.cursor()
    cursor.execute("DROP TABLE accounts")
    sql_create_table(con)

if __name__ == '__main__':
    con = sqllite_connect()
    sql_create_table(con)
    con.close()