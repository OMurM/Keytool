from components.keys.key_utils import (
    generate_private_key,
    save_private_key,
)

from components.certificates.certificate_utils import (
    create_self_signed_certificates,
    import_certificates,
)

from components.certificates.certificate_io import (
    export_certificate,
    save_keystore,
    load_keystore,
    get_from_keystore,
)

from components.keystore.keystore_utils import (
    add_private_key_to_keystore,
    add_certificate_to_keystore,
)

def main():
    # Display menu and handle user input for various key and certificate operations
    while True:
        print("Keytool Menu:")
        print("1. Generate Private Key")
        print("2. Create Self-Signed Certificate")
        print("3. Add Private Key to Keystore")
        print("4. Add Certificate to Keystore")
        print("5. Save Keystore")
        print("6. Load Keystore")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            private_key, public_key = generate_private_key()
            print("Private key generated.")
        
        elif choice == '2':
            common_name = input("Enter common name: ")
            certificate = create_self_signed_certificates(private_key, public_key, common_name)
            print("Self-signed certificate created.")
        
        elif choice == '3':
            alias = input("Enter alias for private key: ")
            add_private_key_to_keystore(alias, private_key)
            print("Private key added to keystore.")
        
        elif choice == '4':
            alias = input("Enter alias for certificate: ")
            add_certificate_to_keystore(alias, certificate)
            print("Certificate added to keystore.")
        
        elif choice == '5':
            filename = input("Enter filename to save keystore: ")
            save_keystore(filename)
        
        elif choice == '6':
            filename = input("Enter filename to load keystore: ")
            load_keystore(filename)
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()