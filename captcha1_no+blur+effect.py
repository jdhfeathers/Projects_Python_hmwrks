
# coding: utf-8

# In[1]:

'''
creating the structure for a captcha
'''
#global info
abc='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
lst=[]
catcha=[]

import random

def lists():
    for e in abc:
        lst.append(e)
    for e in num:
        lst.append(e)   
    return lst

def catpcha(n):
    lists()
    for n in range(0,n):
        catcha.append(random.choice(lst))
    return (catcha)
    

def cathc_m():
    return(catpcha(5))  


def writecatch():
    wrt=list(input('please enter the secuence:\n'))
    return wrt


def last():
    c=cathc_m()
    print(c)
    z=writecatch()
    if c==z:
        print ('ok, welcome')
    elif c!=z:
        print('Invalid Captcha')
    else:
        print('Sorry, try it later')

print(last())


# In[ ]:



