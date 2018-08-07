
import pymysql
db=pymysql.connect("localhost","katherine","123456","db_kate")
cursor=db.cursor()
sql="""select * from t_student"""
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for items in results:
        print(items)
except:
    print("error:unable to fetch data!")
db.close()
