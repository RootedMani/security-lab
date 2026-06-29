import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes

def aes_ed(message):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    aes = AESGCM(key)

    cipher_text = nonce + aes.encrypt(nonce, message.encode(), None)
    plain_text = aes.decrypt(cipher_text[:12], cipher_text[12:], None)

    return f"key: {key.hex()}\ncipher text: {cipher_text.hex()}\nplain text: {plain_text.decode()}"

if __name__ == "__main__":
    print(aes_ed("Hello, My name is Mani!"))