def insertion_sort(a,n):
    for j in range(1,n):
        key = a[j]
        i = j-1
        while i>0 and a[i] > key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a
    
a = [1,24,4,6,7,8, 5, 6,4]
f = insertion_sort(a,len(a))
print f

