# ## packing , unpacking

# ## [1,2,3,4,5]
# ## 1 2 3 4 5

# ## 1 2 3 4 5
# ## (1,2,3,4,5)

# ## packing
# def sumItems(*nums):
#     ## return sum of values
#     sum=0
#     for i in nums:
#         sum+=i
#     return sum

# ##print(sumItems(3,4,5,6,7,10,11))


# def sumTwoValue(n1,n2):
#   return n1+n2

# ##print(sumTwoValue(1,2))

# ls=[1,7]
# ##print(sumTwoValue(ls[0],ls[1]))
# #print(sumTwoValue(*ls))

# def outputDetails(**dic):
#   for key in dic:
#     print(f"{key} => {dic[key]}")

# #outputDetails(cpp = "90%" ,js = "88%" ,dart = "70%", python = "50%")

# dic={
#     "cpp" : "90%" ,
#     "js" : "88%" ,
#     "dart" : "70%",
#     "python" : "50%"
# }

# def outputDetails(**dic):
#   for key in dic:
#     print(f"{key} => {dic[key]}")


# ## outputDetails(**dic)
# outputDetails(cpp = "90%" ,js = "88%" ,dart = "70%", python = "50%")


# def sumTwoValue(n1=0,n2 = 0):
#   return n1+n2

# print(sumTwoValue(2,9))

##x = 0


class Employee:
    def __init__(self,name,age,salary):
      self.name=name
      self.age=age
      self.salary=salary

    def printDetails(self):
      print(f"your name is : {self.name}, and age : {self.age}, and salary : {self.salary}")

    def getponus(self):
      if(self.age>30):
        self.salary+=500

ob1=Employee("ahmed",33,2500)
# ob1.printDetails()
# ob1.getponus()
# ob1.printDetails()


print(dir(str))
print(dir(list))
print("".__class__)
