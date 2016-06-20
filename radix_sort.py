def counting_sort(A,d):
    k = (A[0]/d)%10;
    for i in range(len(A)):
        if ((A[i]/d)%10)>k:
            k = ((A[i]/d)%10);
    C = [];
    for i in range(k+1):
        C.append(0);
    for i in range(len(A)):
        C[((A[i]/d)%10)] += 1;
    print C;
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1];
    B = [];
    for i in range(len(A)):
        B.append(0);
    for i in range(len(A)-1,-1,-1):
        B[C[((A[i]/d)%10)]-1] = A[i];
        C[((A[i]/d)%10)] = C[((A[i]/d)%10)] - 1;
    return B;

def radix_sort(A,d):
    dev = 1;
    for i in range(d):
        A = counting_sort(A,dev);
        print A;
        dev = dev*10;
    return A;

print radix_sort([392,517,364,931,726,912,299,250,600,185],3);
