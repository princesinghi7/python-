# while loop

"""count = 1
while count <= 5:
    print("hello world")
    count +=1
    print(count)


i = 1
while i <= 100000:
    print("hello world", i)
    i +=1"""

#print the numbers from 1 to 1000
"""i = 1
while i <= 1000:
    print(i)
    i += 1"""

"""

count = 100
while count >= 1:
    print(count)
    count -=1"""

"""n = int(input("enter from the user :"))   # input from the user
i = 1
while i <= 10:
    print(n * i)   #direct put the value of place of n
    i += 1"""

#print the elements of the following list using a loop :
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[5])
print(nums[6])    #...print(nums[len(nums)-1])


#orrr
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
heroes = ["spiderman", "thor"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1"""

#search for a number x in this tuple using loop:     (1,4,9,16,25,36,49,64,81,100)

"""nums = (1,4,9,81,25,36,49,64,81,100)

x=81

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)

    else:
        print("finding...")
    i += 1"""

    #using break keyword

"""i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop") 



nums = (1,4,9,81,25,36,49,64,81,100)

x=81

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        break

    else:
        print("finding...")
    i += 1"""


#using continue keyword

"""i = 1
while i <= 5:
    if( i == 3):
        i += 1
        continue
    print(i)
    i += 1

print("end of loop")"""


# for loop  in list

"""nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)



vaggies = ["cucmber", "ladyfinger", "potato", "tomato", "chilly"]
for val in vaggies:
    print(val)

# for loop  in tuple

tup = (1, 2, 3, 4, 5)
for val in tup:
    print(val)
    print(type(tup))

# for loop  in string

str = "prince singh"
for char in str:
    if(char == "i"):
     print("i found")
     break
    print(char)
else:
    print("END")"""


# print the elements of the following list using a loop:   [1,4,9,81,25,36,49,64,81,100]

"""nums = [1,4,9,81,25,36,49,64,81,100]
for el in nums:
    print(el)"""


#search for a number x in this tuple using loop:   [1,4,9,81,25,36,49,64,81,100]
#this process is known as linear search
"""nums = (1, 4, 9, 81, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in nums:
    if (el == x):
        print("number found at idx", idx)
        break
    idx += 1"""


#range function in python

"""seq = range(10)

for i in  seq:
    print(i)

    #orrr

for i in range(20):  #range(stop)
    print(i)"""

"""for i in range(2, 10):  #range(start, stop)
    print(i)

for i in range(2, 101, 2):  #range(start, stop, stop)
      print(i)"""

#print the multiplication table of a number n.

"""n = int(input("enter number :"))
for i in range(1, 11):
    print(n * i)

#use in pass statement

for i in range(5):
    pass

print("some useful works")"""

#find total number of sum

"""n = 7
sum = 0
for i in range(1, n+1):
    sum +=i
print("total sum =", sum)

#sum using while
n = 7
sum = 0
i = 1
while i <= n:
    sum +=i
    i += 1
print("total sum =", sum)

#find the factorial using for loop
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("total factorial =", factorial)"""

