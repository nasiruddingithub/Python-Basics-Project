#Assignment for Basic Pyton
#Assignment no 01
#Assignment taken by NONACADEMY
#My student id:NA-7EE714
#Contact: nasir.du19@gmail.com
#Assingment topics:
# 1.Variables
# 2.Data Types
# 3.Arithmetic & Comparision Operators
# 4.Logical & Assignment Operator
# 5.Identy & Membership Operator

###01.Variables & Data Types

name = "Nasir"
age = 24
is_student = True

print(f"Name: {name}", type(name)) #output: Name: Nasir <class 'str'>

print(f"Age: {age}", type(age)) #output: Age: 24 <class 'int'>

print(is_student , type(is_student)) #output: True <class 'bool'>


###02.Use of Arithmetic operator
my_age = 24
print(my_age + 5) #Output: 29
print(my_age - 5) #Output: 19
print(my_age * 5) #Output: 120
print(my_age / 5) #Output: 4.8


###03.Use of Comparision Operator
age = 24
if (age > 18):
  print("Yes, Your age is greater than 18") #output:Yes, Your age is greater than 18

#Use of ==, !=, <, >
number_1 = 20
number_2 = 50

if (number_1 == number_2):
  print("Both are equal")
elif number_1 != number_2:
  print(number_1,"and", number_2, "are not equal")
else:
  print("No result") 
  
# Two number comparision
if (number_1 > number_2):
  print(number_1, "is greater than", number_2)
else:
  print(number_2, "is greater than", number_1)

#04.Logical operator

email = "hasan@gmail.com"
password = "887757**"
user_email = str(input("Enter your registered email: "))
user_pass = str(input("Enter your password: "))
if email == user_email and password == user_pass:
  print("Login successful! Welcome to Nonacademy")
else:
  print("Please enter valid information")
  
#more use of and operator

marks = str(input("Enter your marks: "))

if (marks >= 0 and marks <= 32):
  print("Pardon me, You failed! Try next time.")
elif (marks >= 33 and marks <= 39):
  print("D")
elif (marks >= 40 and marks <= 49):
  print("C")
elif (marks >= 50 and marks <= 59):
  print("B")
elif (marks >= 60 and marks <= 69):
  print("A")
elif (marks >= 70 and marks <= 79):
  print("A-")
elif (marks >= 80 and marks <= 100):
  print("A+")
else:
  print("You entered invalid number")

#Use of or operator
operator_1 = "Airtel"
operator_2 = "Robi"
  
sim_operator = str(input("Enter your Operator Name: "))

if sim_operator == operator_1 or sim_operator == operator_2:
  print("You are eligible to perticipate in Robi Axiata Summit 2025")
else:
  print("You are not a Robi Axiata Customer")

#Use of not operator
sunny = True
if not sunny:
  print("It is cludy outside")
else:
  print("It is sunny outside")
  
  
###05 Use of Assignment Operators 
#Use of +=, -=, *=, /= 

a = 10
a += 5
print(a) #output is 15

b = 15
b -= 5  
print(b) #output is 10

c = 5
c *= 5
print(c) #output is 25

d = 20
d /= 2
print(d) #output is 10.0

###06.Identy operators

my_list_01 = [30, 20]
my_list_02 = [30,20]
my_list_03 = my_list_01
print(my_list_01 is my_list_03) #output is True
print(my_list_01 is not my_list_02) #output is True
print(my_list_01 == my_list_03 ) #output is True
print(my_list_01 is my_list_02) #output is False

###07.Membership Operators
p_lang = ["Python", "Java Script", "Java", "C", "C++", "R", "Rust", "PHP"]

print( "R" in p_lang) #output: True
print("Python" not in p_lang) #output: False
print("Ruby" not in p_lang) #output: True

#Thank you sir!