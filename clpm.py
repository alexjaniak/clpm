from enum import Flag
from sql_utils import *
from click.decorators import confirmation_option
from utils import *

@click.group()
@click.version_option()
def cli(): # click command group
    pass

@cli.command()
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=False
)
def add(password):
    """Adds account to database."""
    con = sql_connect()
    if sql_compare_master(con, password): # compare password to master
        # menu for adding accounts
        click.echo("Enter account details (\033[37;1m!\033[0m = required).") # bright white unicode
        click.echo("Press \033[37;1mq\033[0m to quit.") # bright white unicode

        account = prompt_rfield("\033[37;1m!\033[0mAccount", "account") # bright white unicode
        if qprompt(account): return None # quit 
        user = prompt_field('Username')
        if qprompt(user): return None
        email = prompt_field('Email')
        if qprompt(email): return None
        tag = prompt_field('Tag')
        if qprompt(tag): return None
        password = prompt_rfield("\033[37;1m!\033[0mPassword", "password")
        if qprompt(password): return None

        # insert account using user input
        sql_insert_account(con, (account, user, password, email, tag))
    else:
         click.echo("Password does not match database password.")
    con.close()


@cli.command()
@click.argument('id', default=None, type=int)
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=False
)
def delete(id, password):
    """Deletes account from database."""
    con = sql_connect()
    if sql_compare_master(con, password): # compare password to master
        sql_delete_account(con, str(id))
    else:
         click.echo("Password does not match database password.")
    con.close()

@cli.command()
@click.option('-a','--accounts', 'type_', flag_value='accounts',
                help="Query by account.", default=True)
@click.option('-t','--tags', 'type_', flag_value='tags',
                help="Query by tags.")
@click.option('-i','--ids', 'type_', flag_value='id',
                help="Query by id.")
@click.option('-l','--all', 'type_', flag_value='all',
                help="Query all.")
@click.argument('val', default=None, required=False)
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=False
)
def query(type_, val, password):
    """Query database."""
    con = sql_connect()
    if sql_compare_master(con, password): # compare password to master
        if val == None or type_ == 'all': # 
            cur = sql_fetch_all_acounts(con)
        else:
            if type_ == 'accounts':
                cur = sql_query_accounts(con, val)
            elif type_ == 'tags':
                cur = sql_query_tags(con, val)
            elif type_ == 'id':
                cur = sql_query_id(con, val)
        print_table(cur)
    else:
         click.echo("Password does not match database password.")
    con.close()

@cli.command()
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True
)
def init(password):
    """Initializes clpm."""
    con = sql_connect()
    sql_create_accounts_table(con) 
    sql_init_master_table(con, password) # sets master assword
    print("Database initialized")
    con.close()

@cli.command()
@click.confirmation_option(prompt="Are you sure you want to reset clpm? All data will be lost.")
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True
)
def reset(password):
    """Resets clpm."""
    con = sql_connect()
    if sql_compare_master(con, password): # compare password to master
        sql_drop_accounts_table(con)
        sql_drop_master_table(con)
        print("Database reset")
    else:
        click.echo("Password does not match database password.")
    con.close()




