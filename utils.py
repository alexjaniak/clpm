from prettytable import from_db_cursor
import prettytable
from sql_utils import *
import click 
from Crypto.Hash import SHA3_256
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from Crypto.Random import get_random_bytes

def print_table(cursor, password):
    rows = cursor.fetchall()
    table = prettytable.PrettyTable()
    table.field_names = ["id", "accounts", "username", "password", "email", "tag"]
    for row in rows:
        row = list(row)
        key, salt = get_private_key(password, salt=row[7])
        row[3] = decode_aes_256(row[3], key, row[6])
        table.add_row(row[:6])
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

def get_private_key(password, salt = None):
    if salt == None: salt = get_random_bytes(32)
    encoded = password.encode('UTF-8')
    key = KDF.scrypt(encoded, salt, 32, N=2**14, r=8, p=1)
    return key, salt

def encode_aes_256(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_b = cipher.encrypt(pad(text.encode('UTF-8'), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_b).decode('utf-8')
    return ct, iv

def decode_aes_256(ciphertext, key, iv):
    try:
        iv = b64decode(iv)
        ct = b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        text = unpad(cipher.decrypt(ct), AES.block_size)
        return text.decode('UTF-8')
    except (ValueError, KeyError) as e:
        print("Incorrect decryption")

def encrypt_password(password, acc_password):
    key, salt = get_private_key(password)
    ct, iv = encode_aes_256(acc_password, key)
    return ct, iv, salt

    