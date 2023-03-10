L = [1,23, 45, 102, 42, 89]
def triage(L):
    for i in range(0, len(L)):
        liste = L[i]
        j = i -1
        while j >=0 and L[j] > liste:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = liste
    return L
print(triage(L))