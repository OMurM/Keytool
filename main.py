from keytool_utils import (
    generate_private_key,
    create_self_signed_certificates,
    import_certificates,
    export_certificate,
    add_private_key_to_keystore,
    add_certificate_to_keystore,
    save_keystore,
    load_keystore,
    get_from_keystore
)

def display_menu():
    print("\nKeytool Menu:")
    print("1. Generate Private Key")
    print("2. Create Self-Signed Certificate")
    print("3. Import Certificate")
    print("4. Export Certificate")
    print("5. Save Keystore")
    print("6. Load Keystore")
    print("7. Retrieve from Keystore")
    print("8. Exit")

def main():
    private_key = None
    public_key = None
    certificate = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            alias = input("Enter an alias for the private key: ")
            private_key, public_key = generate_private_key()
            add_private_key_to_keystore(alias, private_key)
            print(f"Private key generated and added to keystore with alias '{alias}'.")
        elif choice == "2":
            if private_key is None or public_key is None:
                print("Please generate a private key first.")
            else:
                alias = input("Enter an alias for the certificate: ")
                common_name = input("Enter the Common Name (e.g., myorganization.com): ")
                certificate = create_self_signed_certificates(private_key, public_key, common_name)
                add_certificate_to_keystore(alias, certificate)
                print(f"Self-signed certificate created and added to keystore with alias '{alias}'.")
        elif choice == "3":
            filename = input("Enter the filename of the certificate to import: ")
            try:
                certificate = import_certificates(filename)
                alias = input("Enter an alias for the imported certificate: ")
                add_certificate_to_keystore(alias, certificate)
                print(f"Certificate imported and added to keystore with alias '{alias}'.")
            except Exception as e:
                print(f"Failed to import certificate: {e}")
        elif choice == "4":
            alias = input("Enter the alias of the certificate to export: ")
            try:
                item = get_from_keystore(alias)
                if item["type"] == "certificate":
                    filename = input("Enter the filename to export the certificate to: ")
                    export_certificate(item["certificate"], filename)
                    print(f"Certificate exported successfully to '{filename}'.")
                else:
                    print("The alias does not refer to a certificate.")
            except KeyError as e:
                print(e)
        elif choice == "5":
            filename = input("Enter the filename to save the keystore: ")
            save_keystore(filename)
        elif choice == "6":
            filename = input("Enter the filename to load the keystore: ")
            load_keystore(filename)
        elif choice == "7":
            alias = input("Enter the alias to retrieve from the keystore: ")
            try:
                item = get_from_keystore(alias)
                print(f"Retrieved item: {item}")
            except KeyError as e:
                print(e)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()