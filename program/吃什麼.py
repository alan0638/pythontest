
# coding: utf-8

# In[46]:

import random
x=int(input("幾天呢？"))
while (x!=0):
    x-=1
    a=random.randint(1,10)
    test = {1:"自助餐", 2:"丼太郎",3:"燒臘",4:"四海遊龍",5:"吃土",6:"吃全家",7:"鐵板燒",8:"吃自己",9:"麻辣燙",10:"蔥抓餅"}
    print(test[a])


# In[ ]:



