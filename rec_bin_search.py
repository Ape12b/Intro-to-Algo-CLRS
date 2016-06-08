n = [1, 2, 3, 43, 32, 434, 6564, 76753, 3412, 124, 3];
number = int(raw_input("Enter the number to be searched"));
n = sorted(n);

def rec_bin_search(n,number):
    if len(n) == 0 | (len(n) == 1 & number != n[0]):
        return False;
    elif len(n) == 1 & number == n[0]:
        return True;
    elif number == n[len(n)/2]:
        return True;
    elif number > n[len(n)/2]:
        return rec_bin_search(n[len(n)/2:],number);
    else: return rec_bin_search(n[:len(n)/2],number);

if rec_bin_search(n,number): print "found";
else: print "Notfound";
