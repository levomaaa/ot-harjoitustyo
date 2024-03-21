import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortille_latautuu_rahaa(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)
    
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_jos_rahat_riittaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)
    
    def test_jos_rahat_ei_riita_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1300), False)
    
    def test_kortilla_rahaa_str(self):
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")