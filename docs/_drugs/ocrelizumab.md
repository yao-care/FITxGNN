---
layout: default
title: Ocrelizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 269
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **5** kpl
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

# Ocrelizumab: Multippeliskleroosilta HER2-positiiviseen rintakarsinoomaan

## Yhden lauseen yhteenveto

Ocrelizumab on anti-CD20-monoklonaalinen vasta-aine, joka on hyväksytty multippeliskleroosin hoitoon ja toimii CD20-ekspressoivien B-solujen poistamisen kautta.
TxGNN-malli ennustaa, että se voi olla tehokas **HER2-positiiviseen rintakarsinoomaan**,
mutta tällä hetkellä tätä spesifistä yhteyttä tukee **0 kliinistä tutkimusta** ja **0 relevanttia julkaisua** — todistepaketti itse merkitsee ennusteen todennäköisesti tietoverkko-upotusartefaktiksi pikemminkin kuin mekanismivetoiseksi signaaliksi.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Multippeliskleroosi (lääkkeen tietojen perusteella; virallinen DrugBank/mekanismi-tietue on tietoaukko) |
| Ennustettu uusi indikaatio | HER2-positiivinen rintakarsinooma |
| TxGNN-ennusteen pistemäärä | 99.89% |
| Todistusvoiman taso | L5 |
| Suomen markkinoinnin asema | Ei markkinoitu |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia toimintamekanismi-tietoja ei ole saatavissa DrugBankista (merkitty korkean vakavuustason tietoaukoksi). Tunnettujen taustatietojen perusteella ocrelizumab on anti-CD20-monoklonaalinen vasta-aine, joka poistaa CD20-positiivisia B-soluja ja on hyväksytty multippeliskleroosin hoitoon, autoimmuunisairauteen, jonka taustalla on epätyypillinen B-solun aktiviteetti.

HER2-positiivinen rintakarsinooma puolestaan syntyy HER2/neu-reseptorin yliekspressiosta, joka aktivoi proliferatiivisia signalointireittejä — mekanismi, jolla ei ole vakiintunutta biologista yhteyttä B-solun poistamiseen. Todistepaketin oma analyysi on eksplisiitti tästä: se arvioi korkean TxGNN-pistemäärän todennäköisesti heijastavan läheisyyttä tietoverkko-upotusavaruudessa pikemminkin kuin mitään todellista mekanistista yhteyttä.

Ei ole mekanistisia, prekliinisiä tai kliinisiä perusteita, jotka yhdistäisivät CD20-kohdistetun B-solun poistamisen HER2-ohjattuun rintasyövän biologiaan. Tätä ennustetta tulee käsitellä kandidaattina mallin validointiututkimuksiin, ei farmakologisesti perustetuna hypoteesina tässä vaiheessa.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuuden todisteet

Liittyvää kirjallisuutta ei ole tällä hetkellä saatavilla.

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta. Huomio: TFDA/Fimean pakkausselosteen varoitukset ja kontraindikaatiot ovat tällä hetkellä **blokaava** tietoaukko (DG001) ja ne on ratkaistava ennen kuin turvallisuuden esiselvitystä voidaan jatkaa.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Kaikkissa viidessä TxGNN-ennustetussa indikaatiossa (kaikki rintasyövän alatyyppi — HER2-positiivinen, normaalimainen, PR-positiivinen, luminalinen A/B, PR-negatiivinen) puuttuvat tukevia kliinisiä tutkimuksia ja uskottavaa kirjallisuustodistusta. Ainoa löydetty kirjallisuusosuma ("rintasyöpä luminalinen A tai B" -haku, 19 artikkelia) on väärä positiivinen avainsanaosuma kirjaimen "B" perusteella (hepatiitti B -rokotteet, HLA-B-tyypitys, B-1/B-2-lymfosyytit) ilman mitään relevanttia yhteyttä rintakarsinoomaan tai ocrelizumabiin. Todistepaketin oma analyysi johtaa siihen, että korkeat ennusteen pistemäärät todennäköisesti heijastivat tietoverkko-upotusavaruuden läheisyyttä pikemminkin kuin todellista mekanistista signaalia. Yhdessä TFDA/Fimean turvallisuustietojen puuttumisen kanssa tämä kandidaatti ei tällä hetkellä täytä vaatimuksia edetä S0:n yli.

**Edetäkseen tarvitaan seuraavaa:**
- TFDA/Fimean pakkausseloste (varoitukset, kontraindikaatiot) — tällä hetkellä blokaava
- Muodollinen toimintamekanismi-tietue DrugBankista
- Prekliininen/in vitro -todiste CD20+ B-solujen roolista HER2-ohjattavissa tai muissa rintakarsinoomien alaryhmissä
- Kohdistettu kirjallisuushaku käyttäen rintakarsinooma-spesifisiä ja ocrelizumab-spesifisiä termejä kaikkien muiden neljän sijoitetun kandidaatin osalta avainsana-ohjattujen väärien positiivisten poistamiseksi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

