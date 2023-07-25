#!/usr/bin/env python
# coding: utf-8

# # Q1. How do you comment code in Python? What are the different types of comments?

# In[1]:


""""In Python, We can add comments to your code to make it more readable and to explain the purpose or functionality of specific
lines or blocks of code. Comments are ignored by the Python interpreter and are meant for human understanding only."""

# the above line is multi line comment


# In[2]:


# There are two types of comments in Python:


# In[3]:


# 1:- Single-line comments: These are comments that span only a single line and start with the "#" symbol.


# In[4]:


# This is a single Line Comment

print("pankaj")


# In[5]:


# 2- Multi-Line Comments: In Multi-Line we can comments multiple line with the help of triple quotes (""" or ''')



# In[6]:


""""this is Multi-Line Comment
    we can write multiple line in the triple quotes 
    this line will not print"""
print("pankaj")


# # Q2. What are variables in Python? How do you declare and assign values to variables?

# In[7]:


"""In Python variable are used to store the values or we can say that 
A variable is a string of characters and numbers associated with a piece of information. 
The assignment operator, denoted by the “=” symbol, is the operator that is used to assign values to variables in Python."""

# we can assign different type of value into the variable
name = "Joker"
age = 25
height = 5.11
print(name)
print(age)
print(height)



# # Q3. How do you convert one data type to another in Python?

# In[8]:


""" In Python, We can convert one data type to another data type using type conversion functions or constructors.
    Python provides built-in functions to convert between various data types"""

# lets takes some example....
# 1 int() convert any value to int

float_number = 3.14
integer_number = int(float_number)
print(integer_number) 


# In[9]:


#2 float
integer_number = 314
float_number = float(integer_number)
print(float_number) 


# # Q4. How do you write and execute a Python script from the command line?

# In[10]:


""" The most basic and easy way to run a Python script is by using the python command.
You need to open a command line and type the word python followed by the path to your script file like this: 
python first_script.py 
Hello World! 
Then you hit the ENTER button from the keyboard, and that's it."""


# # Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[11]:


my_list=[1,2,3,4,5]


# In[12]:


my_list


# In[13]:


my_list[1:3]


# # Q6. What is a complex number in mathematics, and how is it represented in Python?

# In[14]:


""" the number that contain both real part and imaginary part in the number is called complex number"""

a= 3+4j
print(a)


# In[15]:


type(a)


# # Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[16]:


# The correct way to declare a variable named age and assign the value 25 to it in Python is as follows:
age = 25
print(age)


# # Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?

# In[17]:


price = 9.99
print(price)
print(type(price))


# # Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?

# In[18]:


name = "pankaj gangwar"
print(name)

#The print() function displays the value of the variable name on the console, allowing you to see the full name stored in the name variable.


# # Q10. Given the string "Hello, World!", extract the substring "World".

# In[19]:


string = "Hello, World!"
substring = string[7:12]
print(substring)


# # Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not

# In[20]:


is_student = True


# In[21]:


is_student

