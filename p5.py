import sqlite3

con = sqlite3.connect("Program5")

print("Enter Employee ID")
EId = input()
print("Enter Employee Name :")
Ename = input()
print("Enter Employee City")
Ecity = input()
query = "insert into Employee(EmployeeId,EmployeeName,EmployeeCity) values (" + EId + " , ' " + Ename + " ' , '" + Ecity + "')"

#print("Enter Department ID")
#DId = input()
#print("Enter Department Name :")
#Dname = input()
#query = "insert into Department(DepartmentId,DepartmentName) values (" + DId + " , ' " + Dname + " ')"

#print("Enter Project ID")
#PId = input()
#print("Enter Project Name :")
#Pname = input()
#query = "insert into Project(ProjectId,ProjectName) values (" + PId + " , ' " + Pname + " ')"

con.execute(query)
con.commit()
con.close()
print("date saved...")