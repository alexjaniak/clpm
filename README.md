# CLPM: A Command-Line Password Manager. 
## About 
CLPM is a is an easy-to-use out-of-the-box password manager accesible solely through the command-line. The passwords are encrypted using 256 bit AES and the master password is hashed using 256 bit SHA-3. The master password is used to generate a key for encryption and for accessing the accounts. The accounts are stored in an SQL database. 

## Installation

### Requirements
python >= 3.9
pip >= 21.1.2

### Directly through pip
The easiest way to install is through pip: 
```
pip install clpm
```
Then run `clpm init` to initialize the database.
A prompt & confirmation will appear to input a master password.

*Note: clpm will not work unless a master password is set through `clpm init` first.*

### As a Local Copy
If you prefer to install manually:
1. Clone this repo
2. Run `python setup.py install`


## Usage


## Extra & TODO

### TODO
* Encrypt all account information rather than just passwords.
* Add usage to the README.
* Revamp menu.
* Fix double init/reset error
* Clear terminal history after query/add




won't delete passwords.db file unless manually removed using rm ...

