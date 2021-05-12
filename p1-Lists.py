#Lists: ordered, mutable, allows duplicate elements
mylist = ["hari", "ram", "krish"]
print(mylist)

mylist2 = [4, True, "apple", "apple"]
print(mylist2)

mylist3 = list()
print(mylist3)

item = mylist[-1]
print(item)

for i in mylist2:
    print(i)

if "hari" in mylist:
    print("yes")
else:
    print("no")

if "apple" in mylist:
    print("yes")
else:
    print("no")

#add new element to last
mylist.append('lemon')
print(mylist)

#add new element to a specific position
mylist.insert(2, 'Tea')
print(mylist)

#remove the last element
mylist.pop()
print(mylist)
print(item)

#remove a specific element
mylist.remove('Tea')
print(mylist)

#reverse the list
mylist.reverse()
print(mylist)

#remove all elements
mylist.clear()
print(mylist)

#sorting the list
mylist4 = [3, 3,5,-1,-7]
print(mylist4)
mylist4.sort()
print(mylist4)

#create a new list
newlist = sorted(mylist4)
print(newlist)

#tricks
mylist5 = [0]*2
print(mylist5)

#concatenation
newlist1 = mylist5 + mylist2
print(newlist1)

#slising
a = newlist1[1:4]
print(a)
a = newlist1[1:]
print(a)
a = newlist1[:4]
print(a)
a = newlist1[1:4:2] #step
print(a)
a = newlist1[::-1] #reverse
print(a)

#coping a list
list_org = [1, 2, 3, 4]
# list_cpy = list_org.copy()
#or
# list_cpy = list(list_org)
#or
# list_cpy = list_org[:]
#don't do this to copy
list_cpy = list_org
list_cpy.append('lemon')

print(list_org)
print(list_cpy)

#editing and creating a new list
list1 = [1,2,3,4,5]
list2 = [i*i for i in list1]

print(list1)
print(list2)

