class myschool(object):
    name=""
    address=""
    type="katherine"
    def print_school(self):
        print(myschool.name)
        print(myschool.address)
        print(myschool.type)
def main():
    school1=myschool()
    school1.name="chengdu"
    school1.address="changhuaqu"
    school1.type="daxue"
    school1.print_school()
if __name__=="__main__":
    main()