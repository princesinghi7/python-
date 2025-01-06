#if-elif-else statement use


"""Light = input("Light :")
if (Light == "Red"):
    print("stop")

elif (Light == "Yellow"):
    print("look out")

elif (Light == "Green"):
    print("go")

else:
    print("Light is broken")


#marks condition

marks = int(input("marks : "))
if (marks >= 90):
    print("A")

elif(marks >= 80 and marks < 90):
    print("B")

elif(marks >= 70 and marks < 80):
    print("C")

else:
    print("D")


    #practice print 

A = int(input("A : "))
G = input("M/F : ")

if((A == 1 or A == 2 ) and G == "m"):
    print("fee is 100")

elif((A == 3 or A == 4) and G == "f"):
    print("fee is 200")

elif(A == 5 or G == "m"):
    print("fee is 300")

else:
    print("no fee")


    #single line if/Ternary operator

food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)


food = input("food :")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#clever if /Ternary operator

age = int(input("age : "))
vote = ("yes" , "no") [age <= 18]
print(vote)


sal = float(input("salary :"))
tax = sal*(0.1,0.2) [sal <= 500000]
print(tax)"""

#nesting

age = 95

if (age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
