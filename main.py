import random
MAX_LINES = 3 #globale Konstanze, deshalb auch groß
MAX_WETTE = 100
MIN_WETTE = 1

ZEIlE = 3
SPALTE = 3
symbole_counter = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_solt_maschine_drehen(zeilen, spalte, symbole):
    alle_symbole = []
    for symbol, symbole_counter in symbole.items():
        for _ in range(symbole_counter): # Anonyme Variable
            alle_symbole.append(symbol)
            spalten = []
            for _ in range(spalte):
                spalte = []                       #zzufällige Werte für jede zeile
                aktuelle_symbole = alle_symbole [:] # Kopie
                for _ in range(zeilen):
                    wert = random.choice(aktuelle_symbole)
                    aktuelle_symbole.remove(wert)
                    spalte.append(wert)

                    spalten.append(spalte)

                    return spalten


def print_slot_maschine(spalten):
    for zeile in range(len(spalten[0])): # min eine Spalte
        for spalte in spalten:
            for i, spalte in enumerate(spalten):
                if i != len(spalten) - 1:
                    print(spalte[zeile], "|")
                else:
                    print(spalte[zeile])






def einzahlung():
    while True: #Benutzer gibt so lange Menge ein bis gültig ist
        betrag = input("Wie viel Geld wollen Sie einzahlen? €")
        #Prüfen, ob Betrag eine Nummer ist
        if betrag.isdigit():
            betrag = int(betrag) #Betrag in Zahl umgewandelt
            if betrag > 0:
                break
            else:
                print("Der Betrag muss größer als 0 sein")
        else:
            print("Bitte geben Sie einen gültigen Betrag ein") # Eingegebener Betrag keine Zahl ist

            return betrag

#1. Fragen wie oft und wie viel Wetten wollen
def get_anzahl_der_lines():
    while True: #Benutzer gibt so lange Menge ein bis gültig ist
        lines = input("Wie oft wollen Sie Wetten? (1 - " + str(MAX_LINES) + ") ?")
        #Prüfen, ob Betrag eine Nummer ist
        if lines.isdigit():
            lines = int(lines) #Betrag in Zahl umgewandelt
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Bitte geben Sie Zahl im gültigen Wertebereich ein")
        else:
            print("Bitte geben Sie einen gültige Zahl ein") # Eingegebener Betrag keine Zahl ist

            return lines



def get_wette():
    while True:
        betrag = input("Wie viel Geld wollen Sie pro runde Wetten? €")
        if betrag.isdigit():
            betrag = int(betrag)  # Betrag in Zahl umgewandelt
            if MIN_WETTE <= betrag <= MAX_WETTE:
                break
            else:
                print(f"Der Betrag muss zwischen sein €{MIN_WETTE} - €{MAX_WETTE} sein.")

        else:
            print("Bitte geben Sie eine gültigen Zahl ein")

            return betrag
def main():
   guthaben = einzahlung()
   lines = get_anzahl_der_lines()
   while True:
       wette = get_wette()
       gesamt_wette = wette * lines

       if gesamt_wette > guthaben:
           print(f"Sie haben nicht genug Guthaben, Ihr aktuelles Guthabe beträgt € {guthaben}")
       else:
           break



       print(f"Sie wetten:{wette} mit {lines} Versuchen. Gesamte Wette ist €{gesamt_wette}")
main()

