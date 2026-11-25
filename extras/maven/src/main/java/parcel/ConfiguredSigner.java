package parcel;
import java.security.Signature;
import org.springframework.beans.factory.annotation.Value;
public class ConfiguredSigner {
    @Value("${parcel.signing.algorithm}")
    private String algorithm;
    public Signature newSigner() throws Exception {
        return Signature.getInstance(algorithm);
    }
}
