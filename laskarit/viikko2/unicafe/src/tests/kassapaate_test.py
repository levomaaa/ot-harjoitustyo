import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(100)

    def test_kassapaatteessa_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassapaatteessa_edulliset_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassapaatteessa_maukkaat_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_edullinen_saldo_muuttuu(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_kateisosto_maukas_saldo_muuttuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
    
    def test_kateisosto_edullinen_oikea_vaihtoraha_ostaessa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_kateisosto_maukas_oikea_vaihtoraha_ostaessa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateisosto_edullinen_lounaan_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_maukas_lounaan_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_edullinen_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kateisosto_maukas_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_kateisosto_edullinen_kaikki_rahat_vaihtorahana(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_kateisosto_maukas_kaikki_rahat_vaihtorahana(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_kateisosto_edullinen_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_veloittaa_kortilta_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)

    def test_korttiosto_veloittaa_kortilta_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
    
    def test_korttiosto_veloittaa_edullinen_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_veloittaa_maukas_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttiosto_edullinen_lounaan_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas_lounaan_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_edullinen_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttiosto_maukas_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_korttiosto_ei_veloita_edullinen_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2), False)

    def test_korttiosto_ei_veloita_maukas_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2), False)

    def test_korttiosto_edullinen_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_maukas_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_rahan_lataus_kortille_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)

    def test_rahan_lataus_kortille_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)
    
    def test_kortille_negatiivinen_lataus(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1), None)
