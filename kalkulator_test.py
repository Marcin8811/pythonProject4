import unittest
from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator = Kalkulator()

    def test_dodawania(self):
        wynik = self.kalkulator.dodaj(10, 20)
        self.assertEqual(30, wynik)

    def test_odejmowania(self):
        self.assertEqual(10, self.kalkulator.odejmij(20, 10))

    def test_pomnozenia(self):
        self.assertEqual(30, self.kalkulator.pomnoz(10, 3))

    def test_dzielenia(self):
        self.assertEqual(5, self.kalkulator.podziel(10, 2))
        self.assertEqual(0, self.kalkulator.podziel(0, 2))

    def test_dzielenia_przez_zero(self):
        #self.assertEqual("Nie dzieli się przez zero!", self.kalkulator.podziel(4, 0))
        with self.assertRaises(ValueError):
            self.kalkulator.podziel(4, 0)

if __name__ == '__main__':
    unittest.main()




