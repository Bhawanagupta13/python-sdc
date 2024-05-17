rnge = int(input("ENTER THE RANGE: "))
perfext = []
for i in range(2, rnge):
    sum = 1
    for j in range(2,i):
        if i%j ==0 and j!=i:
            sum +=j
    if(sum == i):
        perfext.append(i)

print(f"ALL THE PERFECT NUMBERS ARE {perfext}")