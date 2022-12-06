alm_tekst = "Her er noget almindelig tekst."

def til_roeversprog(alm_tekst):
    roeversprog = ""
    for karakter in alm_tekst:
        if karakter.lower() in "qwrtpsdfghjklzxcvbnm":
            roeversprog += karakter +"o" + karakter
        else:
            roeversprog += karakter
    return roeversprog
print(til_roeversprog(alm_tekst))
