import mysql.connector as con

class DB:
    # initialising database connection
    def __init__(self):
        self.mydb = con.connect(
            host = "localhost",
            user = "root",
            passwd = "asdfghjkl",
            database = "banking"
        )

    # fetching the data of particular user
    def fetch_data(self , p_id):
        cursor = self.mydb.cursor()
        cursor.execute(f"select * from users where id = {p_id};")
        
        result = cursor.fetchall()
        return result

class Acc_Detail:
    __db = DB()

    def __init__(self , name ,id):
        self.id = id
        self.name = name


    def __str__(self):
        return f"Name : {self.name} \nId : {self.id}"

    # checking the password and validating login if correct
    def validate_login(self , pas):
        res = self.__db.fetch_data(self.id)
        try :
            if res[0][1] != pas:
                return False
            else:
                return True
        except IndexError:
            return False


    # returning balance
    def chk_balance(self):
        data = self.__db.fetch_data(self.id)
        return data[0][11]

    # returning account activation date
    def acc_act(self):
        data = self.__db.fetch_data(self.id)
        return data[0][10]

    # returning account status
    def acc_stat(self):
        data = self.__db.fetch_data(self.id)
        return data[0][9]

    # returning account type
    def acc_type(self):
        data = self.__db.fetch_data(self.id)
        return data[0][8]

