a = []

with open("9 (1).txt") as f:
    for line in f:
        b = []
        for num in str(line).split(" "):
            b.append(int(num))
        a.append(b)

stroki = []

for i in a:
    if len(set(i)) == 5:
        b = 0
        for j in i:
            if i.count(j) == 2:
                b = j
        if b < (sum(i) - 2*b)/4:
            stroki.append(i)

print(len(stroki))