N = int(input("Entrez un nombre entier : "))

while N < 0:
    print("Le nombre doit être positif.")
    N = int(input("Entrez un nombre entier : "))

tables_de_multiplication = 1 

while tables_de_multiplication <= N: 
    print(f"Table de multiplication de {tables_de_multiplication} :")
    i = 1
    while i <= 10:
        print(f"{tables_de_multiplication} x {i} = {tables_de_multiplication * i}")
        i += 1
    tables_de_multiplication += 1
