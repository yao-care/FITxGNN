---
layout: default
title: Chenodeoxycholic Acid
parent: Pelkkä mallin ennuste (L5)
nav_order: 100
evidence_level: L5
indication_count: 5
---

# Chenodeoxycholic Acid
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

# Keenodesoksikoalahappo: Sappihappoaineenvaihdunnan häiriöistä homotsygotiseen familiaaliseen hyperkolesterolemiaan

## Yksilauseen yhteenveto

> Keenodesoksikoalahappo (CDCA) on luonnollisesti esiintyvä primaarinen sappihappo; todistustekapaketti ei kirjaa mitään erityistä Taiwanin/Suomen hyväksymää alkuperäistä indikaatiota tälle yhdisteelle, vaikka se on historiallisesti liitetty sappihapposynteesin ja kolesteroliaineenvaihdunnan häiriöihin (esim. saippalakivien liuotus, cerebrotendinoosinen ksantomatoosi).
> TxGNN-malli ennustaa, että se voi olla tehokas **homotsygotisessa familiaalisessa hyperkolesterolemiassa**,
> jolle on tällä hetkellä tunnistettu **0 kliinistä tutkimusta** ja **1 julkaisu**, ja kyseinen julkaisu käsittelee samankaltaista – ei samaa – sairautta.

## Pikayleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei saatavilla todistustekapaketeissa (`drug.original_indications` on tyhjä; `original_moa` on tiedon puute) |
| Ennustettu uusi indikaatio | Homotsygotinen familiaali hyperkolesterolemia |
| TxGNN-ennustepistemäärä | 99.57% |
| Todisteen taso | L5 (vain mallin ennuste tälle indikaatiolle; ainoa liittyvä julkaisu käsittelee eri, mekanistisesti vierekkäistä sairautta) |
| Suomen markkinoiden asema | Ei markkinoitu (Ei markkinoitu) |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja keenodesoksikoalahapon käytöstä ei ole saatavilla tässä todistustekapaketeissa (merkitty erittäin vakavaksi tiedon puutteeksi, DG002). Yleisen farmakologisen tiedon perusteella CDCA on primaarinen sappihappo, joka osallistuu sappihapposynteesin säätelyyn; sitä on käytetty kliinisesti sappihappoon liittyvillä ja kolesteroliaineenvaihduntaan liittyvillä häiriöillä, mikä tarjoaa uskottavan mekanistisen yhteyden lipidi/kolesterolikasvaintauteihin.

Ainoa haettu julkaisu (PMID 25424010) on katsaus cerebrotendinoosiseen ksantomatoosiin (CTX) – harvinaiseen autosomaalisen resessiiviseen lipidin varastointisairauteen, jonka aiheuttavat CYP27A1-mutaatiot, jotka häiritsevät sappihapposynteesin ja aiheuttavat kolesteroolin/kolestanolin kertymisen. CTX:ää hoidetaan CDCA:n korvaavalla hoidolla, ja taustalla oleva biologia (viallinen sappihappo/kolesterolinkäsittely) on käsitteellisesti samanlainen kuin homotsygotinen familiaali hyperkolesterolemia (HoFH), joka liittyy myös vakavaan kolesterolin sääntelyn häiriöön. Tämä päällekkäisyys kolesteroliradan biologiassa on järkevä perusta TxGNN-mallin yhdistämiselle, mutta sitä tulisi käsitellä mekanistisena hypoteesina pikemminkin kuin suorana todisteena, koska paketeissa oleva mikään tutkimus ei tutki CDKA:ta erityisesti HoFH-potilaissa.

Koska `original_moa` ja `original_indications` eivät täyty tässä todistustekapaketeissa, mekanistisen yhteyden vahvuutta ei voida täysin arvioida; tämä on kirjattu tiedon puutteeksi DG002 ja se tulisi ratkaista DrugBankin/tuotteen merkinnän avulla ennen kuin jatketaan arviointia.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole liittyviä rekisteröityjä kliinisiä tutkimuksia

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|------|--------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Katsaus | Orphanet Journal of Rare Diseases | Kattava katsaus cerebrotendinoosiseen ksantomatoosiin (CTX), CYP27A1-mutaation aiheuttamaan sappihapposynteesin häiriöön, joka aiheuttaa kolestanolin kertymisen; CDCA on CTX:n vakiintunut korvaushoito. Sairaus on mekanistisesti samanlainen, mutta eri kuin homotsygotinen familiaali hyperkolesterolemia. |

## Suomen markkinatiedot

Keenodesoksikoalahappo ei ole tällä hetkellä markkinoitu Suomessa — `taiwan_regulatory.market_status` on "Ei markkinoitu" (Not Marketed), 0 rekisteröidyllä valtuuksella, joten valtuus-/tuotetaulukkoa ei ole saatavilla.

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustietoja.

*(Keskeiset varoitukset, vasta-aiheet ja lääkkeiden väliset yhteisvaikutukset on kaikki kirjattu tiedon puutteiksi tässä todistustekapaketeissa – TFDA:n merkinnän tarkistelu, merkitty DG001, on esto-vakavuuden luokan puute.)*

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Tälle ennustettulle indikaatiolle ei ole kliinisiä tutkimuksia, Taiwanin/Suomen markkinoita, ja ainoa tukeva julkaisu käsittelee samanlaista mutta eri sairautta (CTX, ei HoFH). Yhdessä TFDA:n merkinnöissä olevan esto-vakavuuden luokan tiedon puutteen kanssa, todistusten perusta on tällä hetkellä riittämätön siirtyäkseen mallin ennusteen ulkopuolelle.

**Edistämiseksi tarvitaan seuraavaa:**
- TFDA/EMA pakkausseloste (varoitukset, vasta-aiheet) — ratkaisee esto-vakavuuden luokan puutteen DG001
- DrugBank/MOA-yksityiskohdat CDCA:n mekanismista, joka liittyy lipidiaineenvaihduntaan — ratkaisee puutteen DG002
- Omistautuneet kliiniset tai prekliiniset tutkimukset CDCA:sta erityisesti HoFH tai siihen liittyvillä dyslipidemiaväestöillä
- Lääkeyhteisvaikutusten tietokyselyjen ratkaiseminen (nykyinen tila: ei löydetty)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

