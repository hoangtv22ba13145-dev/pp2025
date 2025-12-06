students = []
courses = []
marks = {}

def inputnumberstudents():
    n = int(input("Number of students: "))
    for _ in range(n):
        id = input("ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        students.append({"id": id, "name": name, "dob": dob})

def inputnumbercourses():
    n = int(input("Number of courses: "))
    for _ in range(n):
        id = input("Course ID: ")
        name = input("Course name: ")
        courses.append({"id": id, "name": name})

def inputmarks():
    courseid = input("Course ID to input marks: ")
    marks[courseid] = {}
    for s in students:
        m = float(input(f"Mark for {s['name']}: "))
        marks[courseid][s["id"]] = m

def liststudents():
    print(" Students ")
    for s in students:
        print(s["id"], s["name"], s["dob"])

def listcourses():
    print(" Courses ")
    for c in courses:
        print(c["id"], c["name"])

def showmarks():
    courseid = input("Course ID: ")
    if courseid in marks:
        for s in students:
            sid = s["id"]
            if sid in marks[courseid]:
                print(s["name"], marks[courseid][sid])
    else:
        print("No marks for this course")

def menu():
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks for course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks of course")
        print("7. Quit")
        c = input("Choose: ")

        if c == "1": inputnumberstudents()
        elif c == "2": inputnumbercourses()
        elif c == "3": inputmarks()
        elif c == "4": liststudents()
        elif c == "5": listcourses()
        elif c == "6": showmarks()
        elif c == "7": break

menu()

