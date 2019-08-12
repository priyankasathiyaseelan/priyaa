#p
from collections import Counter     
string="kabali"

n=int(input())                      
values=[]
count=0
if  n>=1 and n<=1000:                
    for i in range(n):
        values.append((input()))

for val in values:
    if Counter(val)==Counter(string):     
        count=count+1
print(count)
