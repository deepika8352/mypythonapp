# a=10
# b,c=20,30
# d=e=f=40
# print(a,b)
# print(b)
# print(c)
# print(d,e,f)
# a=int(input("Enter a value"))
# b=int(input("Enter b value"))
# print(a)
# print(a+b)
# d,e,f=map(int,input("Enter d and e,f ").split())
# print(e)
# age=18
# if age>18:
#     print("Eligible")
# elif age==18:
#     print("Welcome new voter")
# else:
#     print("Not Eligible")

n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
list2=[x for x in range(n) if x%2==0]
print(list2)