class Book:
    def __init__(self, name, author, publisher):
        self.name = name
        self.author = author
        self.publisher = publisher
        
    def check_book(self):
        print("\n\tBOOK: {} \n\tAUTHOR: {} \n\tPUBLISHER: {}".format(self.name,self.author,self.publisher))
        
            
    def book_checked(self):
        return f'{self.name} by {self.author} which is published by {self.publisher} has already been, checked and it is in perfect condition!'
        
class BookInfo(Book):
    def __init__(self, name, author, publisher, type, language, price ):
        super().__init__(name, author, publisher)
        self.type = type
        self.language = language
        self.price = price
        
    def check_book(self):
        print("\n\tBOOK: {} \n\tAUTHOR: {} \n\tPUBLISHER: {} \n\tTYPE: {} \n\tLANGUAGE: {} \n\tPRICE: {}".format(self.name, self.author, self.publisher, self.type, self.language, self.price))

        

strategyBook = Book('Il principe', 'Nicolo machiavelli', 'Narasi publisher')
print(strategyBook.__dict__)
strategyBook.check_book() # memanggil method dari Book
print("\n\t")
print(strategyBook.book_checked())




print("\n\t")



selfImprovementBook = BookInfo('Grit','Angela Duckworth', 'Gramedia Pustaka', 'self improvement & inspiration', 'Indonesia', 128000)
print(selfImprovementBook.__dict__)
selfImprovementBook.check_book() # memanggil method override dari BookInfo
print("\n\t")
# this method from class Book, which is a base class, is able to be called back from its subclass and has the same format but with different outputs for each object.
# i hope this is true
print(selfImprovementBook.book_checked())



# the output is Polymorphism,
# class nya berbeda beda, methodnya sama, tapi outputnya berbeda
# from different classes & has different outputs but same method from