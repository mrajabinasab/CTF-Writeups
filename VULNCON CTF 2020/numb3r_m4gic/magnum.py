a = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]
looper = len(a) - 1
print(a)
for j in range(looper):
    temp = []
    sum = 0
    sumt = 0
    ctrl = 0
    chk = 0
    for i in a:
        if (i<10):
            sum = sum + i
        b = i/10
        while b!=0:
            sum = sum + (i-b*10)
            i = b
            if (b<10):
                sum = sum + b
            b = b/10
        ctrl = ctrl + 1
        if (ctrl==1 and chk==0):
            sumt = sum
            chk = 1
        if (ctrl>1):
            temp.append(sum)
            sum = sum - sumt
            sumt = sum
    print(temp)
    a = temp
        
    