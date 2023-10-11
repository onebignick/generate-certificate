# This script generates a private key and a self-signed certificate
# saving them to "private_key.pem" and "certificate.pem"

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import os
import datetime

COUNTRY="SG"
STATE="Your state here"
ORG="Your organization"
NAME="Your name"

private_key=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, COUNTRY),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, str(os.environ.get("STATE"))),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, str(os.environ.get("ORGANIZATION"))),
    x509.NameAttribute(NameOID.COMMON_NAME, str(os.environ.get("NAME"))),
])


cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(
    private_key.public_key()
).serial_number(1000).not_valid_before(datetime.datetime.utcnow()).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).sign(private_key, hashes.SHA256(), default_backend())

# Save the private key and certificate to files
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("certificate.pem", "wb") as cert_file:
    cert_file.write(cert.public_bytes(serialization.Encoding.PEM))