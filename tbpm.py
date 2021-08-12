from init_db import sql_reset_table
from utils import *

@click.command()
def insert_account(values):
    con = sqllite_connect()
    sql_insert(con, values)
    con.close()

@click.command()
def delete_account(id):
    con = sqllite_connect()
    cur = sql_delete_account(con, id)
    con.close()

@click.command()
def query_account(account):
    con = sqllite_connect()
    cur = sql_query_accounts(con, account)
    con.close()
    print_table(cur)

@click.command()
def query_tag(account):
    con = sqllite_connect()
    cur = sql_query_tags(con, account)
    con.close()
    print_table(cur)

@click.command()
def fetch_all():
    con = sqllite_connect()
    cur = sql_fetch_all()
    con.close()
    print_table(cur)

@click.command()
def reset_table():
    con = sqllite_connect()
    sql_reset_table(con)
    con.close()



