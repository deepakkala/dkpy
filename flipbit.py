n = int(raw_input())
for i in range(0,n):
    p=1
    q=0
    dec=int(raw_input())
    while dec>0:
        r=dec%2
        q=q+(r*i)
        dec=dec/2
        i=i*10
    
    
print q