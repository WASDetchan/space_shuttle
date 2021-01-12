a = 1
o = []
for b in range(257):
    for i in range (1001):
        a += i
        o.append(a%257)
    print(b, o.count(b))