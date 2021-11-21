from Crypto.Cipher import AES
from Crypto.Protocol import KDF
from Crypto.Random import get_random_bytes

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
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    text = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
    except ValueError:
        print("Key incorrect or message corrupted")
    return text

if __name__== '__main__': 
    key, salt = get_private_key("08082002")
    string = "this gets encrypted"
    ciphertext, nonce, tag = encode_aes_256(string.encode('UTF-8'), key)
    decoded = decode_aes_256(ciphertext, key, nonce=nonce, tag=tag)
    print(string)
    print(ciphertext, nonce, tag)
    print(decoded)
    