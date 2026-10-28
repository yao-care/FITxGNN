---
layout: default
title: Moroctocog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 295
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
description: "Moroctocog Alfa: ennustettu uusi käyttöaihe Primary release disorder of platelets (näytön taso L5). Alkuperäinen käyttöaihe: Hemophilia A"
---

# Moroctocog Alfa
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **8** kpl
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

## Moroctocog Alfa: Primary release disorder of platelets
{: .text-alpha }

## Yhden lauseen yhteenveto

Moroktokogi alfa on rekombinantti, B-domeenista vapautettu hyytymistekijä VIII -valmiste, jota on alun perin käytetty **hemofilia A:n** hoitoon.
TxGNN-malli ennustaa sen voivan tehota **primaariin verihiutaleiden vapautumishäiriöön**, mutta ennusteen tueksi ei ole yhtään kliinistä tutkimusta eikä julkaisua, joten näyttö perustuu pelkkään mallin ennusteeseen (**taso L5**).

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hemophilia A |
| Ennustettu uusi käyttöaihe | Primary release disorder of platelets |
| TxGNN-ennustepisteet | 0.9997 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odotetaan) |

## Miksi ennuste voisi olla perusteltu?

Tämän raportin tietoja ei sisältänyt yksityiskohtaista vaikutusmekanismia. Tiedetyn perusteella moroktokogi alfa korvaa puuttuvan hyytymistekijä VIII:n hemofilia A:ssa, ja sen teho tässä käyttöaiheessa on osoitettu. Mekanistisesti sen soveltuvuus uuteen käyttöaiheeseen on kuitenkin epäselvää.

Verihiutaleiden vapautumishäiriö johtuu verihiutaleiden omasta eritysvauriosta, ei tekijä VIII:n puutteesta. Tekijä VIII:n korvaamiselle ei siksi ole selvää biologista perustetta. Korkea ennustepiste (0,9997) heijastaa todennäköisesti verenvuotosairauksien läheisyyttä tietämysgraafissa, ei todellista biologista yhteyttä.

### Muut ennustetut käyttöaiheet

Mallin muut ennusteet ovat samalla tasolla (kaikki L5, ei tutkimus- tai kirjallisuusnäyttöä, suositus Hold):

| Sija | Sairaus | Pisteet | Mekanistinen arvio |
|------|------|------|------|
| 2 | Pseudo-von Willebrandin tauti | 0.9997 | Löyhä epäsuora yhteys (VWF kantaa tekijä VIII:aa), mutta perusvika on verihiutaleissa (GPIbα) |
| 3 | Glanzmannin trombasteenia | 0.9997 | Vika integriini αIIbβ3:ssa; tekijä VIII ei korjaa sitä. Tavanomaisesti hoidetaan verihiutalesiirrolla ja rekombinantilla tekijä VIIa:lla |
| 4 | Hankinnainen hyytymistekijän puutos | 0.9988 | Biologisesti uskottavin, mutta hankinnaisessa hemofiliassa vasta-aineet neutraloivat tekijä VIII:n, joten korvaushoito on usein tehotonta ja ohitushoidot ovat ensisijaisia |
| 5 | Scottin oireyhtymä | 0.9986 | Heikko epäsuora yhteys; puuttuvaa kalvopintaa (TMEM16F/ANO6) ei voi korvata tekijä VIII:lla |
| 6 | Kollageenireseptorivirheestä johtuva verenvuotoalttius | 0.9973 | Vika verihiutaleiden reseptorisignaloinnissa; ennuste heijastaa verkostolähiyttä |
| 7 | Synnynnäisestä trombosytopeniasta johtuva verenvuotohäiriö | 0.9972 | Syy on verihiutaleiden vähäisyys; tarvitaan verihiutalesiirto tai trombopoieettinen hoito |
| 8 | "Flood factor deficiency" | 0.9911 | Ei tunnistettu vakiintunut sairausnimike, mahdollinen ontologiavirhe; tunnistus on varmistettava |

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Tällä hetkellä ei ole aiheeseen liittyvää kirjallisuutta.

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000232 | ReFacto AF (Pfizer Europe MA EEIG) | – | Hemofilia A |

Tämä myyntilupa on peruutettu, joten valmiste ei ole tällä hetkellä myynnissä Suomessa.

## Turvallisuusnäkökohdat

Turvallisuustietoja ei ole saatavilla tämän raportin aineistossa. Lääkkeiden yhteisvaikutuksia ei löytynyt. Tarkista turvallisuustiedot valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold**

**Perustelut:**
- Ennuste perustuu pelkästään mallin pisteytykseen: tutkimus- tai kirjallisuusnäyttöä ei ole, mekanistinen yhteys on heikko tai puuttuu, ja ainoa Suomen myyntilupa on peruutettu.

**Jatkamiseksi tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden haku Fimean sivustolta (estävä tietoaukko turvallisuusseulonnalle)
- Vaikutusmekanismin tiedot DrugBankista
- Hankinnaisen hyytymistekijän puutoksen (sija 4) mekanistinen ja kliininen arviointi, koska se on biologisesti uskottavin kohde
- Sairausnimikkeen "flood factor deficiency" tunnistaminen ennen arviointia
- Kirjallisuus- ja tutkimushaku ennustetuille käyttöaiheille
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

