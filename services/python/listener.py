import ssl
from cryptography.hazmat.primitives.asymmetric import rsa

def receipt_signer():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key

def legacy_client():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.minimum_version = ssl.TLSVersion.TLSv1
    return context

def listener():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('deploy/edge.pem', 'deploy/edge.key')
    return context
