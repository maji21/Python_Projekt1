import random

MAX_LINES = 3 #Global
MAX_WETTE = 100
MIN_WETTE = 1

ZEILE = 3
SPALTE = 3

symbole_counter = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbole_werte = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_gewinne(spalten,lines,wetten,werte):
  gewinne = 0
  gewinne_lines = []
  for line in range(lines):
      symbol = spalten[0][line]
      for spalte in spalten:
          symbol_check = spalte[line]
          if symbol != symbol_check:
              break
          else:
              gewinne += werte[symbol] * wetten
              gewinne_lines.append(line + 1)

              return gewinne, gewinne_lines




def get_solt_maschine_drehen(zeilen, spalte, symbole):
    alle_symbole = []
    for symbol, symbole_counter in symbole.items():
        for _ in range(symbole_counter): # Anonyme Variable
            alle_symbole.append(symbol)

            spalten = []
            for _ in range(spalte):
                spalte = []                       #zufällige Werte für jede zeile
                aktuelle_symbole = alle_symbole [:] # Kopie
                for _ in range(zeilen):
                    wert = random.choice(aktuelle_symbole)
                    aktuelle_symbole.remove(wert)

                    spalte.append(wert)

                    spalten.append(spalte)

                    return spalten

def print_slot_maschine(spalten):
    for zeile in range(len(spalten[0])): # min eine Spalte
            for i, spalte in enumerate(spalten):
                if i != len(spalten) - 1:
                    print(spalte[zeile], end=" | ")
                else:
                    print(spalte[zeile], end=" ")

            print()


def einzahlung():
    while True: #Benutzer gibt so lange Menge ein bis gültig ist
        betrag = input("Wie viel Geld wollen Sie einzahlen? €")
        if betrag.isdigit():  #Prüfen, ob Betrag eine Nummer ist
            betrag = int(betrag) #Betrag in Zahl umgewandelt
            if betrag > 0:
              #  break
             return betrag
            else:
                print("Der Betrag muss größer als 0 sein")
        else:
            print("Bitte geben Sie einen gültigen Betrag ein") # Eingegebener Betrag keine Zahl ist

            return betrag

# Fragen wie oft und wie viel Wetten wollen
def get_anzahl_der_lines():
    while True: #Benutzer gibt so lange Menge ein bis gültig ist
        lines = input("Wie oft wollen Sie Wetten? (1 - " + str(MAX_LINES) + ") ?")
        #Prüfen, ob Betrag eine Nummer ist
        if lines.isdigit():
            lines = int(lines) #Betrag in Zahl umgewandelt
            if 1 <= lines <= MAX_LINES:
               # break
                 return lines
            else:
                print("Bitte geben Sie Zahl im gültigen Wertebereich ein")
        else:
            print("Bitte geben Sie einen gültige Zahl ein") # Eingegebener Betrag keine Zahl ist

            return lines

def get_wette():
    while True:
        betrag = input("Wie viel wollen Sie auf jede Linie setzen ?")
        if betrag.isdigit():
            betrag = int(betrag)
            if MIN_WETTE <= betrag <= MAX_WETTE:
                return betrag
            else:
                print(f"Betrag muss zwischen € {MIN_WETTE} - € {MAX_WETTE} sein.")

 #           return betrag




def spiel(guthaben):
            lines = get_anzahl_der_lines()
            while True:
                wette = get_wette()
                gesamt_wette =  wette * lines

                if gesamt_wette > guthaben:
                    print(f"Sie haben nicht genug Guthaben, Ihr aktuelles Guthabe beträgt € {guthaben}")
                else:
                    break

            print(f"Sie wetten:{wette} mit {lines} Versuchen. Gesamte Wette ist €{gesamt_wette}")

            slots = get_solt_maschine_drehen(ZEILE, SPALTE, symbole_counter)
            print_slot_maschine(slots)
            gewinne, gewinne_lines = check_gewinne(slots, lines, wette, symbole_werte)
            print(f"Sie haben €{gewinne} gewonnen")
            print(f"You won on lines:", *gewinne_lines)
            return gewinne - gesamt_wette


def main():
   guthaben = einzahlung()
   while True:
       print(f"Ihr aktuelles Guthaben beträgt: €{guthaben}")
       antwort = input("Drücke auf Enter zum Drehen. (b für beenden)")
       if antwort == "b":
           break
       guthaben += spiel(guthaben)
       print((f"Sie haben noch €{guthaben} "))

main()
