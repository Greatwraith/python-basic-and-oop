# Method that returns a value
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
    # this method takes the value of years and multiplies it by 18 
    # to return the pig years equivalent of the piglet's age in human years.


# 
piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())