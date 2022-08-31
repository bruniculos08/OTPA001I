while(1):
    n = int(input())
    if n == 0: break
    cmd = list(map(int, input().split()))
    num = 0
    for i, v in enumerate(cmd):
        num += v + i
    print(num)