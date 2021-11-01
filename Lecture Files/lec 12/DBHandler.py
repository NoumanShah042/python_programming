import pymysql
from Student import Student

class DBHandler:
    def __init__(self , dbipaddress,dbuser,dbpwd,dbname):
        self.dbipaddress=dbipaddress
        self.dbuser=dbuser
        self.dbpwd=dbpwd
        self.dbname=dbname

    def insertRecord(self , student):
        db = None
        cursor = None
        insert= False
        try:
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "insert into students(rollno,name,semmester,cgpa) values(%s,%s,%s,%s)"
            args = (student.rollno, student.name, student.semmester, student.cgpa)
            cursor.execute(query, args)
            db.commit()
            insert=True
        except Exception as e:
            print("Exception occured")
            print(e)
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return insert

    def fetchAllStudents(self):
        # create db connection
        db = None
        cursor = None
        studentsList = []
        try:
            # create db connection
            # db = pymysql.connect("localhost","root","m@vra123","test")
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            # Create cursor object
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "Select id,name,rollno,semmester,cgpa  from students"
            # args=(1)
            cursor.execute(query)
            results = cursor.fetchall()
            print("return type", type(results))
            # print(results)

            for r in results:
                studentsList.append(Student(r["name"],r["rollno"],r["semmester"],r["cgpa"]))
                #print("id", r["id"], "rollno", r["rollno"], "semmester", r["semmester"])

        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return studentsList


db = DBHandler("localhost","root" , "", "db_flask")

std = Student('Humza','bcsf18m005', 5 , 3.8)
db.insertRecord(std)

# res= db.fetchAllStudents()
# for r in res:
#     print(r.name ,r.rollno,  r.semmester, r.cgpa )