Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class myschool():
    name=""
    address=""
    type="大学"
    def print_school(self):
        print(myschool.name)
        print(myschool.address)
        print(myschool.type)
    school1=myschool()
    school2=myschool()
    school1.name="chengdu"
    school1.address="changhuaqu"
    school1.type="daxue"
    school1.name="chuangda"
    school2.address="jinjiang"
    school2.type="daxue"
    school1.print_school()
    school2.print_school()
