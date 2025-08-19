#create an empty list
my_list = list()

#append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print(my_list)

#insert 15 at the second position
my_list.insert(1, 15)

#print(my_list)

#extend my_list with another list
my_list2 = [50, 60, 70]

my_list.extend(my_list2)

#print(my_list)

#remove the last element from my_list
my_list.pop()

#print(my_list)

#sort my_list in ascending order
my_list.sort()

#print(my_list)

#find & print the index of value 30 in my_list
print(my_list.index(30))