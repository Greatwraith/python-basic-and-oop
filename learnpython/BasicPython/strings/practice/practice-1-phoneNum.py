phoneNumber= '2025551212'

area_code = "(" + phoneNumber[:3] + ")"
exchange = phoneNumber[4:7]  
line = phoneNumber[-4:]

ConstructAll = area_code + " " + exchange + "-" + line

print(ConstructAll)

