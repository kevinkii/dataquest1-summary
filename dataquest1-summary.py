# %% [markdown]
#  Python Basic Code

# %%
a_value = 15
a_result = (27-7)*17
print(a_value)
print(a_value+12)
print(a_result + a_value)

# %% [markdown]
# | Snytax Shortcut | Example Code  | Output |
# |-----------------|---------------|--------|
# | +=              | x = 4, x += 2 | 6      |
# | -=              | x = 4, x -= 2 | 2      |
# | *=              | x = 4, x *= 2 | 8      |
# | /=              | x = 4, x /= 2 | 2      |
# | **=             | x = 4, x**=2  | 16     |

# %%
# the `int()` command rounded `4.6` down to `4`
# the `round()` command rounded `4.6` up to `5`
# the string `"Facebook"` or `'Facebook'` is the `str` type
# the integer `2` has the `int` type, and the deciamal number `8.5` has the `float` type

# %%
motto = 'Facebook's old motto was "move fast and break things."'
print(motto)
# it will show the `SyntaxError: invalid syntax`

# %%
motto = 'Facebook\'s old motto was "move fast and break things."'
pritn(motto)

# %% [markdown]
# In python, we have two indexing system for lists:
# * **Positive indexing**: the frist element has he index number 0, the second element has the index number 1, and so on.
# * **Negative indexing**: the last element has the index number -1, the second to last element has the index number -2, and so on.


# %% [markdown]
# ## Data Slicing
# `x[start:stop:step]`
#
# `x[:5]` first five element
#
# `x[5:]` element after index 5
#
# `x[1:5]` from index 1 to index 4
# 
# `x[::2]` every other element
#
# `x[1::2]` every other element, starting from index 1
#
# `x[::-1]` all element, reverse
#
# `x[5::-2]` reverse every other element from index 5

# %% [markdown]
# data_set[0][1] = the second element of the fisrt row in the data_set
#
# create a empty list = `a_list = []`

# %% [markdown]
# ## How to read file using "reader"
#
# `from csv import reader`
#
# `opened_file = open('AppleStore.csv`
#
# `read_file = reader()`
#
# `data_set = list(read_file)`

# %% [markdown]
# ## `For` loop in Python
#
# `for each_list in data_set` mean read every row in the data_set
#
# Once we create a list, we can add (or **append**) values to it using the `append()` command. it has a pattern of `list_name.append()`

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
#
# example of using `if` statement:
#
# if `price  == 0.0`, we appended the string `free` in the list
# * `if price == 0.0:`
#       `app.append("free")`
#
#
# the code within the body of an `elif` clause is executed *only* if:
# * The proceding `if` statement ( or the other proceding `elif` clauses) resolves to `False`; **and**
# * The condition specified after the `elif` keyword evaluates to `True`.
#
# It is also possible the replace the last `elif` clause wiht an `else` clause

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
# To create the dictionary, we use `{}`:
# * Mapped each content rating to its corresponding number by following an `index:value` pattern. For instance, to map a rating of `'4+'` to the number 4,433, we type `'4'+:4433`
# * Typed the entire sequence of `index:value` pairs, and separated each with a comma: `{'4+':4433, '9+':987, '12+':1155, '17+':662}`
# * To get the value of the dictionary, we type `data_set['4+']`
#
#
# To create the dictionary via adding one by one, we:
# * We create an empty dictionary (`{}`) or list (`()`)
# * We add values using the `dictionary_name[index] = value` technique (or the `list_name.append()` command in case of a list)
#
#
# The index of a dictionary value is called a **Key**, then a whole `'4+':4433` is a **key-value pair**
#
# Dictionary key can be of almost any data type, but lists and dictionaries.
#
# Dictionary value can be of any data type: strings, integers, floats, booleans, lists, and dictionaries.
#
# We use the `in` **operator** to check whether a key exists in a dictionary.

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

def square(a_number):
    squared_number = a_number * a_number
    return squared_number

def square(a_number):
    return a_number * a_number

def add(a, b):
    a_sum = a + b
    return a_sum

def freq_table(index, data):
    frequency_table = {}
    for row in data[1:]:
        column = row[index]
        if column in frequency_table:
            frequency_table[column] += 1
        else:
            frequency_table[column] = 1
    return frequency_table

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

def divide():
    print(a_sum)
    print(length)
    return a_sum / length

result = divide()
print(result)

#%% [markdown]
# Below code instead will rewrite `a_sum` and `length`, then follow the function

#%%
a_sum = 1000
length = 50

def divide():
    a_sum = 15
    length = 3
    print(a_sum)
    print(length)
    return a_sum / length

result = divide()
print(result)