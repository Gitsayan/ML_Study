# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,14]
x.sort()

y = [3,6,4,7,8,9,11,13,14,13,19,24]
y.sort()

plt.hist(x,y)
plt.show()

df1 = pd.DataFrame(x)
df1.head()

names= ["sayan mondal","ajay Das","nirmal Roy","Vikram sarabhai","nabanita Das"]
df2=pd.DataFrame(names)

df2["First Name"]=df2[0].apply(lambda x: "Mr. " + x.split(" ")[0])
df2["Last Name"]=df2[0].apply(lambda x: x.split(" ")[1])


mytable ={'roll' : [1,2,3,4,5],
          'Subject' : ["phy","chem","Math","hist","Eng"]
          }

df3= pd.DataFrame(mytable)

