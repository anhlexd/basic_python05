print("Nhap 3 diem kiem tra: ")
a,b,c = map(int,input().split())
AVR = (a + b + c)/3
print("Diem trung binh = {}".format(AVR))
if AVR > 95:
    print("Congratulate the user")
