import mysql.connector as con

class DB:
    def __init__(self):
        self.mydb = con.connect(
            host = "localhost",
            user = "root",
            passwd = "asdfghjkl",
            database = "banking"
        )

    def fetch_data(self , p_id):
        cursor = self.mydb.cursor()
        cursor.execute(f"select * from users where id = {p_id}")
        result = cursor.fetchall()
        # for i in result:
        #     print(i)

        return result

class Acc_Detail:
    __db = DB()
    # data = __db.fetch_data(id)

    def __init__(self , name ,id):
        self.id = id
        self.name = name


    def __str__(self):
        return f"Name : {self.name} \nId : {self.id}"


    def validate_login(self , pas):
        res = self.__db.fetch_data(self.id)
        if res[0][1] != pas:
            return False
        else:
            return True


    def chk_balance(self):
        data = self.__db.fetch_data(self.id)
        return data[0][11]

    def acc_act(self):
        data = self.__db.fetch_data(self.id)
        return data[0][10]

    def acc_stat(self):
        data = self.__db.fetch_data(self.id)
        return data[0][9]

    def acc_type(self):
        data = self.__db.fetch_data(self.id)
        return data[0][8]

