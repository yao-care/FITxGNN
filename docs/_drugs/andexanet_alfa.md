---
layout: default
title: Andexanet Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 31
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Andexanet Alfa: Antikoagulantin palauttava aine — TxGNN-ennusteet eivät vielä saatavilla

## Yhden lauseen yhteenveto

Andexanet alfa on rekombinantti modifioitu ihmisen Factor Xa -köydenheittoproteiini, joka on hyväksytty kansainvälisesti palautuslääkkeeksi Factor Xa -inhibiittorien aiheuttamiin elämää uhkaaviin tai hallitsemattomiin verenvuotoihin. TxGNN-malli ei ole vielä tuottanut ennustettuja indikaatioita tälle lääkkeelle nykyisessä Evidence Packissa — kliinisen tutkimuksen ja kirjallisuuden todisteet eivät siten ole saatavilla. Tämä raportti dokumentoi nykyisen tiedon tilan ja esittelee korjaustoimenpiteet, joita tarvitaan, ennen kuin uudelleenkäytön arviointia voidaan jatkaa.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Factor Xa -inhibiittorien aiheuttaman antikoagulaation peruuttaminen elämää uhkaavissa tai hallitsemattomissa verenvuodoissa (FDA/EMA-hyväksytty; ei vielä rekisteröity Suomessa) |
| Ennustettu uusi indikaatio | ⚠️ Ei saatavilla — TxGNN-ennusteet puuttuvat Evidence Packista |
| TxGNN-ennustepisteet | — |
| Todistelun taso | — (ei voida määrittää ilman ennustettuja indikaatioita) |
| Suomen markkinatilanne | ✗ Ei markkinoinnissa |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | **Keskeytä** |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä Evidence Packissa ei ole saatavilla yksityiskohtaisia toimintamekanismin tietoja (Datakuilu DG002). Tunnettujen farmakologisten tietojen perusteella andexanet alfa on katalyyttisesti inaktiivinen rekombinantti ihmisen Factor Xa -variantti. Se toimii "köydenheittovastaanottimena", joka sitoutuu kilpailussa ja kerää liikkeellä olevia Factor Xa -inhibiittoreita — mukaan lukien apixaban ja rivaroxaban — ja näin palauttaa endogeenisen trombiinin tuotannon sekä peruuttaa antikoagulantin vaikutuksen.

Koska TxGNN-malli vaatii mekanistisen ja graafipohjaisen todistelun perustan uudelleenkäytön ehdokkaiden tuottamiseen, toimintamekanismin tietojen puuttuminen (DG002) ja minkään ennustetun indikaation puuttuminen tästä Evidence Packista tarkoittaa, että ei ole tällä hetkellä mahdollista arvioida, onko andexanet alfan mekanismi soveltuvissa mihinkään uuteen indikaatioon.

Ennen kuin mekanistinen uudelleenkäytön perustelu voidaan muodostaa, kaksi estävää datakuilua (DG001: turvallisuus/pakkausseloste; DG002: toimintamekanismi) on ratkaistava.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröity liittyviä kliinisiä tutkimuksia ennustetusta uudesta indikaatiosta — TxGNN-ennusteet puuttuvat tästä Evidence Packista.

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta ennustetusta uudesta indikaatiosta — TxGNN-ennusteet puuttuvat tästä Evidence Packista.

---

## Suomen markkinatiedot

Andexanet alfaa ei ole tällä hetkellä hyväksytty tai markkinoitu Suomessa. Tutkinnolla ei ole lisenssejä.

| Luvannumero | Tuotteen nimi | Lääkemuoto | Hyväksytty indikaatio |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Yhtään hyväksyntää ei löydetty |

> **Huomautus:** Andexanet alfaa markkinoidaan Yhdysvalloissa nimellä **Andexxa** (AstraZeneca/Pfizer) ja Euroopan unionissa nimellä **Ondexxya** (AstraZeneca). EMA:n myyntilupa on olemassa (EU/1/19/1404), mutta tämä lääke ei ole rekisteröity Fimean kautta Suomen markkinoille tiedon leikkaushetkellä.

---

## Turvallisuutta koskevat näkökohdat

Katso pakkausselosteesta turvallisuustiedot.

> ⚠️ **Datakuilu DG001 (Esto):** Pakkauselosteesta saatavat varoitukset ja vasta-aiheet -tiedot eivät ole jäsennetty Evidence Packiin. Tämä kuilu on ratkaistava ennen kuin mitään turvallisuusseulontaa (S1 Safety Gate) voidaan suorittaa.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Keskeytä**

**Perustelu:**
Andexanet alfan Evidence Pack sisältää kaksi ratkaisematonta datakuilua — turvallisuus-/pakkauseloste-tiedon estävä kuilu (DG001) ja toimintamekanismin tiedon korkean vakavuuden kuilu (DG002) — ja TxGNN-malli ei ole tuottanut ennustettuja indikaatioita tälle lääkkeelle. Ilman ennustettuja indikaatioita uudelleenkäytön hypoteesia ei ole arvioitavaksi.

**Jotta edistystä voidaan tehdä, seuraava on tarpeen:**

1. **Ratkaise DG001 (Esto):** Lataa ja jäsennä TFDA/Fimean pakkauseloste PDF-muodossa poimiaksesi hyväksytyt varoitukset, vasta-aiheet ja erityispopulaatioiden käyttörajoitukset — vaaditaan S1 Safety Gate -sisäänpääsyä varten.
2. **Ratkaise DG002 (Korkea):** Hae DrugBank API:sta andexanet alfan täydellinen toimintamekanismi, farmakodynamiikka ja proteiinikohteet — vaaditaan mekanistisen uskottavuusanalyysin suorittamiseksi.
3. **Suorita TxGNN-putki uudelleen:** Kun toimintamekanismi- ja turvallisuustiedot on täytetty, lähetä andexanet alfa uudelleen TxGNN-ennustusjärjestelmään jotta voit tuottaa ehdokkaat sairausindikaatiot pistein.
4. **Tarkista EMA/Fimea-tila:** Vahvista, onko Ondexxyan EMA-myyntilupa laajennettu Suomen markkinoille hajautetun tai keskinäisen tunnustamisen menettelyn kautta, mikä muuttaisi Suomen markkinatilannetta "Ei markkinoinnissa" -tilasta "Markkinoinnissa" -tilaan.
5. **Arvioi Evidence Pack -versio uudelleen:** Nykyinen versio on v4 ja käyttää ainoastaan `inputs_received: ["drugbank"]`. Täydellinen v5-paketti sisältää TFDA/Fimean sääntelyaineiston, DDI-tiedot ja TxGNN-ennusteet, ennen kuin täydellinen raportti voidaan tuottaa.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

