class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = False

    def add_grades(self, grade):
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print("Error: la nota debe ser un número.")
            return
        if not 0 <= grade <= 100:
            print("Error: la nota debe estar entre 0 y 100.")
            return
        self.gradez.append(grade)

    def calc_average(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez) if self.gradez else 0
        return avg

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = True

    def letter_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        else:
            return "F"

    
    def delete_grade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Number of Grades:", len(self.grades))
        print(f"Average Grade: {self.calculate_average():.2f}")
        print("Letter Grade:", self.letter_grade())
        print("Pass/Fail:", self.pass_status())
        print("Honor Roll:", self.check_honor())


    def pass_status(self):
        if self.calculate_average() >= 60:
            return "Passed"
        return "Failed"

def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()



def main():
    """Ejecuta ejemplos del sistema."""
    try:
        student = Student("001", "Ana")
        student.add_grade(95)
        student.add_grade(90)
        student.add_grade(100)
        student.report()

        student.remove_grade(value=90)
        student.report()

        student.add_grade("Fifty")
        student.add_grade(150)
        student.remove_grade(index=10)

        second_student = Student("002", "Luis")
        second_student.add_grade(50)
        second_student.add_grade(70)
        second_student.report()

        Student("", "")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
