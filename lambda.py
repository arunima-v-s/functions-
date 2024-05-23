# syntax of lamda
# lambda arguments:expression

# add=lambda x,y:x+y
# print(add(2,8))

# a=[1,2,3,4,5]
# x=list(map(lambda x:x*2,a))
# print(x)


#1

# a=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda x:x%2==1,a))
# print("odd numbers")
# print(x)
# y=list(filter(lambda y:y%2==0,a))
# print("even numbers")
# print(y)


#2

# a=[1,2,3,4,5,6,7,8,9,10]
# x=list(map(lambda x:x*x,a))
# print("square")
# print(x)
# y=list(map(lambda y:y*y*y,a))
# print("cube")
# print(y)


#3

# fibonacci=lambda n:[0,1] if n==2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]
# n=int(input("enter number"))
# print(fibonacci(n))


#4

# a=[1,2,3,4,5,6,7,8,9,10]
# count_no=lambda x: {y:x.count(y) for y in set(x)}
# output=count_no(a)
# print(output)



# a=[1,2,3,5,7,8,9,10]
# count_even=len(list(filter(lambda x:x%2==0,a)))
# count_odd=len(list(filter(lambda x:x%2==1,a)))
# print("number of even numbers in the list: ",count_even)
# print("number of odd numbers in the list: ",count_odd)


#5

# a=[2,4,6,9,11]
# x=list(map(lambda x:x*2,a))
# print(x)


#6

# a=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# numeric=sorted(list(map(lambda x:int(x),a)))
# print(numeric)


#7

a=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
count_no=lambda x: {y:x.count(y) for y in set(x)}
output=count_no(a)
print(output)