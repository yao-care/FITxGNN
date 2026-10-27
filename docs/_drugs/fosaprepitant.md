---
layout: default
title: Fosaprepitant
parent: Pelkkä mallin ennuste (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fosaprepitant: ennustettu uusi käyttöaihe Nefrogeeninen antidiureesisyndrooma (NSIAD) (näytön taso L5). Alkuperäinen käyttöaihe: Oksentelu"
monitor_inn: "FOSAPREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
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

## Fosaprepitantti: Oksentelun ja syövän hoidosta nefrogeeniseen antidiureesisyndroomaan (NSIAD)
{: .text-alpha }

## Yhden lauseen yhteenveto

Fosaprepitantti on aprepitantin esilääke ja NK1-reseptorin salpaaja, jota on alun perin käytetty oksentelun (syöpähoitoihin liittyvä pahoinvointi) ehkäisyyn. TxGNN-malli ennustaa sen mahdollisesti tehoavan ensisijaisesti **nefrogeeniseen antidiureesisyndroomaan (NSIAD)**, mutta ennustetta tukevat vain mallin laskennalliset tulokset: **0 kliinistä tutkimusta** ja **0 julkaisua** tälle indikaatiolle.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Oksentelu; syöpä |
| Ennustettu uusi käyttöaihe | Nefrogeeninen antidiureesisyndrooma (NSIAD) |
| TxGNN-ennustepistemäärä | 99,92 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa (MOA) ei ole tällä hetkellä saatavilla. Tunnetun tiedon perusteella fosaprepitantti on aprepitantin esilääke, ja se salpaa NK1-reseptoria (substanssi P:n reseptori). Sen teho oksentelun ehkäisyssä on osoitettu.

NSIAD johtuu vasopressiinin V2-reseptorin (AVPR2) toimintaa lisäävistä muutoksista. Substanssi P/NK1-signalointi ei tunnetusti osallistu tähän reaktioketjuun, joten mekanistista yhteyttä alkuperäiseen käyttöaiheeseen ei voida osoittaa. Korkea pistemäärä on pelkästään graafipohjainen ennuste, eikä sitä tue kliininen tai kirjallisuusnäyttö.

Muut korkeimmin pisteytetyt ennusteet (pneumokystoosi, lepra, kryptokokkimeningiitti, multippeli endokriininen neoplasia, aivojen sisäinen paise, malaria, echinokokkoosi, hyperargininemia) ovat samoin ilman tukevaa näyttöä ja ilman uskottavaa mekanismia. Ainoa poikkeus on **retiniitti** (sijalla 7, pistemäärä 99,68 %), jossa on yksi prekliininen julkaisu (ks. alla). Sen näyttötaso on L4 ja luokitus "tutkimuskysymys".

---

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia (ei NSIAD:lle eikä muille kymmenelle ennustetulle käyttöaiheelle).

---

## Kirjallisuusnäyttö

NSIAD:lle ei ole saatavilla aiheeseen liittyvää kirjallisuutta. Ainoa löydetty julkaisu koskee sijalla 7 olevaa retiniittiä:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/) | 2021 | Prekliininen (hiirimalli) | Ocular Immunology and Inflammation | UVR-B-säteilyn aiheuttama NK1-reseptorin ilmentyminen silmäkudoksissa estyi fosaprepitantilla sekä altistetussa että altistamattomassa silmässä. Näyttö on epäsuoraa: tutkimus koskee UV-vauriota, ei retiniittiä, eikä ihmistutkimuksia ole. |

---

## Myyntilupatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000743 | Ivemend | – | Oksentelu; syöpä (tila: peruutettu) |

---

## Sytotoksisuus

Fosaprepitantti on syöpähoitoihin liittyvän pahoinvoinnin ehkäisyyn käytettävä tukihoito eikä sytotoksinen syöpälääke, joten tätä osiota ei sovelleta.

---

## Turvallisuusnäkökohdat

- **Tietämysgraafin mukaiset vasta-aiheet:** maksan vajaatoiminta (peräisin TxGNN-tietämysgraafista, ei valmisteyhteenvedosta).
- **Lääkeyhteisvaikutukset:** tarkistettuja yhteisvaikutuksia on yhteensä 100. Merkittäviä (Major) ovat:
  - eliglustaatti
  - naloksegoli

  Kohtalaisia (Moderate) ovat mm. deksametasoni, hydrokortisoni, betametasoni, budesonidi, triamsinoloni, klaritromysiini, simetidiini, mikonatsoli, pioglitatsoni, glimepiridi, nateglinidi, saksagliptiini, lansopratsoli, rabepratsoli, alosetroni, dronabinoli ja naldemedini.

Muilta osin tarkista turvallisuustiedot valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste on pelkkä graafipohjainen laskennallinen tulos (L5). Kliinisiä tutkimuksia ja kirjallisuutta ei ole, eikä NK1-salpauksen ja NSIAD:n (V2-reseptorin aktivoituminen) välillä ole uskottavaa mekanistista yhteyttä. Lisäksi ainoa Suomen myyntilupa on peruutettu.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet Fimeasta (estävä tietoaukko turvallisuusseulonnalle)
- Vaikutusmekanismitiedot (MOA) DrugBankista
- Mekanistinen arviointi NK1/substanssi P -reitin ja AVPR2-välitteisen NSIAD:n yhteydestä
- Retiniitti voidaan harkita jatkotutkimuskysymyksenä: tarvitaan lisää prekliinistä näyttöä ja sopivuusarvio antoreiteille (silmään vai systeemisesti)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

