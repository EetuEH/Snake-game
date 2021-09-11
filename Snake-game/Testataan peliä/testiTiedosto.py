import unittest
import pelinOsa

class Test(unittest.TestCase):
    def test_muuttuja(self):
        result = pelinOsa.keltainen()
        self.assertEqual(result, (255, 255, 0))
        tulos =pelinOsa.musta()
        self.assertEqual(tulos, (0,0,0))
        valk = pelinOsa.valkoinen()
        self.assertEqual(valk, (255,255,255))

    def test_nopeus(self):
        self.assertEqual(pelinOsa.nopeus(8), 15)
        self.assertEqual(pelinOsa.nopeus(4),10)        
        self.assertEqual(pelinOsa.nopeus(15),25)
        self.assertEqual(pelinOsa.nopeus(20),30)
        self.assertEqual(pelinOsa.nopeus(6),15)
        self.assertEqual(pelinOsa.nopeus(3),10)

if __name__ == '__main__':
    unittest.main()
