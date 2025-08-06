lst=(input("Enter the numbers:")).split()
l=list(map(int,lst))
evn_lst=[]
odd_lst=[]
for i in l:
    if i%2==0:
        evn_lst.append(i)
    else:
        odd_lst.append(i)
c = evn_lst + odd_lst
print(*c)