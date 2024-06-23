class Person():
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob}"


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return super(Student, self).describe() + f", Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return super(Teacher, self).describe() + f", Subject: {self.subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return super(Doctor, self).describe() + f", Specialist: {self.specialist}"


class Ward():
    def __init__(self, name):
        self.name = name
        self.list_of_people = []

    def add_person(self, person):
        self.list_of_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.list_of_people:
            print(person.describe())

    def count_doctor(self):
        # Use 'list_of_people' instead of 'people'
        return sum(1 for person in self.list_of_people if isinstance(person, Doctor))

    def sort_age(self):
        return sorted(self.list_of_people, key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        sum_of_yob = 0
        count = 0
        for person in self.list_of_people:
            if isinstance(person, Teacher):
                sum_of_yob += person.yob
                count += 1
        return sum_of_yob / count


if __name__ == "__main__":
    student1 = Student("John", 2000, "7")
    print(student1.describe())
    teacher1 = Teacher("Jane", 1990, "Math")
    print(teacher1.describe())
    doctor1 = Doctor("Mike", 1980, "Neurology")
    print(doctor1.describe())

    #
    teacher2 = Teacher("Jane", 1990, "Math")
    doctor2 = Doctor("Mike", 1980, "Neurology")
    ward1 = Ward(name="Ward 1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(doctor1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor2)
    ward1.describe()
    
    print(f"Number of doctors in {ward1.name}: {ward1.count_doctor()}")
    print(f"Sorted list of people in {ward1.name}:")
    for person in ward1.sort_age():
        print(person.describe())
    
    print(f"Average year of birth of teachers in {ward1.name}: {ward1.compute_average()}")