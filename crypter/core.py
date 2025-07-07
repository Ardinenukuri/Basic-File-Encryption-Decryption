from cryptography.fernet import Fernet, InvalidToken

def generate_key() -> bytes:
    """Generates a new Fernet encryption key."""
    return Fernet.generate_key()

def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypts data using the provided Fernet key."""
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(token: bytes, key: bytes) -> bytes:
    """
    Decrypts a token using the provided Fernet key.
    
    Raises:
        cryptography.fernet.InvalidToken: If the token is invalid or the key is wrong.
    """
    f = Fernet(key)
    return f.decrypt(token)