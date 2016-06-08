
def merge(n,m):
    print n,m;
    n_counter = 0;
    m_counter = 0;
    J = [];
    for i in range(len(n)+len(m)):
        if n[n_counter]>=m[m_counter]:
            J.append(m[m_counter]);
            if m_counter==len(m)-1:
                for j in range(n_counter,len(n)):
                    J.append(n[j]);
                return J;    
            m_counter+=1;
        else:
            J.append(n[n_counter]);
            if n_counter==len(n)-1:
                for j in range(m_counter,len(m)):
                    J.append(m[j]);
                return J; 
            n_counter+=1;
    return J;
            
def merge_sort(n):
    if len(n) < 2: return n;
    else:
        return merge(merge_sort(n[0:int(len(n)/2)]),merge_sort(n[int(len(n)/2):len(n)]));


print merge_sort([10,9,8,7,6,5,3,2,21,4,3,2,1,0]);
print sorted([10,9,8,7,6,5,3,2,21,4,3,2,1,0]);
