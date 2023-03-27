# pylint: disable=C
from unittest import TestCase
from spielfeld_klasse import Spielfeld


class Test_spielfeld(TestCase):
    def setUp(self):
        self.eigenes_spielfeld_objekt = Spielfeld(
            [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "")

        self.gegnerisches_spielfeld_objekt = Spielfeld(
            [["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10, ["~"]*10], "")

    def test_feld_zuweisen(self):
        self.eigenes_spielfeld_objekt.feld_zuweisen(0, 1)
        self.assertEqual(self.eigenes_spielfeld_objekt.felder[0][1], "O")

    def test_sperrfeld_zuweisen(self):
        self.eigenes_spielfeld_objekt.sperrfeld_zuweisen(0, 0)
        self.assertEqual(self.eigenes_spielfeld_objekt.felder[0][0], "-")

    def test_feld_beschiessen(self):
        self.gegnerisches_spielfeld_objekt.felder[0][0] = "O"
        getroffen, wiederholt = self.eigenes_spielfeld_objekt.feld_beschießen(
            self.gegnerisches_spielfeld_objekt, 0, 0)
        self.assertEqual(getroffen, True)
        self.assertFalse(wiederholt)
        self.assertEqual(self.eigenes_spielfeld_objekt.felder[0][0], "X")

        self.gegnerisches_spielfeld_objekt.felder[0][0] = "S"
        getroffen, wiederholt = self.eigenes_spielfeld_objekt.feld_beschießen(
            self.gegnerisches_spielfeld_objekt, 0, 0)
        self.assertEqual(getroffen, True)
        self.assertFalse(wiederholt)

        self.gegnerisches_spielfeld_objekt.felder[0][0] = "~"
        getroffen, wiederholt = self.eigenes_spielfeld_objekt.feld_beschießen(
            self.gegnerisches_spielfeld_objekt, 0, 0)
        self.assertEqual(getroffen, False)
        self.assertFalse(wiederholt)
        self.assertEqual(self.eigenes_spielfeld_objekt.felder[0][0], "N")
