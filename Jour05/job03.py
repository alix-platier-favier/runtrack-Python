def tapis(n):
    print("+" + "-"*(n+1) + "+")
    for i in range(n, -1, -1):
        row = ""
        for j in range(n+1):
            if i == j:
                row += " "
            else:
                row += "#"
        print("|" + row + "|")
    print("+" + "-"*(n+1) + "+")

tapis(10)