---
layout: default
title: Bevacizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: edistyneistä kiinteistä kasvaimista silvanteen syöpään

## Yhden lauseen yhteenveto

Bevacizumab (DB00112) on rekombinantti humanisaattu anti-VEGF-A-monoklonaalinen vasta-aine, jota käytetään maailmanlaajuisesti osana yhdistelmiä erilaisille VEGF-vetoisille kiinteille kasvaimille. TxGNN-malli ennustaa, että se saattaa olla tehokas **silvanteen syöpään** (sen korkeimmin pisteytetty ehdokas, pistemäärä 0.9990), mutta tämä näyttöpaketti sisältää tällä hetkellä **nolla kliinistä tutkimusta** ja **nolla julkaisua**, jotka ovat erityisiä tälle käyttöaihkeelle.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen käyttöaihe | Ei saatavilla näyttöpaketissa (`original_indications` tyhjä; Suomi: ei markkinoilla, ei lupa-asiakirjaa) |
| Ennustettu uusi käyttöaihe | Silvanteen syöpä |
| TxGNN-ennustepistemäärä | 99.90% |
| Näyttötaso | L5 |
| Markkinatilanne Suomessa | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pito |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista toimintamekanismin tietoja ei ole saatavilla näyttöpaketissa (`original_moa`: Data Gap DG002). Tunnettujen tietojen perusteella bevacizumab on monoklonaalinen vasta-aine, joka sitoutuu ja neutralisoi verisuonen endoteelin kasvutekijä-A:ta (VEGF-A), estäen angiogeneesin; sitä käytetään maailmanlaajuisesti osana yhdistelmäkemoterapia-annoksia eri VEGF-veto isille kiinteille kasvaimille (esim. metastasoitunut paksusuolen syöpä, ei-levysolusyöpä NSCLC, munuaissolujen karsinooma, munarauhassyöpä, kohdunkaulansyöpä, glioblastooma). Suomalaista markkinointilupia ei ole olemassa tässä näyttöpaketissa (`market_status`: Not marketed / Ei markkinoilla, 0 lupaa).

Silvanteen syövän osalta näyttöpaketti ei sisällä lainkaan kliinisiä tutkimuksia tai kirjallisuutta. Mekanistinen perusteltu on rajoitettu luokkatasoisen yleistämiseen: bevacizumabia on tutkittu muilla pään ja kaulan syöpäkohteilla (katso niihin liittyvät ehdokkaat alla), ja anti-VEGF-terapialla on biologisesti perusteltu rationale pään ja kaulan levysolusyövissä laajasti. Silvanteen syövän kohdalla tämä on kuitenkin vielä vahvistamaton ekstrapolaatio ilman paikan kohtaisia tukemisen tietoja – TxGNN-pistemäärä yksinään (99.90%) ei ole saattanut vahvistavia tutkimuksia tai julkaisuja.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole asiaan liittyviä rekisteröityjä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä kirjallisuutta ei ole saatavilla

## Markkinatiedot Suomesta

Bevacizumabia ei ole tällä hetkellä markkinoilla Suomessa (`total_licenses` = 0; lupa-asiakirjoja ei ole saatavilla).

## Sytotoksisuus

Bevacizumab on antineoplastinen lääke (anti-VEGF-monoklonaalinen vasta-aine, jota käytetään yksinomaan syövän hoitoannoksissa), joten tämä osio koskee sitä.

| Kohta | Sisältö |
|-------|---------|
| Sytotoksisuuden luokittelu | Kohdennettua hoitoa (anti-angiogeniininen monoklonaalinen vasta-aine; ei perinteinen sytostaattinen kemoterapeutti) |
| Ytimen sortumistaipumuksen riski | Katso pakkausseloste varoitukset ja varotoimet |
| Pahoinvointiherkkyysluokittelu | Katso pakkausseloste varoitukset ja varotoimet |
| Seurantakohteet | Katso pakkausseloste varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausseloste varoitukset ja varotoimet |

## Turvallisuusnäkökohdat

Katso turvallisuustietoja pakkauksesta.

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pito**

**Perustelut:**
TxGNN-pistemäärä on korkea (99.90%), mutta silvanteen syövän osalta ei ole kliinisiä tutkimuksia tai kirjallisuuden näyttöä – näyttötaso on L5 (vain mallin ennuste), ja tätä lääkettä ei ole markkinoilla Suomessa.

**Jotta voitaisiin edetä, tarvitaan seuraavaa:**
- Paikankohtaisia kliinisiä tutkimuksia tai kirjallisuuden näyttöä bevacizumabista silvanteen syöpää vastaan
- TFDA/Suomen pakkausseloste varoitukset ja vasta-aiheet (DG001, Esto – tällä hetkellä puuttuu)
- Vahvistettu yksityiskohtainen toimintamekanismin tieto (DG002)
- Vahvistus siitä, että "silvanteen syöpä" on oikein kartoitettu tautiin liittyvä ontologiatermi TxGNN-ennusteessa

---
**Huomautus:** Tämän saman näyttöpaketin sisällä alemmin sijoittuva ehdokas – **kystinen syöpä** (sijoitus 7, TxGNN-pistemäärä 99.89%) – sisältää huomattavasti vahvemman tukemisen näytön (8 kliinistä tutkimusta, joihin sisältyy vaihe 3 RCT, 20 julkaisua, Näyttötaso L1, päätöksentekouasema S3, suositus "Etene varoituksilla"), pääasiassa johtuen bevacizumabin vakiintuneesta käytöstä matalaasteisennytkään munarauhassyövän hoitamisessa. Tuo ehdokas saattaa vaatia erillistä arviointia korkeampiprioriteetin lääkkeen uudelleenkäyttämisen mahdollisuutena.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

