class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.middle_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res 

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_atached and course in self.courses_in_progress and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade (self):
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
            return self.middle_grade() < other.middle_grade()

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade()}'
        return res
    
    def middle_grade (self):
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
            return self.middle_grade() < other.middle_grade()


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

   

stud1 = Student('Петр', 'Орлов', 'м')
stud2 = Student('Нина', 'Радова', 'ж')
stud3 = Student('Андрей', 'Кротов', 'м')
lect1 = Lecturer('Николай', 'Иванович')
lect2 = Lecturer('Виктория', 'Романовна')
lect3 = Lecturer('Альберт', 'Семенович')
lect4 = Lecturer('Ирина', 'Евгеньевна')
rev1 = Reviewer('Алиса', 'Максимовна')
rev2 = Reviewer('Михаил', 'Викторович')
rev3 = Reviewer('Роман', 'Петрович')

stud1.courses_in_progress += ['Математика', 'Русский язык', 'Английский язык', 'Аналитика']
stud2.courses_in_progress += ['Английский язык', 'Аналитика']
stud1.finished_courses = ['Литература']
stud2.finished_courses = ['Математика']

lect1.courses_atached += ['Математика', 'Аналитика']
lect2.courses_atached += ['Русский язык']
lect3.courses_atached += ['Английский язык']
lect4.courses_atached += ['Литература']
rev1.courses_atached += ['Русский язык']
rev2.courses_atached += ['Английский язык']
rev3.courses_atached += ['Математика, Аналитика']

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
stud1.rate_lecturer(lect1, 'Аналитика', 6)
stud1.rate_lecturer(lect2, 'Русский язык', 2)
stud1.rate_lecturer(lect2, 'Русский язык', 6)
stud1.rate_lecturer(lect4, 'Литература', 6) #Не поставится, т.к. студент уже завершил этот курс
stud2.rate_lecturer(lect3, 'Английский язык', 10)

#print(f'Средний бал по оценкам: {middle_grade(lect1)}')
print(rev1)
line()
print(stud1)
line()
print(stud2)
line()
print (stud1 < stud2)
line()
print(lect1)
line()
print(lect2)
line()
print(lect3)
line()
print(lect4)
line()
print(lect1 > lect2)
line()
