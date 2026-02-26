class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    # INSTANCE METHOD
    def ArrangeDate(self):
        dateArranged = str(self.day) + "-" + str(self.month) + "-" + str(self.year)
        # It uses instance data(self.day, self.month, self.year)
        
        return dateArranged
        

        
today = Date(22,2,2026)
# print(today.__dict__)
print(today.ArrangeDate())

