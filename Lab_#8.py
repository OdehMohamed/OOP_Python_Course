## Loop


## WHILE
# x=0
# while x <= 10:
#   print(x)
#   x+=1;
# else:
#   print("True become False")

## FOR
# len = range(5,15)
# for x in len:
#   print(x)

ls = [1,2,3,4,5,6,7]
# for e in ls:
#   x = e*2
#   print(x)

## break
# for e in ls:
#   print(e)
#   if(e == 4):
#     break

## continue
# for e in ls:
#   if(e == 4):
#     continue
#   print(e)

## pass
# for e in ls:
#   if(e == 4):
#     pass
#   print(4)

dic={
    "mohamed":"60%",
    "ahmed":"50%",
    "khaled":"70%"
}
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# for i in dic:
#   # print(f"{i} => {dic[i]}")
#   print(f"{i} => {dic.get(i)}")

dic2={
    "mohamed":{
        "age":25,
        "city":"cairo"
    },
    "ahmed":{
        "age":30,
        "city":"alexandria"
    },
    "khaled":{
        "age":28,
        "city":"cairo"
    },
    "ali":{
        "age":32,
        "city":"alexandria"
    }
}
# print(dic2)
# print(dic2.keys())
# print(dic2.values())

# for i in dic2:
#     print(f"key : {i}, value : ")
#     for j in dic2.get(i):
#         print(f"-- {j} => {dic2[i][j]}")

# ls = [1,2,3,4,5,6,7,8,9,10]
# for i in ls[3:7:2]:
#     print(i)

# cnt =1
# ls =["mohamed",123,-2*2j,1.5]
# for i in ls:
#     print(type(i))
#     if type(i) is str:
#         print(f"the {cnt} element is String")
#     elif type(i) is int:
#         print(f"the {cnt} element is integer")
#     elif type(i) is complex:
#         print(f"the {cnt} element is complex")
#     elif type(i) is float:
#         print(f"the {cnt} element is float")
#     cnt+=1

## set
# s ={1,"sdfds",3,5.5,5}
# for i in s:
#     print(i)   

## Tuple
# t =(1,2,3,4,5)
# for i in t:
#     print(i)   