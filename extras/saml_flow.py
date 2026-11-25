import xmlsec
from lxml import etree

def sign_assertion(assertion, key_path):
    signature = xmlsec.template.create(assertion, xmlsec.Transform.EXCL_C14N, xmlsec.Transform.RSA_SHA1)
    assertion.insert(0, signature)
    ctx = xmlsec.SignatureContext()
    ctx.key = xmlsec.Key.from_file(key_path, xmlsec.KeyFormat.PEM)
    ctx.sign(signature)
    return assertion

def encrypt_assertion(assertion, certificate):
    template = xmlsec.template.encrypted_data_create(assertion, xmlsec.Transform.AES128, type=xmlsec.EncryptionType.ELEMENT)
    key_info = xmlsec.template.encrypted_data_ensure_key_info(template)
    xmlsec.template.add_encrypted_key(key_info, xmlsec.Transform.RSA_OAEP)
    return template
