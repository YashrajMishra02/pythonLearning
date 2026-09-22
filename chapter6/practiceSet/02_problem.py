# findout whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as a input from the user
print("Enter your subject marks out of 100: ")
English = int(input("Enter the english marks: "))
Maths = int(input("Enter the maths marks: "))
Science = int(input("Enter the science marks: "))
Avg= (English+Maths+Science)/3
if(English> 33 and Maths>33 and Science>33 and Avg>40):
    print(f"Your Passed in exam with total percentage of: {Avg} %" )
else:
    print("You Failed in the exam")
