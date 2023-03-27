#!/usr/bin/python
"""Dieses File enthält Die Computergegner Klasse, in der die Botfunktionalität aufgerufen wird.
"""

import random


class ComputerGegner:
    """Diese Klasse enthält statisch alle Bot Funktionalitäten
    """
    @staticmethod
    def ausgelagerte_funktion(_feld, spielfeld, _schifflaenge, zeichen):
        """Ausgelagerte Funktion für den Bot, die schaut, ob das Schiff platzierbar ist.

        Args:
            _feld (list): Enthält Feldauswahl des Bots
            spielfeld (spielfeld): Spielfeld Objekt des Bots
            _schiffl (int): Schifflänge
            zeichen (int): Buchstabe auf Spielfeld

        Returns:
            bool: Ob Schiff auf dem Feld platzierbar ist
        """

        for zahl in range(1, 11):
            if int(_feld[1]) == zahl:
                moegliche_richtungen = ComputerGegner.setz_richtung_generieren(
                    spielfeld, _schifflaenge, zeichen, zahl)
                if (len(moegliche_richtungen)) == 0:
                    _platzierbar = False
                    break
                ausgewaehlte_richtung = random.choice(moegliche_richtungen)
                ComputerGegner.richtung_setzen(
                    spielfeld, ausgewaehlte_richtung, _schifflaenge, zeichen, zahl)
                _platzierbar = True
        return _platzierbar

    @staticmethod
    def schiffe_setzen(spielfeld):
        """Funktion setzt alle Schiffe zufällig für den Bot.

        Args:
            spielfeld (spielfeld): Spielfeld des Bots
        """

        _buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        _schiffe = ["Schlachtschiff", "Kreuzer", "Kreuzer", "Zerstörer",
                    "Zerstörer", "Zerstörer", "U-Boot", "U-Boot", "U-Boot", "U-Boot"]
        _schiffwert = {"Schlachtschiff": 5,
                       "Kreuzer": 4, "Zerstörer": 3, "U-Boot": 2}
        _zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        for schiff in _schiffe:
            _schifflaenge = _schiffwert[schiff]
            _platzierbar = False
            while not _platzierbar:
                _feld = ["A", "1"]
                _feld[0] = random.choice(_buchstaben)
                _feld[1] = random.choice(_zahlen)
                # für jedes Zeichen kriegt er eine Nummer (zeichen: int)
                for zeichen, buchstabe in enumerate(_buchstaben):
                    if _feld[0] == buchstabe:
                        _platzierbar = ComputerGegner.ausgelagerte_funktion(
                            _feld, spielfeld, _schifflaenge, zeichen)

    @staticmethod
    def for_schleife_1(spielfeld, zeichen, schifflaenge, zahl, richtungen):
        """Ausgelagerte for Schleife

        Args:
            spielfeld (spielfeld): Spielfeld des Bots
            zeichen (int): Buchstabe auf Feld
            schifflaenge (int): Schifflänge
            zahl (int): Zahl auf Spielfeld
            richtungen (list): Liste mit allen möglichen Richtungen zum platzieren

        Returns:
            bool: _check_obj
        """
        _check_obj = True
        for i in range(zeichen-schifflaenge, zeichen):
            if spielfeld.felder[zahl-1][i+1] == "O" or spielfeld.felder[zahl-1][i+1] == "-":
                _check_obj = False
        if _check_obj:
            richtungen.append('Links')
        return _check_obj

    @staticmethod
    def for_schleife_2(spielfeld, zeichen, schifflaenge, zahl, richtungen):
        """Ausgelagerte for Schleife

        Args:
            spielfeld (spielfeld): Spielfeld des Bots
            zeichen (int): Buchstabe auf Feld
            schifflaenge (int): Schifflänge
            zahl (int): Zahl auf Spielfeld
            richtungen (list): Liste mit allen möglichen Richtungen zum platzieren

        Returns:
            bool: _check_obj
        """
        _check_obj = True
        for i in range(zeichen, zeichen+schifflaenge):
            if spielfeld.felder[zahl-1][i] == "O" or spielfeld.felder[zahl-1][i] == "-":
                _check_obj = False
        if _check_obj:
            richtungen.append('Rechts')
        return _check_obj

    @staticmethod
    def for_schleife_3(spielfeld, zeichen, schifflaenge, zahl, richtungen):
        """Ausgelagerte for Schleife

        Args:
            spielfeld (spielfeld): Spielfeld des Bots
            zeichen (int): Buchstabe auf Feld
            schifflaenge (int): Schifflänge
            zahl (int): Zahl auf Spielfeld
            richtungen (list): Liste mit allen möglichen Richtungen zum platzieren

        Returns:
            bool: _check_obj
        """
        _check_obj = True
        for i in range(zahl-schifflaenge, zahl):
            if spielfeld.felder[i][zeichen] == "O" or spielfeld.felder[i][zeichen] == "-":
                _check_obj = False
        if _check_obj:
            richtungen.append('Oben')
        return _check_obj

    @staticmethod
    def for_schleife_4(spielfeld, zeichen, schifflaenge, zahl, richtungen):
        """Ausgelagerte for Schleife

        Args:
            spielfeld (spielfeld): Spielfeld des Bots
            zeichen (int): Buchstabe auf Feld
            schifflaenge (int): Schifflänge
            zahl (int): Zahl auf Spielfeld
            richtungen (list): Liste mit allen möglichen Richtungen zum platzieren

        Returns:
            bool: _check_obj
        """
        _check_obj = True
        for i in range(zahl, zahl+schifflaenge):
            if spielfeld.felder[i-1][zeichen] == "O" or spielfeld.felder[i-1][zeichen] == "-":
                _check_obj = False
        if _check_obj:
            richtungen.append('Unten')
        return _check_obj

    @staticmethod
    def setz_richtung_generieren(spielfeld, schifflaenge, zeichen, zahl):
        """In dieser Funktion überprüft der Bot, ob er die Schiffe richtig
        platzieren kann.
        Eine Sperrzone wird eingerichtet, um Schiffberührungen zu vermeiden.

        Args:
            spielfeld (spielfeld): Das Spielfeld des aktuellen Spielers
            schiffl (int): Länge des Schiffes
            zeichen (int): Position des Buchstabens auf dem Spielfeld
            zahl (int): Eingegebene Zahl des Spielers

        Returns:
            bool: Rückmeldung, ob Eingabewert möglich ist
            array: welche Richtungen möglich sind
        """
        richtungen = []

        if schifflaenge <= (zeichen+1):  # zeichen = Buchstabe
            ComputerGegner.for_schleife_1(
                spielfeld, zeichen, schifflaenge, zahl, richtungen)
        if schifflaenge <= (10-zeichen):
            ComputerGegner.for_schleife_2(
                spielfeld, zeichen, schifflaenge, zahl, richtungen)
        if schifflaenge <= zahl:
            ComputerGegner.for_schleife_3(
                spielfeld, zeichen, schifflaenge, zahl, richtungen)
        if schifflaenge <= (11-zahl):
            ComputerGegner.for_schleife_4(
                spielfeld, zeichen, schifflaenge, zahl, richtungen)
        return richtungen

    @staticmethod
    def richtung_setzen(spielfeld, richtung, schifflaenge, zeichen, zahl):
        """Hier setzt die Methode die zufällig eingegebene Richtung
         auf dem Spielfeld um

        Args:
            spielfeld (spielfeld): Spielfeld des Bots
            richtung (str): Richtung, in die gesetzt werden soll
            schiffl (int): Länge des zu setzenden Schiffes
            zeichen (int): Position des gewählten Buchstabens
            zahl (int): Gewählte Zahl
        """
        if richtung == "Links":
            for i in range(zeichen-schifflaenge, zeichen):
                spielfeld.feld_zuweisen(zahl-1, i+1)
                spielfeld.sperrfeld_zuweisen(zahl-2, i+1)
                spielfeld.sperrfeld_zuweisen(zahl, i+1)
            spielfeld.sperrfeld_zuweisen(zahl-1, zeichen-schifflaenge)
            spielfeld.sperrfeld_zuweisen(zahl-1, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen-schifflaenge)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen-schifflaenge)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen+1)

        elif richtung == "Rechts":
            for i in range(zeichen, zeichen+schifflaenge):
                spielfeld.feld_zuweisen(zahl-1, i)
                spielfeld.sperrfeld_zuweisen(zahl-2, i)
                spielfeld.sperrfeld_zuweisen(zahl, i)
            spielfeld.sperrfeld_zuweisen(zahl-1, zeichen+schifflaenge)
            spielfeld.sperrfeld_zuweisen(zahl-1, zeichen-1)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen+schifflaenge)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen-1)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen+schifflaenge)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen-1)

        elif richtung == "Oben":
            for i in range(zahl-schifflaenge, zahl):
                spielfeld.feld_zuweisen(i, zeichen)
                spielfeld.sperrfeld_zuweisen(i, zeichen-1)
                spielfeld.sperrfeld_zuweisen(i, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl-schifflaenge-1, zeichen-1)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen-1)
            spielfeld.sperrfeld_zuweisen(zahl-schifflaenge-1, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl-schifflaenge-1, zeichen)
            spielfeld.sperrfeld_zuweisen(zahl, zeichen)

        elif richtung == "Unten":
            for i in range(zahl, zahl+schifflaenge):
                spielfeld.feld_zuweisen(i-1, zeichen)
                spielfeld.sperrfeld_zuweisen(i-1, zeichen-1)
                spielfeld.sperrfeld_zuweisen(i-1, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen-1)
            spielfeld.sperrfeld_zuweisen(zahl+schifflaenge-1, zeichen-1)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl+schifflaenge-1, zeichen+1)
            spielfeld.sperrfeld_zuweisen(zahl-2, zeichen)
            spielfeld.sperrfeld_zuweisen(zahl+schifflaenge-1, zeichen)

    @staticmethod
    def feld_auswahl(getroffen, speicher_buchstabe, speicher_zahl):
        """Generiert zufälliges Feld oder wählt benachbartes Feld, wenn davor getroffen wurde

        Args:
            getroffen (bool): wurde getroffen
            speicher_buchstabe (str): letzter gewählter Buchstabe
            speicher_zahl (int): letzte gewählte Zahl

        Returns:
            (str): neue Feldauswahl
        """

        buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        feld = ["", ""]

        if not getroffen:

            feld[0] = random.choice(buchstaben)
            feld[1] = random.choice(zahlen)
            strfeld = "".join(feld)
            return strfeld
        auswahl_liste = []
        for i, buchstabe in enumerate(buchstaben):
            if buchstabe == speicher_buchstabe:
                if i != 0:
                    feld[0] = buchstaben[i-1]
                    feld[1] = str(speicher_zahl)
                    strauswahl = "".join(feld)
                    auswahl_liste.append(strauswahl)
                if i != 9:
                    feld[0] = buchstaben[i+1]
                    feld[1] = str(speicher_zahl)
                    strauswahl = "".join(feld)
                    auswahl_liste.append(strauswahl)
                if speicher_zahl != 10:
                    feld[0] = buchstaben[i]
                    feld[1] = str(speicher_zahl+1)
                    strauswahl = "".join(feld)
                    auswahl_liste.append(strauswahl)
                if speicher_zahl != 1:
                    feld[0] = buchstaben[i]
                    feld[1] = str(speicher_zahl-1)
                    strauswahl = "".join(feld)
                    auswahl_liste.append(strauswahl)

        return random.choice(auswahl_liste)
