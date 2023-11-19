def fib(n):
    if n==0:
        return 0
    elif n==1:
        fib=[0]
    elif n>2:
        fib=[0,1]
        for i in range(1,n-1):
            fib.append(fib[i]+fib[i-1])

    return fib

num=int(input("Enter number"))
fibonacci=fib(num)
print(fibonacci)


