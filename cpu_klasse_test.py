# pylint: disable=C
from unittest import TestCase
from computer_gegner import ComputerGegner
import spielfeld_klasse


class Test_cpu_klasse(TestCase):
    def setUp(self):
        self._buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self._schiffe = ["Schlachtschiff", "Kreuzer", "Kreuzer", "Zerstörer",
                   "Zerstörer", "Zerstörer", "U-Boot", "U-Boot", "U-Boot", "U-Boot"]
        self._schiffwert = {"Schlachtschiff": 5,
                    "Kreuzer": 4, "Zerstörer": 3, "U-Boot": 2}
        self._zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        self.spielfeld = spielfeld_klasse.Spielfeld(
            [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], ""
        )

        self.spielfeld_voll_besetzt = spielfeld_klasse.Spielfeld(
            [["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10, ["O"]*10], ""
        )
        
        self.alle_moeglichen_werte = ["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
 
    def test_ausgelagerte_funktion_platzierbar(self):
        _feld = ["A","1"]
        platzierbar = ComputerGegner.ausgelagerte_funktion(_feld, self.spielfeld, 3, 0)
        self.assertTrue(platzierbar)
    
    def test_ausgelagerte_funktion_nicht_platzierbar(self):
        _feld = ["A","1"]
        self.spielfeld.feld_zuweisen(0,1)
        self.spielfeld.feld_zuweisen(1,0)
        platzierbar = ComputerGegner.ausgelagerte_funktion(_feld, self.spielfeld, 5, 0)
        self.assertFalse(platzierbar)

    def test_schiffe_setzen_funktioniert(self):
        ComputerGegner.schiffe_setzen(self.spielfeld)
    
    # Endlosschleifentest, wenn das Feld voll besetzt ist
    # def test_schiffe_setzen_funktioniert_nicht(self):
    #     ComputerGegner.schiffe_setzen(self.spielfeld_voll_besetzt)

    def test_for_schleife_1_true(self):
        richtungen_check = ['Links']
        richtungen = []
        self.spielfeld.feld_zuweisen(6, 6)
        check_obj = ComputerGegner.for_schleife_1(self.spielfeld, 5, 3, 6, richtungen)
        self.assertTrue(check_obj)
        self.assertListEqual(richtungen_check, richtungen)
    
    def test_for_schleife_2_true(self):
        richtungen_check = ['Rechts']
        richtungen = []
        self.spielfeld.feld_zuweisen(6, 6)
        check_obj = ComputerGegner.for_schleife_2(self.spielfeld, 7, 3, 6, richtungen)
        self.assertTrue(check_obj)
        self.assertListEqual(richtungen_check, richtungen)
    
    def test_for_schleife_3_true(self):
        richtungen_check = ['Oben']
        richtungen = []
        self.spielfeld.feld_zuweisen(6, 6)
        check_obj = ComputerGegner.for_schleife_3(self.spielfeld, 6, 3, 5, richtungen)
        self.assertTrue(check_obj)
        self.assertListEqual(richtungen_check, richtungen)
    
    def test_for_schleife_4_true(self):
        richtungen_check = ['Unten']
        richtungen = []
        self.spielfeld.feld_zuweisen(6, 6)
        check_obj = ComputerGegner.for_schleife_4(self.spielfeld, 6, 3, 4, richtungen)
        self.assertTrue(check_obj)
        self.assertListEqual(richtungen_check, richtungen)

    def test_setz_richtung_generieren_alle_richtungen(self):
        check_richtungen = ['Links','Rechts','Oben','Unten']
        richtungen = ComputerGegner.setz_richtung_generieren(self.spielfeld, 4, 6, 6)
        self.assertListEqual(check_richtungen, richtungen)
    
    def test_setz_richtung_generieren_nicht_unten(self):
        check_richtungen = ['Links', 'Rechts','Oben']
        self.spielfeld.feld_zuweisen(7, 6)
        richtungen = ComputerGegner.setz_richtung_generieren(self.spielfeld, 4, 6, 6)
        self.assertListEqual(check_richtungen, richtungen)
    
    def test_setz_richtung_generieren_nicht_oben(self):
        check_richtungen = ['Links', 'Rechts','Unten']
        self.spielfeld.feld_zuweisen(4, 6)
        richtungen = ComputerGegner.setz_richtung_generieren(self.spielfeld, 3, 6, 6)
        self.assertListEqual(check_richtungen, richtungen)
    
    def test_setz_richtung_generieren_nicht_links(self):
        check_richtungen = ['Rechts','Oben','Unten']
        self.spielfeld.feld_zuweisen(4, 4)
        richtungen = ComputerGegner.setz_richtung_generieren(self.spielfeld, 3, 5, 5)
        self.assertListEqual(check_richtungen, richtungen)

    def test_setz_richtung_generieren_nicht_rechts(self):
        check_richtungen = ['Links','Oben','Unten']
        self.spielfeld.feld_zuweisen(4, 6)
        richtungen = ComputerGegner.setz_richtung_generieren(self.spielfeld, 3, 5, 5)
        self.assertListEqual(check_richtungen, richtungen)
    
    def test_setz_richtung_generieren_keien_richtung(self):
        check_richtungen = []
        self.spielfeld.feld_zuweisen(0, 1)
        self.spielfeld.feld_zuweisen(1, 0)
        richtungen = ComputerGegner.setz_richtung_generieren(self.spielfeld, 3, 1, 1)
        self.assertListEqual(check_richtungen, richtungen)
        
    def test_feld_auswahl(self):
        alle_werte_check = self.alle_moeglichen_werte
        ein_zufaelliger_wert = ComputerGegner.feld_auswahl(True, "E", 5)
        self.assertIn(ein_zufaelliger_wert, alle_werte_check)
    
    def test_feld_auswahl_nicht_getroffen(self):
        alle_werte_check = self.alle_moeglichen_werte
        ein_zufälliger_wert = ComputerGegner.feld_auswahl(False, "A", 1)
        self.assertIn(ein_zufälliger_wert, alle_werte_check)

