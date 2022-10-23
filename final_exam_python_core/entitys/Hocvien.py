class Student:

    def __init__(self, mahv, hoten, ngaysinh, gioitinh, diachi, sdt, email, list_score = []):
        self.__mahv = mahv
        self.__hoten = hoten
        self.__ngaysinh = ngaysinh
        self.__gioitinh = gioitinh
        self.__diachi = diachi
        self.__sdt = sdt
        self.__email = email
        self.__listscore = list_score
    
    def setMahv(self, mahv):
        self.__mahv = mahv
    
    def getMahv(self):
        return self.__mahv
    
    def setHoten(self, hoten):
        self.__hoten = hoten
    
    def getHoten(self):
        return self.__hoten
    
    def setNgaysinh(self, ngaysinh):
        self.__ngaysinh = ngaysinh
    
    def getNgaysinh(self):
        return self.__ngaysinh
     
    def setGioitinh(self, gioitinh):
        self.__gioitinh = gioitinh
    
    def getGioitinh(self):
        return self.__gioitinh
    
    def setDiachi(self, diachi):
        self.__diachi = diachi
    
    def getDiachi(self):
        return self.__diachi

    def setSdt(self, sdt):
        self.__sdt = sdt
    
    def getSdt(self):
        return self.__sdt

    def setEmail(self, email):
        self.__email = email
    
    def getEmail(self):
        return self.__email
    
    def setListScore(self, listscore):
        self.__listscore = listscore
    
    def getListScore(self):
        return self.__listscore
    
    def getStudent(self):
        return (self.__mahv, self.__hoten, self.__ngaysinh, self.__gioitinh, self.__diachi, self.__sdt, self.__email)
    
    def toString(self):
        return "Mahv: {}\nHo ten: {}\nNgay sinh: {}\nGioi tinh: {}\nDia chi: {}\nSodt: {}\nEmail: {}\n".format(self.__mahv, self.__hoten, self.__ngaysinh, self.__gioitinh, self.__diachi, self.__sdt, self.__email)