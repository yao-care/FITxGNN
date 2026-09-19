---
layout: default
title: Metreleptin
parent: Pelkkä mallin ennuste (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# METRELEPTIN: dokumentoimattomasta alkuperäisestä indikaatiosta perinnölliseen yleiseen lentiginoosin

## Yhden lauseen yhteenveto

Metreleptin (DrugBank DB09046) on rekombinantti ihmisen leptiini-analogi; sen alkuperäinen hyväksytty indikaatio ja toimintamekanismi eivät ole dokumentoituja nykyisessä tietopaketissa. TxGNN ennustaa mahdollista yhteyttä **perinnölliseen yleiseen lentiginoosin**, mutta tätä ennustusta tuetaan **nolla kliinisen tutkimuksen** ja **nolla julkaisun** avulla, ja mallin omat perustelut merkitsevät sitä todennäköisesti väärä positiiviseksi artefaktiksi pikemminkin kuin aidoksi mekanistiseksi signaaliksi.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei dokumentoitu nykyisessä tietojoukossa (hyväksyttyjä indikaatioita ei ole tiedossa; toimintamekanismi merkitty korkea-asteen tietoaukoksi) |
| Ennakoitu uusi indikaatio | Perinnöllinen yleinen lentignoos |
| TxGNN-ennuste-pistemäärä | 99,71 % |
| Todistusvoimakkuusaste | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Markkinatilanne Suomessa | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidä odotuksessa |

---

## Miksi tämä ennuste on kohtuullinen?

Tällä hetkellä yksityiskohtaiset toimintamekanismin tiedot eivät ole saatavilla (estävät/korkea-asteen tietoaukot DG001 ja DG002 — TFDA-pakkausseloste ja toimintamekanismi ovat molemmat ratkaisemattomia). Yleisen farmakologian perusteella metreleptin on rekombinantti leptiini-analogi, joka vaikuttaa hypotalamuksen leptiini-reseptoreihin säädellen energiaaineenvaihduntaa ja rasvakudokseen liittyvää endokriinista toimintaa.

Korkeimmaksi arvostellun ennakoitu indikaation, perinnöllisen yleisen lentignoosin, biologiaa liittyy pigmentaatio-/melanosyyttihäiriö, joka on yleensä liitetty geeneihin, kuten PTPN11 ja RAS-MAPK-polkuun — biologiseen järjestelmään, jolla ei ole tunnettua yhteyttä leptiini/JAK2-STAT3-signalointiin. Todistepaketin oma mekanistinen arviointi tälle ehdokkaalle ilmoittaa nimenomaisesti, että tunnettu mekanistinen yhteys puuttuu, ja luonnehtii ennustetta todennäköisimmin väärä positiiviseksi artefaktiksi, joka johtuu mallin upotuksien samankaltaisuudesta harvinaisten oireyhtymien solmujen välillä TxGNN-tietograafissa, pikemminkin kuin aidoksi biologiseksi signaaliksi.

Jäljellä olevat yhdeksän arvostellut ehdokkaat (sijoitukset 2–10, kaikki harvinaiset geneettiset oireyhtymät tai syöpätaudit kuten Moynahan-oireyhtymä, rabdoidi tuumori ja periferisen hermon schwannoma) osoittavat saman kuvion: ei mekanistisia perusteluja, ei tutkimuksia ja ei kirjallisuutta. Kahdessa tapauksessa (rabdoidi tuumori, periferisen hermon schwannoma) perustelut jopa toteavat, että leptiini-signalointi on todennäköisemmin syöpää edistävää kuin syöpää estävää, mikä tarkoittaa, että leptiini-agoniisti voisi teoriassa toimia vastoin terapeuttista tavoitetta. Kokonaisuutena tarkasteltuna tämä indikaatioklasteri tulisi käsitellä matalan luottamuksen signaalina, joka vaatii riippumatonta validointia ennen kuin siihen voidaan siirtyä lisätutkimuksiin.

---

## Kliinisten tutkimusten todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

Tällä hetkellä kirjallisuustietoa ei ole saatavilla.

---

## Markkinatilanne Suomessa

Metreleptyniä ei ole tällä hetkellä markkinoilla Suomessa — markkinointilupia ei ole tiedossa (0 lupaa).

---

## Turvallisuushuomiot

Turvallisustiedot löytyvät pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä odotuksessa**

**Perustelut:**
Ennakoitu indikaatio perustuu todistusvoimakkuusasteeseen L5 (vain mallin ennuste) ilman kliinisiä tutkimuksia tai kirjallisuustukea, ja itse mekanistinen perustelut kyseenalaistavat biologisen uskottavuuden yhteydelle. Yhdessä TFDA-pakkauselosteeseen liittyvän estävän tietoaukon (vaaditaan kaikelle turvallisuusarviolle) ja ratkaisemattoman toimintamekanismin kanssa tämä ehdokas ei voi edistyä alkuarvioinnin pidemmälle (päätösvaihe S0).

**Jatkamiseksi tarvitaan seuraavaa:**
- TFDA-pakkausseloste / varoitukset ja vasta-aiheet (DG001, estävä)
- Vahvistetut toimintamekanismin tiedot DrugBank API:n kautta (DG002, korkea)
- Metreleptiinin alkuperäisten hyväksyttyjen indikaatioiden vahvistus, jotka puuttuvat tällä hetkellä tietojoukosta
- Riippumaton mekanistinen tai prekliininen todiste, joka yhdistää leptiini-signaloinnin perinnölliseen yleiseen lentiginoosin ennen kuin tehdään lisätutkimuksia tähän ehdokkaaseen
- Jos muita arvostelluja ehdokkaita halutaan tutkia (rabdoidi tuumori, periferisen hermon schwannoma), riskin suunta tulisi ensin selventää, sillä leptiini-agoniismi voi todennäköisesti edistää syöpäkasvua pikemminkin kuin estää sitä näissä yhteyksissä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

