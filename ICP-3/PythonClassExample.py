class employee:
    counter = 0
    salary_sum = 0

    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        employee.counter = employee.counter + 1
        employee.salary_sum = employee.salary_sum + s

    def avg_salary(self):
        average_salary = self.salary_sum / self.counter
        print("average salary is " + str(average_salary))

    def display(self):
        print("name:" + self.name, "family_name:" + self.family, "salary:" + str(self.salary),
              "department:" + self.department)


class fulltime_employee(employee):
    def __init__(self, n, f, s, d):
        employee.__init__(self, n, f, s, d)

    e1 = employee("Kavin Kumar", "Arumugam", 2000, "IT")
    e2 = employee("Joe", "Blake", 1000, "HR")
    e3 = employee("John", "Smith", 5000, "IT")
    e1.display()
    e2.display()
    e3.display()


e4 = fulltime_employee("Tom", "Jerry", 4000, "Electrical")
e4.display()
print("number of employees:" + str(employee.counter))
employee.avg_salary(employee)
