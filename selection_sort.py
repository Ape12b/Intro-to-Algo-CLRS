n = [10,9,8,7,6,5,3,2,21,4,3,2,1,0];
for i in range(len(n)-1):
    temp = n[i];
    key = i;
    for j in range(i,len(n)):
        if n[j]<temp:
            key = j;
            temp = n[j];
        temp = n[i];    
        n[i] = n[key];
        n[key] = temp;
print n;

