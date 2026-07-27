import os
import certifi

# Automatically set SSL_CERT_FILE to the path provided by certifi if not already set.
# This prevents SSLCertVerificationError on systems without a configured global certificate store.
if "SSL_CERT_FILE" not in os.environ:
    os.environ["SSL_CERT_FILE"] = certifi.where()
