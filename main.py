MAX_LINES = 3 #globale Konstanze, deshabl auch groß
MAX_WETTE = 100
MIN_WETTE = 1
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
            print("Bitte geben Sie eine gültigen Zahl ein")  # Eingegebener Betrag keine Zahl ist

            return betrag
def main():
   guthaben = einzahlung()  # Funktion aufrufen
   lines = get_anzahl_der_lines()
   while True:
       wette = get_wette()
       gesamt_wette = wette * lines
         if gesamt_wette > guthaben:
           print(f"Sie haben nicht genug guthaben, um zu Wetten.Ihr aktuelles Guthaben beträgt: € {guthaben}")
       else:
           break



   print(f"Sie wetten:{wette} mit {lines} Versuchen. Gesamte Wette ist €{gesamt_wette}")
   print(guthaben, lines, wette)

main()

