print("Nama : D.Wita Aeni")
print("NIM : 312110222")

def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:]

def bin_to_hex(bin_string):
    return hex(int(bin_string, 2))[2:]

def encrypt_ecb(plaintext_hex, key_bin):
    plaintext_bin = hex_to_bin(plaintext_hex)
    key_length = len(key_bin)

    # Step 4: Pisahkan per blok 4 bit
    blocks = [plaintext_bin[i:i+4] for i in range(0, len(plaintext_bin), 4)]

    # Step 5-6: XOR dan geser tiap blok
    encrypted_blocks = []
    for block in blocks:
        xor_result = bin(int(block, 2) ^ int(key_bin, 2))[2:].zfill(4)
        shifted_result = xor_result[1:] + xor_result[0]
        encrypted_blocks.append(shifted_result)

    # Step 7: Konversi hasil XOR ke hexadecimal
    encrypted_hex = [str(int(block, 2)) for block in encrypted_blocks]

    return encrypted_hex

# Input user
plainteks_hex = input("Masukkan Plainteks: ").upper()
kunci_bin = input("Masukkan Kunci: ")

# Enkripsi ECB
hasil_enkripsi_ecb = encrypt_ecb(plainteks_hex, kunci_bin)

# Output hasil enkripsi
print("Hasil enkripsi ECB:", hasil_enkripsi_ecb)