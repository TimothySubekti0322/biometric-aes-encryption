import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from dotenv import dotenv_values, set_key

def aes_128_encrypt(key_hex, env_file):
    
    # Convert the hex key to bytes
    key = bytes.fromhex(key_hex)
    if len(key) != 16:
        raise ValueError("Key must be 128 bits (16 bytes) long")

    # Load the environment variables from the file
    env_vars = dotenv_values(env_file)

    # Initialize the AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt each environment variable value
    encrypted_env_vars = {}
    for var, value in env_vars.items():
        # Convert value to bytes and pad it
        value_bytes = value.encode()
        padded_value = pad(value_bytes, AES.block_size)
        
        # Encrypt the padded value
        encrypted_value = cipher.encrypt(padded_value)
        
        # Convert the encrypted value to hex
        encrypted_value_hex = encrypted_value.hex()
        
        # Store the encrypted value in the dictionary
        encrypted_env_vars[var] = encrypted_value_hex

    # Write the encrypted values back to the .env file
    for var, encrypted_value in encrypted_env_vars.items():
        set_key(env_file, var, encrypted_value)


