---
layout: default
title: Trastuzumab Deruxtecan
parent: Pelkkä mallin ennuste (L5)
nav_order: 451
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Trastuzumab Deruxtecan: ennustettu uusi käyttöaihe Lääkkeen aiheuttama osteoporoosi (näytön taso L5). Alkuperäinen käyttöaihe: Rintasyöpä (Breast Neoplasms)"
monitor_inn: "TRASTUZUMAB DERUXTECAN"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

## Trastutsumabideruksekaani: Lääkkeen aiheuttama osteoporoosi
{: .text-alpha }

## Yhden lauseen yhteenveto

Trastutsumabideruksekaani on HER2-kohdennettu vasta-aine–lääkekonjugaatti, jota on alun perin käytetty rintasyövän hoitoon. TxGNN-malli ennustaa sen voivan tehota **lääkkeen aiheuttamaan osteoporoosiin**, mutta ennustetta tukee tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua**, eli kyse on pelkästä mallin ennusteesta.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Rintasyöpä (Breast Neoplasms) |
| Ennustettu uusi käyttöaihe | Lääkkeen aiheuttama osteoporoosi |
| TxGNN-ennustepistemäärä | 0,9931 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennustetta voidaan pitää perusteltuna?

Tämän lääkkeen alkuperäisestä vaikutusmekanismista ei ole tällä hetkellä saatavilla yksityiskohtaista tietoa. Tunnetun tiedon perusteella trastutsumabideruksekaani on HER2-kohdennettu vasta-aine–lääkekonjugaatti, jonka kuormana on topoisomeraasi I:n estäjä (deruksekaani). Sen teho HER2-positiivisessa rintasyövässä on osoitettu.

Tämän raportin käytettävissä olevan datan perusteella HER2-kohdentamisen tai topoisomeraasi I:n eston ja lääkkeen aiheuttaman osteoporoosin ehkäisyn tai hoidon välillä ei ole tunnettua biologista yhteyttä. Korkea TxGNN-pistemäärä (0,9931) on pelkkä TxGNN-mallin (syväoppiminen) tuottama ennuste, jota mikään kliininen tai kirjallisuusnäyttö ei tue.

Pistemäärä tulee TxGNN-mallista (syväoppiminen) ja voi heijastaa mallin oppimia samankaltaisuuksia toisiinsa liittyvien sairauksien välillä, ei biologista näyttöä eikä todellista hoitovaikutusta. Lisäksi solunsalpaajakuorma ja syövän tukihoidon konteksti voivat pikemminkin lisätä luuston terveyteen liittyviä huolia.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005124 | Enhertu | – | Rintasyöpä (Breast Neoplasms) (tila: peruutettu) |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito: vasta-aine–lääkekonjugaatti, jossa topoisomeraasi I:n estäjä -kuorma |
| Luuydinsuppression riski | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksentelua aiheuttavuus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurantakohteet | Katso valmisteyhteenvedon varoitukset ja varotoimet; yleisesti verenkuva, maksa- ja munuaisarvot |
| Käsittelyn suojaus | Noudatettava sytotoksisten lääkkeiden käsittelyohjeita |

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Yhteisvaikutuskyselyssä löytyi yhteensä 42 yhteisvaikutusta. Merkittävimpiä (vaikeusaste Major) ovat:

- Deferipröni
- Samarium (153Sm) leksidronaami
- Adalimumabi
- Barisitinibi
- Sertolitsumabipegoli
- Kladribiini
- Leflunomidi
- Natalitsumabi

Keskivaikeita (Moderate) yhteisvaikutuksia on mm. palifermiinin, strontiumkloridi Sr-89:n, roflumilastin, kloramfenikolin, alemtutsumabin, atsatiopriinin, dimetyylifumaraatin ja niraparibin kanssa. Useat näistä ovat immuunijärjestelmää tai luuytimen toimintaa heikentäviä lääkkeitä.

Muista turvallisuustiedoista (varoitukset, vasta-aiheet) tarkista tiedot valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu ainoastaan TxGNN-mallin pistemäärään (näytön taso L5). Kliinisiä tutkimuksia tai julkaisuja ei ole, eikä uskottavaa mekanistista yhteyttä ole osoitettu. Lisäksi lääkkeen myyntilupa Suomessa on peruutettu.

**Jatkotoimien edellytykset:**
- Vaikutusmekanismitietojen (MOA) täydentäminen esimerkiksi DrugBankista
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivustolta, jotta turvallisuusarviointi voidaan aloittaa
- Prekliiniset tai mekanistiset tutkimukset, jotka selvittävät mahdollisen yhteyden luuhun ja osteoporoosiin
- Myyntiluvan peruuntumisen syyn ja nykyisen saatavuuden selvittäminen
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

