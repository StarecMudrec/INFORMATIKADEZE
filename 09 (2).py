a = []

with open("09 (2).txt") as f:
    for line in f:
        b = []
        for num in str(line).split(" "):
            b.append(int(num))
        a.append(b)

stroki = []

for i in a:
    if len(i) == len(set(i)):
        ch=[]
        nch=[]
        for j in range(len(i)):
            if i[j]%2==0:
                ch.append(i[j])
            else: nch.append(i[j])
        if len(ch)>len(nch) and sum(ch)<sum(nch):
            stroki.append(i)

print(len(stroki))