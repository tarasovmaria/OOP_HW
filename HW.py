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
lecturer_1.courses_attached += ['Python', 'GIT']

lecturer_2 = Lecturer('Salma', 'Fidger')
lecturer_2.courses_attached += ['Python', 'GIT']

reviewer_1 = Reviewer('Micheal', 'Sandler')
reviewer_1.courses_attached += ['GIT']
reviewer_2 = Reviewer('Serge', 'Jermiy')
reviewer_2.courses_attached += ['GIT']

student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'Python', 8)
student_2.rate_lec(lecturer_1, 'Python', 9)
student_2.rate_lec(lecturer_1, 'Python', 10)

student_1.rate_lec(lecturer_2, 'GIT', 7)
student_1.rate_lec(lecturer_2, 'GIT', 10)
student_2.rate_lec(lecturer_2, 'GIT', 9)
student_2.rate_lec(lecturer_2, 'GIT', 9)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_1, 'GIT', 9)
reviewer_2.rate_hw(student_1, 'GIT', 10)
reviewer_2.rate_hw(student_2, 'GIT', 10)
reviewer_2.rate_hw(student_2, 'GIT', 7)


print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(student_1.__lt__(student_2))
print(lecturer_1 > lecturer_2)

# к сожалению, не смогла разобраться, как написать функции для подсчета средней оценки по курсу среди студентов и преподавателей