class SchoolMember:
    """ Represents any school member """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def __repr__(self):
        return '<A {} named {} with age {}>'.format(
            self.classname(),self.name, self.age)

    @classmethod
    def classname(cls):
        return cls.__name__

    def tell(self):
        """ Tell My details """
        print('Name: "{}" Age: "{}"'.format(self.name, self.age))


class Teacher(SchoolMember):
    """ Represents a teacher """
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    """ Represents a student """
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))



    
