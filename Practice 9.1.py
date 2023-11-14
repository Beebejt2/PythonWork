#Practice 9.1
#This program modifies a list

#Create a list with contents:  [7,4,8,6,2,9]
myList = [7,4,8,6,2,9]

#Add 3 to the beginning of the list
myList.insert(0,3)

#Remove 2 from the list.
myList.remove(2)

#Add 5 at position 3.
myList.insert(3,5)

#Delete elements from positions 1-2.
myList.pop(1)
myList.pop(-2)

#Embed new elements 11,12,13 at position 3 (in one statement).
otherList = [11,12,13]
myList = myList[:2] + otherList + myList[2:] 

#Print the resulting list
print(myList)


