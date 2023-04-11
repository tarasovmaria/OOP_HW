class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.current_courses = []
        self.grades = {}
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.current_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'
    def avr_hw_grade(self):
        average = sum(map(sum, self.grades.values()))/sum([1 if isinstance(self.grades[a], int)
            else len(self.grades[a])
            for a in self.grades])
        return average
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.avr_hw_grade()} \nКурсы в процессе изучения: {", ".join(map(str, self.current_courses))}\nЗавершенные курсы: {", ".join(map(str, self.finished_courses))}'
        return res
    def __lt__(self,other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.avr_hw_grade() < other.avr_hw_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def avr_grades(self):
        average = sum(map(sum, self.grades.values()))/sum([1 if isinstance(self.grades[a], int)
            else len(self.grades[a])
            for a in self.grades])
        return average
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.avr_grades()}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.avr_grades() < other.avr_grades()
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.current_courses and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

student_1 = Student('Pet', 'Joe', 'male')
student_1.finished_courses.append('Введение в программирование')
student_1.current_courses.append('Python')
student_1.current_courses.append('GIT')

student_2 = Student('Fionna', 'Saller', 'female')
student_2.finished_courses.append('Введение в программирование')
student_2.finished_courses.append('Figma')
student_2.current_courses.append('Python')
student_2.current_courses.append('GIT')

lecturer_1 = Lecturer('John', 'Lybovski')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached.append('GIT')

lecturer_2 = Lecturer('Salma', 'Fidger')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached.append('GIT')

reviewer_1 = Reviewer('Micheal', 'Sandler')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Serge', 'Jermiy')
reviewer_2.courses_attached += ['GIT']

student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'Python', 8)
student_2.rate_lec(lecturer_1, 'Python', 9)
student_2.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'GIT', 7)
student_1.rate_lec(lecturer_1, 'GIT', 8)
student_2.rate_lec(lecturer_1, 'GIT', 10)
student_2.rate_lec(lecturer_1, 'GIT', 8)

student_1.rate_lec(lecturer_2, 'GIT', 7)
student_1.rate_lec(lecturer_2, 'GIT', 10)
student_2.rate_lec(lecturer_2, 'GIT', 9)
student_2.rate_lec(lecturer_2, 'GIT', 9)
student_1.rate_lec(lecturer_2, 'Python', 10)
student_1.rate_lec(lecturer_2, 'Python', 7)
student_2.rate_lec(lecturer_2, 'Python', 7)
student_2.rate_lec(lecturer_2, 'Python', 5)

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_1, 'GIT', 9)
reviewer_2.rate_hw(student_1, 'GIT', 10)
reviewer_2.rate_hw(student_1, 'GIT', 8)
reviewer_2.rate_hw(student_1, 'GIT', 10)
reviewer_2.rate_hw(student_2, 'GIT', 10)
reviewer_2.rate_hw(student_2, 'GIT', 8)
reviewer_2.rate_hw(student_2, 'GIT', 10)
reviewer_2.rate_hw(student_2, 'GIT', 7)


print(f'Студенты:\n{student_1}\n{student_2}')
print(f'Лекторы:\n{lecturer_1}\n{lecturer_2}')
print(f'Проверяющие:\n{reviewer_1}\n{reviewer_2}')

print(student_1.__lt__(student_2))
print(lecturer_1 > lecturer_2)

student_list = [student_1, student_2]

def av_grade_st(list, course):
    sum_grade = 0
    length = 0
    for stud in list:
        if course in stud.grades.keys():
            sum_grade += sum(stud.grades[course])
            length += len(stud.grades[course])
        else:
            return 'No such course in progress'
    return f'Средний бал за курс {course}: {round(sum_grade / length, 2)}'

print(av_grade_st(student_list, 'Python'))
print(av_grade_st(student_list, 'GIT'))

lecturer_list = [lecturer_1, lecturer_2]
def av_grade_lec(list, course):
    sum_grade = 0
    length_grade = 0
    for lec in list:
        if course in lec.grades.keys():
            sum_grade += sum(lec.grades[course])
            length_grade += len(lec.grades[course])
        else:
            return 'Such course was not taught'
    return f'Средний бал за лекцию {course}: {round(sum_grade / length_grade, 2)}'

print(av_grade_lec(lecturer_list, 'Python'))
print(av_grade_lec(lecturer_list, 'GIT'))
