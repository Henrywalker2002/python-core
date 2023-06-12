from functools import reduce
from zipfile import ZipFile
import logging
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import PyPDF2
from PIL import Image
import unittest

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

def sendmail() : 
    fromaddr = "davisdavis448@gmail.com"
    toaddr = "hung.nguyen0304@hcmut.edu.vn"
    msg = MIMEMultipart()    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "TIÊU ĐỀ CỦA MAIL (SUBJECT)"
    body = "NỘI DUNG MAIL"
    try:
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "aqkjshphizdcdkcq")
        #attach file 
        filename = "first.pdf"
        with open(filename, 'rb') as f:
            attachfile = MIMEBase("application", "octet-stream")
            attachfile.set_payload(f.read())
        encoders.encode_base64(attachfile)
        attachfile.add_header("Content-Disposition", f"attachment; filename = {filename}")
        msg.attach(attachfile)
        
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except Exception as e:
        print(str(e))
        
    
def openPDF() : 
    # Open the PDF file
    with open('report.pdf', 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        infor = pdf_reader.metadata
        print(num_pages, infor)
        first = pdf_reader.pages[0]
        
        writer = PyPDF2.PdfWriter()
        writer.add_page(first)
        writer.write("first.pdf")
        writer.close()
        # Iterate over each page and extract text
        # for page in pdf_reader.pages:
        #     text = page.extract_text()
        #     print(text)

def openExcel():
    df = pd.read_excel("file_example_XLS_50.xls", "Sheet1", index_col= 'Id')
    df = df.drop(columns=[0])

    new_df = df[df.Country == "France"]

    new_df.to_csv("france.csv")
    df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
    df = df.drop(columns= ['First Name', 'Last Name'])
    print(df)

class decorate: 
    pass
        
    # temp = hello_decorator(display)
    # temp()
    # display2()

def openimg():
    img = Image.open('cut.jpg')

    img = img.rotate(180)
    w, h = img.size
    img = img.resize((int(w/2), int(h/2)))

    img.save('img2.jpg')

class arg:
    # args is tuple 
    def func(a, b, *args):
        print(a, b)
        for x in args: 
            print(x)

    # kargs is dict    
    def func2(**kargs):
        for (key, value) in kargs.items():
            print(key, value)
    func(123, 456, 454)
    func2(c = 4, a = 2)
    
class forTest(unittest.TestCase):
    def test_1(self):
        inp = "TEST".lower()
        out = 'test'
        self.assertEqual(inp, out)
        
    def test_2(self):
        inp = "TEST".lower()
        self.assertTrue(inp.isupper(), "not upper")
        