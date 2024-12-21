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
        # FIXME Не работи
        a = ''
        b = 0
        if len(msg) / 128 == 0:
            count = 1
        else:
            count = int(len(msg) / 128) + 1
        for i in range(count):
            a += self.keyPair.encrypt(msg[b:b + 128], self.signer)[0]
            b += 128
        return a
        # return self.keyPair.encrypt(msg, self.signer)[0]

    def decrypt(self, msg):
        # FIXME Не работи
        # msg = self.keyPair.decrypt(msg)
        a = ''
        b = 0
        if len(msg) / 128 == 0:
            count = 1
        else:
            count = int(len(msg) / 128) + 1

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
    PUB = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCfEodyqZBKEkvAO+f3AZBPGq4
zK7nR1brgQEjBoYzBzUKJzWqZhUHHPWCuOdjtOv5F4DQUYIIAU54pu0SqIyRQlJO
aQerphkz60kU+rZKSDD+dyogHCDO1yHDY/9TZk+Fg7782BQycYoyNQvKDlJBeOKp
mjLmFFcYUoCQMvJ2HwIDAQAB
-----END PUBLIC KEY-----
'''
    # data = {"uuid": "4ebd0208-8328-5d69-8c44-ec50939c0967", "end_time": "21.07.2025", "init_time": 1678909492.2224667, "name": "base"}
    # sig = 'd106e0d0347f2e7548d3a0f8606e896885fa8d05bf8fd7f3d8b6304fab32f34492466c95f54a1f0f22c7506568ef246873f34a7ea9ecd310eedabefd856bed877497bea61c2a9d9e8cc8ce4d08bf4934f557ef616b9bd5a78088ab400ce5c1b5ddcb91eeb1d2855e5fc5bc1c6a7f4afcfdc099f481a051b6c07294e6c57d0680'
    # a = b"\xeb\xc8\xf8,*\\\x86\x1d/5\xa45}\x99\xce\xc8\x90`\xd0\xa3\xa8D\x8a\xdem\xad\xc6R44\xc6J\x00~\xc6\x03h\xb0\xf6\x8f\xa0\x8bR\x9e\xd4$\x07\xe4\xcb\x92Nq\xf9\xa7W\xdd\xbd\x06B\r=oe\x0e\xcd\xe15\x15\x9e\xfaC/\x19\xa4\x94\xc36L\x88\xa6y\x04\x1d\t'{\xfdx\x1e\xa8\x9c\xe6n\x9c}\xbf\xb3\xd5\xd8\x04cj\xa1\t%an\xb7\xd3\x80\xa5\x12~JVy\xbb\x86\xfa*\x027\x0bL\xdc\xf7Q\x03"
    import json
    # data = open('/home/dedal/Colibri/license/base.pub').read()
    # data = json.loads(data)
    # data = json.dumps(data)
    # print (bytes.fromhex(sig))
    rsa = RSAKey()
    rsa.load_key(PUB)
    print (rsa.encrypt('data'))
    # print(rsa.mk_public())


