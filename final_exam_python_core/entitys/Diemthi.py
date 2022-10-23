class Score:

    def __init__(self, mahv, mamon, diemqt, diemkt):
        self.__mahv = mahv
        self.__mamon = mamon
        self.__diemqt = diemqt
        self.__diemkt = diemkt
    
    def setMahv(self, mahv):
        self.__mahv  = mahv
    
    def getMahv(self):
        return self.__mahv

    def setMamon(self, mamon):
        self.__mamon  = mamon
    
    def getMamon(self):
        return self.__mamon
    
    def setDiemqt(self, diemqt):
        self.__diemqt  = diemqt
    
    def getDiemqt(self):
        return self.__diemqt

    def setDiemkt(self, diemkt):
        self.__diemkt  = diemkt
    
    def getDiemkt(self):
        return self.__diemkt
    
    def xepLoai(self):
        diemtk = (self.__diemqt + self.__diemkt * 2)/3
        if diemtk >= 9:
            xl ="A"
        elif diemtk >=7:
            xl = "B"
        elif diemtk >= 5:
            xl = "C"
        else:
            xl = "D"
        
        return xl
    
    def getScore(self):
        return (self.__mahv, self.__mamon, self.__diemkt, self.__diemkt, self.xepLoai())
    
    def toDict(self):
        score_dict = {
            "Subject_ID": self.__mamon,
            "Midel_Score":self.__diemqt,
            "Final_Score": self.__diemkt,
        }
        return score_dict

    def toString(self):
        return "Mahv: {}\nMa mon: {}\nDiem qua trinh: {}\nDiem ket thuc: {}\nXep loai: {}\n".format(self.__mahv, self.__mamon, self.__diemqt, self.__diemkt, self.xepLoai())