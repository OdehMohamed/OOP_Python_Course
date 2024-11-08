## Slice------------

# name="mohamed"
# print(name[:]) # print(name)
# print(name[2:5]) # ham
# print(name[:2]) # mo
# print(name[3:]) # amed
# print(name[::]) # mohamed
# print(name[::2]) # mhmd
# print(name[3:6:3]) # a
# print(name[2::2]) # hmd

# ls=[1,3,4,5,"ahmed"]
# print(ls[:2:])
# print(ls[::2])

# tp=(1,2,3,4)
# print(tp[1:3:2])

# s={1,2,3,4,5,6,7,8}
# print(s[::]) # Error

# email =input("enter your email : ")
# indx=email.index("@")
# userName=email[:indx:]
# domain=email[indx+1:]
# print(userName)
# print(domain)

## -------------------------------

## assignment operators ----------------
# x=x+y  => x+=y
# x=x-y  => x-=y
# x=x*y  => x*=y
# x=x/y  => x/=y
# x=x**y  => x**=y
# x=x//y  => x//=y
##---------------
# print(5/2) # 2.5
# print(5//2) # 2

## comparios Operators ------------
# > , >=
# ==
# <, <=
# !=
## --------------------------------
# print(10>100)
# print(10<100)
# print(10>=100)
# print(10<=100)
# print(10==100)
# print(10!=100)


## Boolean Operators ------------

# and
## T and T = T
## T and F = F
## F and T = F
## F and F = F

# or
## T or T = T
## T or F = T
## F or T = T
## F or F = F

# not
## not F = T
## not T = F
## --------------------------------
# x=5
# y=100
# #     F   and F
# print(x>y and y<x) # F

# #      T   and  T
# print(x==5 and x<y) # T

# #      T   or  F
# print(x==5 or x>y) # T

# #      T   Or  T  and  F    and   T
# print(x==5 or x<y and y>100 and not x==y) # T


## control Flow ---------------
# if
# elif
# else
## ------------------------------

# x=input("the value of x : ")
# y=input("the value of y : ")

# if x>y:
#   print("x > y")
# elif x<y:
#   print("x < y")
# else:
#   print("x = y")

## membership operators -------------
# in
# not in
## ----------------------------------

# ls =[1,2,3,4,"jjs"]
# print(5 not in ls)
# userNames=['mohamed','ahmed','fadi','khaled']
# name=input("enter your name : ")

# if name not in userNames:
#   print("in the list")
# else:
#   print("not in the list")
