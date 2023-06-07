from functools import reduce
from zipfile import ZipFile
import logging

logging.basicConfig(level=logging.DEBUG)

def upperFirstChar(s : str):
    #string split
    arr = s.split(' ')
    # string join, string slice, string uppercase, string concatenate
    return ' '.join((reduce(lambda prev, curr : prev + [(curr[0].upper() + curr[1: ])], arr, [])))

class People:
    def __init__(self, name: str, id: int, sex : bool):
        self.name = upperFirstChar(name)
        self.id = id 
        self.sex = sex # true is male 
    
    def __str__(self):
        return 'name: ' + self.name + ' id: ' + str(self.id) + ' sex: ' + ('male' if self.sex else 'female')

#Inheritance
class Student(People):
    def __init__(self, name: str, id: int, sex: bool, math: float, physical: float, chemistry: float):
        super().__init__(name, id, sex)
        self.math = math 
        self.physical = physical
        self.chemistry = chemistry
    
    def calcAverage(self):
        ave = self.math + self.physical + self.chemistry
        ave /= 3
        return round(ave, 2)
    
    def __str__(self):
        ave = self.calcAverage()
        return 'name: ' + self.name + ' id: ' + str(self.id) + ' sex: ' + ('male' if self.sex else 'female') + ' average ' + str(ave)

class ManagementStu:
    def __init__(self):
        self.studentLst = []
        
    def __init__(self, studentLst):
        self.studentLst = studentLst
    
    def __len__(self):
        return len(self.studentLst)
    
    def __str__(self):
        return reduce(lambda prev, curr : prev + '\n' + str(curr) , self.studentLst, "")
    
    def removeLast(self):
        self.studentLst.pop()      
    
    def addStudent(self, stu):
        self.studentLst.append(stu)
    
    def removeStudentById(self, id):
        for x in self.studentLst:
            if x.id == id: 
                self.studentLst.remove(x)
                return
    
    def zipfile(self):
        with ZipFile("file.zip", "w") as f:
            f.write("student.txt")
            
    def extractZip(self):
        with ZipFile("file.zip", 'r') as f:
            f.extractall()
    
    def saveToFile(self):
        f = open("student.txt", 'a')
        # name: str, id: int, sex: bool, math: float, physical: float, chemistry: float
        for x in self.studentLst:
            logging.info(x)
            arr = (x.name, x.id, x.sex, x.math, x.physical, x.chemistry)
            arr = list(map(lambda x : str(x), arr))
            f.write('.'.join(arr) + '\n')
        f.close()
    
    def loadFromFile(self, filename):
        f = open(filename, 'r')  
        for x in f:
            temp = x.split('.')
            stu = Student(temp[0], int(temp[1]), bool(temp[2]), float(temp[3]), float(temp[4]), float(temp[5]))
            self.addStudent(stu)
        f.close()

class Ex(Exception):
    def __init__(self, id):
        super().__init__("duplicate key: " + str(id))

class ManagementStu2: 
    def __init__(self):
        self.studentDic = {}     
    
    def __init__(self, studentLst):
        self.studentDic = {}
        try :
            for x in studentLst:
                if x.id in self.studentDic.keys():
                    raise Ex(x.id)
                self.studentDic[x.id] = x 
        except Ex as e:
            logging.exception(e ,exc_info=True)

    def __str__(self):  
        return reduce(lambda prev, curr: prev + str(curr), self.studentDic.values(), '')
    
    def addStudent(self, stu : Student):
        try : 
            if stu.id in self.studentDic.keys():
                raise Ex(stu.id)
            self.studentDic[stu.id] = stu
        except Ex as e :
            logging.exception(e, exc_info=True)

    def removeStudent(self, id: int):
        self.studentDic.pop(id)
    
def testTuple():
    tup = ('a', 'b' , 'c')
    tup2 = ('d', )
    #tuple concatenate
    tup += tup2
    print(tup)
    # update tuple 
    temp = list(tup)
    temp.append('e')
    tup = tuple(temp)
    print(tup)
    try: 
        tup[1] = 2 
    except Exception as e:
        print(e)
        
def testSet():
    s = {'a', 'b', 'c', 'a'}
    #ignore dup item
    s.add('a')
    print(s)

# Polymorphism
p = People("Nguyen Ngoc Hung", 456, True)
st = Student("Nguyen Ngoc Hung", 456, False, 6.5, 6, 10)
st2 = Student("Nguyen Ngoc Hung", 456, False, 6.5, 6, 9)
st3 = Student("name", 123, True, 5, 6, 7)
# print(st, p)

lst = []
lst.append(st)
lst.append(st2)
manage = ManagementStu2(lst)
manage.addStudent(st3)
manage.removeStudent(456)
# manage.saveToFile()
# manage.studentLst = []
# manage.loadFromFile("student.txt")
# manage.extractZip()
print(manage)

# print(len(manage))
