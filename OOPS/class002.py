# DEFINE COMMON BASE CLASS for all EMPLOYEES

total_employee = 10000
emp_filehnd = open("empfile.txt", "a")

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

    def empFileUpdate(self):
        emp_filehnd.write ("\n")
        emp_filehnd.write ("-" * 25)
        emp_filehnd.write ("\nNAME: %s  %s\nEMAIL Id: %s\nSALARY= %d\n" % (self.first, self.last, self.email, self.pay))
        emp_filehnd.write ("-" * 25)
        emp_filehnd.write ("\n")

"This would create first Object of Employee Class"
emp1 = Employee("Zara", "Khan", 2000)

print "DISPLAY COUNT"
emp1.displayCount()

"This would create the second object of Employee Class"
emp2 = Employee("Amit", "Mannan",5000)

print  "########\n\n"


emp1.displayEmployee()
emp2.displayEmployee()


#employee_dict = {}

print "#" * 25
print "Creating %d  Employee Objects",total_employee
print  "#" * 25


for counter in range(total_employee):
    f_name = "first_" + str(counter)
    l_name = "second_" + str(counter)
    salary = 1000 + counter
    e = Employee(f_name, l_name, salary)

    print "-" * 80
    e.displayEmployee()
    print "-" * 80
    print "\n"
    e.empFileUpdate()

print "Total Employee %d" % Employee.empCount

## print employee_list
## import pprint
## pprint.pprint(employee_dict)


