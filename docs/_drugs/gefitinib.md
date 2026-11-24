---
layout: default
title: Gefitinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 200
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
description: "Gefitinib: ennustettu uusi käyttöaihe Ientenfibromatoosi (fibromatosis, gingival) (näytön taso L5). Alkuperäinen käyttöaihe: Carcinoma, Non-Small-Cell Lung"
---

# Gefitinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **9** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

## Gefitinib: Ientenfibromatoosi (fibromatosis, gingival)
{: .text-alpha }

## Yhden lauseen tiivistelmä

Gefitinibi on EGFR-tyrosiinikinaasin estäjä, jota on alun perin käytetty ei-pienisoluisen keuhkosyövän hoitoon.
TxGNN-malli ennustaa sen voivan tehota **ientenfibromatoosiin** (fibromatosis, gingival), mutta tälle ennusteelle ei löydy **yhtään kliinistä tutkimusta eikä yhtään julkaisua**.
Ennuste perustuu siis pelkästään mallin laskemaan pisteytykseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Carcinoma, Non-Small-Cell Lung |
| Ennustettu uusi käyttöaihe | Ientenfibromatoosi (fibromatosis, gingival) |
| TxGNN-ennustepisteet | 0.9989 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Gefitinib (epävirallinen käännös): ”Epidermaalisen kasvutekijän reseptoria (EGFR) ilmentyy sekä normaalien solujen että syöpäsolujen pinnalla, ja sillä on rooli solujen kasvun ja proliferaation prosesseissa. Joidenkin EGFR:ää aktivoivien mutaatioiden (eksonin 19 deleetio tai eksonin 21 pistemutaatio L858R) NSCLC-soluissa on todettu edistävän kasvainsolujen kasvua, estävän apoptoosia, lisäävän angiogeenisten tekijöiden tuotantoa ja helpottavan etäpesäkkeiden muodostumisen prosesseja. […] Gefitinibi estää palautuvasti villityypin EGFR:n ja tiettyjen EGFR:ää aktivoivien mutaatioiden kinaasiaktiivisuutta ja estää reseptoriin liittyvien tyrosiinitähteiden autofosforylaation, mikä estää signaalinvälityksen alavirtaan ja salpaa EGFR-riippuvaisen proliferaation.” Englanninkielinen alkuteksti: "The epidermal growth factor receptor (EGFR) is expressed on the cell surface of both normal and cancer cells and plays a role in the processes of cell growth and proliferation. Some EGFR activating mutations (exon 19 deletion or exon 21 point mutation L858R) within NSCLC cells have been identified as contributing to the promotion of tumor cell growth, blocking of apoptosis, increasing the production of angiogenic factors and facilitating the processes of metastasis. […] Gefitinib reversibly inhibits the kinase activity of wild-type and certain activating mutations of EGFR, preventing autophosphorylation of tyrosine residues associated with the receptor, thereby inhibiting further downstream signaling and blocking EGFR-dependent proliferation." ([DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41), versio 2023-02-28; haettu 2026-11-20). Tunnetun tiedon perusteella gefitinibi on valikoiva EGFR-tyrosiinikinaasin estäjä, jonka teho EGFR-mutaatiopositiivisessa ei-pienisoluisessa keuhkosyövässä on osoitettu. Mekanistisesti se voisi olla sovellettavissa myös ientenfibromatoosiin.

Mahdollinen yhteys olisi EGFR-välitteinen fibroblastien lisääntyminen. Tätä oletusta ei kuitenkaan tue mikään tässä käytettävissä oleva aineisto. Ennustepisteet voivat heijastaa myös verkostoetäisyyttä tietämyskuvaajassa eikä tautikohtaista mekanismia.

---

## Kliininen tutkimusnäyttö

Ennustetulle käyttöaiheelle ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ennustetulle käyttöaiheelle ei ole tällä hetkellä saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Muut ennustetut käyttöaiheet

Ensisijaisen ennusteen lisäksi aineistossa on yhdeksän muuta ennustetta. Yksikään niistä ei ylitä tasoa L4, ja kaikkien suositus on Hold.

| Sija | Ennustettu käyttöaihe | Pisteet | Näytön taso | Huomio |
|------|------|------|------|------|
| 2 | Keuhkon fibrooma | 0.9986 | L5 | Ei tutkimuksia eikä kirjallisuutta; hyvänlaatuisten kuitukasvainten ei tiedetä olevan EGFR-riippuvaisia |
| 3 | Inkluusiokappalemyopatia, varhain alkava Paget-tauti ja/tai otsa-ohimolohkodementia | 0.9986 | L5 | Ei tutkimuksia; tauti johtuu VCP-mutaatioista, eikä yhteyttä EGFR-estoon ole osoitettu |
| 4 | Keuhkon hamartooma | 0.9986 | L5 | Ei tutkimuksia; pisteet heijastavat todennäköisesti läheisyyttä keuhkokasvaindiagnooseihin |
| 5 | Keuhkoporttisyöpä | 0.9986 | L5 | Vain yksi tapausraportti poikkeuksellisen hyvästä hoitovasteesta; ei erillinen käyttöaihe, vaan keuhkosyövän esiintymismuoto |
| 6 | Keuhkon hyvänlaatuinen kasvain | 0.9985 | L4 | Kirjallisuus koskee pääosin ei-pienisoluista keuhkosyöpää, ei hyvänlaatuisia kasvaimia |
| 7 | Leukomelanoderma-infantilismi-kehitysvammaisuus-hypodontia-hypotrikoosi-oireyhtymä | 0.9984 | L5 | Haetut julkaisut eivät koske tätä oireyhtymää |
| 8 | Keuhkon alkiosolukasvain | 0.9984 | L5 | Ainoa tutkimus (NCT00068497) koskee pään ja kaulan syöpää ja ei-pienisoluista keuhkosyöpää, joten se ei ole relevantti |
| 9 | Keuhkon yläsulkuksen kasvain | 0.9984 | L5 | Kasvaimet ovat tyypillisesti ei-pienisoluisia keuhkosyöpiä, mutta kaksi löytynyttä julkaisua ei koske gefitinibiä tässä kasvaintyypissä |
| 10 | Junktionaalinen epidermolysis bullosa | 0.9984 | L5 | Ei tutkimuksia; EGFR-esto aiheuttaa ihotoksisuutta, mikä puhuu hyödyn puolesta heikosti |

---

## Suomen markkinatiedot

<!-- licenses:begin -->

| Myyntiluvan numero | Valmisteen nimi (EMA) | Vaikuttavat aineet (EMA, englanniksi) | Terapeuttinen alue (EMA, englanniksi) | Tila |
|------|------|------|------|------|
| EMEA/H/C/001016 | Iressa | gefitinib | Carcinoma, Non-Small-Cell Lung | Voimassa |

Lähde: EMA – Medicines output (keskitetysti myyntiluvan saaneet ihmisille tarkoitetut lääkkeet); valmisteen nimi, vaikuttavat aineet ja terapeuttinen alue alkuperäisinä englanninkielisinä. Kansalliset myyntiluvat (Fimea) ja eläinlääkkeet eivät sisälly näihin tietoihin.

<!-- licenses:end -->

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (EGFR-tyrosiinikinaasin estäjä) |
| Luuydinlamaus | Tarkempia tietoja ei ole saatavilla; katso valmisteyhteenvedon varoitukset ja varotoimet |
| Pahoinvointia aiheuttavuus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurantakohteet | Maksan toiminta (maksasairaus on tietämyskuvaajassa vasta-aiheena), keuhko-oireet ja EKG:n QT-aika (kirjallisuudessa kuvattu QT-ajan piteneminen) |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja varotoimet |

---

## Turvallisuusnäkökohdat

- **Tietämyskuvaajan mukaiset vasta-aiheet** (TxGNN/PrimeKG, ei valmisteyhteenvetoteksti): maksasairaus, sappirakon sairaus, interstitiaalinen keuhkosairaus, keuhkofibroosi ja tulehduksen jälkeinen keuhkofibroosi.
- **Kirjallisuudessa kuvatut turvallisuushuomiot**: gefitinibin aiheuttama akuutti keuhkokuume (tapausraportti, potilas menehtyi hengitysvajaukseen), ihotoksisuus (aknetyyppinen ihottuma, kynsivallintulehdus), QT-ajan piteneminen (prekliininen tutkimus) ja yksittäinen tapausraportti toistuvasta sydäninfarktista.
- **Lääkeyhteisvaikutukset**: tietokannasta löytyi yhteensä 100 yhteisvaikutusta. Merkittävimmät kohtalaiset yhteisvaikutukset:
  - Happoa vähentävät lääkkeet: famotidiini, ranitidiini, simetidiini, nitsatidiini sekä protonipumpun estäjät (omepratsoli, esomepratsoli, pantopratsoli, lansopratsoli, dekslansopratsoli, rabepratsoli)
  - Klaritromysiini
  - Atsoliantimykootit: mikonatsoli, klotrimatsoli
  - Deksametasoni
  - Aprepitantti
  - Naltreksoni
  - Troglitatsoni
- Lisäksi kaksi yhteisvaikutusta (kalsitrioli, glimepiridi) on luokiteltu tasolle "tuntematon".

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla, joten niiden osalta on tutustuttava valmisteyhteenvetoon.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ensisijaiselle ennusteelle (ientenfibromatoosi) ei löydy kliinisiä tutkimuksia eikä kirjallisuutta, joten näytön taso on L5 eli pelkkä mallin ennuste. Myöskään muiden ennustettujen käyttöaiheiden näyttö ei riitä jatkoon: osa on vain ei-pienisoluisen keuhkosyövän muunnelmia tai julkaisut ovat kohteen kannalta epärelevantteja.

<!-- review:begin fi-lic-20261106-gefitinib-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Myöskään muiden ennustettujen käyttöaiheiden näyttö ei riitä jatkoon: osa on vain ei-pienisoluisen keuhkosyövän muunnelmia tai julkaisut ovat kohteen kannalta epärelevantteja. / Gefitinibin ainoa Suomessa rekisteröity myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-gefitinib-1 -->

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (tällä hetkellä estävä tietoaukko turvallisuusarvioinnin kannalta)
- Yksityiskohtaiset vaikutusmekanismitiedot
- Prekliiniset tai mekanistiset tutkimukset, jotka osoittavat EGFR:n roolin ientenfibromatoosissa
- Arvio siitä, miten tietämyskuvaajan vasta-aiheet (maksasairaus, interstitiaalinen keuhkosairaus, keuhkofibroosi) vaikuttavat kohdepotilasryhmään
- Selvitys reitti- ja lääkemuotosoveltuvuudesta (esim. paikallinen annostelu ientenfibromatoosissa)

<!-- review:begin fi-lic-20261106-gefitinib-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Selvitys reitti- ja lääkemuotosoveltuvuudesta (esim. paikallinen annostelu ientenfibromatoosissa) / Selvitys myyntiluvan peruuttamisen syistä ja nykyisestä saatavuudesta Suomessa” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Ajantasaiset myyntilupien määrät ja tilat ovat pikakatsauksessa ja markkinatietojen taulukossa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-gefitinib-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Gefitinibin ainoa Suomessa rekisteröity myyntilupa on peruutettu” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Selvitys myyntiluvan peruuttamisen syistä ja nykyisestä saatavuudesta Suomessa” | Korjattu (päivitetty 2026-11-24; aiempi versio tallessa lokissa) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Iressa (EMEA/H/C/001016) on voimassa, ei peruutettu | Korvattu ohjelmallisesti tuotetulla myyntilupataulukolla (aiemmin: Korjattu) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-20 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Iressa (gefitinib) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=827d60e8-7e07-41b7-c28b-49ef1c4a5a41) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

