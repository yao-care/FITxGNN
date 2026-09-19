---
layout: default
title: Brolucizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 79
evidence_level: L5
indication_count: 4
---

# Brolucizumab
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

# Brolucizumabi: kostean ikääntymisen myötä ilmenevän makuukohjuksen rappeutumisesta mitokondriaalisen oksidatiivisen fosforylaation häiriöön

## Yhden lauseen yhteenveto

Brolucizumabi (kauppanimi Beovu) on anti-VEGF-A-vasta-aine-fragmentti, jota käytetään alun perin silmän sisäisellä injektiolla kostean ikääntymisen myötä ilmenevän makuukohjuksen rappeutumisen (AMD) hoitoon. TxGNN-malli ennustaa, että se saattaa olla tehokas mitokondriaalisen oksidatiivisen fosforylaation häiriössä, joka johtuu ydinperimän poikkeavuuksista, mutta tämä on vain mallipistemäärään perustuva ennuste (L5), jonka tueksi ei ole kliinisiä tutkimuksia eikä julkaisuja, ja todistuspaketti itse merkitsee mekanistisen yhteyden biologisesti epätodennäköiseksi — todennäköisesti upotuksiin perustuva väärä positiivinen tulos.

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Kostea ikääntymisen myötä ilmenevä makuukohjuksen rappeutuminen (AMD) — tunnetun lääkkeen profiilin perusteella; ei dokumentoitu toimitetussa Suomen sääntelydatajoukossa |
| Ennustettu uusi indikaatio | Mitokondriaalisen oksidatiivisen fosforylaation häiriö, joka johtuu ydinperimän poikkeavuuksista |
| TxGNN-ennusteen pistemäärä | 99.67% |
| Todistustaso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoilla (Ei markkinoilla) |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia brolucizumabin vaikutusmekanismitietoja ei ole saatavilla DrugBankista (estävä tietoaukko). Tunnettujen lääkkeen tietojen perusteella brolucizumabi on humanisoidtu yksiketjuinen vasta-aine-fragmentti (scFv), joka estää VEGF-A:n ja jota annetaan silmän sisäisellä injektiolla kostean AMD:n hoitoon — sen tehokkuus kyseisessä indikaatiossa on hyvin dokumentoitu.

Ennustettu uusi indikaatio on kuitenkin ydinperimään liittyvä mitokondriaalisen oksidatiivisen fosforylaation häiriö. VEGF-A/angiogeneesi-signaloinnin ja mitokondriaalisen energiametabolismin välillä ei ole tunnetulla biologisella reitillä päällekkäisyyttä. Todistuspaketti merkitsee tätä nimenomaisesti mekanistisen analyysissa: huolimatta korkeasta TxGNN-pistemäärästä (99.67%), perustelusta todetaan, että mekanistinen relevanssi on "äärimmäisen alhainen" ja että kyse on todennäköisesti korkeasta pistemäärästä, mutta biologisesti selittämättömästä ennusteesta — mahdollisesti upotuksiin perustuva väärä positiivinen tulos eikä todellinen farmakologia.

Kolme alhaisemman sijoituksen saaneet kandidaatit (ruokatorven varikositeetti verenvuodolla/ilman verenvuotoa, eksokriinisen haiman vajaatoiminta) ennustettiin myös samankaltaisilla korkeilla pistemäärillä (~99.1%), mutta jokaisella on omat heikkoutensa: brolucizumabin pelkkä silmän sisäinen antoreitti on yhteensopimaton systeemisen tai GI-altistumisen kanssa, joita nämä indikaatiot vaativat, ja anti-VEGF-lääkkeet sisältävät tunnetun verenvuotoriskin, joka on ristiriidassa niiden käytön kanssa verenvuoto-varikositeetissa. Yhdessäkään neljästä kandidaatista ei ole tällä hetkellä mekanistisesti puolustettava peruste.

---

## Kliinisen tutkimuksen todistusaineisto

Tällä hetkellä ei ole rekisteröity asiaan liittyviä kliinisiä tutkimuksia

---

## Kirjallisuuden todistusaineisto

Tällä hetkellä asiaan liittyviä kirjallisia lähteitä ei ole saatavilla

---

## Suomen markkinatiedot

Suomeen ei ole tällä hetkellä rekisteröity myyntilupaa brolucizumabille (markkinatilanne: Ei markkinoilla / ei markkinoilla; total_licenses = 0).

---

## Turvallisuusnäkökohdat

Turvallisustiedoista tulee viitata pakkausselosteeseen.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Korkeimman sijoituksen saanut TxGNN-ennuste ei ole tunnetulla mekanistisella reitillä päällekkäinen brolucizumabin anti-VEGF-A-vaikutukseen, sillä on nolla tukevaa kliinisiä tutkimuksia tai kirjallisuutta, ja se on nimenomaisesti merkitty todistuspaketissa todennäköiseksi upotuksiin perustuvaksi väärän positiiviseksi tulokseksi. Yhdessä lääkkeen myymättömyyden kanssa Suomessa ei ole tällä hetkellä perusteita edetä tämän kandidaatin kanssa.

**Jotta voitaisiin edetä, tarvitaan seuraava:**
- TFDA:n pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä tietoaukko (DG001)
- DrugBank-vaikutusmekanismin yksityiskohdat (DG002)
- Riippumaton mitokondriaalisen häiriön ennusteen biologisen uskottavuuden tarkistus tai alemmalla pistemäärällä olevien mutta mekanistisesti johdonmukaisten kandidaattien uudelleenarviointi
- Jos esofageaalisen varikositeetin signaali tutkitaan sen sijaan, järjestelmällisen/ruoansulatuskanavan lääkkeen altistumisen toteutettavuuden arviointi kun otetaan huomioon brolucizumabin ainoastaan silmän sisäinen antoreitti

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

