def multi(a, b):
    if a == 0 or b == 0: return 0
    if b == 1 or b == -1: return a
    elif b > 1: return a + multi(a, b-1)
    else: return - (a + multi(a, b+1))

print(multi(4, -2))