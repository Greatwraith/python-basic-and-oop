kelipatanDua = [x for x in range(0, 20) if x % 2 == 0]
print(kelipatanDua)

# hitung kelipatan 2 dari 0 sampai 20

# START
# 1st iteration: x = 0, kelipatanDua = [0]

# ‼️ 2nd iteration: x = 1, 
# kelipatanDua = [0] (1 tidak memenuhi kondisi x % 2 == 0)

# ✅ 3rd iteration: x = 2, 
# kelipatanDua = [0, 2]

# ‼️ 
# 4th iteration: x = 3, 
# kelipatanDua = [0, 2] (3 tidak memenuhi kondisi x % 2 == 0)

# ✅ 5th iteration: x = 4, 
# kelipatanDua = [0, 2, 4]

# ‼️ 6th iteration: x = 5, 
# kelipatanDua = [0, 2, 4] (5 tidak memenuhi kondisi x % 2 == 0)