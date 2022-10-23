from ctypes import util
from entitys.Hocvien import Student
from entitys.Monhoc import Subject
from entitys.Diemthi import Score
from services.HocvienService import StudentService
from services.MonhocService import SubjectService
from services.DiemthiService import ScoreService
from utils.Utils import Utils

def menuStudent():
    studentService = StudentService()
    menu = """
        1. Them hoc vien
        2. Sua thong tin hoc vien
        3. Xoa hoc vien
        4. Tim kiem hoc vien
        5. Back
    """
    while True:
        print(menu)
        while True:
            try:
                your_choose = int(input("Enter your choose(1-5): "))
                if your_choose >= 1 and your_choose <= 5:
                    break
                else:
                    print("Please, enter from 1 to 5!")
            except ValueError:
                print("Please, enter number!")
            
        if your_choose == 1:
            student = studentService.createStudent()
            studentService.addStudent(student)

        if your_choose == 2:
            student_id = input("Enter student id: ")
            student = studentService.getStudentByID(student_id)
            if student:
                while True:
                    student_phone = input("Enter student number phone if want to change: ")
                    try:
                        if int(student_phone) and len(student_phone) == 10:
                            break
                        else:
                            print("Please enter correct phone number!")
                    except ValueError:
                        print("Please enter correct phone number!")
        
                while True:
                    student_email = input("Enter student email if want to change: ")
                    if not studentService.getStudentByEmail(student_email):
                        break
                    else:
                        print("Email is user, enter again!")
                
                student.setSdt(student_phone if student_phone else student.getSdt())
                student.setEmail(student_email if student_email else student.getEmail())
                studentService.updateStudent(student)
            else:
                print("Student id is not exists!")
        
        if your_choose == 3:
            student_id = input("Enter student id: ")
            if studentService.getStudentByID(student_id):
                studentService.deleteStudent(student_id)
            else:
                print("Student id is not exists!")
        
        if your_choose == 4:
            print("""
                4.1 Tim theo ID
                4.2 Tim theo Ten
                4.3 Tim theo email
            """)
            while True:
                try:
                    your_choose_4 = int(input("Enter your choose(1-3): "))
                    if your_choose_4 >= 1 and your_choose_4 <= 3:
                        break
                    else:
                        print("Please, enter from 1 to 3!")
                except ValueError:
                    print("Please, enter number!")
    
            if your_choose_4 == 1:
                student_id = input("Enter student id: ")
                student = studentService.getStudentByID(student_id)
                if student:
                    print(student.toString())
                else:
                    print("Student id is not exists!")
            if your_choose_4 == 2:
                student_name = input("Enter student name: ")
                list_student = studentService.getStudentByName(student_name)
                if list_student:
                    for student in list_student:
                        print(student.toString())
                else:
                    print("Student name is not exists!")
            if your_choose_4 == 3:
                student_email = input("Enter student email: ")
                student = studentService.getStudentByEmail(student_email)
                if student:
                    print(student.toString())
                else:
                    print("Student email is not exists!")
        
        if your_choose == 5:
            break  


def menuSubject():
    subjectService = SubjectService()
    menu = """
        1. Them mon hoc
        2. Sua thong tin mon hoc
        3. Xoa mon hoc
        4. Tim kiem mon hoc
        5. Back
    """
    while True:
        print(menu)
        while True:
            try:
                your_choose = int(input("Enter your choose(1-5): "))
                if your_choose >= 1 and your_choose <= 5:
                    break
                else:
                    print("Please, enter from 1 to 5!")
            except ValueError:
                print("Please, enter number!")
        
        if your_choose == 1:
            subject = subjectService.createSubject()
            subjectService.addSubject(subject)

        if your_choose == 2:
            subject_id = input("Enter subject id: ")
            subject = subjectService.getSubjectByID(subject_id)
            if subject:
                subject_name = input("Enter new name subject: ")
                subject.setTenmon(subject_name)
                subjectService.updateSubject(subject)
            else:
                print("Student id is not exists!")
        
        if your_choose == 3:
            subject_id = input("Enter subject id: ")
            if subjectService.getSubjectByID(subject_id):
                subjectService.deleteSubject(subject_id)
            else:
                print("Student id is not exists!")
        
        if your_choose == 4:
            print("""
                4.1 Tim theo ID
                4.2 Tim theo Ten
            """)
            while True:
                try:
                    your_choose_4 = int(input("Enter your choose(1-2): "))
                    if your_choose_4 >= 1 and your_choose_4 <= 2:
                        break
                    else:
                        print("Please, enter from 1 to 2!")
                except ValueError:
                    print("Please, enter number!")
    
            if your_choose_4 == 1:
                subject_id = input("Enter subject id: ")
                subject = subjectService.getSubjectByID(subject_id)
                if subject:
                    print(subject.toString())
                else:
                    print("Subject id is not exists!")
            if your_choose_4 == 2:
                subject_name = input("Enter subject name: ")
                list_subject = subjectService.getSubjectByName(subject_name)
                if list_subject:
                    for subject in list_subject:
                        print(subject.toString())
                else:
                    print("Subject name is not exists!")
        
        if your_choose == 5:
            break
    

def menuScore():
    scoreService = ScoreService()
    studentService = StudentService()
    subjectService = SubjectService()
    menu = """
        1. Them diem thi
        2. Sua diem thi
        3. Tra cuu diem thi
        4. Thong ke diem
        5. Xuat ban diem to json file
        6. Back
    """
    while True:
        print(menu)
        while True:
            try:
                your_choose = int(input("Enter your choose(1-6): "))
                if your_choose >= 1 and your_choose <= 5:
                    break
                else:
                    print("Please, enter from 1 to 6!")
            except ValueError:
                print("Please, enter number!")
        
        if your_choose == 1:
            score = scoreService.createScore()
            scoreService.addScore(score)

        if your_choose == 2:
            while True:
                student_id = input("Enter student id: ")
                if studentService.getStudentByID(student_id):
                    break
                else:
                    print("Student id is not exists, please enter again!")
        
            while True:
                subject_id = input("Enter subject id: ")
                if not subjectService.getSubjectByID(subject_id):
                    break
                else:
                    print("Subject id is not exists, please enter again!")
            if scoreService.getScoreById(student_id, subject_id):
                while True:
                    try:
                        mid_score = int(input("Enter new mid score: "))
                        break
                    except ValueError:
                        print("Please enter int number!")
        
                while True:
                    try:
                        final_score = int(input("Enter new final score: "))
                        break
                    except ValueError:
                        print("Please enter int number!")
        
                    score = Score(student_id, subject_id, mid_score, final_score)
                    scoreService.updateScore(score)
            else:
                print("Score is not exists, Please enter again!")
        
        if your_choose == 3:
            print("""
                3.1 Tra cuu theo student ID
                3.2 Tra cuu theo subject ID
            """)
            while True:
                try:
                    your_choose_3 = int(input("Enter your choose(1-2): "))
                    if your_choose_3 >= 1 and your_choose_3 <= 2:
                        break
                    else:
                        print("Please, enter from 1 to 2!")
                except ValueError:
                    print("Please, enter number!")
    
            if your_choose_3 == 1:
                student_id = input("Enter student id: ")
                arr_score = scoreService.getScoreByStudent_Id(student_id)
                if arr_score:
                    for score in arr_score:
                        print(score.toString())
                else:
                    print("Student id is not exists, please enter again!")
            if your_choose_3 == 2:
                subject_id = input("Enter subject id: ")
                arr_score = scoreService.getScoreBySubject_Id(subject_id)
                if arr_score:
                    for score in arr_score:
                        print(score.toString())
                else:
                    print("Score id is not exists!")
        
        if your_choose == 4:
            list_score = scoreService.getScoreInfor()
            list_score = sorted(list_score, key=lambda tup: tup[3])
            for score in list_score:
                print(score.toString())

        if your_choose == 5:
            list_student = studentService.getStudentInfo()
            arr_score_student = []
            for student in list_student:
                arr_score = scoreService.getScoreByStudent_Id(subject_id)
                dict_arr_score = [score.toDict() for score in arr_score]
                dict_score = {     
                        "Student_ID": student.getMahv(),
                        "Name": student.getHoten(),
                        "DoB": student.getNgaysinh(),
                        "Sex": student.getGioitinh(),
                        "Address": student.getDiachi(),
                        "Mobile_Number": student.getSdt(),
                        "Email": student.getEmail(),
                        "Score_arr": dict_arr_score
                }
                arr_score_student.append(dict_score)
            util = Utils()
            util.utilWriteJson("data_score.json",arr_score_student)
                
        if your_choose == 6:
            break

def menuMain():
    menu = """
        1. Truy cap quan ly hoc vien
        2. Truy cap quan ly mon hoc
        3. Truy cap quan ly diem thi
        4. Exit
    """
    while True:
        print(menu)
        while True:
            try:
                your_choose_main = int(input("Enter your choose(1-4): "))
                if your_choose_main >= 1 and your_choose_main <= 4:
                    break
                else:
                        print("Please, enter from 1 to 4!")
            except ValueError:
                    print("Please, enter number!")
        if your_choose_main == 1:
            menuStudent()
        if your_choose_main == 2:
            menuSubject()
        if your_choose_main == 3:
            menuScore()
        if your_choose_main == 4:
            print("Program end, bye!!!")
            break


def main():
    menuMain()

main()