from utils.Utils import Utils
from entitys.Monhoc import Subject
from mysql.connector import Error

class SubjectService:
    
    def __init__(self):
        self.__utils = Utils()
        self.__filepath = "final_exam_python_core/utils/subjects.json"

    def getSubjectInfo(self):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute(
                    "SELECT * FROM Subject")
                result = cur.fetchall()
                if result:
                    subject_list = list(map(self.__utils.utilMapSubject, result))
                else:
                    subject_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return subject_list

    def createSubject(self):
        while True:
            subject_id = input("Enter subject id: ")
            if not self.getSubjectByID(subject_id):
                break
            else:
                print("Subject id is exists, please enter again!")
        subject_name = input("Enter subject name: ")

        return Subject(subject_id, subject_name)

    def addSubject(self, subject):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = """
                    INSERT INTO Subject(`Subject_ID`, `Name`)
                    VALUES (%s, %s)
                """
                try:
                    cur.execute(sql, subject.getSubject())
                    myconn.commit()
                    print("Insert success!, {} record(s) affected".format(cur.rowcount))
                except Error:
                    print("Error: ", Error)
                    myconn.rollback()
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

    def updateSubject(self, subject):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = "UPDATE Subject SET `Name` = '{}' WHERE `Subject_ID` = '{}'".format(subject.getTenmon(), subject.getMamon())
                try:
                    cur.execute(sql)
                    myconn.commit()
                    print("Update success!, {} record(s) affected".format(cur.rowcount))
                except Error:
                    print("Error: ", Error)
                    myconn.rollback()
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)
    
    def deleteSubject(self, subject_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = "DELETE FROM Subject WHERE `Subject_ID` = '{}'".format(subject_id)
                try:
                    cur.execute(sql)
                    myconn.commit()
                    print("Delete success!, {} record(s) affected".format(cur.rowcount))
                except Error:
                    print("Error: ", Error)
                    myconn.rollback()
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)
    
    def getSubjectByID(self, subject_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Subject WHERE `Subject_ID` = '{}'".format(subject_id))
                result = cur.fetchall()
                if result:
                    subject = map(self.__utils.utilMapSubject, result)
                else:
                    subject = ''
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return subject
    
    def getSubjectByName(self, subject_name):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Subject WHERE `Name` = '{}'".format(subject_name))
                result = cur.fetchall()
                if result:
                    subject = list(map(self.__utils.utilMapSubject, result))
                else:
                    subject = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return subject

    #for json    
    # def getSubjectInfo(self):
    #     subject_json = self.__utils.utilReadJson(self.__filepath)
    #     subject_arr = subject_json["subjects"]["subject"]
    #     subject_list = list(map(self.__utils.utilMapSubject,subject_arr))
    #     return subject_list
    #     # for subject in subject_list:
    #     #     print(subject.toString())