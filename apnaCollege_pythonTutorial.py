"""
first_name = "Tony"
last_name = "stark"
age = 51 
is_genius = True
print(first_name +" " + last_name)
name = input("What is your name ?")
print("hello "+name)

#type convirsion

old_age = input("Enter your old age : ")
#new_age = old_age + 20  #this line will give error as it take old_age as string and string cannot be added to integer 2.
new_age = int(old_age)+2 #this line will not give any error.
print(old_age)
print(new_age)

number = 18
print(float(number))

#Program 1: Add two values

firstNum = input("Enter first number: ")
secondNum = input("Enter second number: ")
sum = int(firstNum) + int(secondNum)
print("sum of two numbers is: "+str(sum))

#Topic: String

name = "Tony Stark"
print(name.upper()) #Upper method is use to change case of sting to upper.
print(name.find('tark')) #find method is use to find the index of any latter or string. if it is present then show the index and if not then -1.
print(name.replace("Tony Stark","Ironman")) #replace is use to replace the sting with another string.
print('S' in name) #in keyword is use to check whether latter/String is present or not. if present it return true else false.

#Topic : Operators
print(5+2) #add
print(5-2) #subtract
print(5*2) #multiply
print(5/2) #divide
print(5%2) #remender
print(5//2) #this operator is use to devide two numbers and it does not show number after the point(.).
print(5**2) #this operator is use for power. eg.(5^2 = 25).

#logical Operators

print(3<2 or 2<3)
print(3>2 and 2<3)
print(not 3>2)

#Topic : if-else statement

age = 13
if age >= 18:
    print("You are an adult.")
elif age<18 and age >3:
    print("You are in school")
else :
    print("Yor are a child")

#Problem 2: Create mini calculator

first = input("Enter first number: ")
operator = input("Enter the operator(+,-,*,/,%): ")
second = input("Enter second number: ")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else :
    print("Invalid operator")

#Topic: Loops
#1. While loop

i = 1
while i<=10:
  print(i)
  i += 1

#Printing star pattern using while
i = 1
while i<=5:
    print(i*"*")
    i += 1

#2. For loop
for i in range(5):
    print(i)

#Topic: list:- it is muteable or we can say it is not inmuteable. we can make changes after creating. it is define using [].

marks = [98,97,99,"maths"]
print(marks)
print(marks[0])
print(marks[1])
print(marks[-1])
print(marks[-2])
print(marks[3])
print(marks[0:2])
print(marks[1:4])

for score in marks:
    print(score)

marks.append(95) #append is use to add item in list. By default it add item in the end of list.
marks.insert(0,96) #insert is alse use to add item in list but using insert we can add item in any index. in this 0 is index and 96 is item.
print(99 in marks) #in is use to check wheather item is present or not. hear 99 is check.
print(len(marks)) #len is use to check the length of list.
print(marks)

marks.clear()  #clear is use to clear the list.
print(marks)
    
#Topic: Break and Continue
students = ["manish","ragini","pulma","gaurav","vikas"]
for student in students:
    if student == "gaurav":
        #continue; #";" it is optional in python
        break
    print(student)
    
#Topic: Tuple :- it is inmuteable. we can not make change after creating. it is define using ().

marks = (98,95,96,97,97,97)  #it is a tuple of marks.

print(marks.count(97))  #count is use to count the occurance of item. eg. hear 97 is occure 3 time. so output is 3.
print(marks.index(96))  #index is use to check index of item. eg. hear index of 96 is checked and output is shown.

#Topic: Set:- set is collection of unique element. it is defined using {}. indexing is not present in set. it is unorderd.

marks = {97,98,99,99,99}
print(marks)

marks1 = {95,98,97,97,97}

for score in marks1:
    print(score)
    
#topic: Dictonary:- it is inorderd. in this we store two pairs. define using {}.

marks = {"Engish":95,"Chemistry":98}
print(marks)
print(marks["Chemistry"])

#Adding elements in dictonary.

marks["physics"] = 97
print(marks)

#Changing/modifying data

marks["physics"] = 99 
print(marks)

#Topic: Functions:- there are three types of functions in python. in-built, module, user define functions.
#2. Module fumction:- it refers to the function of a module. example of module is- Math

import math
print(dir(math))  #it will show all fumctions of math module

#from math import sqrt  #it only import sqrt function of math module.
from math import *   #it will import all function of math module.
print(sqrt(16))

#3. User define function:- 
#       syntex-    def function_name(perameters):
#                       //do something

def print_sum(first, second):
    print(first + second)

print_sum(2,3)
"""
#we can also fix any perameter value

def print_sum(first, second=4):
    print(first + second)

print_sum(4)