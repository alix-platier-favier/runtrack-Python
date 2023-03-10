height = 3 
width = 10 
for i in range(height):
    for j in range(width):
        if j ==0 or j ==(width -1):
            print("|", end="") 
        elif i ==0 or i == (height -1):
            print("-", end="")
        else:
            print(" ", end="")
    print()