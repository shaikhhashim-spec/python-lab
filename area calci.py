#https://github.com/shaikhhashim-spec/python-lab
print("1 = square")
print("2 = rectangle")
print("3 = triangle")
print("4 = circle")
choice = int(input("enter your choice: "))
if choice == 1:
  s = int(input("enter side of square"))
  area = s*s
  print("area of square is: ",area)

elif choice == 2:
    
   l = int(input("enter length of ractangle"))
   b = int(input("enter breadth of rectangle"))
   area = l*b
   print("area of rectangle is: ",area)

elif choice == 3:
    
    h = int(input("enter height of triangle"))
    e = int(input("enter base of triangle"))
    area = 0.5*h*e
    print("area of triangle is: ",area)

else:
    
    r = int(input("enter radius of circle: "))
    area = 3.142*r*r
    print("area of circle is: ",area)

