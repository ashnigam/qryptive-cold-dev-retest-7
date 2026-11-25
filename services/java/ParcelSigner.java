package parcel;
import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.*;
public class ParcelSigner {
  public byte[] rsa(byte[] parcel) throws Exception {
    KeyPairGenerator gen = KeyPairGenerator.getInstance("RSA");
    gen.initialize(2048);
    KeyPair pair = gen.generateKeyPair();
    Signature sig = Signature.getInstance("SHA256withRSA");
    sig.initSign(pair.getPrivate()); sig.update(parcel); return sig.sign();
  }
  public byte[] ec(byte[] parcel) throws Exception {
    KeyPairGenerator gen = KeyPairGenerator.getInstance("EC");
    gen.initialize(256);
    KeyPair pair = gen.generateKeyPair();
    Signature sig = Signature.getInstance("SHA256withECDSA");
    sig.initSign(pair.getPrivate()); sig.update(parcel); return sig.sign();
  }
  public void exchange() throws Exception {
    KeyAgreement ecdh = KeyAgreement.getInstance("ECDH");
    KeyAgreement x = KeyAgreement.getInstance("X25519");
    KeyAgreement dh = KeyAgreement.getInstance("DiffieHellman");
  }
  public void storage() throws Exception {
    KeyGenerator small = KeyGenerator.getInstance("AES");
    small.init(128); SecretKey shortKey = small.generateKey();
    KeyGenerator large = KeyGenerator.getInstance("AES");
    large.init(256); SecretKey longKey = large.generateKey();
    Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
  }
  public void compat() throws Exception {
    MessageDigest md5 = MessageDigest.getInstance("MD5");
    MessageDigest sha1 = MessageDigest.getInstance("SHA-1");
    Cipher des = Cipher.getInstance("DES/ECB/PKCS5Padding");
    Cipher rc4 = Cipher.getInstance("RC4");
    Cipher blowfish = Cipher.getInstance("Blowfish");
  }
}
