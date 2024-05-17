n = 140
hehe =n
factor =[]
st =2
while st<=n:
    if n % st ==0:
        factor.append(st)
        n = n/ st
    else:
        st+=1

print(F"PRIME FACTORS OF {hehe} are {factor}")