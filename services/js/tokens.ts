import { CompactEncrypt, generateKeyPair, SignJWT } from 'jose';
export async function envelope(data: Uint8Array) {
 const { publicKey, privateKey } = await generateKeyPair('RSA-OAEP');
 return new CompactEncrypt(data).setProtectedHeader({alg:'RSA-OAEP-256',enc:'A256GCM'}).encrypt(publicKey);
}
export async function claims(key: any) {
 return new SignJWT({aud:'parcel'}).setProtectedHeader({alg:'RS256'}).sign(key);
}
