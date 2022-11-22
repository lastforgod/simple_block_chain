import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 import Crypto.Random
import collections
import datetime
from Crypto.Hash import SHA
 class Client:
def __init__(self):
random = Crypto.Random.new().read self._private_key = RSA.generate(1024, random) self._public_key = self._private_key.publickey() self._signer = PKCS1_v1_5.new(self._private_key)
@property
def identity(self):
return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii' )

 class Transaction:
def __init__(self, sender, recipient, value):
self.sender = sender
self.recipient = recipient
self.value = value
self.time = datetime.datetime.now()
def to_dict(self):
if self.sender == "Genesis":
identity = "Genesis" else:
identity = self.sender.identity
return collections.OrderedDict({'sender': identity,
'recipient': self.recipient, 'value': self.value,
'time' : self.time})
def sign_transaction(self):
private_key = self.sender._private_key
signer = PKCS1_v1_5.new(private_key)
h = SHA.new(str(self.to_dict()).encode('utf8')) return binascii.hexlify(signer.sign(h)).decode('ascii')

Ali = Client()
Reza = Client()
t = Transaction(Ali,Reza.identity,5.0) signature = t.sign_transaction() print (signature)
