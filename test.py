
# Reviewed under SE2 coding standards guidelines
"""Student grade management system."""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id, name):
        """Initializes the student information."""
        if not str(student_id).strip() or not isinstance(name, str) or not name.strip():
            raise ValueError("El ID y el nombre no pueden estar vacíos.")

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Adds a valid grade."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print("Error: la nota debe ser un número.")
            return
        if not 0 <= grade <= 100:
            print("Error: la nota debe estar entre 0 y 100.")
            return
        self.grades.append(grade)

    def calculate_average(self):
        """Calculates the average grade."""
        total = 0
        for grade in self.grades:
            total += grade
        average = total / len(self.grades) if self.grades else 0
        return average

    def check_honor(self):
        """Checks if the student qualifies for the honor roll."""
        self.honor = self.calculate_average() >= 90
        return self.honor

    def letter_grade(self):
        """Returns the letter grade based on the average."""
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def remove_grade(self, index=None, value=None):
        """Removes a grade by index or value."""
        if (index is None) == (value is None):
            print("Error: indique un índice o un valor.")
            return

        if index is not None:
            if isinstance(index, bool) or not isinstance(index, int):
                print("Error: el índice debe ser un entero.")
                return
            if index < 0 or index >= len(self.grades):
                print("Error: índice fuera de rango.")
                return
            del self.grades[index]
        else:
            if value not in self.grades:
                print("Error: la nota no existe.")
                return
            self.grades.remove(value)

    def pass_status(self):
        """Checks whether the student passed or failed."""
        self.is_passed = self.calculate_average() >= 60
        if self.is_passed:
            return "Passed"
        return "Failed"

    def report(self):
        """Displays the student's grade report."""
        print("\n--- Student Report ---")
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Number of Grades:", len(self.grades))
        print(f"Average Grade: {self.calculate_average():.2f}")
        print("Letter Grade:", self.letter_grade())
        print("Pass/Fail:", self.pass_status())
        print("Honor Roll:", self.check_honor())


def main():
    """Runs examples of the student grading system."""
    try:
        student = Student("001", "Ana")
        student.add_grade(95)
        student.add_grade(90)
        student.add_grade(100)
        student.report()

        student.remove_grade(value=90)
        student.report()

        student.remove_grade(index=0)
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
