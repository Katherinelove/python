filename="write.txt"
with open(filename,"a") as file_object:
    file_object.write("katherine, I love you,do you know?")
    file_object.write("katherine, I love you,do you know?")        #write 不包含换行符
    file_object.write("\nkatherine, I love you,do you know?\n")
    file_object.write("katherine, I love you,do you know?\n")