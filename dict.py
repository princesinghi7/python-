"""info = {
    "name" : "prince",     #string value
    "age" : 19,     #int value
    "is_adult" : True,   #boolean value
    "skill" : ["c", "python", "java"],   #in dictionary we can use list
    "topics" : ("dictionary", "sets"),   #in dictionary we can use tuple
    "learning" : "codeing",
    "cgpa" : 7.5,    #floating value

}
print(info)
print(type(info))
info["name"] = "prince singh"
print(info)

#we can create a null dict

null_dict = {}
print(null_dict)"""


#nested dictionary

"""student = {
    "name" : "prince singh",
    "score" : {
        "chem" : 95,
        "phy" : 94,
        "math" : 99,
    }
}
print(student)


student = {
    "name" : "prince singh",
    "score" : {
        "chem" : 95,
        "phy" : 94,
        "math" : 99,
    }
}
print(student["score"]["phy"])"""

#dictionary method

student = {
    "name" : "prince singh",
    "score" : {
        "chem" : 95,
        "phy" : 94,
        "math" : 99,
    }
}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("key"))
student.update({"city" : "vadodra"}),
print(student)