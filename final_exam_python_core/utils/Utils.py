import json
from entitys.Hocvien import Student
from entitys.Monhoc import Subject
from entitys.Diemthi import Score
import mysql.connector
from mysql.connector import Error


class Utils:

    def __init__(self) -> None:
        self.__nameDatabase = "qlStudent"

    # json
    def utilReadJson(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            json_ob = json.load(f)
        return json_ob

    def utilWriteJson(self, filepath, data):
        with open(filepath, 'w') as f:
            json.dump(data, f)


    def utilMapStudent(self, obj):
        #for json
        # return Student(obj["Student_ID"], obj["Name"], obj["DoB"], obj["Sex"], obj["Address"], obj["Mobile_Number"], obj["Email"])
        #for sql
        return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])

    def utilMapSubject(self, obj):
        #for json
        # return Subject(obj["Subject_ID"], obj["Name"])
        #for sql
        return Subject(obj[0], obj[1])

    def utilMapScore(self, obj):
        #for json
        # return Score(obj["Student_ID"], obj["Subject_ID"], obj["Midel_Score"], obj["Final_Score"])
        #for sql
        return Score(obj[0], obj[1], obj[2], obj[3])


    # sql
    def utilConnectsql(self):
        self.__con = mysql.connector.connect(
            host="localhost", database=self.__nameDatabase, user="root", passwd="root")
        return self.__con

    def utilClosesql(self):
        if self.__con.is_connected():
            self.__con.close()

    def utilCreateDatabase(self, name_database, host="localhost", user="root", passwd="root"):
        try:
            myconn = mysql.connector.connect(
                host=host, user=user, passwd=passwd)
            if myconn.is_connected():
                print('Connected to MySQL Database')
                cur = myconn.cursor()
                cur.execute("create database {}".format(name_database))
                print('Create database success!')
        except Error:
            print("Error: ", Error)
        finally:
            if myconn.is_connected():
                cur.close()
                myconn.close()

    def utilCreateTable(self):
        try:
            myconn = self.utilConnectsql()
            if myconn.is_connected():
                excute = """
        CREATE TABLE `Student`(

            `Student_ID` VARCHAR(10) PRIMARY KEY,
            `Name` VARCHAR(50) NOT NULL,
            DoB DATETIME NULL,
            Sex VARCHAR(10),
            Address VARCHAR(50),
            MobileNumber VARCHAR(50) NOT NULL ,
            Email VARCHAR(50) UNIQUE KEY NOT NULL
            
        );

        CREATE TABLE `Subject`(

        `Subject_ID` VARCHAR(10) PRIMARY KEY,
        `Name` VARCHAR(50) NOT NULL
        );

        CREATE TABLE `Score`(

        `Student_ID` VARCHAR(10),
        `Subject_ID` VARCHAR(10),
        Midel_Score int,
        Final_Score int,
        Xeploai VARCHAR(10),
        FOREIGN KEY(`Student_ID`) REFERENCES `Student`(`Student_ID`) ON DELETE CASCADE,
        FOREIGN KEY(`Subject_ID`) REFERENCES `Subject`(`Subject_ID`) ON DELETE CASCADE
        );
        """
                cur = myconn.cursor()
                cur.execute(excute)
                print('Create table success!')
            self.utilClosesql()
        except Error:
            print("Error: ", Error)

    def utilInsertMutipleRecord(self, sql, vals):
        try:
            myconn = self.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                try:
                    cur.executemany(sql, vals)
                    myconn.commit()
                    print("Insert success!, {} record(s) affected".format(cur.rowcount))
                except Error:
                    print("Error1: ",Error)
                    myconn.rollback() 
            self.utilClosesql()
        except Error:
            print("Error: ",Error)