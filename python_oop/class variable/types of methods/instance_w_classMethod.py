class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    # INSTANCE METHOD → uses object data
    def ArrangeDate(self):
        dateArranged = str(self.day) + "-" + str(self.month) + "-" + str(self.year)
        return dateArranged
        
        
    @classmethod
    def getStringData(cls, string):
        import re
        
        # allow 1 or 2 digit day/month
        data = re.findall(r'\d{1,2}[-/]\d{1,2}[-/]\d{4}', string)[0]
        
        data = data.replace('/', '-')
        day, month, year = data.split('-')
        
        # build and return object
        return cls(day, month, year)
        


today = Date.getStringData('today is 22-2-2026')
print(today.__dict__)
print(today.ArrangeDate())