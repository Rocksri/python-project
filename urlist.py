urlist = ['wood','knife','axe']
mylist = ['tree', 'apple', 'mango', 'melon']

# Using the + operator
combined_list = urlist + mylist
print(combined_list)

# Using the extend() method
urlist.extend(mylist)
print(urlist)

# Using the append() method in a loop
combined_list = []
for item in urlist:
    combined_list.append(item)
for item in mylist:
    combined_list.append(item)
print(combined_list)

# Using the extend() method of list
combined_list = []
combined_list.extend(urlist)
combined_list.extend(mylist)
print(combined_list)

# Using List comprehension
combined_list = [x for x in urlist] + [x for x in mylist]
print(combined_list)
