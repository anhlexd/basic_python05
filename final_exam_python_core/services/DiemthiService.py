from entitys.Diemthi import Score
from HocvienService import StudentService
from MonhocService import SubjectService
from utils.Utils import Utils
from mysql.connector import Error

class ScoreService:

    def __init__(self):
        self.__utils = Utils()
        self.__stuService = StudentService()
        self.__subService = SubjectService()
        self.__filepath = "final_exam_python_core/utils/scores.json"
    
    def getScoreInfor(self):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute(
                    "SELECT * FROM Score")
                result = cur.fetchall()
                if result:
                    score_list = list(map(self.__utils.utilMapScore, result))
                else:
                    score_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return score_list

    def createScore(self):
        while True:
            while True:
                student_id = input("Enter student id: ")
                if self.__stuService.getStudentByID(student_id):
                    break
                else:
                    print("Student id is not exists, please enter again!")
        
            while True:
                subject_id = input("Enter subject id: ")
                if not self.__subService.getSubjectByID(subject_id):
                    break
                else:
                    print("Subject id is not exists, please enter again!")
            if not self.getScoreById(student_id, subject_id):
                break
            else:
                print("Score is exists, Please enter again!")
        
        while True:
            try:
                mid_score = int(input("Enter mid score: "))
                break
            except ValueError:
                print("Please enter int number!")
        
        while True:
            try:
                final_score = int(input("Enter final score: "))
                break
            except ValueError:
                print("Please enter int number!")
        
        return Score(student_id, subject_id, mid_score, final_score)
        

    def addScore(self, score):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = """
                    INSERT INTO `Score`(`Student_ID`,`Subject_ID` , Midel_Score, Final_Score, Xeploai)
                    VALUES (%s, %s, %s, %s, %s)
                """
                try:
                    cur.execute(sql, score.getScore())
                    myconn.commit()
                    print("Insert success!, {} record(s) affected".format(cur.rowcount))
                except Error:
                    print("Error: ", Error)
                    myconn.rollback()
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)
    
    def updateScore(self, score):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = "UPDATE Score SET Midel_Score = {}, Final_Score = {}, Xeploai = '{}' WHERE `Student_ID = '{}' AND `Subject_ID` = '{}'".format(score.getDiemqt(), score.getDiemkt(), score.xepLoai(), score.getMahv(), score.getMamon())
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

    def deleteScore(self, score):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                sql = "DELETE FROM Score WHERE `Student_ID = '{}' AND `Subject_ID` = '{}'".format(score.getMahv(), score.getMamon())
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
    
    def getScoreById(self, student_id, subject_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Score WHERE `Student_ID = '{}' AND `Subject_ID` = '{}'".format(student_id, subject_id))
                result = cur.fetchall()
                if result:
                    score_list = map(self.__utils.utilMapScore, result)
                else:
                    score_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return score_list
    
    def getScoreByStudent_Id(self, student_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Score WHERE `Student_ID = '{}'".format(student_id))
                result = cur.fetchall()
                if result:
                    score_list = list(map(self.__utils.utilMapScore, result))
                else:
                    score_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return score_list

    def getScoreBySubject_Id(self, subject_id):
        try:
            myconn = self.__utils.utilConnectsql()
            if myconn.is_connected():
                cur = myconn.cursor()
                cur.execute("SELECT * FROM Score WHERE `Subject_ID = '{}'".format(subject_id))
                result = cur.fetchall()
                if result:
                    score_list = list(map(self.__utils.utilMapScore, result))
                else:
                    score_list = []
            self.__utils.utilClosesql()
        except Error:
            print("Error: ", Error)

        return score_list


    #for json
    # def getScoreInfor(self):
    #     score_json = self.__utils.utilReadJson(self.__filepath)
    #     score_arr = score_json["subjects"]["subject"]
    #     score_list = list(map(self.__utils.utilMapScore, score_arr))
    #     return score_list
    #     # for score in score_list:
    #     #     print(score.toString())