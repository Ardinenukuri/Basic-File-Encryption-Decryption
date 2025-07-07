# File Crypter CLI

A secure, command-line tool for encrypting and decrypting files using Fernet (AES128-CBC) symmetric encryption from the Python `cryptography` library.

This project demonstrates professional development practices, including a clean architecture that separates core logic from the user interface, a robust CLI built with `argparse`, and unit tests to ensure the reliability and security of the encryption process.

## Features

-   **Secure Encryption**: Uses the industry-standard Fernet symmetric encryption scheme.
-   **Key Management**: Simple commands to generate and use encryption keys.
-   **Full Workflow**: Encrypt and decrypt any file directly from your terminal.
-   **Robust CLI**: A user-friendly interface with distinct commands and helpful messages.
-   **Thoroughly Tested**: Unit tests verify the encryption-decryption cycle and failure modes (e.g., using the wrong key).

## Project Structure

```
file_crypter_project/
├── crypter/
│   └── core.py         # Core encryption/decryption logic
├── tests/
│   └── test_core.py    # Unit tests
├── main.py             # CLI entry point
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

-   Python 3.7 or higher

### Installation

1.  Clone this repository to your local machine.
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

The tool operates via three main commands: `generate-key`, `encrypt`, and `decrypt`.

### Step 1: Generate a Key

First, you must generate an encryption key. This key is required for both encryption and decryption. **Keep this key file safe and secret!**

```bash
python main.py generate-key my_secret.key
```
This will create a file named `my_secret.key` in your directory.

### Step 2: Encrypt a File

Use the generated key to encrypt any file. For this example, create a file named `data.txt` with some secret content.

```bash
python main.py encrypt my_secret.key data.txt
```
By default, this will create an encrypted file named `data.txt.enc`. You can specify a different output file with the `-o` flag:
```bash
python main.py encrypt my_secret.key data.txt -o encrypted_file.dat
```

### Step 3: Decrypt a File

Use the same key to decrypt the file and retrieve the original content.

```bash
python main.py decrypt my_secret.key data.txt.enc
```
This will create a decrypted file named `data.txt.dec`, which will contain the original content of `data.txt`. You can specify a different output file with `-o`.

### How to Run Tests

The project includes unit tests for the core encryption logic. To run them, use Python's built-in `unittest` module from the project's root directory:

```bash
python -m unittest discover
```
An "OK" status confirms that the core logic is working correctly and securely.