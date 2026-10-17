---
layout: default
title: Ertapenem
parent: Pelkkä mallin ennuste (L5)
nav_order: 175
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Ertapenem: ennustettu uusi käyttöaihe Bakteeriniveltulehdus (vaihtoehtoinen ennuste: Staphylococcus aureus… (näytön taso L5). Alkuperäinen käyttöaihe: Bakteeri-infektiot"
monitor_inn: "Ertapenem"
predicted_indications: ["bacterial arthritis", "staphylococcus aureus infection"]
---

# Ertapenem
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

# Ertapeneemi: Bakteeri-infektioista bakteeriniveltulehdukseen

## Yhden lauseen yhteenveto

Ertapeneemi on laajakirjoinen karbapeneemiantibiootti, jota on alun perin käytetty bakteeri-infektioiden, kuten yhteisöhankittujen infektioiden, leikkaushaavainfektioiden ja bakteeriperäisen keuhkokuumeen hoitoon.
TxGNN-malli ennustaa sen voivan tehota **bakteeriniveltulehdukseen** (korkein pistemäärä), mutta tähän suuntaan ei ole yhtään kliinistä tutkimusta, vain **10 julkaisua** (pääosin tapausselostuksia).
Toiseksi sijoittuvasta ennusteesta, **Staphylococcus aureus -infektiosta**, on **2 kliinistä tutkimusta** ja **19 julkaisua**, ja se on tämän raportin vahvin tutkimussuunta.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Bakteeri-infektiot |
| Ennustettu uusi käyttöaihe | Bakteeriniveltulehdus (vaihtoehtoinen ennuste: Staphylococcus aureus -infektio) |
| TxGNN-ennustepistemäärä | 99,72 % (S. aureus -infektio: 99,28 %) |
| Näytön taso | L4 (S. aureus -infektio: L2) |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 2 (kaikki peruutettuja) |
| Suositeltu päätös | Hold (odota) (S. aureus -infektio: tutkimuskysymys) |

---

## Miksi ennuste on perusteltu?

Vaikutusmekanismitietoja ei ole tällä hetkellä saatavilla tähän raporttiin koottujen tietojen perusteella. Ertapeneemi kuuluu karbapeneemien lääkeryhmään, joka estää bakteerin soluseinän synteesiä sitoutumalla penisilliiniä sitoviin proteiineihin. Sen teho bakteeri-infektioissa on osoitettu, ja mekanistisesti se voi sopia myös luu- ja nivelinfektioihin.

Bakteeriniveltulehdus ja luu- ja nivelinfektiot johtuvat usein herkistä gramnegatiivisista bakteereista, anaerobeista ja joistakin grampositiivisista bakteereista, joihin ertapeneemi tehoaa. Ertapeneemia käytetään jo off-label-käytössä luu- ja nivelinfektioissa, erityisesti ESBL-tuottavien enterobakteerien aiheuttamissa tapauksissa. Kerran vuorokaudessa annettava annostelu sopii myös avohoidon suonensisäiseen antibioottihoitoon. Korkea TxGNN-pistemäärä on kuitenkin pelkkä laskennallinen ennuste.

Staphylococcus aureus -infektion osalta ertapeneemi yksinään tehoaa rajallisesti. Yhdessä kefatsoliinin kanssa kaksi beetalaktaamia sitoutuvat toisiaan täydentäviin penisilliiniä sitoviin proteiineihin (kefatsoliini PBP1, ertapeneemi PBP2), mikä voi voimistaa bakteerien tuhoutumista. Tätä yhdistelmää on käytetty sinnikkään metisilliinille herkän S. aureus -bakteremian (MSSA) hoitoon. Tuki perustuu in vitro -synergiaan, tapaussarjoihin ja havainnoiviin vertailuihin, ja teho on vielä vahvistettava satunnaistetuilla tutkimuksilla.

---

## Kliiniset tutkimukset

**Bakteeriniveltulehdus:** Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

**Staphylococcus aureus -infektio:**

| Tutkimustunnus | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Vaihe 2 | Rekrytoi | 60 | Kefatsoliinin ja ertapeneemin yhdistelmä MSSA-bakteremiassa; satunnaistettu osatutkimus SNAP-tutkimusalustassa; tuloksia ei vielä ole |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Vaihe 4 | Rekrytointi kutsulla | 300 | Varhainen kahden antibiootin hoito vs. yksi antibiootti S. aureus -bakteremiassa; ei vahvistettu, sisältääkö yhdistelmä ertapeneemia; tuloksia ei ole |

---

## Kirjallisuusnäyttö

**Bakteeriniveltulehdus (valikoima):**

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Kohorttitutkimus | Antimicrob Agents Chemother | Pitkäaikaisen ertapeneemin avohoidon turvallisuus ja teho 306 potilaalla; luu- ja nivelinfektiot mukana käyttöaiheissa |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Kohorttitutkimus | J Antimicrob Chemother | Ihonalainen suppressiivinen beetalaktaamihoito luu- ja nivelinfektioissa, 10 potilasta |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Tapausselostus | J Chemother | Klebsiella pneumoniae -rannenivelinfektio hoidettu onnistuneesti ertapeneemilla ja levofloksasiinilla |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Tapausselostus | BMJ Case Rep | Citrobacter koseri -osteomyeliitti ja septinen niveltulehdus, hoito ertapeneemilla |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | Prekliininen | Diagn Microbiol Infect Dis | Auranofiini palautti ertapeneemin herkkyyden karbapeneemiresistentille E. colille |

**Staphylococcus aureus -infektio (valikoima):**

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Vertaileva kohorttitutkimus | J Antimicrob Chemother | Karbapeneemiyhdistelmä vs. tavanomainen hoito sinnikkäässä MSSA-bakteremiassa |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Katsaus | Am J Health Syst Pharm | Yhdistelmähoitovaihtoehdot sinnikkäässä MSSA-bakteremiassa |
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Tapaussarja | Clin Infect Dis | Kefatsoliini + ertapeneemi pelastushoitona 11 tapauksessa; välitön puhdistuma (≤24 h) 8 tapauksessa |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Tapaussarja + in vitro | Antimicrob Agents Chemother | Synergia in vitro ja hiirimallissa; sinnikäs bakteremia puhdistui |
| [41759962](https://pubmed.ncbi.nlm.nih.gov/41759962/) | 2026 | Havainnoiva monikeskustutkimus | Infect Dis Now | Ertapeneemin ja penisilliini M:n tai kefatsoliinin yhdistelmä MSSA-bakteremiassa |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Retrospektiivinen kohortti | J Antimicrob Chemother | Hypoalbuminemian vaikutus ertapeneemiyhdistelmähoitoon; ertapeneemi sitoutuu voimakkaasti proteiineihin |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe | Tila |
|---------|------|------|-----------|------|
| EMEA/H/C/005815 | Ertapenem SUN | – | Bakteeri-infektiot | Peruutettu |
| EMEA/H/C/000389 | Invanz | – | Yhteisöhankitut infektiot, streptokokki-infektiot, stafylokokki-infektiot, gramnegatiiviset bakteeri-infektiot, leikkaushaavainfektio, bakteeriperäinen keuhkokuume | Peruutettu |

Molemmat myyntiluvat on peruutettu, joten markkinoilla ei tällä hetkellä ole voimassa olevaa valmistetta.

---

## Turvallisuushuomiot

- **Mahdolliset vasta-aiheet (tietämysgraafin perusteella, ei valmisteyhteenvedosta):** epilepsia, munuaissairaus, virtsanjohtimen märkäinen tulehdus, Clostridium difficile -koliitti, vastasyntyneen nekrotisoiva enterokoliitti.
- **Lääkeyhteisvaikutukset:** yhteensä 38 yhteisvaikutusta. Merkittävä (Major): **bupropioni**. Kohtalaisia (Moderate): pikosulfaatti, polyetyleeniglykoli (3350 elektrolyyteillä) ja natriumsulfaatti. Muiden vaikutusluokka on tuntematon, mm. vankomysiini, metformiini, metronidatsoli ja morfiini.
- **Muu huomio:** Ertapeneemi sitoutuu voimakkaasti proteiineihin, ja hypoalbuminemiapotilailla altistus voi jäädä riittämättömäksi.

Muilta osin tarkista turvallisuustiedot valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota) bakteeriniveltulehduksen osalta; S. aureus -infektion osalta tutkimuskysymys, jota kannattaa seurata**

**Perustelu:**
- Bakteeriniveltulehduksen korkea TxGNN-pistemäärä (99,72 %) on pelkkä laskennallinen ennuste, eikä siitä ole kliinisiä tutkimuksia, vain tapausselostuksia ja pieniä kohorttitutkimuksia (L4).
- S. aureus -infektion osalta kefatsoliini–ertapeneemi-yhdistelmällä on uskottava mekanismi, tapaussarjoja ja käynnissä oleva vaiheen 2 satunnaistettu tutkimus (L2), mutta tuloksia ei vielä ole. Lisäksi kaikki Suomen myyntiluvat on peruutettu.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet Fimean sivustolta (estävä tietoaukko)
- Vaikutusmekanismitiedot DrugBankista
- NCT04886284-tutkimuksen tulokset ja varmistus, sisältääkö NCT07148960 ertapeneemia
- Luu- ja nivelinfektioiden vertaileva kliininen tutkimusnäyttö
- Selvitys valmisteen saatavuudesta Suomessa, koska myyntiluvat on peruutettu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

