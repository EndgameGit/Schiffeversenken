#!/usr/bin/python

"""Dies ist eine Implementation des Spiels Schiffeversenken für die Projektabgabe Programmieren im 1.Semester
Mitglieder: Tobias Traiser, Emanuel Avadani, Lukas Zwaller, Pascal Wildermuth
21.04.2021"""

import os
import json
import random
import spielfeld_klasse
from computer_gegner import ComputerGegner


def print_bild():
    """Gibt Bild für den Startscreen aus

    Returns:
        bild (str): Bild
    """

    bild = """                __/___
          _____/______|           
  _______/_____/_______|_____     
  | ;;           < < <      |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    return bild


def startbildschirm(spielstand_existiert):
    """Erstellt den Startbildschirm, in dem sich der Modus auswählen lässt.

    Args:
        spielstand_existiert (bool): Abfrage, ob Spielstanddatei vorhanden ist

    Returns:
        wahl (int): 1: Neues 2-Spieler  2: Neues 1-Spieler  3: Spiel laden
    """
    print("\nHerzlich Willkommen zum Schiffeversenken.\n")
    print("Neues Zwei-Spieler-Spiel (1)\nNeues Ein-Spieler-Spiel  (2)")
    if spielstand_existiert:
        print("Spiel laden              (3)\n")
    falsche_wahl = True
    while falsche_wahl:
        wahl = input("Auswahl durch Eingabe entsprechender Zahl:\n")
        wahl = wahl.strip()
        if wahl == "1" or wahl == "2" or (wahl == "3" and spielstand_existiert):
            falsche_wahl = False
            return int(wahl)

        print("Ungültige Eingabe")


def farbiges_spielfeld(feld):
    """
    Faerbt das Spielfeld.

    Args:
        feld (str): Ein String, der das Zeichen eines Feldes beinhaltet.
    """
    if feld in ("~", "?"):
        # blauer Hintergrund
        print('\x1b[44m', str(feld), '\x1b[0m', end="")
    elif feld == "-":
        # zyan
        print('\x1b[48;2;30;144;255m', str(feld), '\x1b[0m', end="")
    elif feld == "O":
        # magenta
        print('\x1b[48;2;69;69;69m', str(feld), '\x1b[0m', end="")
    elif feld == "N":
        # gelb
        print('\x1b[31;44m', str(feld), '\x1b[0m', end="")
    elif feld == "X":
        # gruen
        print('\x1b[32;48;2;69;69;69m', str(feld), '\x1b[0m', end="")
    else:
        # if 'S' => rot
        print('\x1b[31;48;2;69;69;69m', str(feld), '\x1b[0m', end="")


def spielfeld_erstellen(spielfeld, gegnerisches_spielfeld):
    """Die Spielfeld Listen werden formatiert in der Konsole geprintet

    Args:
        spielfeld (spielfeld): Spielfeld Spieler 1
        gegnerisches_spielfeld (spielfeld): Spielfeld Spieler 2
    """
    print("     Dein Spielfeld:                       Das gegnerische Spielfeld:")
    print("     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J")
    for i in range(1, 11):
        if i < 10:
            print(i, end="   ")
        else:
            print(i, end="  ")
        for feld in spielfeld.felder[i-1]:
            farbiges_spielfeld(feld)
        if i < 10:
            print("    " + str(i), end="   ")
        else:
            print("    " + str(i), end="  ")
        for feld in gegnerisches_spielfeld.felder[i-1]:
            farbiges_spielfeld(feld)
        if i < 10:
            print("  " + str(i), end="")
        else:
            print("  " + str(i), end="")
        print(" ")
    print("     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J")


def spielfelder_erzeugen(namen):
    """Vier Spielfelder werden als Objekte erzeugt. Jeder Spieler erhält zwei,
    sein eigenes und eine verdeckte Version des Gegnerfeldes.

    Args:
        namen (list): Die zwei Namen der Spieler

    Returns:
        spielfeld: Das Spielfeld Objekt enthält alle Felder und den Namen des Spielers
    """
    spielfeld_spieler1 = spielfeld_klasse.Spielfeld(
        [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10,
         ["~"]*10, ["~"]*10, ["~"]*10], namen[0])

    spielfeld_spieler2 = spielfeld_klasse.Spielfeld(
        [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10,
         ["~"]*10, ["~"]*10, ["~"]*10], namen[1])

    gegnerisches_spielfeld_für_spieler1 = spielfeld_klasse.Spielfeld(
        [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10,
         ["?"]*10, ["?"]*10, ["?"]*10], namen[0])

    gegnerisches_spielfeld_für_spieler2 = spielfeld_klasse.Spielfeld(
        [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10,
         ["?"]*10, ["?"]*10, ["?"]*10], namen[1])

    return spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_für_spieler1, \
        gegnerisches_spielfeld_für_spieler2


def beginner_auslosen(modus):
    """Es werden die Namen der beiden Spieler abgefragt und dann ausgelost,
        welcher Spieler beginnt.
    Args:
        modus (int) = vom Spieler gewählter Spielmodus
    Returns:
        namen (list): namen besteht aus den Namen beider Spieler
    """
    namen_gesetzt = False
    namen = []

    while not namen_gesetzt:
        if len(namen) == 0:
            name = input("Wie lautet dein Name?\n")
        elif modus == 1:
            name = input("Wie lautet der Name deines Gegners?\n")
        elif modus == 2:
            namen.append("B0T")
            return namen
        if name.isalpha():
            namen.append(name.title())
            if len(namen) == 2:
                namen_gesetzt = True
        else:
            print("Ungültige Eingabe.\n")
    spieler_1 = random.choice(namen)
    namen.remove(spieler_1)
    spieler_2 = str(namen[0])
    namen = [spieler_1, spieler_2]
    return namen


def speichern(alle_spielfelder, namen, runde):
    """Die vier Spielfelder werden in der Json-Datei 'Kontenspeicherung.json'
    gespeichert

    Args:
        alle_spielfelder (list): Liste aller Spielfeldobjekte
        namen (list): Liste der zwei Spielernamen
        runde (int): Aktuelle Rundenzahl
    """
    spielfeld_json = []
    for spielfeld in alle_spielfelder:
        spielfeld_json.append(spielfeld.felder)
    speicher_dict = {"Spieler": {
        "Spieler1": namen[0], "Spieler2": namen[1]}, "Runde": runde, "Spielfelder": spielfeld_json}
    with open('Kontenspeicherung.json', 'w') as json_file:
        json.dump(speicher_dict, json_file, indent=4)
    json_file.close()


def datei_loeschen(dateiname):
    """Löscht eine Datei

    Args:
        dateiname (str): Dateiname
    """
    try:
        os.remove(dateiname)
    except FileNotFoundError:
        print("File not found")


def spielstand_auslesen():
    """Liest den Spielstand aus.
    Gibt None zurück, wenn die Datei leer ist oder nicht existiert.
    Gibt ein dictionary names spielstaende zurück.

    Returns:
        (spielstaende) dict: spielstaende, falls nicht vorhanden None
    """
    try:
        if os.path.exists('Kontenspeicherung.json'):
            with open('Kontenspeicherung.json') as file_var:
                spielstaende = json.load(file_var)
                if len(spielstaende) == 0:
                    return None

                return spielstaende
        else:
            return None
    except ValueError:
        return None


def runde_und_namen_laden(spielstaende):
    """Gibt Namen und Runde aus Spielstandspeicher zurück

    Args:
        spielstaende (dict): Spielstaende

    Returns:
        int, list: Runde, Namen
    """
    runde = spielstaende["Runde"]
    namen = spielstaende["Spieler"]
    return runde, namen


def spielfelder_laden(spielstaende):
    """Laedt die Spielfelder aus dem Speicher

    Args:
        spielstaende (dict): spielstaende

    Returns:
        (spielfeld): 4 Spielfelder
    """
    liste_spielfelder = spielstaende["Spielfelder"]
    zustand1 = liste_spielfelder[0]
    zustand2 = liste_spielfelder[1]
    zustand3 = liste_spielfelder[2]
    zustand4 = liste_spielfelder[3]

    spieler = spielstaende["Spieler"]

    spielfeld_spieler1 = spielfeld_klasse.Spielfeld(
        zustand1, spieler["Spieler1"])
    spielfeld_spieler2 = spielfeld_klasse.Spielfeld(
        zustand2, spieler["Spieler2"])
    gegnerisches_spielfeld_spieler1 = spielfeld_klasse.Spielfeld(
        zustand3, spieler["Spieler1"])
    gegnerisches_spielfeld_spieler2 = spielfeld_klasse.Spielfeld(
        zustand4, spieler["Spieler2"])
    return spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_spieler1, gegnerisches_spielfeld_spieler2


def schiffe_setzen(spielfeld, gegnerisches_spielfeld):
    """Überprüft auf richtige Feldeingabe und ruft setz_richtung_generieren auf,
    um das Schiff zu platzieren.

    Args:
        spielfeld (spielfeld): Spielfeld Spieler 1
        gegnerisches_spielfeld (spielfeld): Spielfeld Spieler 2
    """
    buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    schiffe = ["Schlachtschiff", "Kreuzer", "Kreuzer", "Zerstörer",
               "Zerstörer", "Zerstörer", "U-Boot", "U-Boot", "U-Boot", "U-Boot"]
    schiffwert = {"Schlachtschiff": 5,
                  "Kreuzer": 4, "Zerstörer": 3, "U-Boot": 2}

    for schiff in schiffe:
        schifflänge = schiffwert[schiff]
        end = True
        platzierbar = True
        while end or not platzierbar:
            feld = input(
                f"\nBitte setze das erste Feld von deinem {schiff} (Länge: {schifflänge}) (Bsp: D4):\n")
            for zeichen, buchstabe in enumerate(buchstaben):
                if len(feld) > 1:
                    if feld[0] == buchstabe:
                        end, platzierbar = finde_zahl(
                            spielfeld, gegnerisches_spielfeld, zeichen, feld, schifflänge)
            if end:
                print("Falsche Eingabe. Bitte halte dich an das Format 'D4'.")
            if not platzierbar:
                print(
                    "\nAn dieser Stelle ist nicht genügend Platz.\nBitte versuche es erneut:")


def finde_zahl(spielfeld, gegnerisches_spielfeld, zeichen, feld, schifflänge):
    """Hilffunktion für schiffe_setzen, in der auf die Zahleneingabe geprüft wird.

    Args:
        spielfeld (spielfeld): Spielfeld Spieler 1
        gegnerisches_spielfeld (spielfeld): Spielfeld Spieler 2
        zeichen (int): Buchstabenauswahl
        feld (str): Eingabe des Spielers
        schiffl (int): Länge des Schiffes

    Returns:
        (bool): Ob der Eingabewert richtig ist und ob das Feld platzierbar ist
    """
    end = True
    platzierbar = True
    try:
        # Prüfen ob die Eingabe eine 10 ist
        try:
            if int(feld[1]) == 1 and int(feld[2]) == 0:
                platzierbar = setz_richtung_generieren(
                    spielfeld, schifflänge, zeichen, 10)
                if platzierbar:
                    spielfeld_erstellen(
                        spielfeld, gegnerisches_spielfeld)
                end = False
        except IndexError:
            end = True
        for zahl in range(1, 10):
            # Hier werden die Zahlen eingetragen, falls nicht zweistellig
            if int(feld[1]) == zahl and len(feld) == 2:
                platzierbar = setz_richtung_generieren(
                    spielfeld, schifflänge, zeichen, zahl)
                if platzierbar:
                    spielfeld_erstellen(
                        spielfeld, gegnerisches_spielfeld)
                end = False
                break
    except ValueError:
        end = True
    return end, platzierbar


def fall_eins(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        richtung_info(RichtungInfo):

    Returns:
        (bool): check_obj
    """
    check_obj = True
    for i in range(zeichen-schifflänge, zeichen):
        if spielfeld.felder[zahl-1][i+1] == "O" or spielfeld.felder[zahl-1][i+1] == "-":
            check_obj = False
    if check_obj:
        richtung_ausgabe["links"] = True
    return check_obj


def fall_zwei(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        richtung_info(RichtungInfo):

    Returns:
        (bool): check_obj
    """
    check_obj = True
    for i in range(zeichen, zeichen+schifflänge):
        if spielfeld.felder[zahl-1][i] == "O" or spielfeld.felder[zahl-1][i] == "-":
            check_obj = False

    if check_obj:
        richtung_ausgabe["rechts"] = True
    return check_obj


def fall_drei(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        richtung_info(RichtungInfo):

    Returns:
        (bool): check_obj
    """
    check_obj = True
    for i in range(zahl-schifflänge, zahl):
        if spielfeld.felder[i][zeichen] == "O" or spielfeld.felder[i][zeichen] == "-":
            check_obj = False
    if check_obj:
        richtung_ausgabe["oben"] = True
    return check_obj


def fall_vier(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        richtung_info(RichtungInfo):

    Returns:
        (bool): check_obj
    """
    check_obj = True
    for i in range(zahl, zahl+schifflänge):
        if spielfeld.felder[i-1][zeichen] == "O" or spielfeld.felder[i-1][zeichen] == "-":
            check_obj = False
    if check_obj:
        richtung_ausgabe["unten"] = True
    return check_obj


def mach_links(spielfeld, zeichen, schifflänge, zahl, end):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        end (bool): Ende der Runde

    Returns:
        (bool): end
    """
    for i in range(zeichen-schifflänge, zeichen):
        spielfeld.feld_zuweisen(zahl-1, i+1)
        spielfeld.sperrfeld_zuweisen(zahl-2, i+1)
        spielfeld.sperrfeld_zuweisen(zahl, i+1)
    spielfeld.sperrfeld_zuweisen(zahl-1, zeichen-schifflänge)
    spielfeld.sperrfeld_zuweisen(zahl-1, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen-schifflänge)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen-schifflänge)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen+1)
    end = False
    return end


def mach_rechts(spielfeld, zeichen, schifflänge, zahl, end):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        end (bool): Ende der Runde

    Returns:
        (bool): end
    """
    for i in range(zeichen, zeichen+schifflänge):
        spielfeld.feld_zuweisen(zahl-1, i)
        spielfeld.sperrfeld_zuweisen(zahl-2, i)
        spielfeld.sperrfeld_zuweisen(zahl, i)
    spielfeld.sperrfeld_zuweisen(zahl-1, zeichen+schifflänge)
    spielfeld.sperrfeld_zuweisen(zahl-1, zeichen-1)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen+schifflänge)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen-1)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen+schifflänge)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen-1)
    end = False
    return end


def mach_oben(spielfeld, zeichen, schifflänge, zahl, end):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        end (bool): Ende der Runde

    Returns:
        (bool): end
    """
    for i in range(zahl-schifflänge, zahl):
        spielfeld.feld_zuweisen(i, zeichen)
        spielfeld.sperrfeld_zuweisen(i, zeichen-1)
        spielfeld.sperrfeld_zuweisen(i, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl-schifflänge-1, zeichen-1)
    spielfeld.sperrfeld_zuweisen(zahl-schifflänge-1, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl-schifflänge-1, zeichen)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen-1)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl, zeichen)
    end = False
    return end


def mach_unten(spielfeld, zeichen, schifflänge, zahl, end):
    """

    Args:
        spielfeld (spielfeld): Spielfeld
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        schifflänge (int): Länge vom Schiff
        zahl (int): Eingegebene Zahl des Spielers
        end (bool): Ende der Runde

    Returns:
        (bool): end
    """
    for i in range(zahl, zahl+schifflänge):
        spielfeld.feld_zuweisen(i-1, zeichen)
        spielfeld.sperrfeld_zuweisen(i-1, zeichen-1)
        spielfeld.sperrfeld_zuweisen(i-1, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl+schifflänge-1, zeichen-1)
    spielfeld.sperrfeld_zuweisen(zahl+schifflänge-1, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl+schifflänge-1, zeichen)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen-1)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen+1)
    spielfeld.sperrfeld_zuweisen(zahl-2, zeichen)
    end = False
    return end


def checke_links(richtung_ausgabe):
    """
    Die Funktion schaut, welche Richtung
    für den Spieler ausgegeben werden soll.
    Args:
        richtung_info(RichtungInfo): dict in der alle möglichen Richtungen gespeichert werden

    Prints:
        (str): die mögliche Richtungen
        werden ausgegeben
    """
    if richtung_ausgabe["links"] is True:
        print("\nlinks(L)")


def checke_rechts(richtung_ausgabe):
    """
    Die Funktion schaut, welche Richtung
    für den Spieler ausgegeben werden soll.
    Args:
        richtung_info(RichtungInfo): dict in der alle möglichen Richtungen gespeichert werden

    Prints:
        (str): die mögliche Richtungen
        werden ausgegeben
    """
    if richtung_ausgabe["rechts"] is True:
        print("\nrechts(R)")


def checke_oben(richtung_ausgabe):
    """
    Die Funktion schaut, welche Richtung
    für den Spieler ausgegeben werden soll.
    Args:
        richtung_ausgabe(RichtungInfo): dict in der alle möglichen Richtungen gespeichert werden

    Prints:
        (str): die mögliche Richtungen
        werden ausgegeben
    """
    if richtung_ausgabe["oben"] is True:
        print("\noben(O)")


def checke_unten(richtung_ausgabe):
    """
    Die Funktion schaut, welche Richtung
    für den Spieler ausgegeben werden soll.
    Args:
        richtung_ausgabe(RichtungInfo): dict in der alle möglichen Richtungen gespeichert werden

    Prints:
        (str): die mögliche Richtungen
        werden ausgegeben
    """
    if richtung_ausgabe["unten"] is True:
        print("\nunten(U)")


def setz_richtung_generieren(spielfeld, schifflänge, zeichen, zahl):
    """In dieser Funktion wird die mögliche Setzrichtung überprüft
    und nach Nutzereingabe das Schiff entsprechend platziert.
    Eine Sperrzone wird eingerichtet, um Schiffberührungen zu vermeiden.

    Args:
        spielfeld (spielfeld): Das Spielfeld des aktuellen Spielers
        schiffl (int): Länge des Schiffes
        zeichen (int): Position des Buchstabens auf dem Spielfeld
        zahl (int): Eingegebene Zahl des Spielers

    Returns:
        (bool): Rückmeldung, ob Eingabewert möglich ist
    """

    richtung_ausgabe = {"oben": False, "unten": False,
                        "links": False, "rechts": False}

    if schifflänge <= (zeichen+1):
        fall_eins(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe)

    if schifflänge <= (10-zeichen):
        fall_zwei(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe)

    if schifflänge <= zahl:
        fall_drei(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe)

    if schifflänge <= (11-zahl):
        fall_vier(spielfeld, zeichen, schifflänge, zahl, richtung_ausgabe)

    checke_links(richtung_ausgabe)
    checke_rechts(richtung_ausgabe)
    checke_oben(richtung_ausgabe)
    checke_unten(richtung_ausgabe)
    if not (richtung_ausgabe["links"] is True or richtung_ausgabe["rechts"] or richtung_ausgabe["oben"] is True or richtung_ausgabe["unten"] is True):
        return False

    end = True

    while end:
        eingabe = input(
            "\nWähle aus, in welche Richtung das Schiff platziert werden soll:\n")
        eingabe = eingabe.upper()
        if eingabe == "L" and richtung_ausgabe["links"] is True:
            end = mach_links(spielfeld, zeichen, schifflänge, zahl, end)
            return True

        if eingabe == "R" and richtung_ausgabe["rechts"] is True:
            end = mach_rechts(spielfeld, zeichen, schifflänge, zahl, end)
            return True

        if eingabe == "O" and richtung_ausgabe["oben"] is True:
            end = mach_oben(spielfeld, zeichen, schifflänge, zahl, end)
            return True

        if eingabe == "U" and richtung_ausgabe["unten"] is True:
            end = mach_unten(spielfeld, zeichen, schifflänge, zahl, end)
            return True

        print("Ungültige Eingabe.")


def gewinner_suchen(gegnerisches_spielfeld_spieler1, gegnerisches_spielfeld_spieler2):
    """Checkt, ob ein Spieler alle Schiffe versenkt und somit gewonnen hat.

    Args:
        gegnerisches_spielfeld_spieler1 (spielfeld): Spielfeld Spieler 1
        gegnerisches_spielfeld_spieler2 (spielfeld): Spielfeld Spieler 2

    Returns:
        (bool): True, wenn ein Spieler gewonnen hat.
    """
    anzahl_spieler1 = 0
    anzahl_spieler2 = 0
    for i in range(1, 11):
        for feld in gegnerisches_spielfeld_spieler1.felder[i-1]:
            if(feld) == "X":
                anzahl_spieler1 += 1

    for i in range(1, 11):
        for feld in gegnerisches_spielfeld_spieler2.felder[i-1]:
            if(feld) == "X":
                anzahl_spieler2 += 1

    if (anzahl_spieler1) == 30:
        print(
            f"\nGlückwunsch, Spieler {gegnerisches_spielfeld_spieler1.spielername} hat gewonnen!\n")
        print("-----Das Spiel ist beendet------")
        return True
    if (anzahl_spieler2) == 30:
        print(
            f"\nGlückwunsch, Spieler {gegnerisches_spielfeld_spieler2.spielername} hat gewonnen!\n")
        print("-----Das Spiel ist beendet------")
        return True
    return False


def schiff_versenkt(verteidiger_spielfeld, zahl, zeichen):
    """Erkennt, ob Schiff versenkt wurde.

    Args:
        verteidiger_spielfeld (spielfeld): Spielfeld
        zahl (int): Eingegebene Zahl
        zeichen (int): Eingegebener Buchstabe

    Returns:
        bool: Ob Schiff versenkt wurde
    """
    versenkt = True
    if zahl >= 2:
        i = zahl
        while i >= 2 and not verteidiger_spielfeld.felder[i-2][zeichen] == '-':
            if verteidiger_spielfeld.felder[i-2][zeichen] == 'O':
                versenkt = False
                break
            i -= 1
    if zahl <= 9:
        i = zahl
        while i <= 9 and not verteidiger_spielfeld.felder[i][zeichen] == '-':
            if verteidiger_spielfeld.felder[i][zeichen] == 'O':
                versenkt = False
                break
            i += 1
    if zeichen >= 1:
        i = zeichen
        while i >= 1 and not verteidiger_spielfeld.felder[zahl-1][i-1] == '-':
            if verteidiger_spielfeld.felder[zahl-1][i-1] == 'O':
                versenkt = False
                break
            i -= 1
    if zeichen <= 8:
        i = zeichen
        while i <= 8 and not verteidiger_spielfeld.felder[zahl-1][i+1] == '-':
            if verteidiger_spielfeld.felder[zahl-1][i+1] == 'O':
                versenkt = False
                break
            i += 1

    return versenkt


def schiff_abschießen(alle_spielfelder, runde):
    """Die Funktion erkennt Bot oder Spieler und deren korrekte Feldeingabe.
    Dann wird auf das gewählte Feld geschossen und bei einem Treffer der Zug verlängert

    Args:
        alle_spielfelder (list): Liste aller Spielfeld Objekte
        runde (int): Rundenzahl

    Returns:
        bool: returned True um Funktion und Spiel zu beenden
    """
    buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    if runde % 2 == 0:
        angreifer = alle_spielfelder[1]
        gegnerisches_spielfeld_angreifer = alle_spielfelder[3]
        verteidiger = alle_spielfelder[0]
    else:
        angreifer = alle_spielfelder[0]
        gegnerisches_spielfeld_angreifer = alle_spielfelder[2]
        verteidiger = alle_spielfelder[1]

    print(f"{angreifer.spielername} greift an:\n")

    if angreifer.spielername != "B0T":
        spielfeld_erstellen(angreifer, gegnerisches_spielfeld_angreifer)
    speicher_buchstabe = ""
    speicher_zahl = 0
    getroffen = False
    start = True
    wiederholt = False
    while getroffen or start or wiederholt:
        start = False
        gewonnen = gewinner_suchen(
            alle_spielfelder[2], alle_spielfelder[3])
        if gewonnen:
            datei_loeschen("Kontenspeicherung.json")
            return True
        end = True
        while end:
            feld = feld_generieren(angreifer, getroffen,
                                   speicher_buchstabe, speicher_zahl)
            for zeichen, buchstabe in enumerate(buchstaben):
                if len(feld) > 1:
                    if feld[0] == buchstabe:
                        spielfelder = [
                            angreifer, gegnerisches_spielfeld_angreifer, verteidiger]
                        getroffen, end, speicher_buchstabe, speicher_zahl, wiederholt = finde_zahl_abschießen(
                            spielfelder, zeichen, feld, buchstabe)
            if end:
                print("Ungültige Eingabe")

    runde += 1
    if angreifer.spielername != "B0T":
        input("Dein Zug ist beendet. Der andere Spieler ist am Zug. Drücke Enter.")
        os.system('cls' if os.name == 'nt' else 'clear')
        input("Drücke Enter.")
    else:
        input("Der Bot hat seinen Zug beendet. Drücke Enter.")
    os.system('cls' if os.name == 'nt' else 'clear')
    namen = [alle_spielfelder[0].spielername, alle_spielfelder[1].spielername]
    speichern(alle_spielfelder, namen, runde)
    schiff_abschießen(alle_spielfelder, runde)


def finde_zahl_abschießen(spielfelder, zeichen, feld, buchstabe):
    """Hilffunktion für schiff_abschießen, um auf die Zahl zu überprüfen.

    Returns:
        (bool, bool, str, int, bool): getroffen, end, speicher_buchstabe, speicher_zahl, wiederholt
    """
    getroffen = False
    versenkt = False
    end = True
    wiederholt = False
    speicher_buchstabe = ""
    speicher_zahl = 0
    angreifer = spielfelder[0]
    gegnerisches_spielfeld_angreifer = spielfelder[1]
    verteidiger = spielfelder[2]
    try:
        # Prüfen ob die Eingabe eine 10 ist
        try:
            if int(feld[1]) == 1 and int(feld[2]) == 0:
                getroffen, wiederholt = gegnerisches_spielfeld_angreifer.feld_beschießen(
                    verteidiger, 9, zeichen)
                if angreifer.spielername != "B0T":
                    spielfeld_erstellen(
                        angreifer, gegnerisches_spielfeld_angreifer)
                else:
                    print(
                        f"Bot hat auf Feld {buchstabe}10 geschossen.\n")
                if getroffen:
                    versenkt = schiff_versenkt(
                        verteidiger, 10, zeichen)
                    speicher_buchstabe = buchstabe
                    speicher_zahl = 10
                end = False
        except IndexError:
            end = True
        for zahl in range(1, 10):
            if int(feld[1]) == zahl and len(feld) == 2:
                getroffen, wiederholt = gegnerisches_spielfeld_angreifer.feld_beschießen(
                    verteidiger, zahl-1, zeichen)
                if angreifer.spielername != "B0T":
                    spielfeld_erstellen(
                        angreifer, gegnerisches_spielfeld_angreifer)
                else:
                    print(
                        f"Bot hat auf Feld {buchstabe}{zahl} geschossen.\n")
                if getroffen:
                    versenkt = schiff_versenkt(
                        verteidiger, zahl, zeichen)
                    speicher_buchstabe = buchstabe
                    speicher_zahl = zahl
                end = False
                break
    except ValueError:
        end = True
    if versenkt:
        print("\nSchiff versenkt! Glückwunsch")
    return getroffen, end, speicher_buchstabe, speicher_zahl, wiederholt


def feld_generieren(angreifer, getroffen, speicher_buchstabe, speicher_zahl):
    """Hilffunktion für schiff_abschießen in der das Spielfeld ausgewählt wird je nach Bot oder Spieler

    Args:
        angreifer (spielfeld): Spielfeld Angreifer
        getroffen (bool): wurde getroffen
        speicher_buchstabe (str): Buchstabe, der zuletzt gewählt wurde
        speicher_zahl (int): Zahl, die zuletzt gewählt wurde

    Returns:
        str: ausgewähltes Feld
    """
    if angreifer.spielername == "B0T":
        feld = ComputerGegner.feld_auswahl(
            getroffen, speicher_buchstabe, speicher_zahl)
    else:
        feld = input("\nAuf welches Feld möchtest du schießen?\n")
    return feld


def main():
    """Hier startet das Programm und durchläuft den gesamten Spielablauf.
    Je nach Spielermodus ist der Ablauf verändert.
    """
    os.system("")

    spielstaende = spielstand_auslesen()

    bool_ok = True
    if spielstaende is None:
        bool_ok = False

    print(print_bild())

    modus = startbildschirm(bool_ok)

    if modus in (1, 2):

        namen = beginner_auslosen(modus)

        spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_für_spieler1,\
            gegnerisches_spielfeld_für_spieler2 = spielfelder_erzeugen(namen)
        alle_spielfelder = [spielfeld_spieler1, spielfeld_spieler2,
                            gegnerisches_spielfeld_für_spieler1, gegnerisches_spielfeld_für_spieler2]

        spielfeld_erstellen(spielfeld_spieler1,
                            gegnerisches_spielfeld_für_spieler1)
        print(f"\n{namen[0]} ist am Zug.")

        schiffe_setzen(spielfeld_spieler1, gegnerisches_spielfeld_für_spieler1)

        if namen[1] != "B0T":
            input(f"\n{namen[1]} ist am Zug. Drücke Enter.")
            os.system('cls' if os.name == 'nt' else 'clear')

            spielfeld_erstellen(spielfeld_spieler2,
                                gegnerisches_spielfeld_für_spieler2)

            print(f"{namen[1]} ist am Zug.")

            schiffe_setzen(spielfeld_spieler2,
                           gegnerisches_spielfeld_für_spieler2)
            speichern(alle_spielfelder, namen, 1)

            os.system('cls' if os.name == 'nt' else 'clear')
            input(f"{namen[0]} ist am Zug. Drücke Enter.")
            schiff_abschießen(alle_spielfelder, 1)
        else:

            ComputerGegner.schiffe_setzen(spielfeld_spieler2)
            print("\n\n------------------------------------")
            print("Der Bot hat seine Schiffe platziert.")
            print("------------------------------------\n")
            speichern(alle_spielfelder, namen, 1)
            schiff_abschießen(alle_spielfelder, 1)
    else:
        spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_für_spieler1,\
            gegnerisches_spielfeld_für_spieler2 = spielfelder_laden(
                spielstaende)
        runde, namen = runde_und_namen_laden(spielstaende)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Das Spiel befand sich in Runde " + str(runde))

        alle_spielfelder = [spielfeld_spieler1, spielfeld_spieler2,
                            gegnerisches_spielfeld_für_spieler1, gegnerisches_spielfeld_für_spieler2]

        print("Die Namen der Spieler lauten: " +
              namen["Spieler1"] + " & " + namen["Spieler2"] + "\n")

        schiff_abschießen(alle_spielfelder, runde)


if __name__ == "__main__":
    main()
