
# STUDY CASE: HITUNG MUNDUR ROKET

def count_down(start_number):
    
    current = start_number   # angka awal untuk memulai hitung mundur
    
    
    while 0 < current:
        print(current)
        current -= 1
    
    print("Zero!")


count_down(3)



# Rumus perubahan setiap langkah:
# current_baru = current_lama − 1

# MASA AWAL (di awal tidak akan dilakukan loop)
# start_number = 3
# current = 3


# Loop 1:
# current = 3
# cetak 3
# current = 3 − 1 = 2
# cetak lagi dari 3 menjadi 2


# Loop 2:
# current = 2
# cetak 2
# current = 2 − 1 = 1 
# cetak lagi dari 2 menjadi 1


# Loop 3:
# current = 1
# cetak 1
# current = 1 − 1 = 0
# cetak lagi dari 1 menjadi 0


# Loop berhenti karena:
# 0 < current → 0 < 0 ❌ (false)


# HASIL:
# Output:
# 3
# 2
# 1
# Zero!
