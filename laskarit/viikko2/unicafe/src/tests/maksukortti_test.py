import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataaminen_onnistuu(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(self.maksukortti.saldo, 1200.0)
    
    def test_saldo_vähenee_oikein(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(self.maksukortti.saldo, 700.0)
    
    def test_liian_vähän_saldoa(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(self.maksukortti.saldo, 1000.0)
    
    def test_palauttaa_oikean_boolean(self):
        self.assertEqual(self.maksukortti.ota_rahaa(120), True)
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)


    

    
    

