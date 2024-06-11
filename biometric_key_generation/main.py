import cv2
import os

# Import Module
from segment_and_normalize import segment_and_normalize
from estimate_orientation import estimate_orientation
from binarize_and_thin_image import binarize_and_thin_image
from extract_minutiae import extract_minutiae
from generate_biometric_key import generate_biometric_key
from display_image import display_image
from basis_conversion import binary_to_hex, binary_to_ascii

# Fungsi Membaca Gambar
fingerprint_image = cv2.imread("biometric_key_generation/picture/sample2.jpg", cv2.IMREAD_GRAYSCALE)
display_image('Fingerprint Image', fingerprint_image)

# Segmentasi dan normalisasi
segmented_image, normalized_image = segment_and_normalize(fingerprint_image)

# Tampilkan gambar yang telah disegmentasi dan dinormalisasi
# display_image('Segmented Image', segmented_image)
display_image('Normalized Image', normalized_image)

# Estimasi orientasi blok
orientation_image = estimate_orientation(normalized_image)

# Binarisasi dan thinning citra
binary_thin_image = binarize_and_thin_image(normalized_image)

# Tampilkan gambar biner dan hasil thinning
display_image('Binerize and Thin Image', binary_thin_image)


# Ekstraksi minutiae menggunakan perpustakaan
minutiae_points = extract_minutiae(binary_thin_image)

# Ekstraksi minutiae
# minutiae_points = extract_minutiae(binary_thin_image)

print(f"Minutiae Points Length: {len(minutiae_points)}")

# Generasi kunci biometrik
bio_key = generate_biometric_key(minutiae_points)

print(f"Generated Biometric Key: {bio_key}")



# print(f"Hexadecimal Key: {binary_to_hex(bio_key)}")

# print(f"ASCII Key: {binary_to_ascii(bio_key)}")

