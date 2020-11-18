# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:40:44 2020

@author: admin
"""



#apply
#Map
#Reduce
#filter




mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


#Map....................................................................
print('\nMap.........................\n')
x = list(map(lambda x: x*x, mylist))
y = tuple(map(lambda x: x*x, mylist))



#Filter....................................................................
print('\nFilter......................\n')
myodd = list(filter(lambda x: x%2==1 , mylist))
print(myodd)


#Reduce....................................................................
import functools as fnt
print('\nReduce......................\n')
newlist = fnt.reduce(lambda x,y: x+y,mylist)
print(newlist)
#print(fnt.reduce(lambda x,y: x+y, [i for i in mylist if i%2==1]))
#print(fnt.reduce(lambda x,y: x+y, [i for i in mylist if i%2==0]))



#List Comprehention....................................................................
print('\nList Comprehentio................\n')
odder = [i for i in mylist if i%2==1]
print(odder)
evener = [i for i in mylist if i%2==0]
print(evener)




