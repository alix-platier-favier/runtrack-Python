l = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
min = l[0]
max = 0
for i in l:
    if i > max:
        max = i
    if i < min:
        min = i
print(min)
print(max)