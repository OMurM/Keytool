# Keytool Project

This project is designed to manage cryptographic keys and certificates. It provides functionalities for generating private keys, creating self-signed certificates, and managing a keystore for storing these keys and certificates.

## Project Structure

```
KeytoolProject
├── components
│   ├── __init__.py
│   ├── certificates
│   │   ├── __init__.py
│   │   ├── certificate_utils.py
│   │   └── certificate_io.py
│   ├── keystore
│   │   ├── __init__.py
│   │   └── keystore_utils.py
│   └── keys
│       ├── __init__.py
│       └── key_utils.py
├── main.py
└── README.md
```

## Components

- **Keys**: Contains utilities for key generation and management.
- **Certificates**: Contains utilities for creating and managing certificates.
- **Keystore**: Contains utilities for managing the keystore, including adding keys and certificates, and saving/loading the keystore.

## Usage

1. **Generate a Private Key**: Use the key utilities to generate a new private key.
2. **Create a Self-Signed Certificate**: Utilize the certificate utilities to create a self-signed certificate using the generated private key.
3. **Manage the Keystore**: Add the private key and certificate to the keystore, and save/load the keystore as needed.

## Installation

Ensure you have the required dependencies installed. You can install them using pip:

```
pip install cryptography
```

## Running the Application

To run the application, execute the `main.py` file:

```
python main.py
```

This will start the application and present a menu for various key and certificate operations.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!