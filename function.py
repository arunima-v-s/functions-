# function

# def hi():
#     print("hi")
# hi()

# def message(name):
#     print("hi "+name)
# message("arunima")

# def sum():
#     a=int(input("frst no "))
#     b=int(input("secnd no "))
#     print(a+b)
# sum()

# def sum(b):
#     print(int(input("frst no"))+b)
# sum(int(input("secnd no")))


# def sum(a,b):
#     print(a+b)
# sum(int(input("frst no")),int(input("second no")))


# def square(n):
#     print(n*n)
# square(int(input("enter no")))


# def mult(a):
#     b=int(input("enter limit"))
#     for i in range(1,b):
#         c=i*a
#         print(f"{i}*{a}={c}")
# mult(int(input("enetr no to multiply ")))


# def fibonacci(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,x):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibonacci(int(input("enter limit")))


#factorial

# def factorial(n):
#     factorial=1
#     if n<0:
#         print("no factorial")
#     elif n==0 or n==1:
#         print("factorial is 1")
#     else:
#         for i in range(2,n+1):
#             factorial=factorial*i
#         print(factorial)
# factorial(int(input("enter limit")))


# def palindrome(a):
#     b=a[::-1]
#     if b==a:
#         print("its a palindrome")
#     else:
#         print("not a palindrome")
# palindrome(input("enter string ").lower())


# RECURSION

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(int(input("enter no "))))


# def fibonacci(n):
#     if n<=1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(0,int(input("enter limit"))):




# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# num_terms=10
# for i in range(num_terms):
#     print(fibonacci(i), end="")
