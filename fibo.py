def fibo(n : int):
    if n == 1: return 0
    if n == 2: return 1
    return fibo(n-1)+fibo(n-2)

#main
nterm = 5
print("Fibonacci term: ",fibo(nterm))