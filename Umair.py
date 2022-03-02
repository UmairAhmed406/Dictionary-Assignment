#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1
number_of_products = eval(input("Enter Number of products: "))
dictionary ={}
for i in range(number_of_products):
    name_of_product = input("Please Enter Name of Products: ")
    price_of_product = int(input("Please Enter Price of Products: "))
    dictionary[name_of_product] = price_of_product


while True:
    name_of_product = input("Please Enter Name of product you want to get price of : ")
    if name_of_product in dictionary:
        print("The price for your product is ", dictionary[name_of_product])

    else:
        print("This product is not found in dictionary")


print(dictionary)


# In[ ]:


#Question No 2
number_of_products = eval(input("Enter Number of products: "))
dictionary ={}
for i in range(number_of_products):
    name_of_product = input("Please Enter Name of Products: ")
    price_of_product = int(input("Please Enter Price of Products: "))
    dictionary[name_of_product] = price_of_product
print(dictionary)
var1 =eval(input("Enter Amount in Dollars : "))
for key ,values in dictionary.items():
    if  int(values) < var1:
        print (key ,"->",values)


# In[3]:


# Question 3
import operator
year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

#a
name_of_month = input("Enter Name of a month: ")
for key, values in year.items():
     if name_of_month == key:
        print( values)
        break





#c
for keys,values in year.items():
    if int(values) == 31:
        print(keys)
sorted_bymonthdays = dict(sorted(year.items(),key= operator.itemgetter(1)))
print(sorted_bymonthdays)


# In[8]:


#Question 3 (b)
import operator
year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}
rearranged ={key:year[key] for key in sorted(year)}
print(rearranged.keys())


# In[11]:


#Question 3 (c)
import operator
year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}
for keys,values in year.items():
    if int(values) == 31:
      print(keys)


# In[ ]:


# Question 4
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")
x = input("Enter Username: ")    
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))


# In[10]:


# Question 6
def teamInfo():
   number_Of_teams = int(input("Enter Number Of Teams: "))
   team_dictionary={}
   for team in range(number_Of_teams):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dictionary.update({key:value})
       
   return team_dictionary

print(teamInfo())


# In[ ]:




