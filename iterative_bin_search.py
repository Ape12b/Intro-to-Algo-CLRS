n = [1, 2, 3, 43, 32, 434, 6564, 76753, 3412, 124, 3];
number = int(raw_input("Enter the number to be searched"));
n = sorted(n);
print n;
start = 0;
end = len(n);
while start<end-1:
    if n[(start+end)/2] == number:
        print (start+end)/2;
        start = end;
    elif n[(start+end)/2] > number:
        end = (start+end)/2;
    else: start = (start+end)/2;
    print start,end;
if start != end:
    print "Not Found";
    
