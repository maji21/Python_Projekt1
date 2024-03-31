import json


def add_ausgaben(ausgaben, beschreibung, betrag):
    ausgaben.append({"Beschreibung:": beschreibung, "Betrag:": betrag})
    print(f"Ausgabe(n) für  : {beschreibung} , Betrag : {betrag} wurde(n) hinzugefügt")


def gesamt_ausgaben(ausgaben):
    sum = 0
    for i in ausgaben:
        sum += i["Betrag"]
    return sum


def get_guthaben(budget, ausgaben):
    return budget - gesamt_ausgaben(ausgaben)


def budget_anzeigen(budget, ausgaben):
    print(f"Budget: {budget}")
    print(f"Ausgaben:")
    for ausgabe in ausgaben:
        print(f" - {ausgabe['Beschreibung']}: {ausgabe['Betrag']}")
    print(f"Gesamte Ausgaben: {gesamt_ausgaben(ausgaben)}")
    print(f"Verbleibendes Budget: {get_guthaben(budget, ausgaben)}")


def load_budget_data(filepath):  # lesen von Datei
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['start_budget'], data['ausgaben']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Default Wert, wenn Datei leer ist oder nicht existiert


def budget_details(filepath, start_budget, ausgaben):
    data = {
        'start_budget': start_budget,
        'ausgaben': ausgaben}
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    print("Willkommen zu deinem Finanz Tracker")
    filepath = 'budget_data.json'
    start_budget, ausgaben = load_budget_data(filepath)
    if start_budget == 0:
        start_budget = float(input("Gib hier dein Startbetrag ein:"))
        budget = start_budget


 while True:
    print("\nWas möchtest du tun ?")
    print("1. Ausgaben eintragen")
    print("2. Aktuelles Budget anzeigen")
    print("3. Beenden")

    auswahl = input("Bitte wähle zwischen 1-3 aus: ")

    if auswahl == "1":
        beschreibung = input("Was hast du gekauft? ")
        betrag = float(input("Wie viel hast du ausgegeben? "))
        add_ausgaben(ausgaben, beschreibung, betrag)

    elif auswahl == "2":
        budget_anzeigen(budget, ausgaben)

    elif auswahl == "3":
        budget_details(filepath, start_budget, ausgaben)
        print("Programm wird beendet.Bis zum nächsten Mal!")
        break

    else:
        print("Ungültige Eingabe. Bitte nochmal, aber richtig ;)")


  if __name__ == "__main__":
            main()
