#https://github.com/shaikhhashim-spec/Python
print("UIN : 251A011", "DATE : 09-02-2026")
d={}
n = int(input("ENTER NUMBER OF STUDENTS : "))
for i in range(1,n+1):
  Name = input("NAME : ")
  Attendance = input("ATTENDANCE : ")
  d[i] = {"NAME":Name, "ATTENDANCE":Attendance}
print(d)
