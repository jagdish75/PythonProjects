
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("NAME: %s  %s \nEMAIL Id: %s \nSALARY= %d" % (self.first, self.last, self.email, self.pay))
        #print ("NAME : ", self.first + self.last, "\n EMAIL Id: ", self.email, "\n SALARY=", self.pay)

    def empFileUpdate(self):
        print ("NAME: %s  %s \nEMAIL Id: %s \nSALARY= %d" % (self.first, self.last, self.email, self.pay))
        #print ("NAME : ", self.first + self.last, "\n EMAIL Id: ", self.email, "\n SALARY=", self.pay)


emp_filehandler = open("empfile.txt", "w")

    def empFileUpdate(self):
        print ("NAME: %s  %s \nEMAIL Id: %s \nSALARY= %d" % (self.first, self.last, self.email, self.pay))
        #print ("NAME : ", self.first + self.last, "\n EMAIL Id: ", self.email, "\n SALARY=", self.pay)


print "#" * 25
print "Creating 50 Employee Objects"
print  "#" * 25

emp_filehandler = open("empfile.txt", "w")

for counter in range(total_employee):
    f_name = "first_" + str(counter)
    l_name = "second_" + str(counter)
    salary = 500 + counter
    e = Employee(f_name, l_name, salary)

    print "-" * 80
    e.displayEmployee()
    print "-" * 80
    print "\n"


