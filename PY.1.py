# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZIS9VWmBsQr85JVq_OacrTcm7E3z_Hx4
"""

a=150
b=400
if a<b:
  print("hello world")
else:
  print("hai")

a=55
b=55
if a>b:
  print("hai")
elif a>b:
  print("hello")
else:
  print("hiiii")

a=50
b=65
c=40
if a>b and a>c:
  print("a is greater")
elif b>a and b>c:
  print("b is greater")
else:
  print("c is greater")



i=0
while i<10:
   i+=1
   if i==3:
    break
   print(i)

i=0
while i<10:
   i+=1
   if i==3:
    continue
   print(i)

i=1
while i<10:
  i=i+1
  print(i)

for i in range(10,50,5):
  print(i)

for i in range(10,1,-1):
  print(i)

a=["apple","mango","banana","cherry"]
for i in a:
  print(i)

a=[19,5,5,5,19]
if a.count(19)==2 and a.count(5)==3:
     print("true")
else:
    print("false")

a=[19,5,5,5,14,3]
if a.count(19)==2 and a.count(5)==3:
     print("true")
else:
    print("false")

for i in range(1,50,2):
  print(i)

b=[]
a=int(input("enter a number"))
for i in range(1,a,2):
  b.append(i)
print(b)

a=[]
for i in range(12,101):
  if i%12==0:
    a.append(i)
print(a)
b=[]
for j in a:
   if j%14==0:
     b.append(j)

print(b)



a=[]
b=[]
for i in range(1,101):
  if i%2!=0:
    a.append(i)
  else:
    b.append(i)
print(a)
print(b)

a=["sana","hiba","sahla","mubi"]
b=["a12","b12","c12","d12"]
c=input("enter your username")
for i in a:
   if index[a[0]]!=b[ind[0]]:
     print("incorrect username")
   else:
          d=input("enter password")
for i in b:
   if a.ind(0)!=b.ind(0):
     print("invalid password")
   else:
     print("welcome")

a=["sana","hiba","sahla","mubi"]
b=[112,212,312,412]
c=input("enter your username")
for i in a:
  if c == i:
    d=int(input("enter your password"))
    for j in b:
      if d == j:
       print(" welcome")
      else:
       print("incorrect password")
  else:
   print("incorrect username")

a=["sana","hiba","sahla","mubi"]
b=[112,212,312,412]
c=input("enter your username")
d=int(input("enter your password"))
for i in a:
  if c==i:
    print("incorrect username")
    
    for j in b:
      if d==j:
       print(" welcome")
      else:
       print("incorrect password")
  else:
    print("incorrect username")

a=["sana","hiba","sahla","mubi"]
b=[112,212,312,412]
c=input("enter your username")
d=int(input("enter your password"))
for i in a:
  for j in b:
   if c == i and d == j:
     print(" welcome")
   elif d!=j:
       print("incorrect password")
   else:
    print("incorrect username")

a=["sana","hiba","sahla","mubi"]
b=[112,212,312,412]
username=input("enter your username")
if username in a:
  ind=a.index(username)
  password=int(input("enter your password")
  if password in b and ind==b.index(password):
    print("welcome")
  else:
    print("invalid password")
else:
  print("invalid username")