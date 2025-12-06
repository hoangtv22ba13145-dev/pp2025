class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob

    def show(self):
        print(self.sid, self.name, self.dob)


class Course:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

    def show(self):
        print(self.cid, self.name)


class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def inputStudents(self):
        for i in range(int(input("Number of students: "))):
            self.students.append(Student(input("ID: "), input("Name: "), input("DOB: ")))

    def inputCourses(self):
        for i in range(int(input("Number of courses: "))):
            self.courses.append(Course(input("Course ID: "), input("Course name: ")))

    def inputMarks(self):
        cid = input("Course ID: ")
        self.marks[cid] = {}
        for s in self.students:
            self.marks[cid][s.sid] = float(input("Mark for " + s.name + ": "))

    def listStudents(self):
        for s in self.students: s.show()

    def listCourses(self):
        for c in self.courses: c.show()

    def showMarks(self):
        cid = input("Course ID: ")
        if cid not in self.marks:
            print("No marks"); return
        for s in self.students:
            if s.sid in self.marks[cid]:
                print(s.name, self.marks[cid][s.sid])


def menu():
    ms = MarkSheet()
    while True:
        print("1.Input students  2.Input courses  3.Input marks")
        print("4.List students  5.List courses  6.Show marks  7.Quit")
        c = input("Choose: ")
        if c=="1": ms.inputStudents()
        elif c=="2": ms.inputCourses()
        elif c=="3": ms.inputMarks()
        elif c=="4": ms.listStudents()
        elif c=="5": ms.listCourses()
        elif c=="6": ms.showMarks()
        elif c=="7": break

menu()
