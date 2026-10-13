---
layout: default
title: Ramucirumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Ramucirumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Ramusirumabi: Mahasyövän hoidosta kohdun ligamentin adenokarsinoomaan

## Yhden lauseen yhteenveto

Ramusirumabi on VEGFR2-reseptoria estävä vasta-aine, jota on alun perin käytetty mahasyövän hoitoon. TxGNN-malli ennustaa sen voivan tehota **kohdun ligamentin adenokarsinoomaan**, mutta tälle käyttöaiheelle ei ole **yhtään kliinistä tutkimusta eikä julkaisua**, joten ennuste perustuu pelkästään mallin laskemaan pisteytykseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Mahasyöpä (Stomach Neoplasms) |
| Ennustettu uusi käyttöaihe | Kohdun ligamentin adenokarsinooma |
| TxGNN-ennustepisteet | 99,95 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain mitätöity myyntilupa |
| Myyntilupien määrä | 1 (mitätöity) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste on perusteltu?

Ramusirumabi on VEGFR2:ta (verisuonten endoteelikasvutekijän reseptori 2) kohdentava vasta-aine. VEGF/VEGFR2-reitin ohjaama verisuonten uudismuodostus on biologisesti uskottava tekijä myös gynekologisissa adenokarsinoomissa. Tarkkaa vaikutusmekanismia koskevaa tietoa ei ole kuitenkaan tämän raportin aineistossa saatavilla.

Mahasyöpä ja ennustettu kohdun ligamentin adenokarsinooma ovat molemmat adenokarsinoomia, joiden kasvu voi olla riippuvaista angiogeneesistä. Yhteys on kuitenkin löyhä: ennuste nojaa yksinomaan TxGNN-mallin pisteisiin, eikä sitä tue mikään kliininen näyttö tälle käyttöaiheelle.

Samankaltaisia ennusteita mallin kärkisijoilta ovat muun muassa kohdunkaulan endoserviikaalinen karsinooma, kohdunkaulan adenoidikystinen karsinooma sekä useat kohdun ligamentin adenokarsinoomien histologiset alatyypit (seroosi, endometrioidi, kirkassoluinen, musinoottinen). Kaikissa näissä näyttö on L5-tasoa. Kohdunkaulan syövässä anti-angiogeeninen hoito (bevasitsumabi) on osoittanut tehoa, mikä antaa epäsuoran biologisen perustelun. Signettisolu- ja suolen tyyppiset kohdunkaulan musinoottiset adenokarsinoomat muistuttavat histologisesti maha-suolikanavan syöpää, mutta tämä ei ole näyttöä tehosta. Korkeat pisteet johtuvat todennäköisesti jaetuista kohdunkaulansyövän ontologiaa koskevista naapurisolmuista eikä tautikohtaisesta datasta.

---

## Kliininen tutkimusnäyttö

Tälle käyttöaiheelle ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Aiheesta ei ole tällä hetkellä saatavilla asiaan liittyvää kirjallisuutta.

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002829 | Cyramza (Eli Lilly Nederland B.V.) | – | Mahasyöpä (tila: mitätöity) |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (VEGFR2-vasta-aine), ei perinteinen sytotoksinen solunsalpaaja |
| Luuydinsuppression riski | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Oksentelua aiheuttavuus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Seurantakohteet | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja käyttöön liittyvät varotoimet |

---

## Turvallisuusnäkökohdat

Varoituksista ja vasta-aiheista ei ole tämän raportin aineistossa tietoa. Turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

**Lääkeaineyhteisvaikutukset:** Aineistossa on yhteensä 100 yhteisvaikutusta, joista tässä on esitetty 20 ensimmäistä. Merkittävimmät (vakavuusluokka "Major") liittyvät erityisesti verenvuotoriskiin ja veren hyytymiseen vaikuttaviin lääkkeisiin:

- **Verihiutaleiden estäjät ja antikoagulantit:** asetyylisalisyylihappo, abtsiksimabi, alteplaasi, antitrombiini III, apiksabaani, betriksabaani, bivalirudiini, kangrelori, kaplasitsumabi, silostatsoli, klopidogreeli, daltepariini, defibrotidi
- **Radioaktiiviset vasta-aineet:** ibritumomabitiuksetaani, tositumomabi (myös I-131)
- **Muut:** deferasiroksi

Keskivaikeita (Moderate) yhteisvaikutuksia on mm. deksfenfluramiinin, fenfluramiinin ja sibutramiinin kanssa.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-pisteisiin (L5), eikä ainuttakaan kliinistä tutkimusta tai julkaisua ole. Lisäksi ramusirumabin myyntilupa Suomessa on mitätöity ja turvallisuustiedot puuttuvat.

**Etenemiseksi tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimea), jotta turvallisuusseulonta voidaan tehdä
- Tarkka vaikutusmekanismi (DrugBank)
- Prekliininen tai kliininen näyttö ramusirumabista gynekologisissa adenokarsinoomissa, sekä kirjallisuushaku ja tutkimusrekisterien selvitys
- Selvitys valmisteen saatavuudesta ja myyntilupatilanteesta Suomessa
- Verenvuotoriskiin liittyvä yhteisvaikutusten arviointi (antikoagulantit ja verihiutaleiden estäjät)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

