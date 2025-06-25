class Employee:
    def __init__(self, first, last):
        # self = whoever called this method
        self.first = first
        self.last = last

    @property
    def email(self):
        # self = whoever called this method
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Deere')

emp1.first = 'Jonathan'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

