#recursion means a function call itself
def countdown(n):
    if n==0:            # This is called the base case.

                         # Without a base case, the function would keep calling itself forever.
        return
    print(n)
    countdown(n-1)   # recursive call which fuction call itself
countdown(10)
