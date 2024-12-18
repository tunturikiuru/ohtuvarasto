import unittest
from varasto import Varasto




class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #uudet testit
    #7, 11, 17, 25, 29, 33, 35-38, 45

    def test_negatiivinen_tilavuus(self):
        varasto = Varasto(-2)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        varasto = Varasto(10, -1)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alkusaldo_ylittaa_tilavuuden(self):
        varasto = Varasto(10, 12)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisataan_negatiivinen_maara(self):
        varasto = Varasto(10, 8)
        varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(varasto.saldo, 8)

    def test_lisataan_ylimaara(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_otetaan_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_tulostus_oikein(self):
        self.varasto.lisaa_varastoon(2)
        vastaus = str(self.varasto)
        self.assertAlmostEqual(vastaus, "saldo = 2, vielä tilaa 8")
