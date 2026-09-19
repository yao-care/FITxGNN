---
layout: default
title: Turoctocog Alfa
parent: Pelkkä mallin ennuste (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog alfa: Hemofiliasta A primaariseen verihiutaleiden vapautumishäiriöön

## Yhden lauseen yhteenveto

Turoctocog alfa on rekombinantti Factor VIII -valmiste, jota käytetään verenvuotojen hoitoon ja ehkäisyyn hemofiliassa A. TxGNN-malli ennustaa, että se saattaa olla tehokas **primaariseen verihiutaleiden vapautumishäiriöön**, mutta tällä kandidaatilla ei ole tällä hetkellä **tukevia kliinisiä tutkimuksia eikä tukevia kirjallisuuslähteitä**, ja mallin oman perustelun mukaan mekanistinen yhteys on heikko.

## Pika-yhteenveto

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Hemofilia A (Factor VIII -korvaus) — ei voida varmentaa paikallisesta hyväksymistekstistä, koska valmistetta ei tällä hetkellä markkinoida täällä |
| Ennustettu uusi indikaatio | Primaarinen verihiutaleiden vapautumishäiriö |
| TxGNN-ennustepisteet | 99.99% |
| Näytön taso | L5 (vain mallin ennuste, ei tukevia tutkimuksia tai kirjallisuutta) |
| Suomen markkinatilanne | Ei markkinoinnissa (Ei markkinoinnissa) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaiset vaikutusmekanismin tiedot eivät ole saatavilla tässä näyttöpaketissa (`original_moa: [Data Gap]`). Tunnetun farmakologian perusteella turoctocog alfa on rekombinantti Factor VIII (FVIII) -konsentraatti; sen vahvistettu tehtävä on korvata hemofiliassa A puutteellista FVIII:n hyytymisaktiviteettia.

Primaarinen verihiutaleiden vapautumishäiriö on kuitenkin verihiutaleiden granulaarin erityshäiriö (esim. δ-varastopoolin sairaus) eikä hyytymistekijän puute. Verenvuotoriski tässä tilassa johtuu siitä, että verihiutaleista ei vapaudu niiden granulaarin sisältöä, ei puutteellisesta FVIII:sta. Näyttöpaketin oman uudelleenkäyttöperustelun mukaan tämä yhteys on nimenomaisesti heikko: FVIII-täydennys ei voi korjata verihiutaleiden granulaarin vapautumishäiriötä.

Lyhyesti sanottuna TxGNN-pistemäärä on korkea, mutta taustalla oleva biologia ei selvästi tue FVIII-korvauksen ekstrapolointia tähän verihiutaleiden häiriöön. Tämä on tapaus, jossa vahvaa mallipistettä ei seuraa uskottava mekanistinen kertomus, eikä kliinisiä tai kirjallisuusperusteisia todisteita ole tällä hetkellä olemassa ennusteen riippumattomaksi vahvistamiseksi.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla liittyviä kirjallisuuslähteitä.

## Suomen markkinatiedot

Turoctocog alfalla ei ole tällä hetkellä **markkinointilupia** Suomessa (`market_status: Not marketed`, `total_licenses: 0`); mitään luparekistereitä ei ole saatavilla luetteloimista varten.

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkauksen sisällä olevasta tiedotteesta. (Tärkeät varoitukset, vasta-aiheet ja lääkkeen vuorovaikutustiedot ovat kaikki tällä hetkellä saatavilla — DDI-kysely ei palauttanut tuloksia.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Ennustettu indikaatio on alimmalla näyttötasolla (L5) — ei ole kliinisiä tutkimuksia, ei kirjallisuutta, ja mekanistisen perustelun itse arvioidaan olevan heikko (verihiutaleiden granulaarin vapautumishäiriö verrattuna hyytymistekijän korvaamismekanismiin). Useat alemman sijoituksen omaavat kandidaatit tässä samassa näyttöpaketissa (esim. trombotinen trombosytopenia) sisältävät jopa uskottavan turvallisuushuolen, koska FVIII-täydennys on pro-hyytyminen ja saattaisi teoreettisesti pahentaa pro-trombottista tilaa — mikä vahvistaa, että näihin TxGNN-pisteisiin ei pidä ryhtyä toimiin ilman mekanistista ja kliinistä tarkastelua.

**Jatkaakseen seuraavaa tarvitaan:**
- Vahvistettu vaikutusmekanismin (MOA) dokumentaatio turoctocog alfalle (DG002, High severity)
- Paikallinen liitepaperi / sääntelyvaroitukset ja vasta-aiheet (DG001, Blocking severity — vaaditaan ennen mitään S1-turvallisuusseulontaa)
- Hematologian/hyytymisen asiantuntijan katsaus siitä, onko FVIII-korvauksella mitään uskottavaa roolia verihiutaleiden granulaarin vapautumishäiriöissä
- Jatkuva kirjallisuuden/tutkimuksen valvonta, koska mikään ei tällä hetkellä ole olemassa yhdellekään 10:stä ennustetusta indikaatiosta tässä paketissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

