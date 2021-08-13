from init_db import sql_reset_table
from utils import *

@click.group()
def cli():
    pass

@cli.command()
def add():
    account = click.prompt('Account', default=None)
    user = click.prompt('Username', default=None)
    email = click.prompt('Email', default=None)
    tag = click.prompt('Tag', default=None)
    password = click.prompt('Password', default=None)
    
    con = sqllite_connect()
    sql_insert(con,(account, user, password, email, tag))
    con.close()

@cli.command()
def delete(id):
    con = sqllite_connect()
    cur = sql_delete_account(con, id)
    con.close()

@cli.command()
@click.confirmation_option(prompt="Are you sure you want to reset the db? All data will be lost.")
def reset():
    con = sqllite_connect()
    sql_reset_table(con)
    print("Database reset")
    con.close()


@cli.command()
@click.option('-a','--accounts', 'type_', flag_value='accounts',
                default=True)
@click.option('-t','--tag', 'type_', flag_value='tags')
@click.option('-i','--id', 'type_', flag_value='id')
@click.option('-l','--all', 'type_', flag_value='all')
@click.argument('val', default=None, required=False)
def search(type_, val):
    con = sqllite_connect()
    if val == None or type_ == 'all':
        cur = sql_fetch_all(con)
    else:
        if type_ == 'accounts':
            cur = sql_query_accounts(con, val)
        elif type_ == 'tags':
            cur = sql_query_tags(con, val)
        elif type_ == 'id':
            cur = sql_query_id(con, val)
    print_table(cur)
    con.close()




