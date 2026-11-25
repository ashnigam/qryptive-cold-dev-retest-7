const crypto = require('node:crypto');
function rsaLabel(body) {
  const { privateKey } = crypto.generateKeyPairSync('rsa', {modulusLength: 2048});
  return crypto.sign('sha256', body, privateKey);
}
function ecLabel(body) {
  const { privateKey } = crypto.generateKeyPairSync('ec', {namedCurve: 'prime256v1'});
  return crypto.sign('sha256', body, privateKey);
}
function routes() {
  const ecdh = crypto.createECDH('prime256v1'); ecdh.generateKeys();
  const x = crypto.generateKeyPairSync('x25519');
  const dh = crypto.createDiffieHellman(2048); dh.generateKeys();
  return { ecdh, x, dh };
}
function oldDigest(body) {
  return [crypto.createHash('md5').update(body).digest(), crypto.createHash('sha1').update(body).digest()];
}
function vault(key, nonce) {
  return [crypto.createCipheriv('aes-128-gcm', key.subarray(0,16), nonce), crypto.createCipheriv('aes-256-gcm',key,nonce)];
}
function obsolete(key, iv) {
  return [crypto.createCipheriv('des-cbc',key,iv), crypto.createCipheriv('rc4',key,null), crypto.createCipheriv('bf-cbc',key,iv)];
}
module.exports = {rsaLabel, ecLabel, routes, oldDigest, vault, obsolete};
