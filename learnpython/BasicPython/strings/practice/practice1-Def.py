def format_phone(phoneNumber):
    area_code = "(" + phoneNumber[:3] + ")"
    exchange = phoneNumber[3:6]
    line = phoneNumber[-4:]
    return area_code + ' ' + exchange + "-" + line


printFormatPhone = format_phone('2025551212')
print(printFormatPhone)

    