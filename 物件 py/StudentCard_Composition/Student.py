from Date import Date
class Student(Date):
    def __init__(self, name, month, day, year, score):
        super().__init__(month,day,year)
        self.__date = Date(month,day,year)
        self.__name = name
        #self.__date = date
        self.__score = score

    def setName(self, name):
        self.__name = name

    def setDate(self, month, day, year):
        self.__date = Date(month,day,year)

    def setScore(self, score):
        self.__score = score

    def getName(self):
        return self.__name

    def getDate(self):
        return self.__date.toString()

    def getScore(self):
        return self.__score

    def toString(self):
        print(self.__name, self.__date.toString(), self.__score )