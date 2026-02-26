class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    # INSTANCE METHOD
    def ArrangeDate(self):
        return f"{self.day}-{self.month}-{self.year}"
        
    # CLASS METHOD
    @classmethod
    def getStringData(cls, string):
        import re
        
        data = re.findall(r'\d{1,2}[-/]\d{1,2}[-/]\d{4}', string)[0]
        data = data.replace('/', '-')
        day, month, year = data.split('-')
        
        return cls(day, month, year)
        
    # STATIC METHOD
    @staticmethod
    def setDataPattern(string):  # 👈 must accept argument
        parts = string.replace('/', '-').split('-')
        return f"{parts[2]}-{parts[1]}-{parts[0]}"
        

today = Date(22, 2, 2026)

print(Date.setDataPattern('2026-2-22'))
print(today.ArrangeDate())