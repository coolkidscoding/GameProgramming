# Review variables
var1 = 1
var2 = 2.0
var3 = True
var4 = 'Hello'

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

# no keywords

# Data Structures

# list
list1 = [1,2,3,4,5,6,7,8,9]

# how do I get
# via indexing
my_index =-2
print(list1[my_index])

# slicing
my_slice = list1[0:4]
print(my_slice)

# what is the slice that will give me 4,5,6,7
print(list1[3:7])

# Dictionaries- key:values
var1 = {}
var1['a'] = 1

# if key b exists then overwrite otherwise add
var1['b'] = 1

# what is the syntax for me to add 1 to an existing value
var1['b'] = var1['b'] + 1

print(var1)

# tuples
tup1 = (1,2,3,4)
print(type(tup1))
#tup1.append(5)

key = (1,2,3)
value = 1
var1[key] = 1

# set
var_set = set()
print(type(var_set))


set1 = {1,2,3,4}
set2 = {4,5,6,7}

print(type(set1))

print(set2.difference(set1))

# Loops

# while

condition = True
count = 0
while condition == True:
    print('count = ', count)
    count = count + 1

    if count == 10:
        condition = False

# Write the code that will tell me whether the number 5 is in the below list
list1 = [3,6,7,2,6,5,8,4,9]

found_number = False
index = 0
while found_number == False:
    curr_num = list1[index]
    if curr_num == 5:
        found_number = True
        print('Found my number! - in while loop')

    index += 1

# for
for curr_num in list1:
    if curr_num == 5:
        print('Found my number! - in for loop')

for elt in range(21):
    print(elt)


# functions
def DoNothing(arg):
    print('In DoNothing with argument', arg)

DoNothing(1)

def DoNothing2(arg):
    return arg

DoNothing(DoNothing2(2))

def Return1():
    return 1

def Return2():
    return 2

def Return3():
    return 3

var5 = Return1() + Return2() + Return3()
print(var5)







