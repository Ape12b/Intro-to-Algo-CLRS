for i in range(1,101):
    temp = 0;
    for j in range(1,i):
        if i%j == 0:
            temp += 1;
    if temp%2 == 0:
        print i;
