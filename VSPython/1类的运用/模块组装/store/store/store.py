from doc import test

class Store():
    """存货店，一个book子类，一个magazine子类"""
    def __init__(self,title,description,price,id_store):
        self.title=title
        self.description=description
        self.price=price
        self.id_store=id_store
    def change_description(self,description):
        self.description=description
    def change_title(self,title):
        self.title=title
    def change_price(self,price):
        self.price=price

class Book(Store):
    """book 子类"""
    def __init__(self, title, description, price, id_store,author,format):
        super().__init__(title, description, price, id_store)
        self.author=author
        self.format=format
    def change_author(self,author):
        self.author=author
    def change_format(self,format):
        self.format=format
    def print_book_describe(self):
        print(self.author+"  "+self.format)


class Magazine(Store):
    """magazine 子类"""
    def __init__(self, title, description, price, id_store,year,month):
        super().__init__(title, description, price, id_store)
        self.year=year
        self.month=month
    def change_date(self,month,year):
        self.year=year
        self.month=month
    def print_date(self):
        print(str(self.year)+"/"+str(self.month))
my_book=Book("python","program",48,"0281818","kate","书籍")
my_magazine=Magazine("sci","文献",158,"0281616",2018,12)
my_book.print_book_describe()
my_magazine.print_date()
my_book.change_author("zengshuai")
my_book.change_format("杂志")
my_book.print_book_describe()
print(Store.__doc__)
