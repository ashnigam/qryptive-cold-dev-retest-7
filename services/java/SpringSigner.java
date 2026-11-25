package parcel;
import java.security.Signature;
import org.springframework.beans.factory.annotation.Value;
public class SpringSigner {
  @Value("${parcel.signing.algorithm}") private String algorithm;
  public Signature signer() throws Exception { return Signature.getInstance(algorithm); }
}
