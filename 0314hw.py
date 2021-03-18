# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:18:33 2021

@author: user
"""
#作業一
for c in range(2,6):
    
    for a in range (0,c):
        print("*",end="")
    print( )  

print("="*50)
#作業二
a=int(input("請輸入一個大於0的整數"))
for b in range(1,a+1):
    if b %4==0:
        print(b,"是4的倍數")
d=2
for d in range(2,a):
    e=2
    for e in range(2,d):
        if d%e==0:
            break
            
    else:
        print(d,"是質數")
#作業三
import random
lowest=1
highest=100
ans=random.randint(lowest,highest)
print("請輸入1-100之間的整數")
guess=0
count=0
while True  and count<5 : 
    guess=int(input("輸入猜數"))
    if guess> ans:
       highest=guess
       print("請輸入"+str(lowest)+"-"+str(highest)+'之間的整數')
    elif guess<ans:
        lowest=guess
        print("請輸入"+str(lowest)+"-"+str(highest)+'之間的整數')
    else:
        print("猜對了")
        break
    count+=1
else:
    print("猜錯5次,請離開!")
    
    

            
       
    
         
 
    
    
    
        