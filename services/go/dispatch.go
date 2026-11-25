package dispatch
import (
 "crypto/rand"
 "crypto/rsa"
 "crypto/ecdsa"
 "crypto/elliptic"
 "crypto/ecdh"
 "crypto/sha256"
 "crypto/md5"
 "crypto/sha1"
 "crypto/aes"
 "crypto/des"
 "crypto/rc4"
 "crypto/tls"
 "crypto"
)
func receipt(data []byte) {
 digest := sha256.Sum256(data)
 key, _ := rsa.GenerateKey(rand.Reader, 2048)
 rsa.SignPKCS1v15(rand.Reader, key, crypto.SHA256, digest[:])
 ecKey, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
 ecdsa.SignASN1(rand.Reader, ecKey, digest[:])
}
func exchanges() {
 key, _ := ecdh.P256().GenerateKey(rand.Reader)
 peer, _ := ecdh.P256().GenerateKey(rand.Reader)
 key.ECDH(peer.PublicKey())
 x, _ := ecdh.X25519().GenerateKey(rand.Reader)
 xp, _ := ecdh.X25519().GenerateKey(rand.Reader)
 x.ECDH(xp.PublicKey())
}
func compatibility(data []byte) {
 md5.Sum(data)
 sha1.Sum(data)
 aes.NewCipher(make([]byte, 16))
 aes.NewCipher(make([]byte, 32))
 des.NewCipher([]byte("12345678"))
 rc4.NewCipher([]byte("test-only-key"))
}
var client = &tls.Config{MinVersion: tls.VersionTLS10, CurvePreferences: []tls.CurveID{tls.X25519, tls.CurveP256}}
var server = &tls.Config{MinVersion: tls.VersionTLS12}
