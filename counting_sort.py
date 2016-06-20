def counting_sort(A):
    k = A[0];
    for i in range(len(A)):
        if A[i]>k:
            k = A[i];
    C = [];
    for i in range(k+1):
        C.append(0);
    for i in range(len(A)):
        C[A[i]] += 1;
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1];
    B = [];
    for i in range(len(A)):
        B.append(0);
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1] = A[i];
        print A[i],C,B;
        C[A[i]] = C[A[i]] - 1;
    return B;

A = [4,6,3,5,0,5,1,3,5,5];
print counting_sort(A);
        
        
