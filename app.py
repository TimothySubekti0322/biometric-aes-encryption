from flask import Flask, jsonify
from dotenv import load_dotenv, dotenv_values
import os
from AES.aes_128_encrypt import aes_128_encrypt
from AES.aes_128_decrypt import aes_128_decrypt
from AES.get_secret import get_key_secret_manager
from biometric_key_generation.biometric_key_generation import biometric_key_generation

app = Flask(__name__)

# Load environment variables from a file
def load_env_file(env_file):
    load_dotenv(env_file)
    return dotenv_values(env_file)

# Load the environment variables
env_file = ".env"  # Path to the environment variable file
env_vars = load_env_file(env_file)

@app.route("/")
def get_env_vars():
    # Return the environment variables as a JSON response
    return jsonify(env_vars)

@app.route("/encryptEnvirontmentVariables")
def encrypt_env_vars():
    # Import the AES encryption function
    key = biometric_key_generation("biometric_key_generation/picture/sample2.jpg")
    
    print(f"key = {key}")

    # Get the AES key from the environment variables
    # key_hex = os.getenv("AES_KEY")

    # Encrypt the environment variables
    aes_128_encrypt(key, env_file)

    # Return a success message
    return "Environment variables encrypted successfully!"

@app.route("/decryptEnvirontmentVariables")
def decrypt_env_vars():
    
    key = get_key_secret_manager()
    
    env_vars = dotenv_values(env_file)
    
    #Decyrpt semua nilai environment variable dan masukan ke suatu variable dan kirim ke frontend
    
    decrypted_env_vars = {}
    for var, encrypted_value in env_vars.items():
        decrypted_value = aes_128_decrypt(key, encrypted_value)
        decrypted_env_vars[var] = decrypted_value

    # Return the decrypted environment variables as a JSON response
    return jsonify(decrypted_env_vars)



if __name__ == "__main__":
    app.run(debug=True)
