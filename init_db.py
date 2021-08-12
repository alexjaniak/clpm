from utils import sqllite_connect

def create_table(con):
    """creates account table"""
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
        account VARCHAR(255) NOT NULL,
        username VARCHAR(255),
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        fname VARCHAR(255),
        lname VARCHAR(255),
        tag VARCHAR(50) DEFAULT 'NONE'
    )""")
    con.commit()

def reset_table(con):
    """resets account table"""
    cursor = con.cursor()
    cursor.execute("DROP TABLE accounts")
    create_table(con)

if __name__ == '__main__':
    con = sqllite_connect()
    create_table(con)
    con.close()