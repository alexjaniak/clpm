from prettytable import from_db_cursor
from sql_utils import *
import click 
from Crypto.Hash import SHA3_256
from Crypto.Cipher import AES

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
    """Hashes string and returns hexdigest using SHA-256."""
    bstring = string.encode() # convert to bytes
    sha_256 = SHA3_256.new() # sha_256 encoder
    sha_256.update(bstring) # encode string
    return sha_256.hexdigest() # return hexdigest

def get_private_key(password):
    salt = get_random_bytes(32)
    encoded = password.encode('UTF-8')
    key = KDF.scrypt(encoded, salt, 32, N=2**14, r=8, p=1)
    return key, salt

def encode_aes_256(string, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(string)
    return ciphertext, nonce, tag

def decode_aes_256(ciphertext, key, nonce, tag):
    cipher = AES.new(key, AES.AES.MODE_EAX, nonce=nonce)
    text = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
    except ValueError:
        print("Key incorrect or message corrupted")

    return text