# -*- coding:utf-8 -*-
'''
Created on 7.09.2018 г.

@author: dedal
'''

from Cryptodome.Signature.pkcs1_15 import PKCS115_SigScheme
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA512, SHA384, SHA256, SHA, MD5
import Cryptodome.Random
import binascii

class RSAKey():
    def __init__(self, hash="SHA-256"):
        self.hash = hash

    def new_key(self, bits=1024):
        self.keyPair = RSA.generate(bits=bits)
        self.signer = PKCS115_SigScheme(self.keyPair)
        return self.keyPair.exportKey()

    def mk_public(self):
        self.public = self.keyPair.publickey()
        return self.public.exportKey()

    def write_public(self, path):
        my_key_file = open(path, 'w')
        my_key_file.write(self.mk_public().decode())
        my_key_file.close()
        return True

    def mk_key_file(self, path, bits=1024):
        my_key_file = open(path, 'w')
        my_key_file.write(self.new_key(bits).decode())
        my_key_file.close()
        return True

    def load_key(self, key):
        try:
            self.keyPair = RSA.importKey(open(key, 'rb').read())
        except IOError:
            self.keyPair = RSA.importKey(key)
        self.signer = PKCS115_SigScheme(self.keyPair)
        return True

    def encrypt(self, msg):
        a = ''
        b = 0
        if len(msg) / 128 == 0:
            count = 1
        else:
            count = len(msg) / 128 + 1
        for i in range(count):
            a += self.keyPair.encrypt(msg[b:b + 128], self.signer)[0]
            b += 128
        return a
        # return self.keyPair.encrypt(msg, self.signer)[0]

    def decrypt(self, msg):
        # msg = self.keyPair.decrypt(msg)
        a = ''
        b = 0
        if len(msg) / 128 == 0:
            count = 1
        else:
            count = (len(msg) / 128)

        for i in range(count):
            a += self.keyPair.decrypt(msg[b:b + 128])
            b += 128
        return a
        # return msg

    def get_signature(self, msg):
        Cryptodome.Random.atfork()
        if (self.hash == "SHA-512"):
            digest = SHA512.new()
        elif (self.hash == "SHA-384"):
            digest = SHA384.new()
        elif (self.hash == "SHA-256"):
            digest = SHA256.new()
        elif (self.hash == "SHA-1"):
            digest = SHA.new()
        else:
            digest = MD5.new()
        digest.update(msg.encode('utf-8'))
        return self.signer.sign(digest).hex()

    def verify(self, msg, signature):
        if (self.hash == "SHA-512"):
            digest = SHA512.new()
        elif (self.hash == "SHA-384"):
            digest = SHA384.new()
        elif (self.hash == "SHA-256"):
            digest = SHA256.new()
        elif (self.hash == "SHA-1"):
            digest = SHA.new()
        else:
            digest = MD5.new()
        digest.update(msg.encode('utf8'))
        # raise KeyError(self.signer.verify(digest.hexdigest(), signature))
        # raise KeyError( digest, signature)
        try:
            self.signer.verify(digest, bytes.fromhex(signature))
        except ValueError:
            return False
        return True


if __name__ == '__main__':
    rsa = RSAKey()
    a = rsa.new_key()
    print(a)
    rsa.load_key(a)
    print(rsa.mk_public())

