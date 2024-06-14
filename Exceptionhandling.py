#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    print(a+b)
except:
    print('Error')


# In[2]:


try:
    file = open('file.txt',x)
    file.close()
except:
    print("The file already exist")


# In[4]:


try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    print(a/b)
except ValueError:
    print("Enter only int Value!")
except ZeroDivisionError:
    print("Value of b cannot be zero")
    


# In[2]:


try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    c= a/b
    
except ValueError:
    print("Enter only int Value!")
except ZeroDivisionError:
    print("Value of b cannot be zero")
else:
    print(c)


# In[3]:


# assert statement


# In[5]:


age = int(input("Enter age = "))
age >=20


# In[9]:


try:
    age = int(input("Enter age = "))
    assert age>=20
except:
    print("YOU ARE UNDER 20")
else:
    print("WELCOME")


# In[11]:


username = "admin"
password = "admin"
try:
    username1 = input("Enter username = ")
    password1 = input("Enter password = ")
    assert username==username1 and password == password1
except AssertionError:
    print("INVALID USERNAME or PASSWORD")
else:
    print("Login sucessful")


# In[18]:


c = 1
username = "admin"
password = "admin"
def login():
    global c
    try:
        username1 = input("Enter username = ")
        password1 = input("Enter password = ")
        assert username==username1 and password == password1
    except AssertionError:
        print("INVALID USERNAME or PASSWORD")
        c = c+1
        login()
    else:
        print(f"Login sucessful! in {c} attempt")
login()


# In[ ]:





# In[ ]:




