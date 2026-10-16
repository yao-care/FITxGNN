---
layout: default
title: Ruxolitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ruxolitinib: ennustettu uusi käyttöaihe Kohdunrungon perivaskulaarinen epiteloidisolukasvain (PEComa) (näytön taso L5). Alkuperäinen käyttöaihe: Vitiligo"
monitor_inn: "Ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease"]
---

# Ruxolitinib
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

# Ruksolitinibi: vitiligosta ja myeloproliferatiivisista sairauksista hemofagosyyttiseen oireyhtymään (infektioon liittyvä)

## Yhteenveto

Ruksolitinibi on JAK1/JAK2-estäjä, jolla on Suomessa ollut myyntilupa vitiligon (Opzelura) sekä myeloproliferatiivisten sairauksien, polycythemia veran ja graft-versus-host-taudin (Jakavi) hoitoon.
TxGNN-malli ennustaa sen voivan tehota ensisijaisesti sairauteen **kohdunrungon perivaskulaarinen epiteloidisolukasvain (PEComa)**, mutta tälle ennusteelle ei ole kliinistä tai kirjallista tukea. Parhaiten tuettu ehdokas on **infektioon liittyvä hemofagosyyttinen oireyhtymä (HLH)**, jonka tueksi on koottu **21 julkaisua** (pääosin tapaussarjoja ja retrospektiivisiä tutkimuksia) mutta ei yhtään rekisteröityä kliinistä tutkimusta.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Vitiligo; myeloproliferatiiviset sairaudet, polycythemia vera ja graft-versus-host-tauti |
| Ennustettu uusi käyttöaihe (ensimmäinen ennuste) | Kohdunrungon perivaskulaarinen epiteloidisolukasvain (PEComa) |
| TxGNN-ennustepistemäärä | 99,73 % |
| Näytön taso | L5 (ensimmäinen ennuste); parhaiten tuettu ehdokas: infektioon liittyvä HLH, L3 |
| Markkinatilanne Suomessa | Vain peruutettuja lupia |
| Lupien määrä | 2 (molemmat peruutettu) |
| Suositeltu päätös | Hold (ensimmäinen ennuste); Proceed with Guardrails (infektioon liittyvä HLH) |

Huomio: ennusteet on listattu TxGNN-pisteiden mukaan. Kymmenestä ennustetusta käyttöaiheesta vain kahdella (liposarkooma ja HLH-ryhmä) on mitään näyttöä. Raportin loppuosa keskittyy ensimmäiseen ennusteeseen ja nostaa esiin HLH:n, koska se on näytön perusteella lupaavin.

## Miksi ennuste on perusteltu?

Tämän raportin yhteenvetoon koottu tieto ei sisällä yksityiskohtaista vaikutusmekanismia. Tunnetusti ruksolitinibi estää Janus-kinaaseja JAK1, JAK2, JAK3 ja TYK2, ja sen kliininen käyttö kohdistuu myelofibroosiin, polycythemia veraan ja steroidiresistenttiin akuuttiin GvHD:hen.

**Ensimmäinen ennuste (kohdunrungon PEComa):** PEComat johtuvat tyypillisesti mTOR-reitin säätelyhäiriöstä (TSC1/TSC2), eikä JAK/STAT-reitin osuudesta ole näyttöä. Korkea pistemäärä on ennuste, ei validoitu mekanismi. Sama koskee muita PEComa-perheen ennusteita (hyvänlaatuinen PEComa, keuhkojen PEComa, lymfangiomyooma, lymfangioleiomyomatoosi), joissa vakiintunut hoito on mTOR-estäjä sirolimuusi.

**Infektioon liittyvä HLH:** Sairaus on IFN-γ-välitteinen hypertulehdustila, jossa sytokiinisignalointi kulkee JAK/STAT-reitin kautta. Hiirimalleissa ruksolitinibin on osoitettu vaimentavan T-solujen aktivaatiota ja tulehdusta (PMID 31015190) ja herkistävän CD8-T-soluja deksametasonin aiheuttamalle apoptoosille (PMID 32530039). Mekanistinen peruste on siis uskottava, vaikka kliininen näyttö on vielä rajallista.

**Liposarkooma:** Kaksi prekliinistä tutkimusta osoittaa JAK-STAT-signaloinnin liittyvän myksoidin liposarkooman kantasolu- ja kemoresistenssiominaisuuksiin. Perustelu on rajattu tähän alatyyppiin eikä kliinistä näyttöä ole.

## Kliininen tutkimusnäyttö

Rekisteröityjä kliinisiä tutkimuksia ei tällä hetkellä ole kaikille ennustetuille käyttöaiheille.

## Kirjallisuusnäyttö

Ensimmäisen ennusteen (kohdunrungon PEComa) osalta kirjallisuutta ei ole. Alla on infektioon liittyvän HLH:n keskeisin kirjallisuus (enintään 10, tutkimustyypin mukaan priorisoituna).

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Kohorttitutkimus | Blood | Ruksolitinibi ensilinjan lääkkeenä lasten HLH:ssa, hoito porrastettu varhaisen vasteen mukaan |
| [31879790](https://pubmed.ncbi.nlm.nih.gov/31879790/) | 2020 | Tapaussarja | Ann Hematol | Ruksolitinibi steroidiresistentissä akuutissa GvHD:ssa EBV-HLH-potilailla allo-HSCT:n jälkeen (12 potilasta) |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Retrospektiivinen | Br J Haematol | Ruksolitinibipohjainen hoito (n = 53) verrattuna muokattuun HLH-94-kemoterapiaan (n = 42) lasten EBV-HLH:ssa |
| [33523540](https://pubmed.ncbi.nlm.nih.gov/33523540/) | 2021 | Tapaussarja | Eur J Haematol | Ruksolitinibi lisähoitona sekundaarisessa HLH:ssa |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Tapaussarja | Ann Hematol | Sintilimabi yhdistettynä ruksolitinibiin 12 aikuisella EBV-HLH-potilaalla |
| [41934358](https://pubmed.ncbi.nlm.nih.gov/41934358/) | 2026 | Retrospektiivinen kysely | Pediatr Hematol Oncol | Ruksolitinibin käyttö japanilaislapsilla (17 potilasta) |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Prekliininen | Blood | Ruksolitinibin vaikutusmekanismit HLH:n hiirimalleissa |
| [32530039](https://pubmed.ncbi.nlm.nih.gov/32530039/) | 2020 | Prekliininen | Blood | JAK/STAT-esto herkistää CD8-T-solut deksametasonin aiheuttamalle apoptoosille |
| [37702780](https://pubmed.ncbi.nlm.nih.gov/37702780/) | 2023 | Katsaus | Innere Medizin | HLH:n hoito tehohoidossa |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Tapausselostus | J Pediatr Hematol Oncol | Emapalumabi, ruksolitinibi ja deksametasoni vaikeassa EBV-HLH:ssa |

Liposarkoomaan liittyvät prekliiniset tutkimukset: [35186752](https://pubmed.ncbi.nlm.nih.gov/35186752/) (2022, Front Oncol) ja [30650179](https://pubmed.ncbi.nlm.nih.gov/30650179/) (2019, Int J Cancer).

## Markkinatiedot Suomessa

| Lupanumero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005843 | Opzelura | – | Vitiligo (peruutettu) |
| EMEA/H/C/002464 | Jakavi | – | Myeloproliferatiiviset sairaudet, polycythemia vera, graft-versus-host-tauti (peruutettu) |

## Sytotoksisuus

Ruksolitinibi on kohdennettu hoito (JAK-estäjä), ei perinteinen sytotoksinen solunsalpaaja. Sytotoksisuuteen liittyvää tietoa ei ole koottu; katso valmisteyhteenvedon varoitukset ja varotoimet. Hematologinen seuranta (verenkuva) on kuitenkin perusteltua, sillä HLH-aineistossa korostetaan sytopenioiden ja infektioriskin seurantaa.

## Turvallisuushuomioita

Lääkkeiden yhteisvaikutuksia koskevaa tietoa ei ole saatavilla; koottu tieto kuvaa vain lääkkeen kohdeproteiineja (JAK1, JAK2, JAK3, TYK2). Muuta turvallisuustietoa ei ole saatavilla. Katso turvallisuustiedot valmisteyhteenvedosta.

HLH-ehdokkaan suojatoimet: käyttö erikoissairaanhoidon keskuksissa, sytopenioiden ja infektioriskin seuranta sekä löydösten vahvistaminen prospektiivisissa tutkimuksissa.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold** (ensimmäinen ennuste, kohdunrungon PEComa)

**Perustelut:**
- Ennuste perustuu pelkästään mallin pisteytykseen (L5), eikä kliinisiä tutkimuksia tai kirjallisuutta ole. PEComan mTOR-painotteinen biologia ei tue JAK-eston käyttöä.

**Muut ehdokkaat:**
- **Infektioon liittyvä HLH: Proceed with Guardrails (L3).** Tuki koostuu tapaussarjoista, retrospektiivisistä tutkimuksista ja prekliinisestä mekanismityöstä.
- **Liposarkooma ja HLH, johon liittyy pahanlaatuinen sairaus: Research Question (L4).** Näyttö on prekliinistä tai epäsuoraa.

**Jatkotoimet:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kokoaminen Fimean sivustolta (nykyinen tietoaukko estää turvallisuusseulonnan).
- Vaikutusmekanismin tarkka kuvaus DrugBankista.
- Prospektiiviset kliiniset tutkimukset HLH:ssa ja rekisteröityjen tutkimusten haku.
- Suomen myyntilupatilanteen selvittäminen, koska kaikki luvat on peruutettu.
- HLH:n osalta aikuisten ja lasten erillisarviointi sekä malignitologiaan liittyvän HLH:n omat tutkimukset.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

