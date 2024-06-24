def bin_to_dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

# Meminta pengguna memasukkan nombor perduaan
binary_number = input("Masukkan nombor perduaan: ")

# Menukar nombor perduaan kepada nombor perpuluhan
decimal_number = bin_to_dec(binary_number)

# Memaparkan hasil penukaran
print(f"Nombor perduaan {binary_number} dalam perpuluhan adalah {decimal_number}")