import random
MIN = 1
MAX = 100
MAX_GAET = 10

def nyt_spil():
    print(f"Hep hey! Jeg tænker på et tal mellem {MIN} og {MAX}. Kan du gætte det?")
    print(f"Du har {MAX_GAET} gæt til det.")
    hemmeligt_tal = random.randint(MIN, MAX)
    antal_gaet = 0
    while True:
        try:
            brugergaet = int(input(f"{antal_gaet + 1}. forsøg. Hvilket tal tænker jeg på: "))
        except ValueError:
            print("Du skal indtaste et heltal.")
            continue
        antal_gaet += 1
        if brugergaet > hemmeligt_tal:
            print("For højt.")
        elif brugergaet < hemmeligt_tal:
            print("For lavt.")
        else:
            print("Du gættede mit hemmelige tal. Tillykke.")
            break

        if antal_gaet >= MAX_GAET:
            print(f"Du gættede ikke mit hemmelige tal inden for {MAX_GAET} forsøg.")
            print(f"Mit hemmelige tal var {hemmeligt_tal}.")
            break
        
def spil_igen():
    print("Vil du spille igen?")
    while True:
        svar = input(f"Skriv Ja eller Nej: ")
        if svar.lower() in ("ja", "j", "yes", "y"):
            return True
        elif svar.lower() in ("nej", "n", "no"):
            return False
        else:
            print("Dit svar kan ikke bruges. Skriv ja eller nej.")

def main():
    vil_gerne_spille = True
    while vil_gerne_spille:
        nyt_spil()
        vil_gerne_spille = spil_igen()
    print("Tak for spillet.")

main()
