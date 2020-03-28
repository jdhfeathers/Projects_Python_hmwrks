
# coding: utf-8

# In[1]:

import time
import datetime
from collections import namedtuple
from time import sleep

'''
just second watch
'''

h=15
m=26
s=33

wtch=namedtuple('wtch','hour')
tm=wtch(hour=datetime.time(h,m,s))

#print statemts to verify
print(tm.hour)
print(tm.hour.minute)
print(tm.hour.second)

def secndr():

    h=15
    m=28
    s=1

    wtch=namedtuple('wtch','hour')
    tm=wtch(hour=datetime.time(h,m,s))
    
    for hour in tm:
        while tm.hour.second<60:
            if tm.hour.second == 59:
                if tm.hour.hour == 23 and tm.hour.minute ==59 and tm.hour.second == 59:
                    s=0
                    m=0
                    h=0
                    tm=wtch(hour=datetime.time(h,m,s))
                    print(tm.hour,'end')
                    #break
                if tm.hour.second == 59 and tm.hour.minute == 59:
                    s=0
                    m=0
                    h=h+1
                    tm=wtch(hour=datetime.time(h,m,s))
                    print(tm.hour,'done')
                    #break
                else:
                    s=0
                    m=m+1
                    tm=wtch(hour=datetime.time(h,m,s))
                    time.sleep(1)
                    print(tm.hour,'done')
                    break     #this is to stop it after one minute should not suppose to happend but for teaser is necesary
            else:
                s=s+1
                tm=wtch(hour=datetime.time(h,m,s))
                time.sleep(1)
                print(tm.hour)
            continue
print(secndr())


# In[ ]:



