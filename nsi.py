# exercice 1-3
print("bonjour")
nom = input("Entrez votre nom : ")
sexe = input("entrez votre sex (M ou F) : ").strip().upper()
if sexe == 'M':
    print(f"Monsieur {nom}")
elif sexe == 'F':
    print(f"Madame {nom}")
else:
    print(f"Bonjour {nom} (sexe non reconnu)")
age = int(input("Quel est votre âge ? "))
age_2040 = age + 14
print(f"Votre âge est {age}")
print(f"Votre âge en 2040 sera {age_2040} ans.")
# exercice 4
a=int(input("Donner le premier entier : ?"))
b=int(input("Donner le deuxieme entier : ?"))
c=a//b
r=a%b
print("Leur question est ",c)
print("Le reste de la division est ",r)
