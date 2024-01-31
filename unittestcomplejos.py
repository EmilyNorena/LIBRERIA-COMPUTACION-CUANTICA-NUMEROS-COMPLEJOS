import math
import unittest
import libreriacomplejos as cplxlib
class TestCplxMethods(unittest.TestCase):
    def test_suma(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[0], 2.2)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[1], -2.7)
        c1 = (6, 5.9)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[0], 5)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[1], -27.1)
    def test_mult(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(cplxlib.mult(c1, c2)[0], 36.14)
        self.assertAlmostEqual(cplxlib.mult(c1, c2)[1], 64.98)
        c1 = (6, 5.9)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.mult(c1, c2)[0], 188.7)
        self.assertAlmostEqual(cplxlib.mult(c1, c2)[1], -203.9)
    def test_resta(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[0], 9)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[1], -15.1)
        c1 = (6, 5.9)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[0], 7)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[1], 38.9)
    def test_div(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(cplxlib.div(c1, c2)[0], -1.4844)
        self.assertAlmostEqual(cplxlib.div(c1, c2)[1], -0.0892)
        c1 = (6, 5.9)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.div(c1, c2)[0], -0.18412844)
        self.assertAlmostEqual(cplxlib.div(c1, c2)[1], 0.176238532)
    def test_modulo(self):
        c1 = (5.6, -8.9)
        self.assertAlmostEqual(cplxlib.modulo(c1), 10.51522705)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.modulo(c2), 33.01514804)
    def test_conjugado(self):
        c1 = (5.6, -8.9)
        self.assertAlmostEqual(cplxlib.conjugado(c1)[0], 5.6)
        self.assertAlmostEqual(cplxlib.conjugado(c1)[1], 8.9)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.conjugado(c2)[0], -1)
        self.assertAlmostEqual(cplxlib.conjugado(c2)[1], 33)
    def test_cartesiano_polar(self):
        c1 = (5.6, -8.9)
        self.assertAlmostEqual(cplxlib.cartesiano_polar(c1)[0], 10.51522705)
        self.assertAlmostEqual(cplxlib.cartesiano_polar(c1)[1], -1.00917282)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.cartesiano_polar(c2)[0], 33.01514804)
        self.assertAlmostEqual(cplxlib.cartesiano_polar(c2)[1], 1.54050256)
    def test_polar_cartesiano(self):
        c1 = (1,math.pi/2)
        self.assertAlmostEqual(cplxlib.polar_cartesiano(c1)[0], 0)
        self.assertAlmostEqual(cplxlib.polar_cartesiano(c1)[1], 1)
        c2 = (1,math.pi)
        self.assertAlmostEqual(cplxlib.polar_cartesiano(c2)[0], -1)
        self.assertAlmostEqual(cplxlib.polar_cartesiano(c2)[1], 0)
    def test_fase(self):
        c1 = (5.6, -8.9)
        self.assertAlmostEqual(cplxlib.fase(c1), -1.00917282)
        c2 = (-1, -33)
        self.assertAlmostEqual(cplxlib.fase(c2), 1.54050256)   
    
if __name__ == '__main__':
    unittest.main()
