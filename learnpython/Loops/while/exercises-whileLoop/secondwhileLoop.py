# BELAJAR PULL UP
# “Saya sudah bisa 5 pull-up di hari pertama.
# Setiap hari berikutnya, saya menambah beban latihan sebesar nomor hari itu, sampai hari ke-5.”


# rumus pull up yang harus dilakukan secara berkala sampai menyentuh hari ke 5
# total_yg_harus_dilakukan = NomorHariSekarang + totalSekarang


hari_ke = 1
total_pullups = 5   # total sebelum mulai siklus ini/ mulai memperlancar

while hari_ke < 5:
    hari_ke += 1
    total_pullups += hari_ke
    # Alternatif
    # hari_ke = hari_ke + 1
    # total_pullups = total_pullups + hari_ke

print("Total sampai hari ke-5:", total_pullups)






# MASA BELAJAR/ HARI PERTAMA
# pada masa belajar di hari pertama, mampu melakukan 5 pull up.
# hari_ke = 1, total = 5(total 5 kali pull up)


# Loop pertama:
# hari_ke = 2
# total = 5 + 2 = 7

# Loop 2:
# hari_ke = 3
# total = 7 + 3 = 10

# Loop 3:
# hari_ke = 4
# total = 10 + 4 = 14

# Loop 4:
# hari_ke = 5
# total = 14 + 5 = 19
