# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:53:11 2021

@author: user
"""
#作業一
import random
number=[ ]
while True :
    b=random.randint(1,50)
    if len(number)>5:
        break    
    if  number.count(b)==0:     
        number.append(b)
number2=sorted(number)
print(number)
print("遞增排序",number2)


#作業2
import random
data=[ ]
for i in range(0,7):
    a=random.randint(1,101)
    data.append(a)
data.sort( )             
print("遞增排序:",data)
count=0
while True and len(data)>0:
    print(data)
    num=int(input("請輸入串列中的值:"))        
    min_index=0
    max_index=len(data)-1
    mid_index=(min_index+max_index)//2        
    count+=1     
    if num not in data:
        print("此數不在串列")
        break
    elif num< data[mid_index]:
        del data[mid_index:]
    
    elif num> data[mid_index]:
        del data[:mid_index+1]
    else:
         print("次數為:",count)
         break       
print("程式結束")  


#作業三 
a=int(input("請輸入獲利金額:"))
if   a<=100000 :

    print("獲利:%d,獎金:%d" % (a,a*0.1))
elif a<=200000:
    print("獲利:%d,獎金:%d" % (a,100000*0.1+(a-100000)*0.07))
elif a<=400000:
    print("獲利:%d,獎金:%d" % (a,100000*0.1+10000*0.07+(a-200000)*0.03))
else:
    print("輸入錯誤")
                
        