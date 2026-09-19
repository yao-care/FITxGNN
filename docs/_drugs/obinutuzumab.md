---
layout: default
title: Obinutuzumab
parent: Vahva näyttö (L1-L2)
nav_order: 268
evidence_level: L1
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **3** kpl
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

# Obinutuzumab: CD20+-B-solukasvaimista follikulaariseen lymfoomaan

## Yhden lauseen yhteenveto

Obinutuzumab on glykosuunniteltu anti-CD20-monoklonaalinen vasta-aine, jota käytetään jo CD20-positiivisia B-solu-verikasvaimia vastaan, mukaan lukien krooninen lymfosyyttinen leukemia (CLL). TxGNN-mallin huomionarvoinen pääennuste laajentaa tämän aktiivisuuden **follikulaariseen lymfoomaan (FL)**, läheisesti liittyvään B-solu-malignititeettiin, ja tätä suuntaa tukevat **50 kliinistä tutkimusta** (mukaan lukien keskeinen Phase 3 GALLIUM-tutkimus) ja **20 julkaisua**. Malli merkitsee erikseen kaksi erityisen spesifistä CLL/SLL-molekyylialaryhmää, joiden pisteet ovat lähes identtiset (~99,2 %), mutta joita ei tueta ollenkaan tämän aineiston kliinisillä tutkimuksilla tai kirjallisuudella – tämä on todennäköisesti ontologian rakeisuusartefakti eikä todella tuetumaton signaali.

## Pika-yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei saatavilla Suomelle (lääke ei ole markkinoilla siellä; `taiwan_regulatory.licenses` on tyhjä). Tämän todistepaketin tutkimusrekisterit kuvaavat obinutuzumaabia jo hyväksynnäksi muualla kombinaatiohoitoissa CLL:lle ja myöhemmin FL:lle. |
| Ennustettu uusi indikaatio | Follikulaarinen lymfooma |
| TxGNN-ennusteen pistemäärä | 99,18 % |
| Todisteen taso | L1 |
| Suomen markkinoiden tila | Ei markkinoilla |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Etene varauksellisesti |

**Huomautus muista ennusteista:** TxGNN sijoitti myös kaksi molekyylisesti määriteltävää CLL/SLL-alaryhmää ("pre-germinaali-keskus CLL/SLL" ja "CLL/SLL IGHV somaattisen hypermutaation kanssa") oleellisesti samalle pistemäärälle (~99,2 %), mutta näistä ei haettu yhtään kliinistä tutkimusta tai kirjallisuutta – todisteen taso L5, päätösvaihe S0, suositus Odota. Näitä käsitellään tässä matalan prioriteetin signaaleina, jotka eivät vaadi itsenäisiä toimia, kunnes paremmin ratkaistu sairauden terminologia mahdollistaa todisteen linkityksen.

## Miksi tämä ennuste on järkevä?

Muodolliset toimintamekanismin tiedot obinutuzumaamista merkitään tietoaukoksi (DG002, Korkea vakavuus) tässä todistepakitissa. Kuitenkin haetut tutkimukset ja perustelutiedot kuvaavat johdonmukaisesti obinutuzumaabia kolmannen sukupolven, glykosuunniteltuina tyypin II anti-CD20 IgG1-monoklonaalina vesta-aineena, joka tuottaa parantuneita vesta-aineesta riippuvaisen solukon-välittämää sytotoksisuutta (ADCC), komplementista riippuvaista sytotoksisuutta (CDC) ja suoraa B-solu-tappamista verrattaessa rituksimabiin.

Follikulaarinen lymfooma, kuten CLL/SLL, on CD20-positiivinen B-solu-maligniteetti, joten molekyylitavoite, johon obinutuzumabi sitoutuu, ilmenee suoraan molempien sairauksien syöpäsoluissa. Tämä ei ole kaukaa haettu uudelleenkäyttö eri elimistöjärjestelmien välillä – se kuvastaa lääkkeen olemassa olevan mekanistisen jalanjäljen laajentamista indolenteissa B-solu-lymfoproliferatiivisissa sairauksissa yhdestä CD20+-maligniteeteista toiseen.

Tämä mekanistinen uskottavuus vahvistetaan vahvasti todellisen maailman kehityksellä: obinutuzumabi (useampien tämän paketin tutkimusrekisterien kautta, esim. NCT02877550) kuvataan jo hyväksynnäksi yhdessä klorambusillin kanssa käsittelemättömälle CLL:lle ja yhdessä bendamustiinin kanssa FL:lle. TxGNN:n FL-ennuste on siis linjassa lääkkeen indikaatiotilan kanssa, jota se on jo laajasti tutkittu ja joissain markkinoissa hyväksytty – mikä selittää epätavallisen kypsän L1-todistepohjan verrattuna tyypilliseen de novo -uudelleenkäyttö-ehdokkaaseen.

## Kliinisen tutkimuksen todisteet

| Tutkimuksen numero | Vaihe | Tila | Rekrytointi | Tärkeimmät havainnot |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Vaihe 3 | Valmis | 1401 | GALLIUM-tutkimus: obinutuzumabi + kemoterapia vs. rituksimabi + kemoterapia käsittelemättömässä edistyneessä indolenteissa NHL:ssa, obinutuzumabi tai rituksimabi ylläpitohoidossa – keskeinen suora vertailu todisteet. |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Vaihe 3 | Valmis | 413 | Bendamustiini yksin vs. bendamustiini + obinutuzumabi (GA101) rituksimabi-resistentissä indolenteissa NHL:ssa, obinutuzumabi ylläpitohoito. |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Vaihe 2 | Valmis | 217 | ROSEWOOD: zanubrutinibi + obinutuzumabi vs. obinutuzumabi-monoterapia relapsed/refractory FL:ssa. |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Vaihe 4 | Valmis | 114 | Obinutuzumabin turvallisuus lyhytkestoisena (90 minuutin) infuusiona syklistä 2 eteenpäin yhdessä kemoterapian kanssa käsittelemättömässä edistyneessä FL:ssa. |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Vaihe 1/2 | Valmis | 133 | Obinutuzumabi + polatuzumabi vedotin + venetoklaksi relapsed/refractory FL:ssa. |
| [NCT02600897](https://clinicaltrials.gov/study/NCT02600897) | Vaihe 1/2 | Valmis | 114 | Obinutuzumabi + polatuzumabi vedotin + lenalidomidi relapsed/refractory FL:ssa. |
| [NCT03113422](https://clinicaltrials.gov/study/NCT03113422) | Vaihe 2 | Valmis | 56 | Venetoklaksi + obinutuzumabi + bendamustiini etuperävänä hoitona korkean kasvainpainon FL:ssa. |
| [NCT04034056](https://clinicaltrials.gov/study/NCT04034056) | N/A (havainnoiva) | Valmis | 299 | Ei-interventionaalinen, retrospektiivinen/prospektiivinen todellisen maailman tutkimus obinutuzumabin tehokkuudesta ja turvallisuudesta aiemmin käsittelemättömässä edistyneessä FL:ssa. |
| [NCT05783596](https://clinicaltrials.gov/study/NCT05783596) | Vaihe 2 | Aktiivinen, ei enää rekrytoida | 47 | Glofitamabi + obinutuzumabi FL:n ja marginaalivyöhykkeen lymfooman ensimmäisen linjan hoitoon. |
| [NCT05058404](https://clinicaltrials.gov/study/NCT05058404) | Vaihe 3 | Aktiivinen, ei enää rekrytoida | 605 | FIL_FOLL19: lyhennetty vs. standardi kemo-immunoterapia korkean kasvainpainon FL:n alkuhoitoon. |

## Kirjallisuustodisteet

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät havainnot |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | GALLIUM:n pääanalyysi: obinutuzumabi-pohjainen kemo-immunoterapia verrattuna rituksimabi-pohjaisen kemo-immunoterapiaan aiemmin käsittelemättömässä edistyneessä FL:ssa. |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM:n alaanalyysi osoittaa, että obinutuzumabi pidensi merkitsevästi progressiovapaata elinaikaa verrattuna rituksimabiin CHOP/CVP/bendamustiini-kemoterapian selkäosissa. |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: zanubrutinibi + obinutuzumabi vs. obinutuzumabi-monoterapia relapsed/refractory FL:ssa. |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT (lopullinen analyysi) | HemaSphere | GALLIUM:n lopulliset tulokset vahvistivat obinutuzumabi-pohjaisen vs. rituksimabi-pohjaisen immunokemoterapian kestävää PFS-hyötyä käsittelemättömässä FL:ssa. |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN: obinutuzumabi + lenalidomidi relapsed/refractory follikulaarisessa B-solu-lymfoomassa, yksivartaloinen Phase 2. |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Kohortti | Haematologica | Vaihe Ib/II GO29365: polatuzumabi vedotin + bendamustiini + rituksimabi tai obinutuzumabi relapsed/refractory FL:ssa. |
| [40355425](https://pubmed.ncbi.nlm.nih.gov/40355425/) | 2025 | Vaihe 2 tutkimus | Blood Cancer Journal | PrE0403: intermittentti-annostelu venetoklaksia lisätty bendamustiiniin + obinutuzumabiin etuperävänä hoitona korkean riskin FL:ssa. |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Katsaus | Blood and Lymphatic Cancer: Targets and Therapy | Katsaus obinutuzumabiin yksinään ja yhdessä FL:ssa, mekanismi ja kombinaatiovaikutukset. |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Katsaus | Turkish Journal of Haematology | Kattava katsaus FL:n stadiukseen, ennusteeseen ja nykyisiin/nouseviin hoitovaihtoehtohiin, mukaan lukien obinutuzumabi-pohjaisia säännöksiä. |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Katsaus | Targeted Oncology | Katsaus obinutuzumabiin rituksimabi-resistentissa/relapsed FL:ssa, mukaan lukien GADOLIN-tutkimustiedot. |

## Suomen markkinoiden tiedot

Obinutuzumabilla ei ole tällä hetkellä markkinointilupia Suomessa (`market_status`: ei markkinoilla; `total_licenses`: 0). Tuotteen, antomuodon tai hyväksytyn indikaation tiedot eivät ole saatavilla.

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuuden luokitus | Kohdennettu hoito — glykosuunniteltu anti-CD20-monoklonaalinen vesta-aine (ei perinteinen sytostaattinen kemoterapia) |
| Luuydintukahdutuksen riski | Tutustu pakkausselosteen varoituksiin ja huomautuksiin |
| Emetogenisuuden luokitus | Tutustu pakkausselosteen varoituksiin ja huomautuksiin |
| Seurantatarvikeet | Tutustu pakkausselosteen varoituksiin ja huomautuksiin |
| Käsittelysuoja | Tutustu pakkausselosteen varoituksiin ja huomautuksiin |

## Turvallisuusnäkökohdat

Tutustu pakkausselosteen turvallisuustietoihin. (Keskeisiä varoituksia, vasta-aiheita ja lääkkeiden vuorovaikutustietoja merkitään kaikki tietoaukoiksi tässä todistepakitissa – erityisesti DG001, Estävä vakavuustaso TFDA-ekvivalentin nimikkeen varoituksille/vasta-aiheille.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Etene varauksellisesti**

**Perustelut:**
Follikulaarisen lymfooman ennuste tuetaan L1-tason todistuksella – erityisesti valmiilla Phase 3 GALLIUM-tutkimuksella (n=1401) ja sen lopullisella julkaistulla analyysillä – ja se on mekanistisesti sopusoinnussa obinutuzumabin tunnetun anti-CD20-aktiivisuuden kanssa CD20+-B-solu-maligniteteissa. Kaksi Estävä/Korkea-vakavuus tietoaukkoa (TFDA-ekvivalentti turvallisuus-nimike ja muodollinen MOA-dokumentaatio) on kuitenkin suljettava, ennen kuin tämä voidaan siirtää alkuturvaksiarvioinnin jälkeen.

**Edetäkseen tarvitaan seuraavaa:**
- TFDA/Fimea pakkausseloste varoitukset ja vasta-aiheet (DG001, Estävä)
- Muodollisesti dokumentoitu toimintamekanismi (DG002, Korkea)
- Suomen/Taiwanin markkinointiluvan polun vahvistaminen, koska obinutuzumabilla on tällä hetkellä nolla lisenssejä tiedostossa
- Reitti-yhteensopivuuden ja annostelun arviointi (tällä hetkellä merkitty "odottavaksi" todistepakitissa)
- Kahden CLL/SLL-molekyylialyryhmän uudelleenhaku laajempien/ylemmän tason sairauden termien alla sen määrittämiseksi, onko nykyinen nolla-todiste todellinen aukko vai ontologian-vastaavuusartefakti

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

