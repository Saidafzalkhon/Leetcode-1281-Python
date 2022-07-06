n = int(input())
q = 0
k = 1
for i in str(n):
    q += int(i)
    k *= int(i)
print(k-q)