import hashlib
import ssl
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding, dh, x25519
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from Crypto.Cipher import DES, ARC4, Blowfish

def sign_manifest(payload):
    signing_key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    return signing_key.sign(payload, padding.PKCS1v15(), hashes.SHA256())

def sign_label(payload):
    signing_key = ec.generate_private_key(ec.SECP256R1())
    return signing_key.sign(payload, ec.ECDSA(hashes.SHA256()))

def agree_route(peer):
    key = ec.generate_private_key(ec.SECP256R1())
    return key.exchange(ec.ECDH(), peer)

def agree_session(peer):
    key = x25519.X25519PrivateKey.generate()
    return key.exchange(peer)

def agree_legacy(peer, p, g=2):
    params = dh.DHParameterNumbers(p, g).parameters()
    key = params.generate_private_key()
    return key.exchange(peer)

def seal_short(payload, nonce):
    key = AESGCM.generate_key(bit_length=128)
    return AESGCM(key).encrypt(nonce, payload, None)

def seal_long(payload, nonce):
    key = AESGCM.generate_key(bit_length=256)
    return AESGCM(key).encrypt(nonce, payload, None)

def old_checksums(payload):
    return hashlib.md5(payload).digest(), hashlib.sha1(payload).digest()

def old_ciphers():
    return DES.new(b'12345678', DES.MODE_ECB), ARC4.new(b'test-only-key'), Blowfish.new(b'test-only-key', Blowfish.MODE_ECB)
