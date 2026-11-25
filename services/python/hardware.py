from tpm2_pytss import ESAPI, TPM2B_PUBLIC, TPMT_SIG_SCHEME, TPMT_TK_HASHCHECK, TPM2_ALG, TPM2_RH, TPM2_ST

def sign_dispatch(digest):
    tpm = ESAPI()
    handle, public, _, _, _ = tpm.create_primary(in_sensitive=None, in_public=TPM2B_PUBLIC.parse("rsa2048:rsassa-sha256"), primary_handle=TPM2_RH.OWNER)
    scheme = TPMT_SIG_SCHEME(scheme=TPM2_ALG.RSASSA)
    validation = TPMT_TK_HASHCHECK(tag=TPM2_ST.HASHCHECK, hierarchy=TPM2_RH.NULL)
    return tpm.sign(handle, digest, scheme, validation)
