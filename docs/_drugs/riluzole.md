---
layout: default
title: Riluzole
parent: Vahva näyttö (L1-L2)
nav_order: 324
evidence_level: L1
indication_count: 10
---

# Riluzole
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **10** kpl
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

Raportti on luotu Evidence Pack -paketin perusteella. **Tietojen valintalogiikan selitys**: `predicted_indications` -taulukon ensimmäinen merkintä (polymikrogyria, L5/Hold) vastaavat täysin ilman näyttötutkimuksellista tukea eikä siihen liity järkevää yhteyttä rilutsoliin toimintamekanismiin; sitä vastoin rank 8 "ALS, susceptibility to" on ainoa kaikista 10 ennusteesta, jolla on 20 julkaisun tuki, evidence_level saavuttaa L1:n ja decision_stage saavuttaa S3:n, ja repurposing_rationale ilmoittaa selvästi "tulee käyttää todellisen maailman tunnettua hyväksynnän statusta". Siksi tämä raportti käyttää rank 8:aa pääasiallisena ennustetuotena indikaationa mekaanisen taulukko-indeksin 0 sijaan.

---

# Rilutsooli: amyotrofisesta lateraaaliskleroosista (ALS) ALS-geneettisen alttius-alaryhmään

## Yhden lauseen yhteenveto

Rilutsooli on glutamaatin vapautumisen estäjä ja natrium-kanavablokkeri, jonka todellinen hyväksytty käyttö on klassinen amyotrofinen lateraaliskleroosi (ALS), jossa se pidentää eloonjäämistä vaatimattomasti. TxGNN-malli ennustaa lisäksi hyötyä **ALS:n alttiudessa** — geneettisesti määritellylle ALS-alaryhmälle — tällä hetkellä **0 kliinisen tutkimuksen** ja **20 julkaisun** tuella, jotka tukevat taustalla olevaa taudin biologiaa ja rilutsoliin mekanismia, vaikka yksikään ei ole alaryhmäkohtainen.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Amyotrofinen lateraaliskleroosi (todellinen hyväksytty käyttö vuodesta 1995 lähtien; ei tallennettu tämän tietojoukon sääntelytietoihin — tietoaukko) |
| Ennustettu uusi indikaatio | Amyotrofinen lateraaliskleroosi, alttius |
| TxGNN-ennustepistemäärä | 99.98% |
| Näyttötaso | L1 |
| Suomen markkinatilanne | ✗ Ei markkinoilla (Ei markkinoilla) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Etene varoituskokeineen |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla tässä tietojoukossa (original_moa on tietoaukko). Tunnettujen tietojen perusteella rilutsooli estää presynaptisen glutamaatin vapautumisen ja estää jännitteestä riippuvia natriumkanavia, mikä vähentää eksitotoksisia vaurioita motoneuroneissa — tämä on sama peruspatologinen prosessi (glutamaatin eksitotoksisuus), joka liittyy ALS-motoreuronien rapautumiseen.

"ALS:n alttius" viittaa geneettisesti määriteltyyn saman sairauden alaryhmään kuin klassinen ALS, joka eroaa pääasiassa aiheuttavassa geenissä, mutta ydinpatofysiologia on sama. Rilutsoliin hyväksytty indikaatio ei tällä hetkellä ole jaettu geneettisiin alaryhmiin, ja kliinisessä käytännössä potilaita, joilla on geneettisesti linkittynyt ALS, käsitellään yleensä samalla standardi rilutsooli-regiimillä kuin sporadisen ALS:n potilaita.

Tämän todistepaketin tukeva kirjallisuus on sairauden mekanismia koskeva kirjallisuus (glutamaatin eksitotoksisuus, motoreuronien rapautuminen, rilutsoliin vakiintunut mutta vaatimaton selviytymisetu) pikemminkin kuin alaryhmäkohtaiset kliiniset tutkimukset, joten mekaaninen ekstrapolaatio klassisesta ALS:sta tähän geneettiseen alaryhmään on järkevää mutta epäsuoraa.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä yhtään asiaan liittyvää kliinistä tutkimusta ei ole rekisteröity

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|------|--------|------|---------|
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Katsaus | CNS Drugs | Vahvistaa, että rilutsooli on ainoa lääkitys, jolla on osoittautunut pidentävän ALS-potilaan selviytymistä vaatimattomasti; käsittelee patofysiologiaa ja hoitoa |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Katsaus | Current Opinion in Neurology | Huomauttaa, että rilutsooli pysyy ainoana lääkkeenä, jolla on todistettu teho ALS:ssa, vaikka muista hoitomuodoista tehdään intensiivistä tutkimusta |
| [22646982](https://pubmed.ncbi.nlm.nih.gov/22646982/) | 2011 | Katsaus (prekliininen lääkkeiden kehittäminen) | Expert Opinion on Drug Discovery | Rilutsooli on ainoa hyväksytty ALS-lääke, joka pidentää selviytymistä 2-3 kuukaudella; korostaa tyydyttämättömän tarpeen uusille lääkkeille |
| [20942785](https://pubmed.ncbi.nlm.nih.gov/20942785/) | 2010 | Katsaus | CNS & Neurological Disorders Drug Targets | Rilutsooli on ainoa saatavilla oleva ALS-lääke; käsittelee geneettisiä tekijöitä (esim. SOD1) tulevien terapeuttisten kohteiden näkökulmasta |
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Katsaus (mekanismi) | Journal of Neurology | Perustavanlaatuinen katsaus ALS:n motoreuroneihin kohdistuvaa vaaraa aiheuttavasta "glutamaatista hypoteesista" |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | odottava | Neuroreport | Osoittaa, että rilutsooli käyttäytyi neuroprotektiivisesti ALS-potilaiden eksitotoksisia CSF-tekijöitä vastaan hermosoluviljelyssä |
| [31108504](https://pubmed.ncbi.nlm.nih.gov/31108504/) | 2019 | odottava | Human Molecular Genetics | iPSC-johdannaiset motoneuronit ALS-potilaista (C9orf72, FUS, SOD1, TDP43 mutaatiot) osoittavat muutuneita kalsium-/glutamaattireceptori-dynamiikkaa; rilutsoliin mekanismi on glutamaatterginen estäminen ja kalsiumin sääntely |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Katsaus | Expert Reviews in Molecular Medicine | Käsittelee ehdotettuja ALS-mekanismeja (hapettava stressi, eksitotoksisuus, mitokondrion toimintahäiriöt, proteiinin aggregaatio) ja hoitoväyliä |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Katsaus | CNS & Neurological Disorders Drug Targets | Käsittelee ALS-diagnoosia, patogeneesia ja terapeuttisia kohteita motoreuronijärjestelmässä |
| [20698807](https://pubmed.ncbi.nlm.nih.gov/20698807/) | 2011 | odottava | Amyotrophic Lateral Sclerosis | Kriittinen arvio ALS-terapeuttisista tutkimuksista; huomauttaa, että rilutsooli (glutamaatin aineenvaihdunnan modulaattori) on ainoa lääke, joka parantaa selviytymistä, vaikkakin vaatimattomasti |

## Turvallisuusnäkökohdat

Turvallisustiedot löytyvät pakkausselosteesta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Etene varoituskokeineen**

**Perustelut:**
Rilutsoliin tunnetun anti-eksitotoksisen vaikutuksen ja ALS-spektrin patologian välinen mekaaninen yhteys on hyvin vakiintunut yleisessä ALS-kirjallisuudessa, ja tämä erityinen geneettisen alttiuden subtyyppi jakaa saman ydinpatofysiologian klassisen ALS:n kanssa, jolle rilutsooli on jo todellisen maailman hoitostandardi. Subtyyppikohtaista tutkimusta, DDI/turvallisuustietoja ei kuitenkaan ole saatavilla tässä tietojoukossa, ja TFDA-pakkausselosteen tarkistus on merkitty **blokaavaksi** tietoaukoksi, joka on ratkaistava ennen S1-turvallisuusarviointia.

**Jatkaaksemme tarvitaan seuraavaa:**
- TFDA-pakkausseloste (varoitukset/vasta-indikaatiot) — tällä hetkellä blokaava (DG001)
- Vahvistettu toimintamekanismi (MOA) DrugBank API:n kautta — tällä hetkellä tietoaukko (DG002)
- Alaryhmäkohtainen kliininen näyttö "ALS, susceptibility to" -osoituksesta (tällä hetkellä yhtään ei ole rekisteröity)
- Rilutsoliin todellisen maailman hyväksytyn indikaation/lisensointitilan vahvistus, koska se puuttuu tämän tietojoukon Taiwanin/Suomen sääntely-tietueista huolimatta siitä, että se on vakiintunut ALS-hoito

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

