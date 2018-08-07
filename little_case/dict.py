def get_sprecial():
    monday={"B":"milk","L":"shuai","D":"shui"}
    tuesday={"B":"milk","L":"shuai","D":"shui"}
    wednsday={"B":"milk","L":"shuai","D":"shui"}
    thursday={"B":"milk","L":"shuai","D":"shui"}
    friday={"B":"milk","L":"shuai","D":"shui"}
    saturday={"B":"milk","L":"shuai","D":"shui"}
    sunday={"B":"milk","L":"shuai","D":"shui"}
    specials={"M":monday,
              "T":tuesday,
              "W":wednsday,
              "R":thursday,
              "F":friday,
              "St":saturday,
              "Sn":sunday}
    return specials
def print_special(special):
    print("The special is:")
    print(special)
    print("*"*15)
def get_day():

    day=input("day [M/T/W/R/F/St/Sn]:")
    if(day.upper() in ["M","T","W","R","F","ST","SN"]):
        return day.upper()
    else:
        print("I am sorry,{} is not valid".format(day))
def get_time():

    time=input("time [B/L/D]:")
    if time.upper() in ["B","L","D"]:
         return time.upper()
    else:
         print("I am sorry ,{} is invalid".format(time))
def main():
    specials=get_sprecial()
    print("this script can tell you the specials for any day of any week,and any time.")
    while True:
        day=get_day()
        special=specials[day]
        time=get_time()
        print_special(special[time])
        another=input("do you want to check another day and time?(Y/N)")
        if another.lower()=="n":
            break
if __name__=="__main__":
    main()

