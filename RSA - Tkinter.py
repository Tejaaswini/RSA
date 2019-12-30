#!/usr/bin/env python
# coding: utf-8

# In[40]:


from tkinter import *
def euclid(a, b):
       
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
 


# In[41]:


def keys_generation(p, q):


    n = p * q
    m = (p - 1) * (q - 1) 
 
    e = int(2)
    """e"""
    while e < m:
        if euclid(e, m) == 1:
            break
        else:
            e = e + 1
     

    """d"""
    w=1
    while(((e*w)%m)!=1):
         w=w+1
         
    d=w
    return [(e, n), (d, n)]


# In[48]:



def rsa():
    global l2
    p= int(a.get())
    q= int(b.get())
    msg= int(c.get())
   
    
    pub_key, pri_key = keys_generation(p, q)
    
    print ('Public Key: ', pub_key)
    print ('Private Key: ', pri_key)
 
    e, n = pub_key
    d, n = pri_key
 
    crypted = (msg ** e) % n
    l2.config(text=crypted)
    return crypted**d % n


# In[49]:



def decryp():
    b=rsa()
    global l3
    original = b
    l3.config(text=original)
    


# In[62]:


root = Tk()    
root.title('RSA')   

l = Label(root,text='Enter First Prime')
l.pack() 

a = Entry(root) 
a.pack()

l = Label(root,text='Enter Second Prime')
l.pack()

b = Entry(root) 
b.pack()

l = Label(root,text='Enter Message (only numbers)')
l.pack()

c = Entry(root)
c.pack()

f2=Frame()
f2.pack(side=TOP)
l2= Label(f2,text='Crypted Msg')
l2.pack(side=LEFT)

l3=Label(f2,text='Decrypted Msg')
l3.pack(side=RIGHT)


# In[63]:



f1=Frame()
f1.pack(side=TOP)
button = Button(f1,text="Encrypt",command=rsa) 
button.pack(side=LEFT)
button2= Button(f1,text="Decrypt",command=decryp)
button2.pack(side=LEFT)
button3= Button(f1,text="More info",command=info)
button3.pack(side=TOP)
root.mainloop()


# In[ ]:




