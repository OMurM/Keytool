from components.certificates.certificate_utils import save_certificate

def export_certificate(certificate, filename):
    with open(filename, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))