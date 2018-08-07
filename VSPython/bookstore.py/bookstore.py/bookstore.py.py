class InventoryItem(object):
    def __init__(self, title,description,price,store_id):
        self.title=title
        self.description=description
        self.price=price
        self.store_id=store_id
    def __str__(self):
        return self.title
    def __eq__(self, other):
        if self.store_id==other.title:
            return True
        else:
            return False
    def change_description(self,description=""):
        if not description:
            description=input("please give me a description:")
        self.description=description
    def change_prie(self,price=-1):
        while price<0:
            price=input("please give me a new price[X.XX]:")
            try:
                price=float(price)
                break
            except:
                print("I am sorry,but {} is invalid".format(price))
        self.price=price
    def change_title(self,title=""):
        if not title:
            title=input("please give me a title:")
        self.title=title
class book(InventoryItem):
    def __init__(self, title,description,price,format,author,store_id):
        super(book,self).__init__(title=title,
        description=description,
        price=price,
        store_id=store_id)
        self.format=format
        self.author=author
    def __str__(self):
        book_line="{title} by {author}".format(title =self.title,author=self.author)
        return book_line
    def __eq__(self, other):
        if self.title==other.title and self.author==other.author:
            return True
        else:
            return False
    def change_format(self,format=""):
        if not format:
            format=input("please give me the new format:")
        self.format=format
    def change_author(self,author):
        if not author:
            author=input("please give me the new author:")
        self.author=author
hamlet=book(title="hamlet",
            description="A dane has a bad time",
            price=5.99,
            format="paperback",
            store_id="29382918",
            author="William shakespear")
hamlet_hardback=book(title="hamlet",
            description="A dane has a bad time",
            price=10.99,
            format="hardback",
            store_id="3894083920",
            author="William shakespear")
macbeth=book(title="Macbetch",
            description="Katherinelove",
            price=99.99,
            format="paperback",
            store_id="23928932",
            author="William shakespear")
print(hamlet==hamlet_hardback)
print(hamlet==macbeth)
print(hamlet,hamlet_hardback,macbeth)
hamlet.change_description()
print(hamlet.description)
macbeth.change_format(format="audiobook")
print(macbeth.format)
hamlet.change_title()
print(hamlet.title)
hamlet.change_format()
print(hamlet.format)