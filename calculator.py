
# coding: utf-8

# In[3]:

#a caclulator created exclusevely with functions.

def calculator(a,b):
    a=float(input('Enter the number one:\n'))
    b=float(input('Enter,the number two:\n'))
    #functions to sums
    def sums(a,b):
        s=a+b
        return s
    

    #Functions to rest

    def rest(a,b):
        r=a-b
        return r
    

    #functions to multiply

    def mult(a,b):
        m=a*b
        return m
    


    #Functions to Divide
    def div(a,b):
        d=a/b
        return d
    
    def choose():
        if a >0 and b>0:
            
            sel=input('Please Select your operation,\nS for Sums,\nR for Rest,\nM for Multiply and\nD for Division :\n').lower()

            if sel == 's':

                print (sums(a,b))

            elif sel == 'r':

                print (rest(a,b))

            elif sel =='m':

                print( mult(a,b))

            elif sel =='d':

                print( div(a,b))
            else:
                print('Sorry, I cannot Calculate that operation!!')
    return choose()

print(calculator(a=0,b=0))       
    


# In[ ]:



