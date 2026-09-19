---
layout: default
title: Zonisamide
parent: Pelkkä mallin ennuste (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamidi: Epilepsiasta Touretten oireyhtymään

## Yhden lauseen yhteenveto

Zonisamidi on laaja-kirjoilla vaikuttava antiepileptinen lääke (AED), jota käytetään vakiintuneesti osittain alkavien kohtausten apu- tai monolääkkeenä. TxGNN-mallin parhaaksi rankattu ennuste tälle kandidaatille on **Touretten oireyhtymä** (pistemäärä 99,85%), mutta tämä spesifinen ennuste on tällä hetkellä tuettu **nollalla kliinisellä tutkimuksella ja nollalla julkaisulla** — se on puhdas mallin tuotos ilman vahvistavaa näyttöä.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Epilepsia (osittain alkavat kohtaukset) — tunnetun AED-luokituksen perusteella; virallista Taiwan-lisenssi tekstiä ei saatavilla (lääke on markkinoimaton) |
| Ennustettu uusi käyttöaihe | Touretten oireyhtymä |
| TxGNN-ennusteen pistemäärä | 99,85% |
| Näytön taso | L5 (mallin ennuste vain) |
| Taiwanin markkinatilanne | Ei markkinoitu (Ei markkinoitu) |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on järkevä?

Yksityiskohtaisia toimintamekanismin tietoja ei ole saatavilla tässä näyttöpaketissa (`original_moa` on tietojen puutepaikka). Saatavilla olevien tietojen perusteella zonisamidi kuuluu antiepileptisen lääkkeen (AED) luokkaan, ja sen teho epilepsiassa on kliinisesti ja farmakologisesti hyvin vakiintunut (jännitteestä riippuvaisten natriumkanavien ja T-tyypin kalsiumkanavien modulaatio muun muassa, kuten tässä paketissa oleva AED-kirjallisuus viittaa).

Touretten oireyhtymän perusteluksi esitetään, että TxGNN:n korkea pistemäärä voi heijastaa zonisamidin hypoteesin mukaisia dopaminergisia ja serotoninergisia moduloivia vaikutuksia, koska Touretten oireyhtymä on teoreettisesti yhdistetty dopamiinikierron toimintahäiriöihin. Tämä on uskottava mekanistinen *hypoteesi*, ei näyttöön perustuva yhteys — tämän paketin mikään kliininen tutkimus tai julkaisu ei testaa zonisamidia erityisesti Touretten oireyhtymässä.

Kliinisten tutkimusten tai kirjallisuuden täydellisen puuttuessa (näytön taso L5) tämä ennuste tulisi käsitellä vain hypoteesin luomisen signaalina, ei kliinisen tai sääntelyluonteisen toiminnan perustana.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole merkityksellisiä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla merkityksellisiä julkaisuja.

## Taiwanin markkinatiedot

Zonisamidia ei ole tällä hetkellä markkinoitu Taiwanissa (0 valtuutusta arkistossa; `total_licenses` = 0, valtuutustietueita ei ole saatavilla).

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustiedot. (Tärkeimmät varoitukset, vasta-aiheet ja lääkkeen yhteisvaikutukset eivät ole saatavilla tässä näyttöpaketissa — TFDA pakkausselosteen haku on merkitty **estävä** tietojen puutteeksi, DG001.)

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Touretten oireyhtymän ennuste perustuu pelkästään TxGNN-pisteytykseen, jolle ei ole tukea kliinisissä tutkimuksissa, kirjallisuudessa tai vahvistetusta toimintamekanismista — riittämätön mistään arviointivaiheesta etenemisen perustelemiseksi (S0).

**Jatkaakseen seuraavaa tarvitaan:**
- TFDA/sääntelyasetuksen pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä (DG001)
- Vahvistettu toimintamekanismin tieto (DG001/DG002 korjaus DrugBank API:n kautta)
- Vähintään prekliininen tai tapauksen tasolla oleva näyttö, joka erityisesti yhdistää zonisamidin Touretten oireyhtymään ennen kuin edetään S0:n ohi

---

**Huomautus tästä näyttöpaketista:** Tämä kandidaattipaketti sisältää 10 TxGNN-ennustettua zonisamidin käyttöaihetta, joista useilla on aineellisesti vahvempi näyttö kuin parhaaksi rankattu Touretten oireyhtymän osuma — erityisesti **poissaoloepilepsian** (L1, päätösvaihe S3, "Etene varovaisuustoimiin", tuettu 583 potilaan täytetyllä vaiheen 3 satunnaistetulla kontrolloidulla tutkimuksella) ja **maaninen bipolaarinen affektiivinen häiriö** (L2, päätösvaihe S1, "Tutkimuskysymys", tuettu omalla satunnaistetulla kontrolloidulla tutkimuksella, PMID 22506436). Jos repurposing-raportti on toivottu jollekin näille korkeamman näytön omaavista kandidaateista sen sijaan, erillinen raportti tulisi tuottaa käyttäen `predicted_indications[6]` (bipolaarinen) tai `predicted_indications[7]` (poissaoloepilepsian) pääsisäntönä. Useat muut korkean pistemäärän saavat ennusteet (metahemoglobinemian variantit) ovat merkitty perusteluissa mekanistisesti *ristiriitaisiksi* — zonisamidin sulfonamidirakenne on tunnettu metahemoglobinemian riskitekijä, ei hoito — ja niitä tulisi käsitellä turvallisuussignaaleina, ei repurposing-mahdollisuuksina.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

