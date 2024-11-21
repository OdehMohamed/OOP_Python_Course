
## ----------------------------------------------------------------------------
# def say_hello(fname,mname,lname):
#     print(f"hello {fname.upper()} {mname[:1].capitalize()} {lname.lower()}")


# say_hello("ahmed","mohamed","fadi")
# # hello ahmed mohamed fadi
# # hello Ahmed M Fadi
# # hello AHMED M FADI
# # hello AHMED M fadi
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------

# def sum(num1,num2):
#     return num1+num2
# print(sum(1,2))

## ----------------------------------------------------------------------------
## ----------------------------------------------------------------------------

def sumTheList(elements):
    sum=0
    for i in elements:
        sum+=i
    return sum

def checkOddOREven(elements):
    for i in elements:
        if(i%2==0):
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")

ls=[1,10,4,5,2,9]

# print(sumTheList(ls))
# checkOddOREven(ls)

## ----------------------------------------------------------------------------



## ----------------------------------------------------------------------------
## packing,unpacking
# (*) tuple , (**) dic
## ----------------------------------------------------------------------------

## ----------------------------------------------------------------------------
### Unpacking
## ----------------------------------------------------------------------------
# def sum(num,num2,num3):
#     print(num+num2+num3)

# ls =[1,5,6,7]
# print(ls)

# sum(*ls)
# sum(ls[0],ls[1],ls[2],ls[3])

## ----------------------------------------------------------------------------
## Packing
## ----------------------------------------------------------------------------
# def sum(*nums):
#     print(type(nums))
#     sum=0
#     for i in nums:
#         sum+=i
#     return sum

# print(sum(2,3))

def fun(**dic):
    print(dic)

d={
    "mohamed":90,
    "ahmed":88,
    "khaled":43,
    "fadi":66,
}

# fun(mohamed="90%",ahmed="88%",khaled="43%")

## ----------------------------------------------------------------------------
############################# Error
# def fun2(n,m,c,v):
#     print(n,m,c,v)

# # print(**d)
# fun2(**d)

# # def fun(a, b, c):
# #     print(a, b, c)

# # # A call with unpacking of dictionary
# # d = {'a':2, 'b':4, 'c':10}
# # fun(**d)
## ----------------------------------------------------------------------------