from Crypto import Random
from Crypto.Cipher import AES
import datetime
import json
from urllib import parse
import collections
import decimal
import base64

class AESCipher(object):

    def __init__(self, key, size=32):
        self.bs = size
        assert len(key) == size
        self.key = key

    def encrypt(self, raw, iv=None):
        raw = self._pad(raw)
        # Use a random IV or the one set by the caller
        if iv is None:
            iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode('ascii')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + ((self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)).encode('ascii')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


cipher = AESCipher('12345678901234567890123456789012', 32)


