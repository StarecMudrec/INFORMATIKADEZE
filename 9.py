a = []

with open("9.txt") as f:
    for line in f:
        b = []
        for num in str(line).split(" "):
            b.append(int(num))
        a.append(b)

stroki = []

for i in a:
    if len(i) == len(set(i)):
        if max(i) < (sum(i) - max(i)):
            stroki.append(i)

print(len(stroki))