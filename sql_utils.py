import sqlite3 as sql
import click

def sql_connect(db = 'passwords.db'):
    """Connects/Creates passwords database."""
    try:
        con = sql.connect(db)
        return con

    except sql.Error as error:
        click.echo("Error accessing database:")
        click.echo(error)

def sql_create_table(con):
    """Creates accounts table."""
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
    """Resets account table."""
    cursor = con.cursor()
    cursor.execute("DROP TABLE accounts")
    sql_create_table(con)

def sql_insert(con, vals):
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
        click.echo(error)

def sql_delete_account(con, id_):
    """Deletes an account from the accounts table."""
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM accounts WHERE id=?",id_) # delete row
        con.commit()
    except sql.Error as error:
        click.echo("Error deleting account, make sure id is correct:")
        click.echo(error)


def sql_query_accounts(con, account):
    """Returns cursor of accounts that match specific account."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE account=?
        """, (account,))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts:")
        click.echo(error)

def sql_query_tags(con, tag):
    """Returns cursor of accounts that match specific tag."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE tag=?
        """, (tag,))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts:")
        click.echo(error)

def sql_query_id(con, id_):
    """Returns cursor of accounts that match specific id."""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE id=?
        """, (id_,))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts:")
        click.echo(error)

def sql_fetch_all(con):
    """Return cursor with all rows from the accounts table."""
    cursor = con.cursor()
    cursor.execute("SELECT * FROM accounts") # selects all rows
    return cursor # returns cursor query
