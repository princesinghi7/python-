# wap to input 2 number & print their sum

"""first = int(input("enter first number : "))
second = int(input("enter second number : "))
print("sum : ", first + second)"""

#indexing in python

"""str = "hello_prince"
ch = str[6]
print(ch)"""

#slicing in python

"""str = "hello prince"
print(str[5:len(str)])"""

#string functions

"""str = "i am a coder"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("e" , "r"))
print(str.find("c"))
print(str.count("c"))"""


#wap to input user first name & print its length

"""name = input("enter your name :")
print("length of your name", len(name))"""

#wap to print dollar$

"""str = "hii $i am the symbol of $ a dollar$  99.99$"
print(str.count("$"))"""



#wap input to side of square &print its area.

"""side = float(input("enter square of area : "))
print("area =", side ** 5)"""


#wap to input 2 floating point numbers &print their average.

"""a = float(input("enter first : "))
b = float(input("enter second : "))
print("avg =", (a+b)/2)"""


#wap to check if a number entered by the user is odd or even

"""num = int(input("enter number : "))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")"""


    #OR

"""num = int(input("enter number : "))

if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")"""


#wap to find the greatest of 3 numbers entered by the user.

"""a = int(input(" ENTER THE FIRST NUMBER : "))
b = int(input(" ENTER THE SECOND NUMBER : "))
c = int(input(" ENTER THE THIRD NUMBER : "))

if(a >= b and a >= c):
    print("FIRST NUMBER IS LARGEST", a)
elif(b >= c):
    print("SECOND NUMBER IS LARGEST", b)
else:
    print("THIRD NUMBER IS LARGEST", c)"""


#wap to check if a number is a multiple of 7 or not

"""x = int(input(" ENTER NUMBER : "))

if(x % 7 == 0):
    print("multiple of seven")
else:
    print("not a multiple")"""


#wap to ask the user to enter names of their 3 favourite movies & store them in a list

"""movies = []
mov1 = input("enter 1st movie : ")
mov2 = input("enter 2nd movie : ")
mov3 = input("enter 3rd movie : ")

movies.append(mov1)
movies.append(mov3)
movies.append(mov2)

print(movies)"""

#wap to check if a list contains a palindrome of elements.(hint : use copy()method)
#  [1,2,3,2,1]              [1,"abc","abc",1]

"""list1 = [1,2,3,2,1]
list2 = [1,2,3,4,5]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")"""

#wap to count the number of students with the "A" grade in the folllowing tuple.
#   ["c", "d", "a", "a","b","b","a"]

"""grade = ("c", "d", "a", "a","b","b","a")
print(grade.count("a"))
print(grade)"""

#store the above values in a list & sort them from "A" to "D".

"""grade = ["c", "d", "a", "a","b","b","a"]
grade.sort()
print(grade)"""


#SET 
# store following word meanings in a python dictionary :
# table: "a piece of furniture", "list of facts & figures"
#cat : "a small animal"

"""dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture ", "list of facts & figures"],
}
print(dict)"""

#you are given a list of subjects for students.assume one classroom is required for 1 subject. how many classroomsare needed by all students.
#"python", "java", "c++",  "python", "javascript", "java", "python", "c++" "c"

"""subjects = {"python", "java", "c++",  "python", "javascript", "java", "python", "c++", "c"}
print(subjects)
print(len(subjects))"""

# wap to enter marks of 3 subjects from the user and store them in a dictionary .start with an empty dictionary & add one by one .use subject name as key & marks as value.
"""marks = {}
x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)"""


#figure out a way to store 9 & 9.0 as seprate values in the set .(you can take help of built in data types)

values = { 9, "9.0"}
print(values)

#built in data types

values = {("float", 9.0), ("int", 9)}
print(values)


