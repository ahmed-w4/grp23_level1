# print student marks
# inputs

Student_grade = input("Enter your grade in capital letter: ")
# processing and output

if Student_grade == 'A' or 'a':
    print("Excellent")
elif Student_grade == 'B' or 'b':
    print("Very Good")
elif Student_grade == 'C' or 'c':
    print("Good")
elif Student_grade == 'D' or 'd':
    print("Pass")
elif Student_grade == 'E' or 'e':
    print("Fail")
else:
    print("Invalid grade")