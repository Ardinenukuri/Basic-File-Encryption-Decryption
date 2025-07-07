import argparse
from cryptography.fernet import InvalidToken
from crypter.core import generate_key, encrypt_data, decrypt_data

def handle_generate_key(args):
    """Handles the 'generate-key' command."""
    key = generate_key()
    try:
        with open(args.key_file, 'wb') as f:
            f.write(key)
        print(f"✅ Key successfully generated and saved to '{args.key_file}'")
    except IOError as e:
        print(f"❌ Error: Could not write key to file. {e}")

def handle_encrypt(args):
    """Handles the 'encrypt' command."""
    try:
        with open(args.key_file, 'rb') as f:
            key = f.read()
        with open(args.input_file, 'rb') as f:
            data = f.read()
        
        encrypted_data = encrypt_data(data, key)
        
        output_file = args.output_file or f"{args.input_file}.enc"
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)
        
        print(f"✅ File '{args.input_file}' encrypted successfully to '{output_file}'")
        
    except FileNotFoundError as e:
        print(f"❌ Error: File not found. {e}")
    except IOError as e:
        print(f"❌ Error: Could not read or write file. {e}")

def handle_decrypt(args):
    """Handles the 'decrypt' command."""
    try:
        with open(args.key_file, 'rb') as f:
            key = f.read()
        with open(args.input_file, 'rb') as f:
            token = f.read()

        decrypted_data = decrypt_data(token, key)

        output_file = args.output_file or args.input_file.replace('.enc', '.dec')
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        print(f"✅ File '{args.input_file}' decrypted successfully to '{output_file}'")

    except FileNotFoundError as e:
        print(f"❌ Error: File not found. {e}")
    except InvalidToken:
        print("❌ Decryption Failed: Invalid key or corrupted file.")
    except IOError as e:
        print(f"❌ Error: Could not read or write file. {e}")

def main():
    """Main function to run the File Crypter CLI."""
    parser = argparse.ArgumentParser(description="A tool to encrypt and decrypt files.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # --- Generate Key Command ---
    parser_genkey = subparsers.add_parser("generate-key", help="Generate a new encryption key.")
    parser_genkey.add_argument("key_file", help="The path to save the new key file (e.g., mykey.key).")
    parser_genkey.set_defaults(func=handle_generate_key)

    # --- Encrypt Command ---
    parser_encrypt = subparsers.add_parser("encrypt", help="Encrypt a file.")
    parser_encrypt.add_argument("key_file", help="The path to the encryption key file.")
    parser_encrypt.add_argument("input_file", help="The path to the file to encrypt.")
    parser_encrypt.add_argument("-o", "--output", dest="output_file", help="The path to save the encrypted file.")
    parser_encrypt.set_defaults(func=handle_encrypt)

    # --- Decrypt Command ---
    parser_decrypt = subparsers.add_parser("decrypt", help="Decrypt a file.")
    parser_decrypt.add_argument("key_file", help="The path to the encryption key file.")
    parser_decrypt.add_argument("input_file", help="The path to the file to decrypt.")
    parser_decrypt.add_argument("-o", "--output", dest="output_file", help="The path to save the decrypted file.")
    parser_decrypt.set_defaults(func=handle_decrypt)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()