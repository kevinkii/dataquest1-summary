#%% [markdown]
# ##Python Basic Code

#%%
a_value = 15
a_result = (27-7)*17
print(a_value)
print(a_value+12)
print(a_result + a_value)

#%% [markdown]
# | Snytax Shortcut | Example Code  | Output |
# |-----------------|---------------|--------|
# | +=              | x = 4, x += 2 | 6      |
# | -=              | x = 4, x -= 2 | 2      |
# | *=              | x = 4, x *= 2 | 8      |
# | /=              | x = 4, x /= 2 | 2      |
# | **=             | x = 4, x**=2  | 16     |

#%%
float(10)
int(4.6) #round down
round(4.6) #round up
type('Facebook') #string
print("a" * 5) #repeat "a" 5 five
print("a" * 0) #no output
print("a" * -1) #no output

#%%
motto = 'Facebook\'s old motto was "move fast and break things."'
print(motto)

#%% [markdown]
# ## List in Python

#%%
a_list = [] #creating an empty list
row1 = ["Facebook", 0.0, "USA", 2857673, 3.5] #creating a list
row2 = ["Instagram", 0.0, "USA", 2567673, 4.5] #creating a list
data = [row1, row2] #creating a list of lists
first_row = data[0]
first_element_in_first_row = data[0][0] # or `first_row[0]`
last_element_in_first_row = data[0][-1] # or `first_row[-1]`

# %% [markdown]
# ## Data Slicing

#%%
import numpy as np
x = np.arange(10)
x # it is the same as the positive index
#%%
x[0] #the fist element
#%%
x[-1] #the last element
#%%
x[:5] #first five element
#%%
x[:-5] #first five element
#%%
x[5:] #element after index 5
#%%
x[-5:] #last five element
#%%
x[1:5] #from index 1 to index 4
#%%
x[::2] #every other element
#%%
x[1::2] #every other element, starting from index 1
#%%
x[::-1] #all element, reverse
#%%
x[5::-2] #reverse every other element from index 5

# %% [markdown]
# ## How to read file using "reader"
#
# `from csv import reader`
#
# `opened_file = open('AppleStore.csv)`
#
# `read_file = reader()`
#
# `data_set = list(read_file)`

#%% [markdown]
# ## `For` loop in Python
# `for` loop will iterate every element one by one in a list or every row row by row in a data.

#%%
rating = [3,5,1,2]
for element in rating:
    print(element)

#%%
a_list = [1,3,5]
for value in a_list:
    print(value)
    print(value -1)

a_sum = 0
for value in a_list:
    a_sum += value
    print(a_sum)

#%%
list1 = [1, 2]
list1.append(3) #add integer 3 to list1
print(list1)

# %% [markdown]
# ## `If` Statement in Python
# the output of `if` statement return `True` or `False`
#
# | Comparison (text) | Comparison operator | Comparison (code) |
# | ---- | ---- | ---- |
# | `A` is **equal** to `B` | == | `A` == `B` |
# | `A` is **not equal** to `B` | != | `A` != `B` |
# | `A` is **greater** to `B` | > | `A` > `B` |
# | `A` is **greater or equal** to `B` | >= | `A` >= `B` |
# | `A` is **less** to `B` | < | `A` < `B` |
# | `A` is **less or equal** to `B` | <= | `A` <= `B` |

#%%
print("game" == "music")
print("game" != "music")

#%%
if True:
    print(1)

#%%
if True:
    print(2)
    print(3)

#%%
if 3 > 1 and "data" == 'data':
    print("Both conditions are true!")

#%%
if 10 < 20 or 4 <= 5:
    print("At least one condition is true")

#%%
if (20 > 3 and 2 != 1) or "Games" == "Games":
    print("At least one condition is true")

#%%
if False:
    print(1)
else:
    print("The condition above was false")

#%%
if False:
    print(1)
elif 30 > 5:
    print("The condition above was false")

#%%
print(True and True)
print(False and True)
print(True and False)
print(False and False)

#%%
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#%% [markdown]
# ## `Dictionary` in the Python
# The index of a dictionary value is called a **Key**, then a whole `'4+':4433` is a **key-value pair**
#
# **Dictionary key** can be of almost any data type, but lists and dictionaries.
#
# **Dictionary value** can be of any data type: strings, integers, floats, booleans, lists, and dictionaries.
#
# We use the `in` **operator** to check whether a key exists in a dictionary.

#%%
# Frist Way
dictionary1 = {"key_1":1,"key_2":2}
dictionary1["key_1"] #retrieve individual dictionary value

#%%
# Second Way
dictionary2 = {}
dictionary2["key_3"] = 100
dictionary2["key_4"] = 200
dictionary2["key_4"]

#%%
# Check whether a certain value exisit in the dictionary as a key

"key_1" in dictionary2 # output False
"key_3" in dictionary2 # output True
100 in dictionary2 # output False (we can't check value)

#%%
# Updating dictionary value

dictionary3 = {"key_1":100,"key_2":200}
dictionary3["key_1"] += 600 # This will change the value to 700

# %% [markdown]
# To find out the minimum and the maximum values of a column, we can use the `min()` and the `max()` command.

#%%
list1 = {1, 8, 10, 9, 7, 5}

sum1 = 0
for element in list1:
    sum1 += element
print(sum1)

#%%
sum_1 = sum(list1)
print(sum_1)

#%% [markdown]
# ## Creating a function

#%%
def square1(a_number):
    squared_number = a_number * a_number
    return squared_number

#%%
def square2(a_number):
    return a_number * a_number

square2(a_number=6) #a_number is **parameter**; 6 is **argument**

#%%
def add(a, b):
    a_sum = a + b
    return a_sum
add(3,6)

#%%
def freq_table(index, data):
    frequency_table = {}
    for row in data[1:]:
        column = row[index]
        if column in frequency_table:
            frequency_table[column] += 1
        else:
            frequency_table[column] = 1
    return frequency_table

#%%
def sum_or_difference1(a,b):
    a_sum = a + b
    difference = a - b
    return a_sum, difference #the output return as `tuple`

def sum_or_difference2(a,b):
    a_sum = a + b
    difference = a - b
    return [a_sum, difference] #the output return as `list`

#%% [markdown]
# The **tuple** is a data type that is very similar to a list, where is usually used for storing multiple values.

#%%
a_list = [1, 'a', 10.5]
a_tuple1 = (1, 'a', 10.5)
a_tuple2 = 1, 'a'

#%% [markdown]
# **Immutable** data types is a data type where we can't change their state after they've been created.
# **Mutable** data types is a data type where we can change their state after they've been created.
#
# | **Mutable** | **Immutable** |
# | ----- | ---- |
# | Lists | Tuples |
# | Dictionaries | Integers |
# | | Floats | 
# | | Strings | 
# | | Booleans | 

#%%
a_tuple = 1, 2
first_element = a_tuple[0]
second_element = a_tuple[1]

first_element, second_element = a_tuple

#%%
a_list = 1, 2
first_element = a_list[0]
second_element = a_list[1]

first_element, second_element = a_list

#%% [markdown]
# ## Temporary memory in Python
# Below code will follow the function and ignore the main program

#%%
a_sum = 1000
length = 50

def divide1():
    print(a_sum)
    print(length)
    return a_sum / length

result = divide1()
print(result)

#%% [markdown]
# Below code instead will rewrite `a_sum` and `length`, then follow the function

#%%
a_sum = 1000
length = 50

def divide2():
    a_sum = 15
    length = 3
    print(a_sum)
    print(length)
    return a_sum / length

result = divide2()
print(result)