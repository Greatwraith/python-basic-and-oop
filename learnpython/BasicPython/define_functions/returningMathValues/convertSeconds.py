def convert_seconds(seconds):
    hours = seconds // 3600 #Menghitung berapa jam penuh dari total detik || Convert seconds to hours
    minutes = (seconds - hours * 3600) // 60 #Menghitung menit penuh setelah jam diambil || Convert remaining seconds to minutes
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds #Menghitung detik sisa setelah jam dan menit diambil || Remaining seconds
 
remainingHoursMinutesSeconds= convert_seconds(5000)

print(str(remainingHoursMinutesSeconds), "Hours", str(remainingHoursMinutesSeconds), "minutes", str(remainingHoursMinutesSeconds), "Second")