import math

x=int (input("Введіть x:"))
y=int (input("Введіть y:"))
print("\n")

z= math.cos(x)**2+math.sin(y)**2+((1/4)*math.sin(2*x)**2)-1

print("Відповідь:")
print(z)