#%% [markdown]
#  Python Basic Code

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
# the `int()` command rounded `4.6` down to `4`
# the `round()` command rounded `4.6` up to `5`
# the string `"Facebook"` or `'Facebook'` is the `str` type
# the integer `2` has the `int` type, and the deciamal number `8.5` has the `float` type

#%%
motto = 'Facebook's old motto was "move fast and break things."'
print(motto)
# it will show the `SyntaxError: invalid syntax`

#%%
motto = 'Facebook\'s old motto was "move fast and break things."'
pritn(motto)

#%% [markdown]
# In python, we have two indexing system for lists:
# * **Positive indexing**: the frist element has he index number 0, the second element has the index number 1, and so on.
# * **Negative indexing**: the last element has the index number -1, the second to last element has the index number -2, and so on.


#%% [markdown]
# `a_list[m:n]`, where
# * `m` represents the index number of the first element
# * `n` represents the index number of the last element + 1
#
#
# `a_list[:x]` when we want to select the first `x` elements.
#
# `a_list[-x:]` when we want to select the last `x` elements.

#%% [markdown]
# data_set[0][1] = the second element of the fisrt row in the data_set

#%% [markdown]
# ## How to read file using "reader"
#
# `from csv import reader`
#
# `read_file = reader()`
#
# `data_set = list(read_file)`

#%% [markdown]
# ## `For` loop in Python
#
# `for each_list in data_set` mean read every row in the data_set
#
# Once we create a list, we can add (or **append**) values to it using the `append()` command. it has a pattern of `list_name.append()`

#%%
