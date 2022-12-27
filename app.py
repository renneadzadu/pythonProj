"""print('hello world')
name = "renne"
last_name = "adzadu"
age = 30
age = age -5
is_old = False, "not old"
print(name, last_name, age, is_old) """

"""patient_name = "John Smith"
age = 20
patient_status = "new pt"
print(patient_name, age,patient_status)"""


# name = input("What is your name? ")
 # print("hello " + name)

""" # this will convert a data type
 int()
 float()
 bool()
 str()"""


"""birth_year = input("enter you birth year: ")
age = 2023 - int(birth_year)
print("you are " , age) """


"""first = input("First: ")
second = input("Second: ")
sum = int(first) + float(second)
# if not convected, it will print as a string
print("the sum is = " , sum)"""

'''#another way to perform the methos up with concatination
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
# if not convected, it will print as a string
print("the sum is = " + str (sum))'''
#########################################################################################################################################
'''#Methods / functions
# working with python functions or methods => Strings are immutable - you cannot change them.
course = "PyThOn for BeginNErs"
print(course.upper()) # this built in method will print in uppercase
print(course) # our original course method is not changed. it stays the same
print(course.lower()) # this built in method will print in uppercase
print(course.find('E'))
print(course.find('for'))
print(course.replace('for', '4'))
print("for" in course) ## the in operator checks to see if it exsits
'''
#######################################################################################################
"""#MATH OPERATORS
print(5 + 4)
print(5 - 4)
print(5 * 4)
print(5 / 4) # this gives float
print(5 // 4) # this gives int
print(21 % 4) # remainder of 1
print(20 % 4) # remainder of 0
print(10 ** 3) # 10 to the power of 3

x = 10
x = x + 3 #same as
x += 3
x -= 3
print(x)
x = 10 + 3 * 2
print(x)
x1 = (10 + 3) * 2
print(x1)
# boolean expression
# comparison operator = <, <=, >, >=, ==, !=
x = 3 > 2
print(x)
x = 3 <= 3
print(x)
x = 3 == 2
print(x)
x = 3 != 2
print(x) """

###########################################################################
''''# logical operator => AND(both must be true), OR(one must be true), NOT(inverse of any value)
price = 5
print(price > 10)
print(not price > 10)
print(price > 10 and price < 30)# is price greatter than 10 AND is price less than 30 = False
print(price > 10 or price < 30) # is price greatter than 10 OR is price less than 30 = True
'''

##############################################################################################
# working with conditional statements => IF STATEMENT
'''
temperature = 25
# indentations = a block of code. no need for {}
if temperature > 30:
    print("it's a hot day!!!")
    print("Drink alot of water")
elif temperature > 20:
    print("its a nice day")
elif temperature > 10:
    print("its a bit cold")
else:
    print("It's Cold")
print("Done")'''
################################################################
'''# EXCESISE : get an input of weight and unit.
weight = int(input("what is your weight? "))
kg_lbs = input("Is your weight in (K)g or (L)bs? ")
if kg_lbs.upper() == 'K':
    converted = weight/ 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))'''

#######################################################################
#WHILE LOOP

'''i = 1
while i <= 1_000:
    print(i)
    i = i + 1'''

''' i = 1
while i <= 10:
    print(i * "$") # this prints the dollar signs and increnments
    i = i + 1 '''

'''# LIST
names = ["rene", "john",'abbey','ronny']
print(names[0])
names[0] = 'Renne' # this will chage the list Index 0 to Renne instade of rene
print(names[-1]) # gives you end of list
print(names)
print(names[0:3]) # gives you less index from original but does not change the original list
'''
'''numbers = [1,2,3,4,5,6,7,8,9]
#numbers.append(6) # insert 6 at the end
#numbers.insert(0, -1)  # insert -1 at the begaining of list
#numbers.remove(6) # removing the 6 in between
#numbers.clear() # gives you an empty list
#print(numbers)
#print(6 in numbers) # search if 6 is in the list => boolean expression
#print(10 in numbers) #theres no 10 in the list
#print(len(numbers))
'''

######################################################################################

''''# this is a for-loop
numbers = [1,2,3,4,5,6,7,8,9]
for item in numbers:
    print(item)


i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1 # this increments. i++ in java

# range of 0 - 4 will print out
numbers = range(5)
for n in numbers:
    print(n)

# range of 5 - 9 will print out
numbers = range(5,10)
for n in numbers: # for loop
    print(n)

# range of 5 - 9 will print out but 2 by 2 => 5,7,9
numbers = range(5,10,2)
for n in numbers: # for loop
    print(n)

for n in range(5): # for loop
    print(n)
'''
###################################################################################
#CREATING A TUPLE OBJECT => tuples are immutable => once created, cannot be changed

numbers = (1,4, 3, 2, 1, 1,2,3,4)
print(numbers.count(1))

