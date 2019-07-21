
def factorial(n):
    product_sum=1
    for i in range(n):
        product_sum*=n
        n=n-1
    print(product_sum)

factorial(3)