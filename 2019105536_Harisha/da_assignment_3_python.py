# -*- coding: utf-8 -*-
"""DA_Assignment_3_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BzB5VmBLskXCFIQjidCp-4FT94leeoGH

## Exercises

Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

** What is 7 to the power of 4?**
"""

print(7**4)

"""** Split this string:**

    s = "Hi there Sam!"
    
**into a list. **
"""

s = "Hi there Sam!"

print(s.split())

"""** Given the variables:**

    planet = "Earth"
    diameter = 12742

** Use .format() to print the following string: **

    The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers" .format(planet, diameter))

"""** Given this nested list, use indexing to grab the word "hello" **"""

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2])

"""** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d['k1'][3]['tricky'][3]['target'][3]

"""** What is the main difference between a tuple and a list? **"""

#tuple is immutable, but list is mutable
atup = (1, 2, 3)
alst = [1, 2, 3]
#atup[2] = 22
alst[2] = 22

"""** Create a function that grabs the email website domain from a string in the form: **

    user@domain.com
    
**So for example, passing "user@domain.com" would return: domain.com**
"""

mail = "user@domain.com"

print(mail.split('@')[1])

"""** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **"""

doggy = "Seungmin has dog as his mascot."

for i in doggy.split():
  if (i == "dog"):
    print("True")

"""** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **"""

doggy1 = "Seungmin has dog as his mascot. He is a dog reincarnate."

count = 0
for i in doggy1.split():
  if (i == "dog"):
    count += 1
print(count)

"""### Problem
**You are driving a little too fast, and a police officer stops you. Write a function
  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
  If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
  cases. **
"""

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

caught_speeding(122, 0)

caught_speeding(85, 1)

"""Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. """

sal = ["kai", 22222, "lino", 33333, "soonie", 44444, "doongie", 55555, "dori", 66666]
sal_tot = 0
for i in range(1, 10, 2):
  sal_tot += sal[i]
print(sal_tot)

"""Create two dictionaries in Python:

First one to contain fields as Empid,  Empname,  Basicpay

Second dictionary to contain fields as DeptName,  DeptId.

Combine both dictionaries. 
"""

dict_22 = {"Empid" : 22, "Empname" : "IN", "Basicpay" : 77777}
dict_33 = {"DeptName" : "Stray Kids", "DeptId" : 8}
dict_44 = {**dict_22, **dict_33}
print(dict_44)

