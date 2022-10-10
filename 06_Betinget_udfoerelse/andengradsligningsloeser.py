print("Velkommen til min 2.gradsligningsloeser!")
a = float(input("Indtast a: "))
b = float(input("Indtast b: "))
c = float(input("Indtast c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print(f"Der er 2 løsninger. x1 = {x1:.3f} og x2 = {x2:.3f}.")
elif d == 0:
    x = -b/(2*a)
    print(f"(Der er kun én løsning. x = {x:.3f}")
else:
    print(f"Diskriminanten er negativ (d = {d:.3f}).")
    print("Så der er relle løsninger.")
