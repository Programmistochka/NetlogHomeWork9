class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res 

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_atached and course in self.courses_in_progress and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade (self):
        amount_grade = 0
        grades = 0
        for course in self.grades.keys():
            grades += sum(self.grades[course])
            amount_grade += len(self.grades[course])
        if amount_grade>0:
            res = round(grades/amount_grade, 2)
        else:
            res = 0
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Сравнение не возможно, {other} не относится к студентам')
        else:
            return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_atached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_atached = []
        self.grades = {}
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res
    
    def average_grade (self):
        amount_grade = 0
        grades = 0
        for course in self.grades.keys():
            grades += sum(self.grades[course])
            amount_grade += len(self.grades[course])
        if amount_grade>0:
            res = round(grades/amount_grade, 2)
        else:
            res = 0
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Сравнение не возможно, {other} не относится к лекторам')
        else:
            return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_atached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_atached and course in student.courses_in_progress and grade in range(1, 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def line(n=10):
    print()
    print('---'*n)

def average_studgrade_by_course(students, course):
    grades_by_course = 0
    amount_grade_by_course = 0
    for stud in students:
        for course_grades in stud.grades.values():
            if course in stud.courses_in_progress:
                grades_by_course += sum(course_grades)
                amount_grade_by_course += len(course_grades)
                break
    res = grades_by_course / amount_grade_by_course
    return res

def average_lectgrade_by_course(lectures, course):
    grades_by_course = 0
    amount_grade_by_course = 0
    for lect in lectures:
        for course_grades in lect.grades.values():
            if course in lect.courses_atached:
                grades_by_course += sum(course_grades)
                amount_grade_by_course += len(course_grades)
                break
    res = grades_by_course / amount_grade_by_course
    return res

stud1 = Student('Петр', 'Орлов', 'м')
stud2 = Student('Нина', 'Радова', 'ж')

lect1 = Lecturer('Николай', 'Иванович')
lect2 = Lecturer('Виктория', 'Романовна')
lect3 = Lecturer('Мария', 'Степановна')

rev1 = Reviewer('Алиса', 'Максимовна')
rev2 = Reviewer('Михаил', 'Викторович')

stud1.courses_in_progress += ['Математика', 'Русский язык']
stud2.courses_in_progress += ['Английский язык', 'Аналитика']
stud1.finished_courses = ['Литература']
stud2.finished_courses = ['Математика']

lect1.courses_atached += ['Математика', 'Аналитика']
lect2.courses_atached += ['Русский язык']
lect3.courses_atached += ['Русский язык']

rev1.courses_atached += ['Русский язык']
rev2.courses_atached += ['Английский язык']

rev1.rate_hw(stud1,'Русский язык',3)
rev1.rate_hw(stud1,'Русский язык',4)
rev1.rate_hw(stud2,'Русский язык',10)
rev1.rate_hw(stud2,'Русский язык',8)
rev2.rate_hw(stud1,'Английский язык',6)
rev2.rate_hw(stud1,'Английский язык',8)
rev2.rate_hw(stud2,'Английский язык',3)
rev2.rate_hw(stud2,'Английский язык',9)

stud1.rate_lecturer(lect1, 'Математика', 2)
stud1.rate_lecturer(lect1, 'Математика', 6)
stud1.rate_lecturer(lect1, 'Аналитика', 6) #не должна попасть в расчет Аналитики нет в текущих курсах
stud1.rate_lecturer(lect2, 'Русский язык', 8)
stud1.rate_lecturer(lect2, 'Русский язык', 6)
stud1.rate_lecturer(lect3, 'Русский язык', 9)
stud1.rate_lecturer(lect3, 'Русский язык', 9)

print(rev1)
line()
print(stud1)
line()
print(stud2)
line()
print (f'Сравнение студентов: {stud1.name} {stud1.surname} и {stud2.name} {stud2.surname}')
print ('Результат: ', stud1 < stud2)
line()
print(lect1)
line()
print(lect2)
line()
print(lect3)
line()
print (f'Сравнение лекторов: {lect1.name} {lect1.surname} и {lect2.name} {lect2.surname}')
print ('Результат: ', lect1 < lect2)

line()

course = 'Математика'

students = [stud1, stud2]
print(f'Средний бал за дз студентов по курсу "{course}": {average_studgrade_by_course(students, course)}')
line()
lectures = [lect1, lect2, lect3]
print(f'Средний бал за лекции лекторов по курсу "{course}": {average_lectgrade_by_course(lectures, course)}')