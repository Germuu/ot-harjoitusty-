```mermaid
sequenceDiagram
  actor Main
  participant laitehallinto
  participant rautatientori
  participant ratikka6
  participant bussi244
  
  Main ->> rautatientori : Lataajalaite()
  Main ->> ratikka6: Lukijalaite()
  Main ->> bussi244: Lukijalaite()

  Main ->> laitehallinto : lisaa_lataaja(rautatientori)
  Main ->> laitehallinto : lisaa_lukija(ratikka6)
  Main ->> laitehallinto : lisaa_lukija(bussi244)
  

 
```
