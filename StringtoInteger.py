str="1234"
result,factor=0,1
for i in reversed(str):
    result+=int(i)*factor
    factor*=10
print(result)