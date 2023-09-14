#1
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
#2
# лінія 20 * кожна 3-я = 
ans = ''
for i in range(1,21):
    s = '*'
    if i % 3 == 0:
        s = '='
    ans = ans + s

print(ans)
#3
# піраміда
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5 
size = int(input("Введіть розмір піраміди = "))
for i in range(0,size):
    for j in range(size-i,size+1):
        print(j, end =" ")
    print()