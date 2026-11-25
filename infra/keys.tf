resource "aws_kms_key" "receipts" {
  customer_master_key_spec = "RSA_2048"
  key_usage = "SIGN_VERIFY"
}
resource "azurerm_key_vault_key" "label" {
  name = "label-signing"
  key_vault_id = var.vault_id
  key_type = "RSA"
  key_size = 2048
  key_opts = ["sign", "verify"]
}
resource "google_kms_crypto_key" "route" {
  name = "route"
  key_ring = var.key_ring
  purpose = "ASYMMETRIC_SIGN"
  version_template { algorithm = "EC_SIGN_P256_SHA256" }
}
resource "vault_transit_secret_backend_key" "manifest" {
  backend = "transit"
  name = "manifest"
  type = "rsa-2048"
}
resource "tls_private_key" "old" { algorithm = "RSA" rsa_bits = 1024 }
