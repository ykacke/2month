class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "married" if self.is_married else "not married"
        print(f"Name: {self.full_name}, Age: {self.age}, Marital Status: {marital_status}")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        super().introduce_myself()
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")

    def counter_average(self):
        if not self.marks:
            return 0
        average = sum(self.marks.values()) / len(self.marks)
        return round(average, 2)


class Teacher(Person):
    base_salary = 25000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Experience: {self.experience} years")
        print(f"Base Salary: {Teacher.base_salary}")

    def calculate_salary(self):
        bonus_percentage = 0.05
        if self.experience > 3:
            bonus = (self.experience - 3) * bonus_percentage * Teacher.base_salary
        else:
            bonus = 0
        total_salary = Teacher.base_salary + bonus
        return round(total_salary, 2)


def create_students():
    students = []

    student_data = [
        ('Adina Bekboeva', 17, False, {"Math": 90, "Physics": 85, "Chemistry": 88}),
        ('Medina Nurlanova', 17, False, {'Math': 87, 'Physics': 98, 'Chemistry': 93}),
        ("Kurmova Jesika", 23, True, {"Math": 80, "Physics": 89, "Chemistry": 84}),
    ]

    for data in student_data:
        full_name, age, is_married, marks = data
        student = Student(full_name, age, is_married, marks)
        students.append(student)

    return students


students = create_students()
for student in students:
    student.introduce_myself()
    average_mark = student.counter_average()
    print('Average Mark:', average_mark)
    print('---')
