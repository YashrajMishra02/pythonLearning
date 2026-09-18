# Program to accept marks of 6 students and display them in a sorted manner

Marks = []
s1 = int(input("Enter student 1 marks: "))
Marks.append(s1)
s2 = int(input("Enter student 2 marks: "))
Marks.append(s2)
s3 = int(input("Enter student 3 marks: "))
Marks.append(s3)
s4 = int(input("Enter student 4 marks: "))
Marks.append(s4)
s5 = int(input("Enter student 5 marks: "))
Marks.append(s5)
s6 = int(input("Enter student 6 marks: "))
Marks.append(s6)
Marks.sort()
print(Marks)
