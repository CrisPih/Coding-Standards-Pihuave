class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, g):
        self.gradez.append(g)

    def calc_average(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez) if self.gradez else 0
        return avg

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
