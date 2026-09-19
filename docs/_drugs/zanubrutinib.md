---
layout: default
title: Zanubrutinib
parent: Kohtalainen näyttö (L3-L4)
nav_order: 409
evidence_level: L4
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **6** kpl
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

# Zanubrutinib: B-solujen pahanlaatuisista kasvaimista myelooisen leukemian tutkimukseen

## Yhden lauseen yhteenveto

Zanubrutinib on toisen sukupolven BTK (Bruton's tyrosine kinase) -inhibiittori, jonka tunnettu farmakologinen käyttö on **B-lymfosyytin** pahanlaatuisten kasvaimien (CLL/SLL, MCL, Waldenströmin makroglobulinemian) hoito. TxGNN-malli ennustaa sen olevan mahdollisesti tehokas **myelooisen leukemian (Myeloid Leukemia)** hoidossa, ennustuspistemäärä saavuttaa 99,65 %, mutta tällä hetkellä tukena on ainoastaan **2 kliinistä tutkimusta** (kumpikin ilman suoria zanubrutinib-todistusaineita) ja **epäsuora kirjallisuustieto**, mekanistinen yhteys on heikko, todistusten tasoksi L4.

---

## Pikakatsaus

| Erä | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | B-lymfosyytin pahanlaatuiset kasvaimet (CLL/SLL jne.; tämä Evidence Pack ei sisällä virallista hyväksyttyjen indikaatioiden luetteloa) |
| Ennustettu uusi indikaatio | Myeloosi leukemia (Myeloid Leukemia) |
| TxGNN-ennustuspistemäärä | 99,65 % (rank 4274) |
| Todistusten taso | L4 |
| Suomen markkinoiden tila | Markkinoimaton |
| Lupien määrä | 0 |
| Päätössuositus | Hold |

---

## Miksi tämä ennuste on huomion arvoinen (tai kyseenalainen)?

DrugBank ei tällä hetkellä tarjoa virallista rakenteista mekanismin kuvausta (MOA-kenttä on tiedon puutekohta). Tunnetun julkisen tiedon perusteella zanubrutinib on toisen sukupolven BTK-inhibiittori, jonka farmakologinen vaikutus perustuu B-solujen reseptorin (BCR) signaaliradan estoon, ja se on todistettu tehokkaiksi CLL/SLL-, MCL-, Waldenströmin makroglobulinemian sekä muiden B-lymfosyytin pahanlaatuisten kasvaimien hoidossa. Verrattuna ensimmäisen sukupolven ibrutinibiin sillä on parempi kinaasispesifisyys ja vähemmän pois-kohdistuneiden vaikutusten riski.

Myeloosi leukemia (AML) on **ydin**- eikä lymfosyytti-alkuperäinen kasvain. Sen patogeneettisesti keskeisiä mutaatioita (esim. FLT3-ITD, NPM1, IDH1/2) ja BTK-signalointia ei ole kuvattu selvästi samana tai päällekkäisenä. BTK:n rooli ydinsoluperäisissä soluissa on heikosti dokumentoitu ja rajoittuu makrofagien ja mastosolujend toissijaisiin signaalireitteihin, eikä se ole AML:n keskeinen patogeneettinen kinaasi. Tämän todistusten paketin kaksi kliinistä tutkimusta (NCT05665530, NCT04477291) käyttivät tutkimuslääkkeitä PRT2527 (CDK9-inhibiittori) ja CG-806 (monikinaasisen inhibiittori), **kumpikin ei ole zanubrutinib itse**, vaan ne kuuluvat vain "kinaasi-inhibiittorit verituumoreissa" -kategoriaan, ja molempien relevanssi-arvio on Grade C.

Näin ollen TxGNN:n korkea pistemäärä heijastaa todennäköisesti "kinaasi-inhibiittorit" -lääkkeen luokan ja AML-solmujen topologista läheisyyttä tietotaidokaaviossa, ei zanubrutinib-molekyylin omaa erityisyyttä. Tämä johtopäätös vastaa myös muita 5 alemmalla sijoituksella olevia ennusteita (harvinaiset perinnölliset syndroomat, neuroblastooma, Ewingin sarkooma) – nämä ennusteet ovat ilman kliinisiä tutkimuksia tai kirjallisuustodistetta ja ne on luokiteltu Hold-tasoksi, mikä osoittaa, että TxGNN:n kokonaistodistusten taso tälle lääkkeelle ydin- ja kiinteiden kasvaimien suunnalla on heikko.

---

## Kliinisten tutkimusten todistusaineisto

| Tutkimuksen numero | Vaihe | Tila | Potilasrekrytoinni | Pääkohdat |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Vaihe 1 | Valmis | 86 | PRT2527 (CDK9-inhibiittori) arvioitiin yksinään tai yhdessä zanubrutinib/venetoclaksin kanssa tekijänä tutkittaessa turvaa ja alustavaa tehoa uusiutuvissa/hoitoresistenteissa hematologisissa maligniteeteissa; **tutkimuslääke ei ole zanubrutinib itse**, vain yksi yhdisteltyjen käsittelyjen käsi, relevanssi-luokitus Grade C |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Vaihe 1a/1b | Keskeytetty | 45 | Suun kautta annettavaa CG-806:aa (luxeptinib, monikinaasinen inhibiittori) tutkittiin turvallisuuden ja syöpävastustavan aktiivisuuden osalta uusiutuvien/hoitoresistenttien AML- tai korkean riskin MDS-potilaiden hoitoon; **zanubrutinibilla ei ole käytetty**, tutkimus on keskeytetty, vain samankaltaisen mekanismin hypoteesin viittaus, relevanssi-luokitus Grade C |

> Molemmat tutkimukset eivät ole suoria zanubrutinib-hoidon todistusaineita myelooisen leukemian tapauksessa, vain mekanismin vertailun viitteiksi.

---

## Kirjallisuuden todistusaineisto

| PMID | Vuosi | Tyyppi | Lehti | Pääkohdat |
|------|------|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA-tutkimus (vaihe 3) 5 vuoden seurannan päivitys: zanubrutinib verrattuna BR-skeemaan alkuvaiheen CLL/SLL-hoidossa |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Kohortti | Blood Advances | BGB-3111-215-tutkimuksen päivitys: zanubrutinib on turvallinen ja tehokas ibrutinib/acalabrutinib-intoleranteissa CLL/SLL-potilaissa |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Kohortti | Lancet Haematol | Vaihe 2 -yksivartaloinen tutkimus: zanubrutinib aiemmin BTK-inhibiittoreille intoleranteissa B-lymfosyytin pahanlaatuisissa kasvaimissa |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Katsaus | Blood Advances | Useiden kliinisten tutkimusten välinen analyysi zanubrutinibista del(17p)/TP53-mutaatiolla varustettujen CLL/SLL-potilaiden hoitossa |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Katsaus | Pharmaceutics | Kroonisen leukemian (CML, CLL) tirosiinikinaasin estäjien aikakauden katsaus |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Katsaus | Leukemia | BTK-inhibiittorit Waldenströmin makroglobulinemian hoitojohtamisessa |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Katsaus | Clin Lymphoma Myeloma Leuk | BTK-inhibiittorit (sisältäen zanubrutinib) -potilaiden B-hepatiitin reaktivaatioriskiä koskevia tutkimuksia |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Katsaus | Anticancer Agents Med Chem | FDA:n hyväksymät syöpälääkkeet -synteesimenetelmän katsaus, joka mainitsee vain zanubrutinibiin kemiallisen synteesin |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Tapausraportti | Front Immunol | Waldenströmin makroglobulinemian harvinainen tapaus B-ALL:n kanssa (KMT2D/MECOM-mutaatio) |

> Kaikki edellä mainitut kirjallisuuslähteet keskittyvät zanubrutinibiin **B-lymfosyytin** pahanlaatuisissa kasvaimissa (CLL/SLL, WM) teholla ja turvallisuudella, **mikään lähde ei käsittele myeloosista leukemiaa (AML)**, vain lääkkeen taustan ja turvallisuuden viitteiksi.

---

## Suomen markkinoiden tiedot

Zanubrutinib ei ole tällä hetkellä saanut markkinointilupaa Suomessa (Markkinoimaton, lupien määrä 0), hyväksyttyjä lääkekohteita ei voida luetella.

---

## Sytotoksisuuden tiedot (kohdistetun hoidon lääkkeiden viite)

Zanubrutinib kuuluu B-lymfosyytin pahanlaatuisten kasvaimien hoitolääkkeisiin ja on tunnetun farmakologisen luokittelun perusteella kohdistetun hoidon lääke, joten seuraavat viitetiedot luetelaan:

| Erä | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdistettu hoito (BTK-inhibiittori), ei perinteinen sytotoksinen kemoterapialääke |
| Luuytimen tukahduttamisen riski | Katso valmisteen yhteenveto ja varoitukset |
| Pahoinvointiluokitus | Katso valmisteen yhteenveto ja varoitukset |
| Seurantakohteet | Katso valmisteen yhteenvedon ehdottamat seurantakohteet |
| Käsittelysuojaus | Katso valmisteen yhteenveto ja varoitukset |

---

## Turvallisuusnäkökohtia

Katso valmisteen yhteenvetoa turvallisuustiedoista.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Hold**

**Perustelut:**
Vaikka TxGNN:n ennustuspistemäärä on korkea (99,65 %), kaikki tukevat todistusaineistot eivät ole suoria zanubrutinib-hoidon todistusaineita myelooisen leukemian kohdalla – molemmat kliiniset tutkimukset käyttivät tutkimuslääkkeitä, jotka eivät ole zanubrutinib, ja kirjallisuustodisteet keskittyvät kokonaan B-lymfosyytin pahanlaatuisiin kasvaimiin, ei ydin-kasvaimiin; mekanismin osalta BTK ei ole AML:n keskeinen patogeneettinen kinaasi. Samalla Suomen markkinoilla lääkettä ei ole markkinoitu ja virallisia turvallisuustietoja ei ole saatavilla, eikä nykyinen aineisto riitä seuraavan arviointivaiheeseen.

**Jos työtä jatketaan, tarvitaan seuraavat lisätiedot:**
- Zanubrutinibbin virallinen toimintamekanismi (MOA) strukturoituina DrugBank-tiedoina
- TFDA/Fimea:n virallisen valmisteen yhteenvedon varoitukset ja vasta-indikaatiot
- Zanubrutinibille suorat prekliiniset tai kliiniset todistusaineistot ydin-kasvaimissa (AML/MDS)
- Lääkkeiden keskinäisvaikutukset (DDI) täydellisina tietoina

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

