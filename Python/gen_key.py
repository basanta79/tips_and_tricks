from operator import xor
import datetime
import json
import collections
import decimal
import base64
from datetime import date, timezone, datetime
import sys



def generate_long_key(number):
    number_left = number * (16 // len(number) + 1)
    d_string = 'DDDDDDDDDDDDDDDD'
    number_rigth = sxor(number_left, d_string)
    
    encrypt = aes.encrypt(number_left)
    print(number_left)
    print(number_rigth)
    print(encrypt)


def sxor(s1, s2):  
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


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




generate_long_key('123456')