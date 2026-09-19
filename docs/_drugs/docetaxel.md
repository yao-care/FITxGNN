---
layout: default
title: Docetaxel
parent: Vahva näyttö (L1-L2)
nav_order: 125
evidence_level: L1
indication_count: 10
---

# Docetaxel
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **10** kpl
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

# Docetaxel: Dokumentoimattomasta alkuperäisestä indikaatiosta naisen rintasyöpään

## Yhden lauseen yhteenveto

Docetaxel (DrugBank DB01248) on taksiini-luokan sytostaattinen aine; evidenssipaketti ei sisällä dokumentoitua alkuperäistä indikaatiota tai Suomen/Taiwanin lisenssi­tietoja, mutta lääkkeen tosielämän kliininen käyttöyhteys on rintasyövän kemoterapia.
TxGNN-malli ennustaa jatkuvaa/vahvistunutta tehoa **naisen rintasyövän** hoitoon, ja kirjallisuushaussa löydettiin **50 kliinistä tutkimusta** ja **20 julkaisua** tukevia tätä havaintoa.
Koska tämä indikaatio päällekkäistyy docetakselin jo vakiintuneen tosielämän käytön kanssa (evidenssipaketin omat perustelut osoittavat), tätä tulisi lukea pikemmin **vahvistavan signaalin** kuin **uuden uudelleenkäyttötarkoituksen kandidaatin**.

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu evidenssipakettiin (ei `original_indications` tai lisenssi­tietoja arkistossa) |
| Ennustettu uusi indikaatio | Naisen rintasyöpä |
| TxGNN-ennusteen pistemäärä | 99.90% |
| Evidenssin taso | L1 |
| Suomen/Taiwanin markkinatilanne | ✗ Ei markkinoitu |
| Hyväksynnän kokonaismäärä | 0 |
| Suositeltu päätös | Jatka varauksin |

---

## Miksi tämä ennuste on järkevä?

Docetaxel on taksiini. Se stabiloi mikrotubuluksia ja estää niiden depolymeroitumista, mikä lukitsee nopeasti jakautuvat solut G2/M-vaiheeseen ja ajaa apoptoosin. Koska rintasyövän solut ovat nopean lisääntymisen vaiheessa, tämä mekanismi on suoraan olennainen ennustettuun indikaatioon.

Evidenssipaketin oman uudelleenkäyttöperustelun mukaan on tärkeä varoitus: docetaxel (Taxotere) on **tällä hetkellä hyväksytty kemoterapia rintasyövän hoitoon** useimmilla markkinoilla — tämä ei ole tyypillinen "vanha lääke, uusi tauti" -uudelleenkäyttötapaus. Se ilmestyy tähän vain siksi, koska tämän evidenssipaketin `original_indications`-kenttä on tyhjä, joten malli/pisteytysputki arvioi rintasyövän ikään kuin vahvistamattomaksi kandidaatiksi. Alla olevan valmistuneiden 3. vaiheen tutkimusten hyvin suuri määrä (mukaan lukien tutkimukset, joissa oli >2 000–3 000 rekrytoitua potilasta) heijastaa tätä: ne ovat tutkimuksia, jotka vakiintuvat/optimoivat docetakselin roolia rintasyövän hoidossa, eivät tutkivia uudelleenkäyttötutkimuksia.

Koska tähän evidenssipakettiin ei ole sisällytetty Suomen/Taiwanin markkinoiden lisenssi- tai sääntelydokumentaatiota ("Ei markkinoitu", 0 hyväksyntää), käytännöllinen seuraava vaihe on sääntelyvoiman vahvistus eikä jatkomekanistisen perustelun.

---

## Kliinisen tutkimuksen evidenssi

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät löydökset |
|---------|------|------|------|---------|
| [NCT00002544](https://clinicaltrials.gov/study/NCT00002544) | 3. vaihe | Valmistunut | 300 | Mitokantroni ± docetaxel ensimmäisen linjan kemoterapiana levinneessä rintasyövässä huonolla ennusteella |
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | 3. vaihe | Valmistunut | 150 | Viikoittainen docetaxel vs. CMF adjuvantti­hoitona korkean riskin ≥65 vuotta tai antrasykliini-kelpaamattomissa rintasyöpäpotilaissa |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | 3. vaihe | Valmistunut | 3270 | Docetaxel+syklofosfamiidi tai doksorubisiini+syklofosfamiidi→paklitakseli, ± trastuzumabi, solmukkeiden sisältävissä/korkean riskin HER2-matalissa rintasyövissä |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | 3. vaihe | Valmistunut | 2611 | Adriamysiini/Cytoxan seurattuna Taxoteella ± Xelodalla; kokonaisselviytyminen korkean riskin rintasyövässä |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | 3. vaihe | Valmistunut | 2411 | Esileikkausta edeltävä AC vs. AC seurattuna pre- tai postleikkausta jälkeisellä docetakselilla hoitokelpoisessa rintasyövässä |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | 3. vaihe | Valmistunut | 315 | Neoadjuvantti docetaxel, karboplatiini, trastuzumabi, pertuzumabi (TCHP) ± estrogeenistriippaus HR+/HER2+-rintasyövässä |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | 3. vaihe | Valmistunut | 204 | TAC (docetaxel/doksorubisiini/syklofosfamiidi) vs. TCX (docetaxel/syklofosfamiidi/kapesitabiini) adjuvantti­hoitona korkean riskin HER2-negatiivisessa rintasyövässä |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | 3. vaihe | Valmistunut | 478 | Tiivis-annostettu FE75C→docetaxel vs. paklitakseli adjuvantti­hoitona solmuke-positiivisessa rintasyövässä |
| [NCT03252431](https://clinicaltrials.gov/study/NCT03252431) | 3. vaihe | Valmistunut | 393 | F-627 vs. Neulasta naisissa, joilla on Stage I–III rintasyöpä ja jotka saavat myelotoksiaa aiheuttavaa (docetaxel-sisältävää) kemoterapiaa |
| [NCT00003565](https://clinicaltrials.gov/study/NCT00003565) | 2. vaihe | Valmistunut | 109 | Docetakselin populaatiofar­makokinetiikat kaukaasialaisissa ja afrikkalaisen alkuperän kantaisissa kiinteän kasvaisuuden potilaissa |

---

## Kirjallisuuden evidenssi

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät löydökset |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | Docetaxel+syklofosfamiidi (TC) vs. antrasykliini-taksiini-regiimit (TaxAC) varhaisvaiheen rintasyövässä (ABC-tutkimuksien yhdistetty analyysi) |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Katsaus | Drug and Therapeutics Bulletin | Paklitakselin ja docetakselin varhaiskatsaus rintasyövän ja munuaisovarian syövän hoidossa |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Katsaus | The Oncologist | Docetakselin ja paklitakselin kliinisen käytön katsaus rintasyövän hoidossa |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Kohortti­tutkimus | Anti-Cancer Drugs | Yhteys adjuvantti docetaxel-pohjaisen kemoterapian ja rintasyöpään liittyvän lymfödeemin välillä |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Katsaus (luokitus vireillä) | J Clin Oncol | Docetakselin (Taxotere) preclinical- ja klinisen profiilin perustutkimus­katsaus |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Tutkimus (luokitus vireillä) | Breast Cancer (Tokyo) | Docetaxel+syklofosfamiidi+trastuzumabi neoadjuvantti­hoitona HER2+-ensisijaisen rintasyövän hoidossa |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Tutkimus (luokitus vireillä) | Breast Cancer (Tokyo) | CEF seurattuna docetakselilla esileikkausta edeltävänä kemoterapiana varhaisvaiheen rintasyövässä |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Tutkimus (luokitus vireillä) | Cancer | Kapesitabiini + docetaxel + epirubisiini (TEX) ensimmäisen linjan hoitona edistyneessä rintasyövässä |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Tutkimus (luokitus vireillä) | Oncology | Viikoittainen docetaxel + gemitsitiini ensimmäisen linjan hoitona levinneessä rintasyövässä |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Tutkimus (luokitus vireillä) | J Clin Oncol | Tiivis-annostettu doksorubisiini/docetaxel/G-CSF ± tamoksifeeni esileikkausta edeltävänä hoitona hoitokelpoisessa rintasyövässä |

---

## Suomen ja Taiwanin markkinatiedot

Tähän evidenssipakettiin ei ole sisällytetty docetakselin hyväksynnän tietueita. Markkinatilanne merkitään **Ei markkinoitu**, jossa on **0 hyväksyntää yhteensä**.

---

## Sytostaattinen vaikutus

| Kohta | Sisältö |
|------|---------|
| Sytostaattisen vaikutuksen luokitus | Tavanomainen sytostaatti (taksiini-luokka, mikrotubuli-stabiloiva aine) |
| Luuydintykitysriski | Katso pakkausselosteen varoituksista ja varotoimista |
| Pahoinvointi-induktioriskin luokitus | Katso pakkausselosteen varoituksista ja varotoimista |
| Seurantakohdat | Katso pakkausselosteen varoituksista ja varotoimista |
| Käsittelysuojaus | Katso pakkausselosteen varoituksista ja varotoimista |

---

## Turvallisuusnäkökohdat

Katso turvallisuustietoja pakkausselosteen osalta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksin**

**Perustelut:**
Todistusaineisto on vahva (L1: useita valmistuneita 3. vaiheen satunnaistettuja kontrolloituja tutkimuksia, mukaan lukien tutkimukset, joissa oli >2 000–3 000 rekrytoitua potilasta) ja mekanistisesti johdonmukainen, mutta tämä indikaatio näyttää heijastavan docetakselin jo vakiintunutta kliinistä käyttöä rintasyövän hoitoon eikä todellista uutta uudelleenkäyttötarkoitusta — ja pakettiin ei ole Suomen/Taiwanin sääntelyyn tai turvallisuuteen liittyvää dokumentaatiota itsenäisen arvioimisen tueksi.

**Jatkamista varten tarvitaan seuraavat:**
- TFDA/Fimea pakkausselose (varoitukset, vasta­indikaatiot) — tällä hetkellä este (DG001)
- Vahvistetut lääkkeiden väliset interaktiot (DDI) — nykyinen kysely ei tuonut tuloksia
- Docetakselin todellisen alkuperäisen ja/tai hyväksytyn indikaation/indikaatioiden vahvistaminen, koska `original_indications` on tyhjä tässä paketissa
- Paikallisen (Taiwanin/Suomen) markkinan ja lupa­tilanteen selventäminen ennen kuin väiteetään "uudesta indikaatiosta", koska nykyinen status on Ei markkinoitu ja hyväksyntöjä on 0

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

