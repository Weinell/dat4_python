

class Course:

    def __init__(self, name, classroom, teacher, ECTS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade


class DataSheet:

    def __init__(self):
        self.python = Course('Python', '105', 'Thomas', 10)
        self.oop = Course('OOP', '105', 'Kim', 10, 10)
        self.java = Course('Java', '205', 'Tess', 30, 10)
        self.gamedev = Course('GameDev', '105', 'Jesper', 10, 12)
        self.courseList = [self.python, self.oop,self.java, self.gamedev]

    def get_grades_as_list(self):
        courses = self.courseList
        coursesWithGrade = []
        for course in courses:
            if course.grade != None:
                coursesWithGrade.append(course.grade)
        return coursesWithGrade


        

class Student:

    def __init__(self, name, gender, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = DataSheet()
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        sumGrade = 0
        for grade in grades:
            sumGrade = sumGrade + grade

        return sumGrade / len(grades)


def create_students(n):
    for student in len(n):
        student = Student()
    pass


if __name__ == '__main__':

    grades = DataSheet().get_grades_as_list()
    studentGrades = Student('Nikolaj','Male','lol').get_avg_grade()
    print(grades)
    print(studentGrades)

