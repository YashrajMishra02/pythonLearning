# program to calculate the grade of student from his marks from scheme
marks = int(input("Enter your marks to know in which grade do you lie: "))
if(marks>=90 and marks<=100):
    print("Excellent grade")
elif(marks>=80 and marks<90):
    print("A grade")
elif(marks>=70 and marks<80):
    print("B grade")
elif(marks>=60 and marks<70):
    print("C grade")
elif(marks>=50 and marks<60):
    print("D grade")
elif(marks<50):
    print("F grade")
else:
    print("Invalid Marks types")
