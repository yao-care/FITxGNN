---
layout: default
title: Emicizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: Hemofiliasta A pseudo-von Willebrandin tautiin

## Yhden lauseen yhteenveto

Emicizumab on biokaksinkertainen monoklonaalinen vasta-aine, jonka vakiintunut kliininen käyttö (tämän evidenssipaketin kirjallisuuden perusteella) on verenvuotojen profylaksia synnynnäisessä ja hankitussa hemofiliassa A. TxGNN-mallin parhaiten sijoittava ennuste on **pseudo-von Willebrandin tauti**, mutta tätä ehdokasta tukee **0 kliinistä tutkimusta** ja **0 julkaisua**, ja evidenssipaketin oma mekanistinen katsaus toteaa, että **mekanistista yhteyttä emicizumabiin ja tähän tautiin ei ole**. Viralliset Suomen/TFDA:n sääntelytiedot (alkuperäinen käyttöaihe, pakkausselosteen varoitukset, vaikutusmekanismi) eivät ole tällä hetkellä saatavissa ja ne on merkitty tietovajeiksi.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihe | Ei saatavissa sääntelytiedoissa (tietovaje). Tämän paketin kirjallisuuskonteksti osoittaa synnynnäistä/hankittua hemofiliaa A (FVIII-mimeettinen profylaksia) |
| Ennustettu uusi käyttöaihe | Pseudo-von Willebrandin tauti |
| TxGNN-ennustepisteet | 99.99% |
| Näyttötaso | L5 |
| Suomen markkina-asema | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin (MOA) tietoja ei ole saatavissa DrugBankista tässä evidenssipakettissa (tietovaje DG002, vakavuus: Korkea). Tämän evidenssipaketin muista kohdista löydetyn tiedon perusteella (kirjallisuuden abstraktit kerätty "hankittu koagulaatiotekijän puutos" -ehdokkaan alle) emicizumab on biokaksinkertainen vasta-aine, joka jäljittelee aktivoidun koagulaatiotekijä VIII:n yhteistekijän toimintoa silloittamalla tekijät IXa ja X, palauttaen trombiitin tuotantoa. Sitä käytetään kliinisesti verenvuotojen profylaksiin sekä synnynnäisessä hemofiliassa A (FVIII-estäjien kanssa tai ilman) että yhä enemmän hankitussa hemofiliassa A.

TxGNN:n parhaiten sijoitettu ehdokas, pseudo-von Willebrandin tauti, on trombosyyttien kalvon glykoproteiini Ib:n (GPIbα) toiminnon vahvistuma-häiriö, joka aiheuttaa epänormaalin spontaanin sitoutumisen trombosyyttien ja von Willebrand-tekijän välillä. Tämä on **trombosyytin reseptoridefekti**, ei koagulaatiotekijän kaskadi -defekti – mekanistisesti eroaa emicizumabiin liittyvästä FIXa–FX-silloituksesta. Evidenssipaketin oma repurposing-perustelu tälle ehdokkaalle päättelee eksplisiittisesti, että "mekanistinen uskottavuus ei ole tuettu" (無機轉合理性支持) tälle yhdistelmälle.

Tämä on tärkeä varoitus tulkittaessa 99.99%:n TxGNN-pistemäärää: vaikka se on yksittäin korkeimmin sijoitettu ennuste näiden kymmenen ehdokkaan joukossa tässä paketissa, se kantaa heikoimman mahdollisen näyttötason (L5 – vain mallin ennuste, ei tutkimuksia, ei kirjallisuutta) ja mekanistisen perustelun, joka väittää *vastaan* biologista uskottavuutta. Mallin korkea samankaltaisuuspisteet tulisi lukea verkkotopologian signaaliksi, ei mekanistisen sopivuuden näytöksi – nämä kaksi on arvioitava erikseen, kuten tässä paketissa tehdään.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavissa asiaan liittyvää kirjallisuutta

---

## Muut tämän evidenssipaketin ehdokkaat (täydentävät)

Koska parhaiten sijoitetulla ehdokkaalla on pohjimmiltaan nolla suoraa näyttöä, on arvokasta huomata, että kaksi alemmin sijoitettua ehdokasta samassa evidenssipakettissa kantaa merkittävästi vahvempaa tukea ja voivat olla parempia seuranta-arviointikohteita:

| Sijoitus | Tauti | TxGNN-pisteet | Näyttötaso | Tukeva näyttö |
|------|---------|-------------|-----------------|----------------------|
| 3 | Glanzmannin trombastenia | 99.98% | L4 | 1 rekisteri-tyyppinen tutkimus ([NCT04398628](https://clinicaltrials.gov/study/NCT04398628), ei-interventionaalinen, relevanssusaste C) + 1 katsausartikkeli (PMID [37391649](https://pubmed.ncbi.nlm.nih.gov/37391649/), keskittyy rFVIIa:han, ei emicizumab-spesifinen). Mekanistinen yhteys on epäsuora – Glanzmannin trombastenia on GPIIb/IIIa-trombosyytin aggregaatiodefekti, ei FVIII/IX/X-polku-defekti. |
| 5 | Hankittu koagulaatiotekijän puutos | 99.90% | Ei vielä lopullista tässä paketissa ("odottava"), mutta tiedot viittaavat siihen, että sen pitäisi sijoittua hyvin L4:n yläpuolelle | 1 rekisteri-tutkimus + **20 PubMed-julkaisua**, mukaan lukien valmis vaiheen 3 tutkimus (AGEHA, PMID [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/)) ja julkaistu vaiheen 2 tutkimus, joka testasi suoraan emicizumab-hoitoa hankitussa hemofiliassa A (GTH-AHA-EMI, *Lancet Haematology*, PMID [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/)). Mekanismi vastaa suoraan emicizumabiin tunnetun FVIII-mimeettisen toiminnan kanssa. |

**Riskiliput, jotka on tunnistettu muualla tässä paketissa ja joita ei pitäisi jatkaa eteenpäin:**
- **Sijoitus 8 – Trombotinen trombosytopenia**: mekanistisesti kontraindiseroitu. TTP on pro-trombotinen, ADAMTS13-puutoshäiriö; pro-koagulantsin (emicizumab) antaminen on suuntaa vastaan hoitotavoitteelle ja aiheuttaa turvallisuushuolen, ei vain näyttövajeelle.
- **Sijoitus 10 – "tulva tekijän puutos"**: evidenssipaketti itse merkitsee tämän todennäköiseksi OCR/tiedonmäärityshäväksi ilman ratkaistavaa taudin ontologia -vastaavuutta; se pitäisi korjata lähteessä ennen jatkoarvioita.

---

## Suomen markkina-tiedot

Emicizumab ei ole tällä hetkellä markkinoilla Suomessa – `taiwan_regulatory.market_status` ilmoittaa "Not Marketed" (ei markkinoilla) 0 rekisteröidyllä markkinointiluvan myönnöllä. Yhteenvetoon saatavilla olevia lisenssitietueita ei ole.

---

## Turvallisuuteen liittyvät näkökohdat

Tutustu pakkausselosteeseen turvallisuustietojen osalta.

*(Tärkeät varoitukset, vasta-aiheet ja lääkkeiden vuorovaikutustiedot kaikki merkitään tietovajeiksi tässä evidenssipakettissa – mukaan lukien estävän vakavuuden vaje TFDA:n pakkausselosteen varoituksille/vasta-aiheille, DG001 – joten S1 turvallisuuden esiseulonta ei voi olla valmis tällä hetkellä.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
TxGNN:n parhaiten sijoitetulla ennusteella (pseudo-von Willebrandin tauti) on L5-näyttö – ei kliinisiä tutkimuksia, ei kirjallisuutta – ja sen oman mekanistisen perustelun mukaan biologinen uskottavuus on selvästi suljettu pois. Yhdessä estävän vakavuuden tietovajeen kanssa TFDA:n pakkausselosteen turvallisuustiedoissa ja vasta-aiheissa (DG001), tätä ehdokasta ei voi edistyä S0/S1:n pidemmälle nykysessä muodossaan.

**Jatkamiseksi seuraavat ovat tarpeen:**
- TFDA/EU-pakkausselosteen varoitukset ja vasta-aiheet (DG001, estävä) – vaaditaan ennen mitään S1 turvallisuuden esiseulontaa
- Vahvistettu vaikutusmekanismin tieto DrugBankista (DG002, korkea)
- Vahvistettu alkuperäinen käyttöaihe ja Suomen lisensointihistoria (tällä hetkellä puuttuu `taiwan_regulatory`-lähteestä)
- Jos jatketaan tämän evidenssipaketin evaluointia, **ohjaa arvioinnin prioriteetti rank 5:lle (hankittu koagulaatiotekijän puutos)**, jolla on jo valmis vaiheen 3 tutkimus (AGEHA) ja julkaistu vaiheen 2 RCT (GTH-AHA-EMI), joka tukee suoraan emicizumab-hoitoa – tämä ehdokas todennäköisesti ansaitsee L1/L2 näyttötason uudelleen arvioinnin pikemminkin kuin "odottava" -status, joka on tällä hetkellä näytetty
- Korjaa taudin ontologia -määritys rank 10:lle ("tulva tekijän puutos") ennen jatkokäyttöä
- Sulkea pois rank 8 (TTP) repurposing-harkinnasta mekanistisista/turvallisuusperusteista

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

