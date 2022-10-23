class Subject:

    def __init__(self, mamon, tenmon):
        self.__mamon = mamon
        self.__tenmon = tenmon
    
    def setMamon(self, mamon):
        self.__mamon = mamon
    
    def getMamon(self):
        return self.__mamon
    
    def setTenmon(self, tenmon):
        self.__tenmon = tenmon
    
    def getTenmon(self):
        return self.__tenmon
    
    def getSubject(self):
        return (self.__mamon, self.__tenmon)

    def toString(self):
        return "Ma mon: {}\nTen mon: {}\n".format(self.__mamon, self.__tenmon)