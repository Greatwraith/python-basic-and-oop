# Rumus pertumbuhan produk setiap versi:
# product_baru = product_lama × versi_sekarang

versi_product = 1
product = 1

while versi_product < 5:
    product = product * versi_product
    versi_product += 1


print("dari percobaan membuat versi terbaru, dari versi pertama sampai versi terbaru telah menghasilkan", product, "products")
print("Versi Terbaru:", versi_product)


# RUMUS
# product_baru = product_lama × versi_sekarang


# MASA AWAL
# Pada versi pertama:
# versi_product = 1
# product = 1 (1 produk awal)


# Loop 1:
# versi_product = 1
# product = 1 × 1 = 1
# lalu versi_product naik → 2


# Loop 2:
# versi_product = 2
# product = 1 × 2 = 2
# lalu versi_product naik → 3


# Loop 3:
# versi_product = 3
# product = 2 × 3 = 6
# lalu versi_product naik → 4


# Loop 4:
# versi_product = 4
# product = 6 × 4 = 24
# lalu versi_product naik → 5


# Loop berhenti karena:
# versi_product < 5 → 5 < 5 ❌ (false)

# HASIL AKHIR:
# Total produk = 24
# Versi terbaru = 5