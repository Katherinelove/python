def count_words(file_name):
    """同时统计多本书！"""
    try:
        with open(file_name) as file_object:
            words = file_object.read()
    except:
        msg = "sorry"
        print("sorry,the file " + file_name + " does not exist")
    else:
        words_list = words.split()  # 利用split分析文本 eg：统计大致单词数
        words_num = len(words_list)
        msg = "this file " + file_name + " has about " + str(words_num) + " words"
        print(msg)

#file_name="write.txt"        #这样一个一个调用文件名不明智，可以选择利用list列表存储书名
#count_words(file_name)
#file_name="11.txt"
#count_words(file_name)

file_names=["write.txt","sb.txt","11.txt"]
for file_name in file_names:
    count_words(file_name)