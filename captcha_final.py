
# coding: utf-8

# In[ ]:

'''
creating the structure for a captcha
'''
#global info
abc='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
lst=[]
catcha=[]
#wrt=[]
#Modules
import random
from colorama import Fore
import colored
from colored import stylize
from colored import fg,bg,attr





# This function is to create the elements that most be iterate for captcha
def lists():
    for e in abc:
        lst.append(e)
    for e in num:
        lst.append(e)   
    return lst

#print(lists())

#this function is to create  catch
#this are the elementss that I will ask for
def catpcha(n):
    lists()
    for n in range(0,n):
        catcha.append(random.choice(lst))
    return (catcha)
    
#this function is to return 5 elements in the list
def cathc_m():
    return(catpcha(5))  
#print (cathc_m())



#this function is to create a list input elements
def writecatch():
    wrt=list(input('please enter the secuence:\n'))
    return wrt
#print(writecatch())



#to verify that the list are equal
def last():
    c=cathc_m()
    print(Fore.BLUE)
    print(bg(109))
    x=print(c[0]+c[1]+c[2]+c[3]+c[4])
    print(stylize('{}'.format(x),colored.attr('underlined')))
    #print(z)
    print(Fore.BLACK)
    z=writecatch()
    if c==z:
        return ('\nwelcome')
    elif c!=z:
        return('Invalid Captcha')
    else:
        return('Sorry, try it later')

print(last())


# In[ ]:

print(stylize('{}'.format(num),colored.attr('underlined')))


# In[ ]:

ls=['1','b','4']
print(ls[0]+ls[1]+ls[2]+ls[3]+ls[4])


# In[ ]:



