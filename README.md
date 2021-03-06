# CLPM: A Command-Line Password Manager. 
## Table of Contents
1. [About](#About)
2. [Installation](#Installation)
    1. [Requirements](#Requirements)
    2. [Regular Install](#Regular-Install)
    3. [Local/Manual Install](#Local-Install)
    4. [Uninstall](#Uninstall)
3. [Usage](#Usage)
    1. [Add Account](#Add-Account)
    2. [Remove Account](#Remove-Account)
    3. [Query Database](#Query)
    4. [Reset](#Reset)
4. [TODO](#TODO)


## About <a name="About"></a>
CLPM is a is an easy-to-use out-of-the-box password manager accesible solely 
through the command-line. The passwords are encrypted using 256 bit AES and the
master password is hashed using 256 bit SHA-3. The master password is used to
generate a key for encryption and for accessing the accounts. The accounts are
stored in a local SQL database. 

## Installation <a name="Installation"></a>
### Requirements
* `python >= 3.9`
* `pip >= 21.1.2`

Automatically installed by pip:
* `Click >= 8.1.3`
* `pycryptodome >= 3.14.1`
* `prettytable >= 3.3.0`

### Regular Install <a name="Regular-Install"></a>
For most, installing this project can be done running `pip install clpm`, 
which pulls the project from [PyPI](https://pypi.org/project/clpm/).


### Local/Manual Install <a name="Local-Install"></a>
If needed, this project can be installed and run locally:
1. Clone this project to a local repository.
2. Run `python setup.py install`
*Note: setup.py uses pip to install the project as a package on the local system*

### Uninstall <a name="Uninstall"></a>
To uninstall this project, for both remote and local installations, run 
`pip uninstall clpm`

If clpm has been already been initialized, pip won't delete the file 
`passwords.db` which contains all stored account information. This means that
clpm can be reinstalled and still retain the same accounts & master password.
If you wish to completely remove clpm from your device, you must manually remove
`passwords.db` by either using the `rm` command or a file explorer. 

   
## Usage <a name="Usage"></a>
Run `clpm init` to initialize the database. A prompt & confirmation will appear 
to input a **master password**. The master password is required for to access 
the database for all commands. In fact, all commands - including `init` - accept
a `--password` argument for the master password instead of a prompt.

*Note: clpm will not work unless a master password is set through `clpm init` 
first.* 

### Add Account <a name="Add-Account"></a>
To add an account to the database, run `clpm add`. After a prompt to input the 
master password, a menu will appear that requests input for **account name**, 
username, email, tag and **password**. Bolded fields are required. If the field 
is not required, press *Enter* to leave it empty. At any point, press *q* to 
terminate the command. 

Each Account includes an automatically generated id that iterates for each 
added account.

### Remove Account <a name="Remove-Account"></a>
To remove an account from the database, run `clpm delete ID` where ID is the
accounts id. Once again, a prompt to input the master password will appear.

### Query Database <a name="Query"></a>
To query the database, run `clpm query`. This command alone will simply output
all accounts and information. Use arguments to search by attributes:
1. `-l/--all` serve the same purpose as `clpm query` with no arguments.
2. `-a/--accounts ACCOUNT` search for accounts with the account field ACCOUNT.
3. `-t/--tags TAG` search for accounts that with the tag field TAG.
4. `-i/--ids ID` retrieves the acccount with an id field of ID.


### Reset <a name="Reset"></a>
To reset the database (i.e, remove all accounts and master password), run 
`clpm reset`. A confirmation prompt as well as a master password prompt will
appear. This will clear `passwords.db` but leave the file on the system.

*Note: after reset, clpm will not work unless it is reinitialized.*

## TODO <a name="TODO"></a>
* Encrypt all account information rather than just passwords.
* Revamp menu.
* Fix double init/reset error.
* Clear terminal history after query/add.
