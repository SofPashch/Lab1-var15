a = int(input("Введіть x:"))
b = int(input("Введіть y:"))

def nsd(a,b):
    while a*b!=0:
        if a>=b:
            a=a%b
        else:
            b=b%a
    return a+b

print("НСД цих чисел:")
print(nsd(a,b))

nsk=a*b//nsd(a,b)
print("НСК цих чисел:")
print(nsk)
