from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509 import load_pem_x509_certificate
import json
import datetime

keystore = {}

# Add private key to the keystore
def add_private_key_to_keystore(alias, private_key):
    keystore[alias] = {
        "type": "private_key",
        "key": private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode("utf-8")
    }

# Add certificated to keystore
def add_certificate_to_keystore(alias, certificate):
    keystore[alias] = {
        "type": "certificate",
        "certificate": certificate.public_bytes(
            serialization.Encoding.PEM
        ).decode("utf-8")
    }

# Save to keystore to a file
def save_keystore(filename):
    with open(filename, "w") as f:
        json.dump(keystore, f, indent=4)
    print(f"Keystore save to '{filename}'.")

# Load keystore to a file
def load_keystore(filename):
    global keystore
    with open(filename, "r") as f:
        keystore = json.load(f)
    print(f"Keystore loaded from '{filename}'.")

# Retrive item from the keystore
def get_from_keystore(alias):
    if alias in keystore:
        return[alias]
    else:
        raise KeyError(f"Alias '{alias}' not found in the keystore.")

# Generate a private key
def generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Selfe signed certificates
def create_self_signed_certificates(private_key, public_key, common_name, country="ES", State="Catalonia", locality="Barcelona", organization="My Organization"):
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Catalonia"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Barcelona"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Organization"),
        x509.NameAttribute(NameOID.COMMON_NAME, "myorganization.com"),
    ])

    certificate = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        public_key
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName("myorganization.com")]),
        critical=False,
    ).sign(private_key, hashes.SHA256())
    return certificate

# Save private key to file
def save_private_key(private_key, filename):
    with open(filename, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

# Save certificate to a file
def save_certificate(certificate, filename):
    with open(filename, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

# Import certificates from a file
def import_certificates(filename):
    with open(filename, "rb") as f:
        certificate_data = f.read()
        certificate = load_pem_x509_certificate(certificate_data)
    return certificate

# Export certificate to a file
def export_certificate(certificate, filename):
    with open(filename, "wb") as r:
        r.write(certificate.public_bytes(serialization.Encoding.PEM))


