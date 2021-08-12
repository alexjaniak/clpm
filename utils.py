import sqlite3 as sql
from sqlite3.dbapi2 import DatabaseError

def sqllite_connect():
    """connects/creates passwords database"""
    try:
        con = sql.connect('passwords.db')
        return con

    except sql.Error as error:
        print("Error accessing database:", error)

def insert_account(con, values):
    """insert a row into the accounts table"""
    cursor = con.cursor()
    try:
        cursor.execute("""
        INSERT INTO accounts (account, username, password, email, fname, lname, tag)
        VALUES (?,?,?,?,?,?,?)
        """,values)
        con.commit()
    except sql.Error as error:
        print("Error inserting account:", error)

def query_accounts(con, col, val):
    """returns list of accounts that match query search"""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE ?=?
        """, (col,val))
        return cursor.fetchall() # returns entire query as a list
    except sql.Error as error:
        print("Error querying accounts:", error)

def fetch_all(con):
    """return all rows & cols from the accounts table"""
    cursor = con.cursor()
    cursor.execute("SELECT * FROM accounts") # selects all rows
    return cursor.fetchall() # returns entire query as a list
