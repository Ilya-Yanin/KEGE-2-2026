res = []
for N in range(1, 30):
    R = f'{N:b}'
    if N % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    R = int(R, 2)
    res.append(R)

print(max(res))