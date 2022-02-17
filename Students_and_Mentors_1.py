class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def marks_to_lecturer(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.marks:
                lecturer.marks[course] += [mark]
            else:
                lecturer.marks[course] = [mark]
        else:
            return 'Ошибка'

    def count_mid_mark(self):
        for values_list in self.grades.values():
            a = sum(values_list)/len(values_list)
            return a
    def __str__(self):
        self.finished_courses_str = ', '.join(self.finished_courses)
        self.courses_in_progress_str = ', '.join(self.courses_in_progress)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{self.count_mid_mark()}\nКурсы в процессе обучения: {self.courses_in_progress_str}\nЗавершенные курсы: {self.finished_courses_str}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.count_mid_mark() < other.count_mid_mark()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
student_2 = Student('Lili', 'Oldr', 'your_gender')
student_2.courses_in_progress+= ['Java']
student_2.courses_in_progress+= ['Python']
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(). __init__(name, surname)
        self.marks = {}
    def __str__ (self):

        for grades in self.marks.values():
            res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(grades)/len(grades)}'
            return res

    def count_mid_mark(self):
        for values_list in self.marks.values():
            a = sum(values_list)/len(values_list)
            return a
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9.8)
cool_mentor.rate_hw(best_student, 'Python', 9.9)
cool_mentor.rate_hw(student_2, 'Python', 1)
cool_mentor.rate_hw(student_2, 'Python', 8)
cool_mentor.rate_hw(student_2, 'Python', 9)
print(best_student.grades)


mentor_lecturer = Lecturer('Some', 'Buddy')
mentor_lecturer.courses_attached = ['Java']
Student.marks_to_lecturer(student_2, mentor_lecturer, 'Java', 9.9)
Student.marks_to_lecturer(student_2, mentor_lecturer, 'Python', 7)
print(mentor_lecturer.marks)
print(cool_mentor)
print(best_student)
print(mentor_lecturer)
print(student_2.__lt__(best_student))
print(mentor_lecturer.count_mid_mark())
