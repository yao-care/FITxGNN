---
layout: default
title: Diroximel Fumarate
parent: Pelkkä mallin ennuste (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Diroximel Fumarate: ennustettu uusi käyttöaihe Diabeettinen kaihi (näytön taso L5). Alkuperäinen käyttöaihe: Relapsoiva-remittoiva multippeliskleroosi"
monitor_inn: "DIROXIMEL FUMARATE"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "tetanic cataract", "immature cataract", "cortical cataract", "nuclear senile cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "mature cataract"]
---

# Diroximel Fumarate
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

## Drug: ennustettu uusi käyttöaihe diabeettinen kaihi
{: .text-alpha }

## Yhteenveto

Diroksimeelifumaraatti on monomeetyylifumaraatin (MMF) esilääke, jota on käytetty aaltoilevan MS-taudin (relapsoiva-remittoiva multippeliskleroosi) hoitoon.
TxGNN-malli ennustaa sen voivan tehota ensisijaisesti **diabeettiseen kaihiin** ja **diabeettiseen retinopatiaan**,
mutta ennusteen tueksi ei ole toistaiseksi **yhtään kliinistä tutkimusta eikä julkaisua**.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Relapsoiva-remittoiva multippeliskleroosi |
| Ennustettu uusi käyttöaihe | Diabeettinen kaihi |
| TxGNN-ennustepistemäärä | 1,0000 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Käytettävissä olevassa aineistossa vaikutusmekanismitietoa ei ole. Tunnetun tiedon perusteella diroksimeelifumaraatti on MMF:n esilääke, ja MMF aktivoi Nrf2-antioksidanttireitin. Tämä reitti vaikuttaa oksidatiivista stressiä ja tulehdusta vastaan, mikä on keskeistä MS-taudissa.

Oksidatiivinen stressi ja polyolireitin aiheuttama vaurio edistävät diabeettista linssin samentumaa ja verkkokalvon vaurioita. Nrf2:n aktivointi on siksi teoriassa uskottava, mutta testaamaton yhteys. Diabeettisen retinopatian osalta fumaraateilla on laajemmassa kirjallisuudessa prekliinistä työtä verkkokalvomalleissa, mutta sitä ei toimitettu tähän raporttiin, joten sitä ei voi arvioida.

Kaikkien ennustettujen käyttöaiheiden yhteys on heikosti perusteltu. Esimerkiksi tetaniakaihi liittyy hypokalsemiaan, eikä Nrf2-aktivaatiolla ole uskottavaa yhteyttä kalsiumin aiheuttamaan linssin samentumaan. Kraniosynostoosiin liittyvä kaihi on harvinainen synnynnäinen tila, ja korkea pistemäärä johtuu todennäköisesti verkoston rakenteesta. Kypsä kaihi on rakenteellisesti vakiintunut, eikä systeeminen antioksidantti todennäköisesti korjaa sitä; leikkaus on edelleen ratkaiseva hoito.

## Kliininen tutkimusnäyttö

Toistaiseksi ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Toistaiseksi ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Tiedot Suomen markkinoilta

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005437 | Vumerity | – | Relapsoiva-remittoiva multippeliskleroosi (tila: peruutettu) |

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yhteensä 100 yhteisvaikutusta. Luetelluista, kohtalaisiksi (Moderate) luokitelluista yhteisvaikutuksista keskeisimpiä ovat:
  - Kortikosteroidit: hydrokortisoni, triamsinoloni, deksametasoni, betametasoni, budesonidi, prednisolooni ja prednisoni
  - Naltreksoni ja etanoli
  - Deksratsoksaani
  - Radioaktiiviset ja immunologiset syöpälääkkeet: ibritumomabitiuksetaani, jobenguaani (I-131), tositumomabi (I-131) ja tositumomabi
  - Levamisoli, trimetreksaatti ja merkaptopuriini
  - Roflumilasti ja dupilumabi

Muuta turvallisuustietoa, kuten varoituksia ja vasta-aiheita, ei ole tässä raportissa saatavilla. Tarkista ne valmisteyhteenvedosta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-mallin pisteytykseen (L5). Tukevia kliinisiä tutkimuksia tai julkaisuja ei ole, ja valmisteen ainoa Suomen myyntilupa on peruutettu.
- Turvallisuuden arvioinnin estävä tietoaukko (valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat) estää etenemisen turvallisuusseulontaan.

**Jatkaminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivustolta
- Vaikutusmekanismitietojen täydentäminen DrugBankista
- Prekliinisen näytön kartoitus Nrf2-aktivaatiosta diabeettisen kaihin ja retinopatian malleissa
- Antoreitin ja silmäkudoksen altistuksen arviointi, koska systeemisen suun kautta annettavan lääkkeen riittävä altistus linssille on epävarma
- Painopisteen rajaaminen diabeettisiin käyttöaiheisiin (diabeettinen retinopatia ja kaihi), koska muiden kaihityyppien yhteys on heikko, sekä vertailu nykyhoitoihin (anti-VEGF ja laserhoito)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

