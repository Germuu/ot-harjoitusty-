import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    #Alkutilanne kunnossa
    
    def test_rahaa_alussa(self):
        rahaa = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(rahaa, 1000.0)
    
    def test_lounaita_myyty_alussa(self):
        edulliset = self.kassapaate.edulliset
        maukkaat  = self.kassapaate.maukkaat
        self.assertEqual(maukkaat + edulliset, 0.0)

    #Edulliset käteisellä tarpeeksi rahaa
    
    def test_edullinen_käteinen_raha_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        
    def test_edullinen_käteinen_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 250-240)
        
    def test_edullinen_käteinen_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    #Maukkaat käteisellä tarpeeksi rahaa
    
    def test_maukas_käteinen_raha_kassaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        
    def test_maukas_käteinen_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 500-400)
        
    def test_maukas_käteinen_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    #Edulliset käteisellä ei tarpeeksi rahaa

    def test_edullinen_käteinen_ei_rahaa_ei_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_käteinen_ei_rahaa_palautus(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(vaihto, 150)

    def test_edullinen_käteinen_ei_rahaa_lounaat_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.edulliset, 0)


    #Maukkaat käteisellä ei tarpeeksi rahaa

    def test_maukas_käteinen_ei_rahaa_ei_kassaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_käteinen_ei_rahaa_palautus(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(vaihto, 150)

    def test_maukas_käteinen_ei_rahaa_lounaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.maukkaat, 0)

   #Edulliset kortilla tarpeeksi rahaa

    def test_edullinen_kortilla_vähennys(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-240)
    
    def test_edullinen_kortilla_True(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_edullinen_kortilla_lounaat_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

   #Edulliset kortilla ei tarpeeksi rahaa

    def test_edullinen_kortilla_saldo_pysyy(self):
        maksukortti = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 1)
    
    def test_edullinen_kortilla_False(self):
        maksukortti = Maksukortti(1)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(tulos, False)

    def test_edullinen_kortilla_lounaat_ei_kasvaa(self):
        maksukortti = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
   #Maukkaat kortilla tarpeeksi rahaa

    def test_maukas_kortilla_vähennys(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-400)
    
    def test_maukas_kortilla_True(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_maukas_kortilla_lounaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

   #Maukkaat kortilla ei tarpeeksi rahaa

    def test_maukas_kortilla_saldo_pysyy(self):
        maksukortti = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 1)
    
    def test_maukas_kortilla_False(self):
        maksukortti = Maksukortti(1)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(tulos, False)

    def test_maukas_kortilla_lounaat_ei_kasvaa(self):
        maksukortti = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)    

    #Rahamäärä ei muutu kortilla ostettaessa

    def test_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # summa >= 0 lataus

    def test_kortille_ladattu_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 200 + 1000)
    
    def test_kassaan_lisäys(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 200 + 100000)
    
    # summa < 0 lataus

    def test_vihe_lataus(self):
        tulos = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -7)
        self.assertEqual(tulos, None)   






