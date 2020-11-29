#!/usr/bin/env python
# coding: utf-8

# In[7]:


def change_list():
    l=[int(x) for x in input().split()]
    print(l)
    l1=[]
    i=int(input("Enter the number of elements you want to change: "))
    for k in range(i):
        f=int(input("Enter the element: "))
        l1.append(f)
    print("New list: ",l1)

