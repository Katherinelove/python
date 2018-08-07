class Car():
	""""创建一个car类！"""
	def __init__(self,make,,modle,year):
		self.make=make
		self.modle=modle
		self.year=year
	
	def change_make(self,make=""):
		if not make:
			message="please input new make:"
			new_make=input(message)
		self.make=new_make		

	def change_modle(self,modle=""):
		if not modle:
			message="please input new modle:"
			new_modle=input(message)
		self.modle=new_modle	
	def change_year(self,year=""):
		if not year:
			message="please input new year:"
			new_year=input(message)
		self.year=new_year	
	def get_descrption(self):
		long_name=str(self.year)+" "+make+" "+modle
		return long_name

my_car=Car(audi,A4,2016)
print(my_car.get_description())
