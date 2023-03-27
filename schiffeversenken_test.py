# pylint: disable=C
from schiffeversenken import startbildschirm, beginner_auslosen, spielfelder_erzeugen, farbiges_spielfeld, spielstand_auslesen, spielfeld_erstellen, schiffe_setzen, gewinner_suchen, speichern, schiff_versenkt, runde_und_namen_laden, spielfelder_laden, finde_zahl, setz_richtung_generieren, schiff_abschießen, main, feld_generieren, finde_zahl_abschießen
import spielfeld_klasse
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import json
import os


class Test_schiffeversenken(TestCase):
    def setUp(self):
        self.spieler1_spielfeld_objekt = spielfeld_klasse.Spielfeld(
            [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "")

        self.spieler2_spielfeld_objekt = spielfeld_klasse.Spielfeld(
            [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "")

        self.spieler1_geg_spielfeld_objekt = spielfeld_klasse.Spielfeld(
            [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10], "")

        self.spieler2_geg_spielfeld_objekt = spielfeld_klasse.Spielfeld(
            [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10], "")

        self.gegnerisches_spielfeld_leer = spielfeld_klasse.Spielfeld(
            [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10], "Verlierer")

        self.gegnerisches_spielfeld_sieg1 = spielfeld_klasse.Spielfeld(
            [["X"]*10, ["X"]*10, ["X"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10], "Sieger1")

        self.kontenspeicherung = {
            "Spieler": {
                "Spieler1": "Chap",
                "Spieler2": "Chip"
            },
            "Runde": 1,
            "Spielfelder": [
                [
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
                ],
                [
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                    ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
                ],
                [
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]
                ],
                [
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]
                ]
            ]
        }

    def test_startbildschirm_modus_1(self):
        with patch("sys.stdin", new=StringIO("1")):
            wert = startbildschirm(True)
            self.assertEqual(wert, 1)

    def test_startbildschirm_modus_2(self):
        with patch("sys.stdin", new=StringIO("2")):
            wert = startbildschirm(False)
            self.assertEqual(wert, 2)

    def test_startbildschirm_modus3(self):
        with patch("sys.stdin", new=StringIO("3")):
            wert = startbildschirm(True)
            self.assertEqual(wert, 3)

    def test_startbildschirm_ungueltige_Eingabe(self):
        with patch('builtins.input', side_effect=['Hallo', "1"]), patch('sys.stdout', new=StringIO()) as fake_out:

            wert = startbildschirm(False)
            lines = fake_out.getvalue().splitlines()
            self.assertIn('Ungültige Eingabe', lines)
            self.assertEqual(wert, 1)

    def test_spielfelder_erzeugen_instanz(self):
        spielfeld_spieler1 = spielfelder_erzeugen([
            "Tobi", "Lukas"])

        self.assertIsInstance(
            spielfeld_spieler1[0], spielfeld_klasse.Spielfeld)

    def test_spielfelder_erzeugen_spielfeld1_name(self):
        spielfeld_spieler1 = spielfelder_erzeugen([
            "Tobi", "Lukas"])

        self.assertEqual(spielfeld_spieler1[0].spielername, "Tobi")
        self.assertEqual(
            spielfeld_spieler1[2].spielername, "Tobi")

    def test_spielfelder_erzeugen_spielfeld2_name(self):
        spielfeld_spieler1 = spielfelder_erzeugen([
            "Tobi", "Lukas"])

        self.assertEqual(spielfeld_spieler1[1].spielername, "Lukas")
        self.assertEqual(
            spielfeld_spieler1[3].spielername, "Lukas")

    def test_spielfelder_erzeugen_spielfelder(self):
        spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_für_spieler1, \
            gegnerisches_spielfeld_für_spieler2 = spielfelder_erzeugen([
                                                                       "Tobi", "Lukas"])

        test_spielfeld_s1 = test_spielfeld_s2 = [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10,
                                                 ["~"]*10, ["~"]*10, ["~"]*10]
        test_gegnerisches_spielfeld_s1 = test_gegnerisches_spielfeld_s2 = [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10,
                                                                           ["?"]*10, ["?"]*10, ["?"]*10]

        self.assertEqual(test_spielfeld_s1, spielfeld_spieler1.felder)
        self.assertEqual(test_spielfeld_s2, spielfeld_spieler2.felder)
        self.assertEqual(test_gegnerisches_spielfeld_s1,
                         gegnerisches_spielfeld_für_spieler1.felder)
        self.assertEqual(test_gegnerisches_spielfeld_s2,
                         gegnerisches_spielfeld_für_spieler2.felder)

    def test_spielstand_auslesen_leeres_dict(self):
        leeres_dict = {}
        with open('Kontenspeicherung.json', 'w') as fp:
            json.dump(leeres_dict, fp)
        spielstaende = spielstand_auslesen()
        self.assertIsNone(spielstaende)

    def test_spielstand_auslesen_exisitiert_pfad(self):
        if os.path.exists('Kontenspeicherung.json'):
            os.remove('Kontenspeicherung.json')
        spielstaende = spielstand_auslesen()
        self.assertIsNone(spielstaende)

    def test_spielstand_auslesen_leere_datei(self):
        new_file = open('Kontenspeicherung.json', 'w')
        new_file.close()
        spielstaende = spielstand_auslesen()
        self.assertIsNone(spielstaende)

    def test_spielfeld_erstellen(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            spielfeld_erstellen(self.spieler1_spielfeld_objekt,
                                self.spieler2_spielfeld_objekt)
            lines = fake_out.getvalue().splitlines()
            self.assertIn("1   \x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m    1   \x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m  1 ", lines)
            self.assertIn("10  \x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m    10  \x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m\x1b[44m ~ \x1b[0m  10 ", lines)

    def test_gewinner_suchen_kein_sieger(self):
        bool_gewinner = gewinner_suchen(
            self.gegnerisches_spielfeld_leer, self.gegnerisches_spielfeld_leer)
        self.assertFalse(bool_gewinner)

    def test_gewinner_suchen_spieler1_sieger(self):
        bool_gewinner = gewinner_suchen(
            self.gegnerisches_spielfeld_sieg1, self.gegnerisches_spielfeld_leer)
        self.assertTrue(bool_gewinner)

    def test_gewinner_suchen_spieler2_sieger(self):
        bool_gewinner = gewinner_suchen(
            self.gegnerisches_spielfeld_leer, self.gegnerisches_spielfeld_sieg1)
        self.assertTrue(bool_gewinner)

    def test_gewinner_suchen_spieler1_print(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            gewinner_suchen(
                self.gegnerisches_spielfeld_sieg1, self.gegnerisches_spielfeld_leer)
            lines = fake_out.getvalue().splitlines()
            self.assertIn("Glückwunsch, Spieler Sieger1 hat gewonnen!", lines)

    def test_gewinner_suchen_spieler2_print(self):
        gegnerisches_spielfeld_sieg2 = spielfeld_klasse.Spielfeld(
            [["X"]*10, ["X"]*10, ["X"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10], "Sieger2")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            gewinner_suchen(
                self.gegnerisches_spielfeld_leer, gegnerisches_spielfeld_sieg2)
            lines = fake_out.getvalue().splitlines()
            self.assertIn("Glückwunsch, Spieler Sieger2 hat gewonnen!", lines)

    def test_speichern(self):
        alle_spielfelder = [self.spieler1_spielfeld_objekt, self.spieler2_spielfeld_objekt,
                            self.spieler1_geg_spielfeld_objekt, self.spieler2_geg_spielfeld_objekt]
        namen = ["Chap", "Chip"]
        runde = 1
        speichern(alle_spielfelder, namen, runde)
        with open('Kontenspeicherung.json') as json_file:
            speicher = json.load(json_file)
        self.assertDictEqual(self.kontenspeicherung, speicher)

    def test_schiff_abschießen_mit_spielern(self):
        os.system("")
        spieler1_spielfeld = spielfeld_klasse.Spielfeld([["~"]*10, ["~"]*10, ["~"]*10, [
                                                        "~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["O"]*10, ["O"]*10, ["O"]*10], "Person1")
        spieler2_spielfeld = spielfeld_klasse.Spielfeld([["O"]*10, ["O"]*10, ["O"]*10, [
                                                        "~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "Person2")
        with patch("builtins.input", side_effect=["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7"]):

            alle_spielfelder = [spieler1_spielfeld, spieler2_spielfeld,
                                self.spieler1_geg_spielfeld_objekt, self.spieler2_geg_spielfeld_objekt]
            fertig = schiff_abschießen(alle_spielfelder, 1)
        self.assertTrue(fertig)

    def test_schiff_abschießen_ungueltige_eingabe(self):
        os.system("")
        spieler1_spielfeld = spielfeld_klasse.Spielfeld([["~"]*10, ["~"]*10, ["~"]*10, [
                                                        "~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["O"]*10, ["O"]*10, ["O"]*10], "Person1")
        spieler2_spielfeld = spielfeld_klasse.Spielfeld([["O"]*10, ["O"]*10, ["O"]*10, [
                                                        "~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "Person2")
        with patch("builtins.input", side_effect=["A10", " ", " ", "A1", " ", " ", "#", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7"]), patch('sys.stdout', new=StringIO()) as fake_out:

            alle_spielfelder = [spieler1_spielfeld, spieler2_spielfeld,
                                self.spieler1_geg_spielfeld_objekt, self.spieler2_geg_spielfeld_objekt]
            schiff_abschießen(alle_spielfelder, 1)
            self.assertIn("Ungültige Eingabe",
                          fake_out.getvalue().splitlines())

    def test_schiff_abschießen_mit_bot(self):
        os.system("")
        spieler1_spielfeld = spielfeld_klasse.Spielfeld([["~"]*10, ["~"]*10, ["~"]*10, [
                                                        "~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["O"]*10, ["O"]*10, ["O"]*10], "Person1")
        bot_spielfeld = spielfeld_klasse.Spielfeld([["O"]*10, ["O"]*10, ["O"]*10, [
            "~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "B0T")
        with patch("builtins.input", side_effect=[" ", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7"]):

            alle_spielfelder = [bot_spielfeld, spieler1_spielfeld, self.spieler2_geg_spielfeld_objekt,
                                self.spieler1_geg_spielfeld_objekt]
            schiff_abschießen(alle_spielfelder, 1)

    @staticmethod
    def test_main_mit_spielern():
        with patch("builtins.input", side_effect=["1", "Anna", "Marvin", "A1", "r", "A3", "r", "A5", "r", "A7", "r", "A9", "r", "J1", "l", "J3", "l", "J5", "l", "F3", "u", "G10", "o", " ", "A1", "r", "A3", "r", "A5", "r", "A7", "r", "A9", "r", "J1", "l", "J3", "l", "J5", "l", "F3", "u", "G10", "o", " ", "A1", "A3", "A5", "A7", "A9", "J1", "J3", "J5", "F3", "G10", "B1", "B3", "B5", "B7", "B9", "C1", "C3", "C5", "C7", "C9", "D1", "D3", "D5", "E1", "F3", "F4", "G9", "G10", "H1", "I1", "I3", "I5", "J1", "J3", "J5"]):
            main()

    @staticmethod
    def test_main_mit_modus3():
        with open('Kontenspeicherung.json', 'w') as json_file:
            json.dump({"Spieler": {"Spieler1": "Marvin", "Spieler2": "Anna"}, "Runde": 1, "Spielfelder": [[["O", "O", "O", "O", "O", "-", "-", "O", "O", "O"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["O", "O", "O", "O", "-", "O", "-", "-", "O", "O"], ["-", "-", "-", "-", "-", "O", "-", "-", "-", "-"], ["O", "O", "O", "O", "-", "-", "-", "-", "O", "O"], ["-", "-", "-", "-", "-", "~", "~", "-", "-", "-"], ["O", "O", "O", "-", "~", "~", "~", "~", "~", "~"], ["-", "-", "-", "-", "~", "-", "-", "-", "~", "~"], ["O", "O", "O", "-", "~", "-", "O", "-", "~", "~"], ["-", "-", "-", "-", "~", "-", "O", "-", "~", "~"]], [["O", "O", "O", "O", "O", "-", "-", "O", "O", "O"], ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ["O", "O", "O", "O", "-", "O", "-", "-", "O", "O"], ["-", "-", "-", "-", "-", "O", "-", "-", "-", "-"], ["O", "O", "O", "O", "-", "-", "-", "-", "O", "O"], ["-", "-", "-", "-", "-", "~", "~", "-", "-", "-"], ["O", "O", "O", "-", "~", "~", "~", "~", "~", "~"], ["-", "-", "-", "-", "~", "-", "-", "-", "~", "~"], ["O", "O", "O", "-", "~", "-", "O", "-", "~", "~"], [
                      "-", "-", "-", "-", "~", "-", "O", "-", "~", "~"]], [["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]], [["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"], ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]]]}, json_file, indent=4)
        with patch("builtins.input", side_effect=["3", "A1", "A3", "A5", "A7", "A9", "J1", "J3", "J5", "F3", "G10", "B1", "B3", "B5", "B7", "B9", "C1", "C3", "C5", "C7", "C9", "D1", "D3", "D5", "E1", "F3", "F4", "G9", "G10", "H1", "I1", "I3", "I5", "J1", "J3", "J5"]):
            main()

    @staticmethod
    def test_main_mit_bot():
        with patch("builtins.input", side_effect=["2", "Anna", "A1", "r", "A3", "r", "A5", "r", "A7", "r", "A9", "r", "J1", "l", "J3", "l", "J5", "l", "F3", "u", "G10", "o", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10"]):
            main()

    def test_schiffe_setzen(self):
        os.system("")
        with patch("builtins.input", side_effect=["A1", "r", "A3", "r", "A5", "r", "A7", "r", "A9", "r", "J1", "l", "J3", "l", "J5", "l", "F3", "u", "G10", "o"]):
            schiffe_setzen(self.spieler1_spielfeld_objekt,
                           self.spieler1_geg_spielfeld_objekt)

    def test_schiffe_setzen_falsch_eingabe(self):
        os.system("")
        with patch("builtins.input", side_effect=["a", "A1", "r", "A3", "r", "A5", "r", "A7", "r", "A9", "r", "J1", "l", "J3", "l", "J5", "l", "F3", "u", "G10", "o"]), patch('sys.stdout', new=StringIO()) as fake_out:
            schiffe_setzen(self.spieler1_spielfeld_objekt,
                           self.spieler1_geg_spielfeld_objekt)
            lines = fake_out.getvalue().splitlines()
            self.assertIn(
                "Falsche Eingabe. Bitte halte dich an das Format 'D4'.", lines)

    def test_schiffe_setzen_platzproblem(self):
        os.system("")
        with patch("builtins.input", side_effect=["A1", "r", "A1", "A3", "r", "A5", "r", "A7", "r", "A9", "r", "J1", "l", "J3", "l", "J5", "l", "F3", "u", "G10", "o"]), patch('sys.stdout', new=StringIO()) as fake_out:
            schiffe_setzen(self.spieler1_spielfeld_objekt,
                           self.spieler1_geg_spielfeld_objekt)
        lines = fake_out.getvalue().splitlines()
        self.assertIn(
            "An dieser Stelle ist nicht genügend Platz.", lines)

    def test_finde_zahl(self):
        os.system("")
        with patch("sys.stdin", new=StringIO("u")):
            end, platzierbar = finde_zahl(self.spieler1_spielfeld_objekt,
                                          self.spieler1_geg_spielfeld_objekt, 0, "A1", 5)
            self.assertFalse(end)
            self.assertTrue(platzierbar)

    def test_finde_zahl_platzierbar_false(self):
        os.system("")
        self.spieler1_spielfeld_objekt.feld_zuweisen(0, 1)
        self.spieler1_spielfeld_objekt.feld_zuweisen(1, 0)
        with patch("sys.stdin", new=StringIO("u")):
            end, platzierbar = finde_zahl(self.spieler1_spielfeld_objekt,
                                          self.spieler1_geg_spielfeld_objekt, 0, "A1", 5)
            self.assertFalse(end)
            self.assertFalse(platzierbar)

    def test_finde_zahl_end_true(self):
        os.system("")
        with patch("sys.stdin", new=StringIO("u")):
            end, platzierbar = finde_zahl(self.spieler1_spielfeld_objekt,
                                          self.spieler1_geg_spielfeld_objekt, 0, "AA", 5)
            self.assertTrue(end)
            self.assertTrue(platzierbar)

    def test_schiff_versenkt_true(self):
        spieler1_spielfeld_objekt = self.spieler1_spielfeld_objekt
        spieler1_spielfeld_objekt.feld_zuweisen(1, 1)
        versenkt = schiff_versenkt(spieler1_spielfeld_objekt, 2, 1)
        self.assertTrue(versenkt)

    def test_schiff_versenkt_false_1(self):
        spieler1_spielfeld_objekt = self.spieler1_spielfeld_objekt
        spieler1_spielfeld_objekt.feld_zuweisen(1, 1)
        spieler1_spielfeld_objekt.feld_zuweisen(0, 1)
        versenkt = schiff_versenkt(spieler1_spielfeld_objekt, 2, 1)
        self.assertFalse(versenkt)

    def test_schiff_versenkt_false_2(self):
        spieler1_spielfeld_objekt = self.spieler1_spielfeld_objekt
        spieler1_spielfeld_objekt.feld_zuweisen(1, 1)
        spieler1_spielfeld_objekt.feld_zuweisen(2, 1)
        versenkt = schiff_versenkt(spieler1_spielfeld_objekt, 2, 1)
        self.assertFalse(versenkt)

    def test_schiff_versenkt_false_3(self):
        spieler1_spielfeld_objekt = self.spieler1_spielfeld_objekt
        spieler1_spielfeld_objekt.feld_zuweisen(1, 1)
        spieler1_spielfeld_objekt.feld_zuweisen(1, 0)
        versenkt = schiff_versenkt(spieler1_spielfeld_objekt, 2, 1)
        self.assertFalse(versenkt)

    def test_schiff_versenkt_false_4(self):
        spieler1_spielfeld_objekt = self.spieler1_spielfeld_objekt
        spieler1_spielfeld_objekt.feld_zuweisen(1, 1)
        spieler1_spielfeld_objekt.feld_zuweisen(1, 2)
        versenkt = schiff_versenkt(spieler1_spielfeld_objekt, 2, 1)
        self.assertFalse(versenkt)

    def test_runde_und_namen_laden(self):
        runde, namen = runde_und_namen_laden(self.kontenspeicherung)
        self.assertEqual(runde, 1)
        self.assertDictEqual(namen, {'Spieler1': 'Chap', 'Spieler2': 'Chip'})

    def test_spielfelder_laden_Instanz_von_Spielfeld(self):
        spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_spieler1, gegnerisches_spielfeld_spieler2 = spielfelder_laden(
            self.kontenspeicherung)
        self.assertIsInstance(spielfeld_spieler1,
                              spielfeld_klasse.Spielfeld)
        self.assertIsInstance(spielfeld_spieler2,
                              spielfeld_klasse.Spielfeld)
        self.assertIsInstance(gegnerisches_spielfeld_spieler1,
                              spielfeld_klasse.Spielfeld)
        self.assertIsInstance(gegnerisches_spielfeld_spieler2,
                              spielfeld_klasse.Spielfeld)

    def test_spielfelder_laden_namen(self):
        spielfeld_spieler1, spielfeld_spieler2, gegnerisches_spielfeld_spieler1, gegnerisches_spielfeld_spieler2 = spielfelder_laden(
            self.kontenspeicherung)
        self.assertEqual(spielfeld_spieler1.spielername, "Chap")
        self.assertEqual(
            gegnerisches_spielfeld_spieler1.spielername, "Chap")

        self.assertEqual(spielfeld_spieler2.spielername, "Chip")
        self.assertEqual(
            gegnerisches_spielfeld_spieler2.spielername, "Chip")

    def test_spielfelder_laden_spieler_felder(self):
        spielfeld_spieler1 = spielfelder_laden(
            self.kontenspeicherung)
        self.assertTrue(
            spielfeld_spieler1[1].felder == spielfeld_spieler1[0].felder == [
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
                ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
            ])

    def test_spielfelder_laden_gegner_felder(self):
        spielfeld_spieler1 = spielfelder_laden(
            self.kontenspeicherung)
        self.assertTrue(
            spielfeld_spieler1[2].felder, spielfeld_spieler1[3].felder == [
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
                ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]
            ])

    def test_setz_richtung_generieren_funktioniert(self):
        with patch("sys.stdin", new=StringIO("u")):
            eingabe_möglich = setz_richtung_generieren(
                self.spieler1_spielfeld_objekt, 5, 0, 1)
        self.assertTrue(eingabe_möglich)

    def test_setz_richtung_generieren_falsche_eingabe(self):
        with patch("builtins.input", side_effect=["HI", "#", "r"]), patch('sys.stdout', new=StringIO()) as fake_out:
            eingabe_möglich = setz_richtung_generieren(
                self.spieler1_spielfeld_objekt, 5, 0, 1)
        self.assertTrue(eingabe_möglich)
        self.assertIn("Ungültige Eingabe.", fake_out.getvalue().splitlines())

    def test_feld_generieren(self):
        erwartet_eingabe = "A1"

        with patch('sys.stdin', new=StringIO(erwartet_eingabe)):
            eingetregenen_feld = feld_generieren(
                self.spieler1_geg_spielfeld_objekt, True, "A", 1)

        self.assertEqual(erwartet_eingabe, eingetregenen_feld)

    def test_feld_generieren_bot(self):
        alle_moeglichen_werte = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
                                 "I5", "J5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10"]
        spieler1_geg_spielfeld_bot = spielfeld_klasse.Spielfeld(
            [["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10, ["?"]*10], "B0T")
        feld = feld_generieren(spieler1_geg_spielfeld_bot, True, "A", 1)
        self.assertIn(feld, alle_moeglichen_werte)

    def test_finde_zahl_abschießen_value_error(self):
        angreifer_eigenes_spielfeld_objekt = spielfeld_klasse.Spielfeld([
            ["O", "O", "O", "O", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
        ], "B0T")

        spielfelder_liste = [angreifer_eigenes_spielfeld_objekt,
                             self.spieler1_geg_spielfeld_objekt, self.spieler2_spielfeld_objekt]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            finde_zahl_abschießen(spielfelder_liste, 0, 'A10', 'A')
            lines = fake_out.getvalue().splitlines()
            self.assertIn("Bot hat auf Feld A10 geschossen.", lines)

        werte = finde_zahl_abschießen(spielfelder_liste, 0, 'AA', 'A')
        self.assertTrue(werte[1])


class test_farbiges_spielfeld(TestCase):

    def runTest(self, parameter, output):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            farbiges_spielfeld(parameter)
            self.assertIn(output, fake_out.getvalue().splitlines())

    def test_farbiges_spielfeld_tilde(self):
        self.runTest('~', '\x1b[44m ~ \x1b[0m')

    def test_farbiges_spielfeld_minus(self):
        self.runTest('-', '\x1b[48;2;30;144;255m - \x1b[0m')

    def test_farbiges_spielfeld_O(self):
        self.runTest('O', '\x1b[48;2;69;69;69m O \x1b[0m')

    def test_farbiges_spielfeld_N(self):
        self.runTest('N', '\x1b[31;44m N \x1b[0m')

    def test_farbiges_spielfeld_X(self):
        self.runTest('X', '\x1b[32;48;2;69;69;69m X \x1b[0m')

    def test_farbiges_spielfeld_S(self):
        self.runTest('S', '\x1b[31;48;2;69;69;69m S \x1b[0m')


class test_beginner_auslosen(TestCase):

    def runTest(self, modus, get_input):
        with patch("builtins.input", side_effect=get_input):
            namen = beginner_auslosen(modus)
            for anzahl, name in enumerate(get_input):
                get_input[anzahl] = name.title()

            self.assertTrue(namen[0] in get_input and namen[1] in get_input)

    def test_beginner_auslosen_modus_1(self):
        self.runTest(1, ["Anna", "Marvin"])

    def test_beginner_auslosen_modus_1_ungültige_Eingabe(self):
        self.runTest(1, ["123", "KLAUS", "?ß#Zw", "PeTeR"])

    def test_beginner_auslosen_modus_2_bot(self):
        self.runTest(2, ["Anna", "B0T"])

    def test_beginner_auslosen_modus_2_name_falsch(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.runTest(2, ["a5bc7", "Anna", "B0T"])
            self.assertIn("Ungültige Eingabe.",
                          fake_out.getvalue().splitlines())
