def swap(i,j):
    return(j,i);

def partition(A,p,r):
    x = A[r];
    i = p-1;
    for j in range(p,r):
        if A[j] <= x:
            i = i+1;
            (A[i],A[j]) = swap(A[i],A[j]);
    (A[i+1],A[r]) = swap(A[i+1],A[r]);
    print A;
    return i+1;
    
def quick_sort(A,p,r):
    if p < r :
        q = partition(A,p,r);
        print q;
        quick_sort(A,p,q-1);
        quick_sort(A,q+1,r);

A = [1,45,6,2,564,23,4,6,2,6];
quick_sort(A,0,len([1,45,6,2,564,23,4,6,2,6])-1);
print A;
