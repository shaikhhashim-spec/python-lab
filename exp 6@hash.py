#student enrollment manager
print("251A001", "HASHIM")
CET={"251A011", "251A054", "251A010"}
JEE={'251A020', '251A053', '251A049', '251A006'}
NEET={'251A022', '251A024', '251A016'}
print (CET | JEE|NEET) #total students
print("Total students appeared in the exams:",CET|JEE|NEET)
#total no.of students
print ("Total students appeared in all exams:", CET&JEE&NEET)
print("Total students appeared only in cet and neet exams:", (CET&JEE)-NEET)
print("Total students appeared only in cet and neet exams:", (CET&NEET)-JEE)
print (CET | JEE) # total students appeared in cet and jee #either cet or jee but not both
print (CET|JEE) #students appeared in both cet and jee
print (CET-JEE)
print((CET|JEE) - (CET&JEE)) #either cet or jee but not both
