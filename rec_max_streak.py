
"""
Created on Wed Jun 08 12:31:01 2016

@author: Aprat
"""
def find_max_mid(low,high,mid,A):
    sum_partial = 0;
    left = 0;
    right = 0;
    sum_mid = 0;
    temp = 0;
    for i in range(mid,low-1,-1):
        temp += A[i];
        if temp > sum_partial:
            left = i;
            sum_partial = temp;
    sum_mid += sum_partial;
    sum_partial = 0;
    temp = 0;
    for i in range(mid+1,high):
        temp += A[i];
        if temp > sum_partial:
            right = i;
            sum_partial = temp;
    return (left,right,(sum_mid+sum_partial));
    
    
def find_max_streak(low,high,A):
    if low == high:
        return(low, high, A[0]);
    else: mid = int((high+low)/2);
    (low_left,high_left,max_left)= find_max_streak(low,mid,A);
    (low_right,high_right,max_right)= find_max_streak(mid+1,high,A);
    (low_mid,high_mid,max_mid) = find_max_mid(low,high,mid,A);
    print max_right,max_left,max_mid;
    if (max_left >= max_right) and (max_left >= max_mid):
        print "L";
        return (low_left,high_left,max_left);
    elif (max_right >= max_left) and (max_right >= max_mid):
        print "R";
        return (low_right,high_right,max_right);
    else:
        print "M";
        return (low_mid,high_mid,max_mid);
    
print find_max_streak(0,len([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]),[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]);
print find_max_streak(0,len([-12, -10, -23, -12, -4]),[-12, -10, -23, -12, -4]);
