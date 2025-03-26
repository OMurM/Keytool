from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.x509 import load_pem_x509_certificate
from cryptography.x509.oid import NameOID
import datetime

def create_self_signed_certificates(private_key, public_key, common_name, country="ES", State="Catalonia", locality="Barcelona", organization="My Organization"):
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, State),
        x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
        x509.NameAttribute(NameOID.COMMON_NAME, common_name),
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
        x509.SubjectAlternativeName([x509.DNSName(common_name)]),
        critical=False,
    ).sign(private_key, hashes.SHA256())
    
    return certificate

def import_certificates(filename):
    with open(filename, "rb") as f:
        certificate_data = f.read()
        certificate = load_pem_x509_certificate(certificate_data)
    return certificate

def save_certificate(certificate, filename):
    with open(filename, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

def export_certificate(certificate, filename):
    with open(filename, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))
