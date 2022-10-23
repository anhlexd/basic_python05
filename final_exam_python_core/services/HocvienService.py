from entitys.Hocvien import Student
from utils.Utils import Utils
from mysql.connector import Error

class StudentService:

    def __init__(self):
        self.__utils = Utils()
        self.__filepath = "final_exam_python_core/utils/students.json"

    # sql
    def getStudentInfo(self):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute(
                    "SELECT * FROM Student")
                result = cur.fetchall()
                if result:
                    student_list = list(map(self.__utils.utilMapStudent, result))
                else:
                    student_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return student_list
    
    def createStudent(self):
        while True:
            student_id = input("Enter student id: ")
            if not self.getStudentByID(student_id):
                break
            else:
                print("Student id is exists, please enter again!")
                
        student_name = input("Enter student name: ")
        student_dob = input("Enter birthday of student(yyyy-MM-dd): ")
        sex_dict = {
            'f' :'Female',
            'm' :'Male',
        }
        while True:
            student_sex_input = input("Enter student sex(f/m): ").lower()
            if student_sex_input == 'f' or student_sex_input == 'm':
                student_sex = sex_dict.get(student_sex_input)
                break
            else:
                print("Pleas enter f/m!")

        student_add = input("Enter student address: ")
        while True:
            student_phone = input("Enter student number phone: ")
            try:
                if int(student_phone) and len(student_phone) == 10:
                    break
                else:
                    print("Please enter correct phone number!")
            except ValueError:
                print("Please enter correct phone number!")
        
        while True:
            student_email = input("Enter student email: ")
            if not self.getStudentByEmail(student_email):
                break
            else:
                print("Email is user, enter again!")
        
        return Student(student_id, student_name, student_dob, student_sex, student_add, student_email)


    def addStudent(self, student):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = """
                    INSERT INTO Student(`Student_ID`, `Name`, DoB, Sex, Address, MobileNumber, Email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                try:
                    cur.execute(sql, student.getStudent())
                    myconn.commit()
                    print("Insert success!, {} record(s) affected".format(cur.rowcount))
                except Error:
                    print("Error: ", Error)
                    myconn.rollback()
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)
    
    def updateStudent(self,student):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = "UPDATE STUDENT SET MobileNumber = '{}', Email = '{}' WHERE `Student_ID` = '{}'".format(student.getSdt(), student.getEmail(), student.getMahv())
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
    
    def deleteStudent(self, student_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = "DELETE FROM STUDENT WHERE `Student_ID` = '{}'".format(student_id)
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
    
    def getStudentByID(self, student_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Student WHERE `Student_ID` = '{}'".format(student_id))
                result = cur.fetchall()
                if result:
                    student = map(self.__utils.utilMapStudent, result)
                else:
                    student = ''
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return student
    
    def getStudentByName(self, student_name):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Student WHERE `Name` = '{}'".format(student_name))
                result = cur.fetchall()
                if result:
                    student_list = list(map(self.__utils.utilMapStudent, result))
                else:
                    student_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return student_list
    
    def getStudentByEmail(self, student_email):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Student WHERE `Email` = '{}'".format(student_email))
                result = cur.fetchall()
                if result:
                    student_list = map(self.__utils.utilMapStudent, result)
                else:
                    student_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return student_list



    #for json
    # def getStudentInfo(self):
    #     student_json = self.__utils.utilReadJson(self.__filepath)
    #     student_arr = student_json["students"]["student"]
    #     student_list = list(map(self.__utils.utilMapStudent, student_arr))
    #     # for student in student_list:
    #     #     print(student.toString())
    #     return student_list
