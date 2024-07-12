
# Write a program to accept marks of 6 students and display them in a sorted 
# manner.

marks = []

s1 = int(input("enter marks of student "))
marks.append(s1)   # for inputing marks from student
s2 = int(input("enter marks of student "))
marks.append(s2)
s3 = int(input("enter marks of student "))
marks.append(s3)
s4 = int(input("enter marks of student "))
marks.append(s4)
s5 = int(input("enter marks of student "))
marks.append(s5)
s6 = int(input("enter marks of student "))
marks.append(s6)


marks.sort() # we sort marks using sort

print(marks)
