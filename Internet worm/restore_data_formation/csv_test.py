import csv


#字段序列必须相互对应，  csv是一种常见用逗号或制表符分割的字符串格式
header=['ID','Username','password','age','country']
rows=[                                            #rows列表中的元组数据，也可以是字典数据
    (1001,'qiye','adf',24,'china'),
    (1002,'shuai','gdsa',25,'English'),
    (1003,'mary','gas',26,'Usa')
     ]

#创建csv文件
with open('katheine.csv','w') as fp:
    f_csv=csv.writer(fp)   #创建一个csv.writer（）对象，写入数据
    f_csv.writerow(header)  #写入单行
    f_csv.writerows(rows)    #写入多行
#读取csv文件
with open('katheine.csv') as fp:
    data=csv.reader(fp)  #data为一个迭代器
    #header=next(data)
    #print(header)
    for row in data:  #访问剩余行
        if row:       #出去中间为空行的数据
            print(row)
            #可以甩列表索引的下表访问字段
            print(row[1],row[2])

#为了方便访问列字段，建议使用读取字典序列方法
with open('katheine.csv') as fp:
    f_csv=csv.DictReader(fp)
    for row in f_csv:
        if row:
            print(row)
            print(row.get("Username"),row.get("password"))
