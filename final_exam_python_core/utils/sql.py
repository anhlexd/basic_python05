import json
from entitys.Hocvien import Student
from entitys.Monhoc import Subject
from entitys.Diemthi import Score
from services.HocvienService import StudentService
from services.MonhocService import SubjectService
from services.DiemthiService import ScoreService
from Utils import Utils




util = Utils()
util.utilCreateDatabase("qlStudent")
util.utilCreateTable()

stu =StudentService()
stuli = stu.getStudentInfo()
vals = [student.getStudent() for student in stuli]
sql = """
                    INSERT INTO Student(`Student_ID`, `Name`, DoB, Sex, Address, MobileNumber, Email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
util.utilInsertMutipleRecord(sql, vals)
sub = SubjectService()
subli = sub.getSubjectInfo()
vals = [subject.getSubject() for subject in subli]
sql = """
                    INSERT INTO Subject(`Subject_ID`, `Name`)
                    VALUES (%s, %s)
                """
util.utilInsertMutipleRecord(sql, vals)

sco = ScoreService()
scoli = sco.getScoreInfor()
vals = [score.getScore() for score in scoli]
sql = """
                    INSERT INTO `Score`(`Student_ID`,`Subject_ID` , Midel_Score, Final_Score, Xeploai)
                    VALUES (%s, %s, %s, %s, %s)
                """

util.utilInsertMutipleRecord(sql, vals)