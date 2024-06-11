from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_128_decrypt(key_hex, encrypted_data):
    try:
        # Convert key and encrypted data to bytes
        print(f"key_hex = {key_hex}")
        key = bytes.fromhex(key_hex)
        encrypted_bytes = bytes.fromhex(encrypted_data)

        # Initialize the AES cipher in ECB mode
        cipher = AES.new(key, AES.MODE_ECB)

        # Decrypt the message
        decrypted_bytes = cipher.decrypt(encrypted_bytes)

        # Unpad the message
        decrypted_message = unpad(decrypted_bytes, AES.block_size)

        # Convert bytes to string
        decrypted_text = decrypted_message.decode('utf-8')

        return decrypted_text
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None
