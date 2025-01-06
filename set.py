"""collection = {1, 2, 3, 4, "hello", "prince"}
print(collection)
print(type(collection))

#ignore duplicate value

collection = {1, 2, 2, 1, "prince", "prince", "singh"}
print(collection)
print(type(collection))
print(len(collection))  #total numbers of items

#empty set syntax 
collection = set()     #empty set () : syntax
print(collection)
print(len(collection))"""

#set method in python

collection = set()
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.remove(4)
collection.clear()


collection = {1, 2, 3, 4, "hello", "prince"}
print(collection.pop())

# union set method

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))   #{1,2,3,4}

#or old value can print then it can aour value like
print(set1)
print(set2)


#intersection set method

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))  # {2,3}

