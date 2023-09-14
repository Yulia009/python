# 2*a + b  a > b
# -2 a == b 
# (a-5) /  b   a < b 

a = int(input("Введіть а = "))
b = int(input("Введіть b = "))

if a > b:
    ans = 2 * a + b
if a == b:
    ans = -2
if a < b:
    ans = (a-5) / b

print("Результат обчислення виразу", ans)