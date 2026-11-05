for n in range (2, 1001):
    est_premier = True
    for m in range (2, n):
        if n % m == 0:
            est_premier = False
            break
    if est_premier:
        print(n)