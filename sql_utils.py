import sqlite3 as sql
import click 
from utils import * 

def sql_connect(db = 'passwords.db'):
    """Connects/Creates passwords database."""
    try:
        con = sql.connect(db)
        return con

    except sql.Error as error:
        click.echo("Error accessing database:")
        raise error

def sql_create_accounts_table(con):
    """Creates accounts table."""
    try: 
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
    except sql.Error as error:
        click.echo("Error creating accounts table:")
        raise error

def sql_drop_accounts_table(con):
    """Resets account table."""
    cursor = con.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS accounts")
        con.commit()
    except sql.Error as error:
        click.echo("Error droping account table:")
        raise error

def sql_insert_account(con, vals):
    """Insert a row into the accounts table."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        INSERT INTO accounts (account, username, password, email, tag)
        VALUES (?,?,?,?,?)
        """, vals)
        con.commit()
    except sql.Error as error:
        click.echo("Error inserting account:")
        raise error

def sql_delete_account(con, id_):
    """Deletes an account from the accounts table."""
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM accounts WHERE id=?",id_) # delete row
        con.commit()
    except sql.Error as error:
        click.echo("Error deleting account, make sure id is correct:")
        raise error


def sql_query_accounts(con, account):
    """Returns cursor of accounts that match specific account 
    from the account table."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE account=?
        """, (account,))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts:")
        raise error

def sql_query_tags(con, tag):
    """Returns cursor of accounts that match specific tag
    from the account table."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE tag=?
        """, (tag,))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts:")
        raise error

def sql_query_id(con, id_):
    """Returns cursor of accounts that match specific id
    from the account table."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE id=?
        """, (id_,))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts:")
        raise error

def sql_fetch_all_acounts(con):
    """Return cursor with all rows from the accounts table."""
    cursor = con.cursor()
    cursor.execute("SELECT * FROM accounts") # selects all rows
    return cursor # returns cursor query

def sql_init_master_table(con, password):
    """Creates master password table and inserts master password."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS master(
            id INTEGER PRIMARY KEY,
            password TEXT(256) NOT NULL
        )
        """)
        cursor.execute("""
        INSERT INTO master(id, password)
        VALUES (1,?)""", (password,))
        con.commit()
    except sql.Error as error:
        click.echo("Error initializing master table:")
        raise error

def sql_drop_master_table(con):
    cursor = con.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS master")
        con.commit()
    except sql.Error as error:
        click.echo("Error droping master table:")
        raise error

def sql_compare_master(con, digest):
    """Compare string to master password."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM master
        WHERE id=1 """) 
        master_pass = cursor.fetchone()[1] # returns row as list of cols

    except sql.Error as error:
        click.echo("Error comparing master to input:")
        raise error

    if master_pass == digest: return True
    return False

