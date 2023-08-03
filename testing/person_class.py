class Person:
    def __init__(self, name, surname, age, country, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city

    def introduce_yourself(self):
        print(
            f"Hello,my name is {self.name} {self.surname} and I'm {self.age} years old. My hometown is in {self.country}. It's called {self.city}.")

    def age_difference(self, input_age):
        if input_age < self.age:
            return f"I'm {self.age-input_age} years older than you."
        elif input_age > self.age:
            return f"You're {input_age-self.age} years older than me."
        else:
            return f"We're the same age."


class Student(Person):
    def __init__(self, name, surname, age, country, city, student_ID, university, faculty):
        super().__init__(name, surname, age, country, city)
        self.student_ID = student_ID
        self.university = university
        self.faculty = faculty

    def introduce_yourself(self):
        print(
            f"Hello, my name is {self.name} {self.surname} and I'm {self.age} years old .I go to university called {self.university}.My faculty named {self.faculty}.")

    def return_student_ID(self, university, name):
        if university == self.university and name == self.name:
            return self.student_ID
        return "No such student or university"


class Teacher(Person):
    def __init__(self, name, surname, age, country, city, university, position, salary):
        super().__init__(name, surname, age, country, city)
        self.university = university
        self.position = position
        self.salary = salary

    def introduce_yourself(self):
        print(f"My name is {self.name} {self.surname}. My salary is very small - {self.salary}. I am currently working as an {self.position}, but plan to become a principal. You'd better earn my favor")

    def salary_supplement(self, procent):
        self.salary += (self.salary*procent)/100
        return self.salary

    def threat(self, students_name):
        return f"Did you leave your head at home? I'll call your parents, {students_name}."


if __name__ == "__main__":
    person_1 = Person("Adriana", "Levalina", 14, "Poland", "Warshaw")
    person_1.introduce_yourself()
    person_1.age_difference(20)

    student_1 = Student("Ulinka", "Farington", 24, "Croatia", "Zagreb",
                        2345, "Josip Juraj Strossmayer University of Osijek", "World economy")
    student_1.introduce_yourself()
    print(student_1.return_student_ID(
        "Josip Juraj Strossmayer University of Osijek", "Ulinka"))

    teacher_1 = Teacher("Nurbel", "Kazulnutova", 37, "Kazakhsan", "Astana",
                        "Al-Farabi Kazakh National University", "english teacher", 100)
    teacher_1.introduce_yourself()
    teacher_1.salary_supplement(5)
    print(teacher_1.salary)
    teacher_1.threat("Sultan")
