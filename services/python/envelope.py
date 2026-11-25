from jwcrypto import jwk, jwe, jwt

def wrap_dispatch(payload):
    recipient = jwk.JWK.generate(kty="RSA", size=2048)
    token = jwe.JWE(payload, protected={"alg": "RSA-OAEP", "enc": "A256GCM"})
    token.add_recipient(recipient)
    return token.serialize(compact=True)

def sign_claims(key):
    token = jwt.JWT(header={"alg": "RS256"}, claims={"aud": "parcel"})
    token.make_signed_token(key)
    return token.serialize()
