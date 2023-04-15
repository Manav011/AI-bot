import mysql.connector as con

class DB:
    def __init__(self):
        self.mydb = con.connect(
            host = "localhost",
            user = "root",
            passwd = "asdfghjkl",
            database = "banking"
        )

    def fetch_data(self , p):
        cursor = self.mydb.cursor()
        cursor.execute(f"select * from usersb where id = {p.id}")
        result = cursor.fetchall()
        # for i in result:
        #     print(i)

        return result

class Acc_Detail:
    def __init__(self , name ,id):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Name : {self.name} \nId : {self.id}"

    def validate_login(self , pas):
        db = DB()
        res = db.fetch_data(self)
        if res[0][4] != pas:
            print("Invalid password")
        else:
            print(res)



name , id = input("Enter your name and user id: ").split()
p1 = Acc_Detail(name , id)

passw = input("Enter your password : ")
p1.validate_login(passw)

