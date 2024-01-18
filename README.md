# GROZA UZ KATRU DIENU 

Ko programmatūra dara?
-
**Savāca produktu grozu, nosūta uz e-pastu galīgo sarakstu ar to cenām.**

Šajā projektā es uzkatu problēmu par došānu uz veikalu, kur mēs pastāvīgi aizmirstam par galveniem pirkumiem. Mēs pērkam visu, kas vajadzīgs, aizmirstot par svarīgākajām lietām. Šis programma ļauj atzīmet preces, kuras vēlamies nopirkt ejot uz Rimi veikalu, sūta sarakstu uz e-pastu, raksta kopējo, atseviško preču cenu, un datumu kad mēs vēlamies doties uz veikalu. 

Kā lietot:
-
Programma prasa ievadīt vēlamo produktu nosaukumu, un piedāvā sarakstu no _1-20_ punktiem ar nosaukumu-cenu, vadoties pēc cena un nosaukuma, liekam grozā ievadot numuru, ja vēlamā prece nav, mēs restartējam ciklu, ievadot ciparu _0_.
Pēc tam programma jautā, vai mēs vēlamies pievenot vēl preci _(y/n)_, un pievienos kamēr nepateiksim programmai nē. Tālak programma mums jautā dienu, kurā plānojam apmeklēt veikalu, un e-pastu, kur nosūtīt piezīmi.

**Galīgais rezultāts uzskatās šādi:**

- Iepirkšanās datums

- Produkti

- Katras preces cena

- Kopējā cena


Atomatizācijas process projektā - vēlamo produktu pievienošana, gala cena, paziņojums e-pastā. Domāju, ka projekta ideja atbilst uzdevumam un materiālam, kuru es saņēmu kursa laikā. Projekta ideja var tikt attīstīt tālāk, pevienot papildu funkcionalitāti, veikspēju.

No 2024. gada 18. janvāra programma darbojas pareizi, izmaiņas pašas vietnes interfeisā var izraisīt nepareizas programmas darbību. 


**Bibliotēkas:**

- _Selenium_ - ļāva man strādāt ar pēdējo Google Chrome versiju, izdeidoja vairākus uzdevumus darba, ar web-lapu.

- _BeautifulSoup4_ - Pamatojoties uz datu analīzi, es iegūvu datus no web-lapas, kas man bija nepieciešami turpmākai apstrādei.

- _time_ - ļāva konfigurēt pieprasījumu aizkavi, strādājot kopā ar _Selenium_

- _requests_ - Darba ar web-lapus, iegūt GET datus.

- _smtplib_ - nosūtīšana uz e-pastu. 



**_Autors:_**

_Vladislavs Vasiļjevs 211REC081._
