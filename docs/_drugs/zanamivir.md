---
layout: default
title: Zanamivir
parent: Pelkkä mallin ennuste (L5)
nav_order: 408
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Zanamivir: Influenssasta pyelonefriittiin

## Yhden lauseen yhteenveto

Zanamivir on neuraminidaasin estäjä, jota käytetään influenssa A ja B -infektioihin. TxGNN-mallin parhaan ennusteen mukaan sillä saattaa olla tehokkuutta **pyelonefriittiin**, mutta tällä yhdistelmällä on tällä hetkellä **0 kliinistä tutkimusta** ja **0 tukevaa julkaisua** — mallin omassa perustelussa se merkitään todennäköisesti graafimeluiksi pikemminkin kuin todelliseksi mekanistiseksi signaaliksi.

---

## Lyhyt yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Influenssa A/B (päätelty farmakologisesta luokituksesta tämän näytöpaketin tukevassa kirjallisuudessa – Fimean hyväksytyn indikaation tekstiä ei ole saatavilla; katso Markkinatilanne) |
| Ennustettu uusi indikaatio | Pyelonefriitti |
| TxGNN:n ennusteen pistemäärä | 99.84% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoilla (Not marketed) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia toimintamekanismin tietoja DrugBankista ei ole saatavilla (tietoaukko, korkea vakavuus). Liitekirjallisuudessa kerätyn farmakologisen luokituksen perusteella zanamivir on neuraminidaasin estäjä, joka estää influenssa A/B -viruspartikkelien vapautumisen infektoiduista isäntäsoluista — kapeasti kohdennettu antiviraalinen mekanismi, ei laaja-alainen.

Pyelonefriitti on bakteeriaalinen ylävirtsateiden infektio. Ei ole tunnettua polkua, joka yhdistäisi viraalisen neuraminidaasin estämisen – tai minkään isäntäsialidaasin välittämän prosessin – bakteeriaalisen pyelonefriiitin patogeneesiin. TxGNN:n 99.84 % pistemäärä heijastaa pelkkää graafi-upotuksen samankaltaisuutta; sitä ei seuraa edes yksi kliininen tutkimus tai julkaisu.

Mallin oma uusintakäytön perusteleminen tälle parille ilmaisee selvästi, että yhteys on kannustamatonta ja todennäköisesti edustaa tietojoukon melua/väärää positiivista pikemminkin kuin uskottavaa biologista signaalia. Täydellisen tukevaan näyttöön puuttuessa ja selkeän mekanistisen epäsopivuuden vuoksi tämä yhdistelmä ei täytä tällä hetkellä vaatimuksia jatkotutkimukselle.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia ei ole.

---

## Kirjallisuuden näyttö

Tällä hetkellä asiaan liittyvää kirjallisuutta ei ole saatavilla.

---

## Suomen markkinatiedot

Zanamivir ei tällä hetkellä pidä markkinoikeutta Suomessa (markkinatilanne: Ei markkinoilla / Not marketed). Ei olemassa luetteloitavia lisenssitietueita.

---

## Lisäennustettu indikaatio (sijoitus 2): Tyrosiinin aineenvaihdunnan häiriö

Täydellisyyden vuoksi mallin palauttama toinen ehdokas:

| Kohde | Sisältö |
|-------|---------|
| TxGNN:n ennusteen pistemäärä | 99.02% (sijoitus 9324) |
| Näyttötaso | L5 |
| Suositeltu päätös | Pidä |

Automaattinen haku palautti kolme PubMedin tietuetta, mutta mikään niistä ei käsittele tyrosiinin aineenvaihduntasairautta:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-------|--------|-------|----------------------|
| [23675925](https://pubmed.ncbi.nlm.nih.gov/23675925/) | 2013 | Katsaus | Infectious Disorders Drug Targets | Oseltamiviirinsisäkkyyden valvonta (H275Y neuraminidaasin mutaatio) – ei liity tyrosiinin aineenvaihduntaan |
| [25727669](https://pubmed.ncbi.nlm.nih.gov/25727669/) | 2015 | Metodologia | J Mol Recogn | SPR-assay neuraminidaasin estämisen herkkyydelle (zanamivir/oseltamivir vs. H274Y mutantti) – assay-kehitys, ei sairauden kannalta merkityksellinen |
| [21367898](https://pubmed.ncbi.nlm.nih.gov/21367898/) | 2011 | Perusviirologia | J Virology | N294S neuraminidaasin mutaatio ja H5N1 patogenisyys – ei liity tyrosiinin aineenvaihduntaan |

Nämä vastattiin todennäköisesti satunnaisella termin päällekkäisyydellä (esim. "tyrosiini" ilmaantuu neuraminidaasin mutaation nomenklatuurissa, kuten H274Y/N294S) pikemminkin kuin todellisella sairauden merkityksellisyydellä. Ei tunnettua polkua, joka yhdistäisi viraalisen neuraminidaasin estämisen endogeenisten tyrosiinia metaboloivien entsyymien (esim. FAH, TAT, HPD) kanssa. Myös tämä ehdokas tulisi pidättyä.

---

## Turvallisuusnäkökohdat

Katso turvallisuustietoja varten pakkausseloste.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelut:**
Molemmat ehdokasindikaatiot on luokiteltu L5:ksi (pelkkä mallin ennuste), nolla tukevia kliinisiä tutkimuksia ja ei genuiinisti merkityksellisiä julkaisuja – mallin omassa mekanistisessa perustelussa molemmat yhdistelmät merkitään todennäköisesti väärillä positiiveiksi pikemminkin kuin uskottaviksi uusintakäytön signaaleiksi.

**Edistämiseksi tarvitaan seuraavaa:**
- Hae TFDA/Fimea pakkausselosteen varoitukset ja vasta-aiheet (tällä hetkellä **esto** tietoaukko)
- Hanki vahvistetut toimintamekanismin tiedot DrugBankista (korkea-vakavuus tietoaukko)
- Tunnista mikä tahansa kirjallisuus tai prekliiniset tutkimukset, jotka erityisesti yhdistävät zanamivirin pyelonefriittiin tai tyrosiinin aineenvaihdunnan polkuihin – yhtään nykyään ei ole olemassa
- Jos mitään genuiini tukeva näyttö ei ilmene, alenna tämä ehdokaspari etusijalla korkeamman näyttötason TxGNN-ennustuksiin nähden

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

