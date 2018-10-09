class Book:

    def __init__(self, title, pageCount, isbn):
        self.title = title 
        self.pageCount = pageCount 
        self.ISBN = isbn
        self.isCheckedOut = False
        self.dayCheckOut = -1

    # Getters
    def getTitle(self):
        return  self.title
    
    def getPageCount(self):
        return self.pageCount

    def getISBN(self):
        return self.ISBN

    def getIsCheckedOut(self):
        return self.isCheckedOut

    def getDayCheckOut(self):
        return self.dayCheckOut

    # Setters
    def setIsCheckedOut(self, checkOut, currentDay):
        self.isCheckedOut = checkOut

    def __setDayCheckOut(self, day):
        self.dayCheckOut = day

if __name__ == "__main__":
    x = Book("harry potter", 88, 4444)
    print(x.getTitle())


