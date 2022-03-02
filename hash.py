def poly_hash(s, b=91, m=100):
    h=0
    for c in s:
        h=(h*b+ord(c))%m
    return h

def insert(key, value):
    h=poly_hash(key)
    if len(table[h%10])>0 and table[h%10][-1][1]==key:
        table[h%10][-1][2]=value
    else:
        table[h%10].append([h,key,value])
    
table=[[] for _ in range(10)]
m=int(input())
for i in range(m):
    key, value=input().split()
    insert(key, value)
for i in range(10):
    if len(table[i])>0:
        print(i)
    for j in range(len(table[i])):
        print(*table[i][j])
