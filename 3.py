a=[]
n=int(input("Введіть розмір масиву:"))
print("Введіть елементи масиву:")
for i in range(n):
    a.append(int(input()))
print("Масив:")
print(a)
answer = 1

print("Мінімальний елемент:")
print(min(a))

print("Ненульові непарні елементи масиву:")
for i in range(len(a)):
    if(a[i]>0 and a[i]%2>0):
        print(a[i])
        answer *= a[i]

print("Їх добуток:")
print(answer)

a.reverse()
print("Масив у зворотньому порядку:")
print(a)
