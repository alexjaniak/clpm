from init_db import sql_reset_table
from utils import *

@click.group()
def cli():
    pass

@cli.command()
def add():
    click.echo("Enter account details (\033[37;1m!\033[0m = required).")
    click.echo("Press \033[37;1mq\033[0m to quit.")

    account = prompt_rfield("\033[37;1m!\033[0mAccount", "account")
    if qprompt(account): return None
    user = prompt_field('Username')
    if qprompt(user): return None
    email = prompt_field('Email')
    if qprompt(email): return None
    tag = prompt_field('Tag')
    if qprompt(tag): return None
    password = prompt_rfield("\033[37;1m!\033[0mPassword", "password")
    if qprompt(password): return None

    con = sqllite_connect()
    sql_insert(con, (account, user, password, email, tag))
    con.close()


@cli.command()
@click.argument('id', default=None, type=int)
def delete(id):
    con = sqllite_connect()
    sql_delete_account(con, str(id))
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




