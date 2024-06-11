def generate_biometric_key(minutiae_points):
    # Mengubah setiap minutiae point tuple menjadi binary string
    minutiae_points_str = [''.join(format(x, '08b') for x in point) for point in minutiae_points]
    
    # Step 1: Identifikasi titik Minutiae pada RoI
    NP = len(minutiae_points_str)
    
    # Step 2: Menghitung modulus dari jumlah titik Minutiae dengan 128
    Rem = NP % 128
    
    # Step 3: Menghitung total titik Minutiae yang tersedia untuk penyimpanan
    NP = NP - Rem
    
    # Step 4: jumlah interaksi yang diperlukan untuk mengompresi ukuran kunci menjadi 128-bit
    J = NP // 128
    
    # Step 5: menghilangkan 64 bit kiri dan 64 bit kanan. Bagi sisa kunci yang tersisa menjadi ML dan MR
    key_set = ''.join(minutiae_points_str[:NP])
    ML = []
    MR = []
    
    for i in range(J):
        segment = key_set[i*128:(i+1)*128]
        ML.append(segment[:64])
        MR.append(segment[64:])
    
    # Step 6: Tukar ML dan MR
    swapped_keys = [MR[i] + ML[i] for i in range(J)]
    
    # kombinasikan semua kunci yang ditukar menjadi satu kunci 128-bit
    combined_key = ''.join(swapped_keys)[:128]
    
    # Step 7: ubah 128 bit ini menjadi angka heksadesimal
    biometric_key = hex(int(combined_key, 2))[2:].zfill(32)
    
    return biometric_key