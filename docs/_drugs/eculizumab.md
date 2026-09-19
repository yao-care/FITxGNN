---
layout: default
title: Eculizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Ekulitsumabi: Paroksysmaalisen yöllisen hemoglobiinuriasta sykliseen verisolujen muodostukseen

## Yhden lauseen yhteenveto

Ekulitsumabi on komplementin C5-estäjä, jonka vakiintunut käyttöaihe on komplementinmedioidut häiriöt, kuten paroksysmaalinen yöllinen hemoglobiinuria (PNH) ja atypillinen hemolyysi-uremiasyndromi (aHUS). TxGNN-malli ennustaa, että se voi olla tehokas **syklisessä verisolujen muodostuksessa**, mutta tämä sijoitus perustuu puhtaasti upotukseen perustuvan samankaltaisuuden pohjalle — **0 kliinistä tutkimusta** ja **0 julkaisua** tukee tätä erityistä yhdistelmää, eikä taustalla olevan sairauden biologia (ELANE-väliintuleva neutrofiilisykli) ole tunnustetulla tavalla yhteydessä komplementtireittiin.

## Pikaohjeistus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihe | Komplementinmedioidut häiriöt (PNH, atypillinen HUS) — päätelmä kirjallisuudesta, joka on otettu tähän näyttöpakettiin; ei ole erikseen vahvistettu rakenteisen lääketietueen kautta |
| Ennustettu uusi käyttöaihe | Syklinen verisolujen muodostus |
| TxGNN-ennustepisteet | 99,97% |
| Näyttöjen taso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Markkinointilupapäätösten lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaista, lähteillä tuettua vaikutusmekanismin tietoa ekulitsumabista ei ole saatavilla tässä näyttöpaketissa (merkitty korkeimman vakavuuden tietovajeeksi, DG002). Tukevassa kirjallisuudessa ja perustelutietueissa sisältyvien tietojen perusteella ekulitsumabi on humanisaitu monoklonaalinen vasta-aine, joka sitoutuu komplementtiproteiiniin C5 ja estää sen pilkkoutumisen C5a:ksi ja C5b-9:ksi, mikä estää terminaalisen komplementin (kalvohyökkäysmonimerin) aktivaatiota. Tämä mekanismi selittää sen vakiintuneen tehokkuuden komplementinmedioidussa hematologisessa sairaudessa (PNH, aHUS) ja tässä kuvatuissa laadullisissa kirjallisuusglähteissä muissa komplementtiin liittyvissä tiloissa, kuten thrombotisissa mikroangiopatioissa ja CD59-puutossyndroomeissa.

Syklinen verisolujen muodostus on kuitenkin granulosyytin tuotannon jaksoittainen häiriö, jonka aiheuttaa ELANE-mutaatiot (neutrofiilielastaasin mutaatiot), jotka vaikuttavat myeloidisolujen esiasteikkojen erilaistumiseen ja selviytymiseen — reitillä, jolla ei ole tunnettua yhteyttä terminaalisen komplementin aktivaatioon. Tähän kandidaattiin liitetyssä repurposoinnin perustelutekstissä nimenomaisesti todetaan, että ei ole tunnettua mekanismia, jolla C5-esto korjaisi ELANE-aiheuttamaa syklistä häiriötä, ja tämä sijoitus johtuu puhtaasti TxGNN:n opitusta upotukseen perustuvan samankaltaisuudesta sairauksien välillä, ei mistään jaetusta patofysiologiasta.

Näiden mekanististen eroavuuksien ja täydellisen kliinisten tai kirjallisuuslähtöjen puuttumisen vuoksi tätä ennustetta olisi tulkittava vain hypoteesia luovaksi signaaliksi, ei kliinisesti tuetuksi repurposointimahdollisuudeksi.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä vastaavia kliinisiä tutkimuksia.

## Kirjallisuuslähtöjen näyttö

Tällä hetkellä ei ole saatavilla vastaavia kirjallisuuslähtöjä.

## Suomen markkinatiedot

Markkinointilupapäätösten tietueita ei ole saatavilla tälle markkinalle — ekulitsumabi ei ole tällä hetkellä **markkinoilla** tässä alueella (0 lupapäätöstä tiedostoissa).

## Turvallisuushuomiot

Turvakkautta koskevat tiedot löytyvät pakkaussesite-dokumentista. (TFDA:n pakkausesite-tietoja ei ole vielä saatu — merkitty estävaksi tietovaheeksi, DG001, vaatii muuta ennen kuin voidaan edetä vaiheen 1 turvallisuusarviointiin.)

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Ennuste on tuettu vain TxGNN:n upotukseen perustuvan samankaltaisuuden pohjalla (L5, S0), jossa on nolla kliinistä tutkimusta ja nolla kirjallisuuslähtöjä, ja repurposoinnin perusteluteksti itse tunnistaa, ettei ole uskottavaa mekanistista yhteyttä komplementin C5-estontyökalun ja ELANE-aiheuttaman syklisen verisolujen muodostuksen välillä. Huomaa, että 9 muuta TxGNN:n ennustamaa indikaatiota tälle kandidaatille (kaikki synnynnäiset neutropeniat/immuunivajavuussyndroomat) käytiin läpi rinnakkain tämän kanssa ja ne näyttävät samalta mallilta — korkeat samankaltaisuuspisteet mutta ei mekanistista, tutkimus- tai todella aiheeseen liittyvää kirjallisuustukea.

**Jotta voitaisiin edetä, seuraavaa tarvitaan:**
- TFDA:n/paikallisten sääntelyviranomaisten pakkausesite (varoitukset, vasta-aiheet) — tällä hetkellä estävä tietovahe
- Vahvistettu vaikutusmekanismin dokumentaatio DrugBank:sta tai alkuperäisestä kirjallisuudesta
- Prekliiniset tai mekanistiset tutkimukset, jotka suoraan yhdistävät komplementtireittiaktiviteetin ELANE-aiheuttamaan neutrofiilisykliin, jos tällainen yhteys koskaan muodostetaan
- Kirjallisuushaun termien uudelleentarkistus, koska aiemmat kyselyt vastaavista kandidaateista (esim. sijoitus 4 ja sijoitus 10) palautivat osumia, joita ohjasivat avainsanayhtymät eikä sairauksille spesifinen relevanssi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

