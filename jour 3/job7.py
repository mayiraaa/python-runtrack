chaine = "abcdefghijklmnopqrstuvwxyz" * 10 
i, j = 0, 1
# decoupage pyramidal de la chaine
while i + j <= len(chaine):
    print(chaine[i:i + j])
    i = i + j
    j = j + 2