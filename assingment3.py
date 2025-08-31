n=int(5)
def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
result=factorial(n)
print('Enter a number:',n)
print('factorial of',n,'is',result)
