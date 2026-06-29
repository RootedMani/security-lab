import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes

def aes_ed(message: str):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    aes = AESGCM(key)

    cipher_text = nonce + aes.encrypt(nonce, message.encode(), None)
    plain_text = aes.decrypt(cipher_text[:12], cipher_text[12:], None)

    return f"key: {key.hex()}\ncipher text: {cipher_text.hex()}\nplain text: {plain_text.decode()}"

def rsa_ed(message: str):
    """ A function that encrypts the message given to it with rsa algorithm and returns 
    the encrypted message in hexodecimal format and also the plain text of it.

    Args:
        message (str): A text given to the function that will be encrypted and decrypted
    Returns:
        str: the encrypted version of the message in hexodecimal
        str: The plain text of the message given 
    Note:
        The encryption process is done with RSA encryption algorithm.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    cipher_text = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    plain_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher_text.hex(), plain_text.decode()

if __name__ == "__main__":
    print(aes_ed("Hello, My name is Mani!"))