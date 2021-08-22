from prettytable import from_db_cursor
from sql_utils import *
import click 
import hashlib

def print_table(cursor):
    """Prints table of accounts."""
    table = from_db_cursor(cursor)
    print(table.get_string())

def is_blank(string):
    """Checks if string is either empty or just whitespace."""
    if not string or string.isspace():
        return True
    return False

def prompt_field(prompt):
    """Prompts user for a for a field."""
    field = click.prompt(prompt, default="",show_default=False)
    if is_blank(field): field = None
    return field

def prompt_rfield(prompt, prompt_name):
    """Prompts user for a required field."""
    while True:
        field = click.prompt(prompt, default="", show_default=False)
        if not is_blank(field): return field
        click.echo("Field {} is required.".format(prompt_name))
    
def qprompt(string):
    """Quit option for prompt."""
    if not string == None and string.strip() == "q":
        click.echo("Aborted!")
        return True
    return False

def digest_sha_256(string):
    """Hashes string and returns digest using SHA-256."""
    encoded = string.encode() # convert to bytes
    hashed = hashlib.sha256(encoded) # hash using SHA-256
    return hashed.digest() # convert to digest