class Book:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_name(self):
        return self.name

    def to_string(self):
        return(self.name + self.category)


my_book = Book("Hary potter", "Finc")
your_book = Book("TLOFT", "NS")

print(my_book.get_name())
print(your_book.to_string())
print("hello")
print('h')