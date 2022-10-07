s1 = input()
gl = ['а', 'о', 'я', 'у', 'ю', 'е', 'ё', 'э', 'ы', 'и']
sogl = 'йцкнгшщзхъждлрпвфчсмтьб'
n = len(s1)
k1 = 0
k2 = 0
k3 = 0
p = " "
for i in range(n):
    c = 0
    for j in range(10):
        if s1[i] == gl[j]:
            k1 = k1 + 1
            c = 1
    if c == 0:
        for y in range(23):
            if s1[i] == sogl[y]:
                k2 = k2 + 1
if k1 == k2:
    for i in range(n):
        for j in range(10):
            if s1[i] == gl[j]:
                print(s1[i])
else:
    print(k1, k2)
for i in range(n):
    if s1[i] == p:
        k3 = k3 + 1
print("количество слов: ", k3 + 1)
