# DEFINE COMMON BASE CLASS for all EMPLOYEES

class Employee:
    empCount = 0

    def __init__(self,fname,lname,pay):
        self.first = fname
        self.last = lname
        self.email =  fname + '.' + lname + '@company.com'
        self.pay = pay
        Employee.empCount +=1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("NAME: %s  %s \nEMAIL Id: %s \nSALARY= %d" % (self.first, self.last, self.email, self.pay))
        #print ("NAME : ", self.first + self.last, "\n EMAIL Id: ", self.email, "\n SALARY=", self.pay)

"This would create first Object of Employee Class"
emp1 = Employee("Zara", "Khan", 2000)

print "DISPLAY COUNT"
emp1.displayCount()

"This would create the second object of Employee Class"
emp2 = Employee("Amit", "Mannan",5000)

print  "########\n\n"


emp1.displayEmployee()
emp2.displayEmployee()

total_employee = 5000

employee_dict = {}

print "#" * 25
print "Creating 50 Employee Objects"
print  "#" * 25


for counter in range(total_employee):
    f_name = "first_" + str(counter)
    l_name = "second_" + str(counter)
    salary = 500 + counter
    e = Employee(f_name, l_name, salary)
    print "-" * 80
    e.displayEmployee()
    print "-" * 80
    print "\n"


print "Total Employee %d" % Employee.empCount
## print employee_list
## import pprint
## pprint.pprint(employee_dict)


