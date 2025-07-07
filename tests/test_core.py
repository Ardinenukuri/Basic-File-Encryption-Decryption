import unittest
from cryptography.fernet import InvalidToken
from crypter.core import generate_key, encrypt_data, decrypt_data

class TestCrypterCore(unittest.TestCase):

    def setUp(self):
        """Set up keys for the tests."""
        self.key1 = generate_key()
        self.key2 = generate_key() 

    def test_encryption_decryption_cycle(self):
        """Tests that data can be encrypted and then decrypted back to the original."""
        original_data = b"This is a secret message for testing."
        
        # Encrypt the data
        encrypted_data = encrypt_data(original_data, self.key1)
        
        # Assert that encrypted data is not the same as the original
        self.assertNotEqual(original_data, encrypted_data)
        
        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data, self.key1)
        
        # Assert that decrypted data matches the original
        self.assertEqual(original_data, decrypted_data)

    def test_decryption_fails_with_wrong_key(self):
        """Tests that decryption raises an InvalidToken error if the wrong key is used."""
        original_data = b"Another secret."
        
        # Encrypt with key1
        encrypted_data = encrypt_data(original_data, self.key1)
        
        # Assert that decrypting with key2 raises the correct exception
        with self.assertRaises(InvalidToken):
            decrypt_data(encrypted_data, self.key2)

    def test_decryption_fails_with_corrupted_data(self):
        """Tests that decryption fails if the encrypted token is altered."""
        original_data = b"Data to be corrupted."
        encrypted_data = encrypt_data(original_data, self.key1)
        
        # Corrupt the data by changing one byte
        corrupted_data = encrypted_data[:-1] + b'X'

        with self.assertRaises(InvalidToken):
            decrypt_data(corrupted_data, self.key1)