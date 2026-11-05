# ask the user to input three numbers and store them in variables a, b, and c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
match (a, b, c):
        case (a, b, c) if a == b and c <= a and c <= b:
            print("le triangle est isocèle")
        case (a, b, c) if a**2 + b**2 == c**2:
            print("le triangle est rectangle")
        case (a, b, c) if a == b == c:
            print("le triangle est équilatéral")
        case (a, b, c) if a != b and b != c and a != c:
            print("le triangle quelconque")

# il manque le cas du triangle équilatéral et du triangle quelconque.(plus préciiiiis) Il faut ajouter ces deux cas pour que le programme soit complet lol