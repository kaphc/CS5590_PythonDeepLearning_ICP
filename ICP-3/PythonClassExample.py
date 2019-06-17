class Employee():
    employeeCount = 0
    totalSalary = 0

    def _init_(self, employeeId, name, salary, family):
        self.eid = employeeId
        self.name = name
        self.salary = salary
        self.family = family
        Employee.employeeCount += 1
        Employee.totalSalary += self.salary

    def displayEmployee(self):
        print("\n eid : ", self.eid, "\n Name : ", self.name, "\n Salary: ", self.salary, "\n family: ", self.family)


class FullTimeEmp(Employee):
    def _init_(self, employeeId, name, salary, family, exp):
        Employee._init_(self, employeeId, name, salary, family)
        self.exp = exp

    def displayEmployee(self):
        print("\n eid : ", self.eid, "\n Name : ", self.name, "\n Salary: ", self.salary, "\n Family: ", self.family,
              "\n Experience:", self.exp)


details = ["Emp ID", "Name", "Salary", "Family Members", "Experience"]
m = 4
n = int(input('number of employees : '))
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(0, n):
    for j in range(0, m):
        print('Employee: ', i + 1, '\ndetail: ', details[j])
        matrix[i][j] = input()
# print(matrix)
for i in range(0, n):
    emp1 = Employee(int(matrix[i][0]), matrix[i][1], int(matrix[i][2]), int(matrix[i][3]))
    emp1.displayEmployee()

matrix2 = []
m = 5
n = int(input('number of FullTime employees : '))
matrix2 = [[0 for j in range(m)] for i in range(n)]
for i in range(0, n):
    for j in range(0, m):
        print('FullTimeEmployee: ', i + 1, ' detail: ', details[j])
        matrix2[i][j] = input()
# print(matrix2)
for i in range(0, n):
    emp2 = FullTimeEmp(int(matrix2[i][0]), matrix2[i][1], int(matrix2[i][2]), int(matrix2[i][3]), int(matrix2[i][4]))
    emp2.displayEmployee()

print("Total Employees(with Full Time) %d" % Employee.employeeCount)
print("Average salary of the employees is", (Employee.totalSalary / Employee.employeeCount))
