#!/usr/bin/python
"""Dieses File enthält die Spielfeld Klasse,
in der die Spielfeld Listen erstellt und bearbeitet werden.
    """
# Felder erklärung: 1 ist standard,
# O hier ist ein eigenes Schiff,
# X hier liegt ein getroffenes gegnerisches Schiff
# S hier ist ein eigenes Schiff getroffen,
# N ist ein Feld ohne gegnerisches Schiff


class Spielfeld:
    """Diese Klasse erstellt und bearbeitet die Spielfeld Listen.
    """

    def __init__(self, felder, spielername):
        self.felder = felder
        self.spielername = spielername

    def feld_zuweisen(self, feldnummer, buchstabe):
        """Setzt ein Schiffteil auf die Spielfeld Liste.

        Args:
            feldnummer (int): Zeile (Zahl), auf die platziert wird
            buchstabe (int): Spalte (Buchstabe), auf die platziert wird
        """
        self.felder[feldnummer][buchstabe] = "O"

    def sperrfeld_zuweisen(self, feldnummer, buchstabe):
        """Setzt ein Sperrfeld auf die Spielfeld Liste

        Args:
            feldnummer (int): Zeile (Zahl), auf die platziert wird
            buchstabe (int): Spalte (Buchstabe), auf die platziert wird
        """
        if (0 <= feldnummer <= 9) and (0 <= buchstabe <= 9):
            self.felder[feldnummer][buchstabe] = "-"

    def feld_beschießen(self, angegriffenes_spielfeld, feldnummer, buchstabe):
        """Setzt eine Treffermarkierung auf die Spielfeldliste oder markiert einen
        Wassertreffer. Spielfeld und gegnerisches Spielfeld werden aktualisiert.

        Args:
            angegriffenes_spielfeld (spielfeld): Spielfeld des Verteidigers
            feldnummer (int): Zahl auf Spielfeld
            buchstabe (int): Buchstabe auf Spielfeld

        Returns:
            getroffen (bool): Wurde ein Schiff getroffen?
            wiederholt (bool): Wurde das Feld bereits beschossen?
        """
        wiederholt = False
        print("\n------Schuss------")
        if angegriffenes_spielfeld.felder[feldnummer][buchstabe] == "O":
            print("Treffer!")
            angegriffenes_spielfeld.felder[feldnummer][buchstabe] = "S"
            self.felder[feldnummer][buchstabe] = "X"
            getroffen = True
        elif angegriffenes_spielfeld.felder[feldnummer][buchstabe] == "S":
            print("Auf diesem Feld hast du bereits ein Schiffteil getroffen!")
            getroffen = True
        else:
            getroffen = False
            if self.felder[feldnummer][buchstabe] == "N":
                print("Auf dieses Feld hast du bereits geschossen!")
                wiederholt = True
            self.felder[feldnummer][buchstabe] = "N"
            print("Leider daneben")
        print("------------------")
        return getroffen, wiederholt
