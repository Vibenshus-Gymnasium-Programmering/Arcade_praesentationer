def til_roeversprog(alm_tekst):
    roeversprog = ""
    for karakter in alm_tekst:
        if karakter.lower() in "qwrtpsdfghjklzxcvbnm":
            roeversprog += karakter +"o" + karakter
        else:
            roeversprog += karakter
    return roeversprog

while True:
    print(til_roeversprog(input("Skriv din tekst her: ")))
