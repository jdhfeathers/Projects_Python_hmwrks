
# coding: utf-8

# In[4]:

import time
from time import sleep
from overprint import overprint
from colored import fg,bg,attr

'''
Declaring the object bar
'''


class Bar:
    #initilizing the Class
    
    def __init__(self,symbol=' ',t=1):
        self.symbol=symbol
        self.t=t
    
    #M e t h o d s
    
    def prn_m(self):
        with overprint() as (reprint,print):
            print(bg(68))
            while self.t <=10:
                reprint(self.symbol*self.t*2)
                time.sleep(.5)
                self.t+=+1
            return 'Ready!!'

b=Bar()
print(b.prn_m())


# In[ ]:



