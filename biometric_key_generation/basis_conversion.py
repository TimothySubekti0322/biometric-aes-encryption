def binary_to_hex(binary_key):
    """
    Mengonversi string biner 128-bit menjadi string hexadecimal.
    
    Parameters:
    binary_key (str): String biner 128-bit
    
    Returns:
    str: String hexadecimal yang setara
    """
    # if len(binary_key) != 128:
    #     raise ValueError("Panjang kunci biner harus 128 bit.")
    
    # Mengonversi string biner ke integer, kemudian ke hexadecimal
    hex_key = hex(int(binary_key, 2))[2:]
    
    # Pastikan panjang hexadecimal adalah 32 karakter (128 bit)
    return hex_key.zfill(32)

def binary_to_ascii(binary_key):
    """
    Mengonversi string biner 128-bit menjadi string ASCII.
    
    Parameters:
    binary_key (str): String biner 128-bit
    
    Returns:
    str: String ASCII yang setara
    """
    # if len(binary_key) != 128:
    #     raise ValueError("Panjang kunci biner harus 128 bit.")
    
    # Membagi string biner menjadi kelompok 8-bit
    ascii_chars = [chr(int(binary_key[i:i+8], 2)) for i in range(0, len(binary_key), 8)]
    
    # Menggabungkan karakter ASCII menjadi string
    ascii_key = ''.join(ascii_chars)
    
    return ascii_key