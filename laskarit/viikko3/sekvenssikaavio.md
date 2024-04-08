```mermaid
sequenceDiagram
  actor Main
  participant laitehallinto
  participant rautatientori
  participant ratikka6
  participant bussi244
  participant Matkakortti
  
  Main ->> rautatientori : Lataajalaite()
  Main ->> ratikka6: Lukijalaite()
  Main ->> bussi244: Lukijalaite()

  Main ->> laitehallinto : lisaa_lataaja(rautatientori)
  Main ->> laitehallinto : lisaa_lukija(ratikka6)
  Main ->> laitehallinto : lisaa_lukija(bussi244)

  Main ->> lippu_luukku : Kioski()
  Main ->> lippu_luukku : osta_matkakortti("Kalle")
  lippu_luukku ->> Matkakortti : Matkakortti(Kalle)
  Matkakortti -->> kallen_kortti : uusi_kortti

  Main ->> rautatientori : lataa_arvoa(kallen_kortti, 3)
  rautatientori ->> kallen_kortti : kasvata_arvoa(3)
  rautatientori -->> Main 
  
  

  
  

 
```
