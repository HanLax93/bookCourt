import base64
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms


def get_key(d, value):
    k = [k for k, v in d.items() if v == value]
    return k


def pkcs7_padding(data):
    if not isinstance(data, bytes):
        data = data.encode()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    return padded_data


class cryptCBCPkcs7(object):

    def __init__(self, key: str, iv: str):
        self.ciphertext = " "
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.iv = iv.encode('utf-8')

    def encrypt(self, text: str):
        cryptor = AES.new(self.key, self.mode, self.iv)

        text = text.encode('utf-8')
        text = pkcs7_padding(text)
        self.ciphertext = cryptor.encrypt(text)

        return base64.b64encode(self.ciphertext)