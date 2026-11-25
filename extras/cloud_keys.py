import boto3

def sign_receipt(digest):
    kms = boto3.client("kms")
    return kms.sign(KeyId="alias/parcel-sign", Message=digest, MessageType="DIGEST", SigningAlgorithm="RSASSA_PKCS1_V1_5_SHA_256")
