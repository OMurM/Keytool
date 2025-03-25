keystore = {}

def add_private_key_to_keystore(alias, private_key):
    keystore[alias] = {
        "type": "private_key",
        "key": private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode("utf-8")
    }

def add_certificate_to_keystore(alias, certificate):
    keystore[alias] = {
        "type": "certificate",
        "certificate": certificate.public_bytes(
            serialization.Encoding.PEM
        ).decode("utf-8")
    }

def save_keystore(filename):
    with open(filename, "w") as f:
        json.dump(keystore, f, indent=4)
    print(f"Keystore saved to '{filename}'.")

def load_keystore(filename):
    global keystore
    with open(filename, "r") as f:
        keystore = json.load(f)
    print(f"Keystore loaded from '{filename}'.")

def get_from_keystore(alias):
    if alias in keystore:
        return keystore[alias]
    else:
        raise KeyError(f"Alias '{alias}' not found in the keystore.")