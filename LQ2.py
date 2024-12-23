import random

#dictionary information of the student and classmate to stored
students = {
# student
    "student": {"name": "Francis", "grade": 95},
#classmate
    "classmate": {"name": "Angelbert", "grade": 92}
}

#list of the lengths of student names to store 
name_len =
# student length
 [len(students["student"]["name"]),
 # classmate length
  len(students["classmate"]["name"])]

# List of class numbers to sort and reverse
classNum = [3, 5, 2, 9, 1]
classNum.sort(reverse=True)  # list to sort and reverse 

# Function that contains IF...ELIF...ELSE condition
def quizTwo(user_name, student_grade, classmate_grade):
# if statement
    if student_grade > classmate_grade:
# print {user_name}, {students['student']['name']} has a higher grade than {students['classmate']['name']}.")
        print(f"{user_name}, {students['student']['name']} has a higher grade than {students['classmate']['name']}.")
 # elif statement
    elif student_grade < classmate_grade:
# print "{user_name}, {students['classmate']['name']} has a higher grade than {students['student']['name']}.")
        print(f"{user_name}, {students['classmate']['name']} has a higher grade than {students['student']['name']}.")
 # else statement
    else:
 #print "{user_name}, both {students['student']['name']} and {students['classmate']['name']} have the same grade."
        print(f"{user_name}, both {students['student']['name']} and {students['classmate']['name']} have the same grade.")

# ask you to enter you name
user_name = input("please enter your name: ")

# user input that call the function and pass
quizTwo(user_name, students["student"]["grade"], students["classmate"]["grade"])

#display the sorted and reversed class numbers
print(f"Reversed sorted class numbers: {classNum}")

#display the length of student names
print(f"Lengths of names: {name_len}")
