l = [12, 75, 150,180,145,525,50]
l2 = []
for i in l:
    if i >150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        l2.append(i)

print(l2)