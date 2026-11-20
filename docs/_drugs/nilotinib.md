---
layout: default
title: Nilotinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 303
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
description: "Nilotinib: ennustettu uusi käyttöaihe Dermatofibrosarcoma protuberans (näytön taso L5). Alkuperäinen käyttöaihe: Leukemia, Myelogenous, Chronic, BCR-ABL Positive"
---

# Nilotinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

## Nilotinib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## Yhden lauseen yhteenveto

Nilotinibi on tyrosiinikinaasin estäjä, jota on alun perin käytetty BCR-ABL-positiivisen kroonisen myelooisen leukemian hoitoon.
TxGNN-malli ennustaa sen voivan tehota **dermatofibrosarcoma protuberans -kasvaimeen (DFSP)**.
Tukena on tällä hetkellä **0 kliinistä tutkimusta** ja **1 julkaisu** (katsaus), joten näyttö on toistaiseksi vähäistä.

---

## Pikakatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Leukemia, Myelogenous, Chronic, BCR-ABL Positive |
| Ennustettu uusi käyttöaihe | Dermatofibrosarcoma protuberans |
| TxGNN-ennustepistemäärä | 0.9931 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 2/2) |
| Myyntilupien määrä | 2 (voimassa: 2) |
| Suositeltu päätös | Hold (odotetaan) |

---

## Miksi ennuste on perusteltu?

Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohdan ”Mechanism of Action” mukaan valmisteesta Nilotinib (epävirallinen käännös): ”Nilotinibi on BCR-ABL-kinaasin estäjä. Nilotinibi sitoutuu ABL-proteiinin kinaasidomeenin inaktiiviseen konformaatioon ja stabiloi sen. In vitro nilotinibi esti BCR-ABL-välitteistä proliferaatiota hiiren leukemiasolulinjoissa ja ihmisen solulinjoissa, jotka oli peräisin Ph+ CML -potilailta.” Englanninkielinen alkuteksti: "Nilotinib is an inhibitor of the BCR-ABL kinase. Nilotinib binds to and stabilizes the inactive conformation of the kinase domain of ABL protein. In vitro, nilotinib inhibited BCR-ABL mediated proliferation of murine leukemic cell lines and human cell lines derived from patients with Ph+ CML." ([DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc), versio 2026-07-20; haettu 2026-11-19). Alla oleva mekanistinen perustelu perustuu yleiseen tietoon nilotinibin kinaasiprofiilista, ei toimitettuun aineistoon.

DFSP:lle on tyypillistä COL1A1-PDGFB-fuusio, joka johtaa PDGFRB-reseptorin jatkuvaan autokriiniseen aktivaatioon. Nilotinibi estää BCR-ABL:n lisäksi PDGFR:ää (alfa ja beeta), KIT:iä sekä DDR1/2:ta, joten kohdetasolla ennuste on uskottava.

Sama signalointireitti on imatinibin vakiintuneen tehon perusta DFSP:ssä. Nilotinibi voisi siksi olla mekanistisesti läheinen vaihtoehto esimerkiksi imatinibiresistenssin tai -intoleranssin yhteydessä. Korkea TxGNN-pistemäärä (0,9931) sopii tähän PDGFR-pohjaiseen yhteyteen, mutta se on laskennallinen ennuste eikä kliininen todiste.

---

## Kliininen näyttö

Tällä hetkellä ei ole aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Katsaus | Pharmacological Research | Katsaus pienmolekyylisten PDGFR-estäjien roolista kasvainsairauksien hoidossa; PDGF-perhe ja sen signalointi kasvaimissa |

---

## Myyntiluvat Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000798 | Tasigna (voimassa) | – | BCR-ABL-positiivinen krooninen myelooinen leukemia |
| EMEA/H/C/006315 | Nilotinib Accord (voimassa) | – | BCR-ABL-positiivinen krooninen myelooinen leukemia |

<!-- review:begin fi-row-20261112-nilotinib-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/000798 / Tasigna (peruutettu) / – / BCR-ABL-positiivinen krooninen myelooinen leukemia; EMEA/H/C/006315 / Nilotinib Accord (peruutettu) / – / BCR-ABL-positiivinen krooninen myelooinen leukemia” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntiluvat Tasigna (EMEA/H/C/000798), Nilotinib Accord (EMEA/H/C/006315) ovat voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-nilotinib-1 -->

---

## Sytotoksisuus

| Kohde | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (tyrosiinikinaasin estäjä) |
| Myelosuppression riski | Keskisuuri (KG-aineistossa neutropenia, trombosytopenia ja anemia mainitaan vasta-aihe-/varoitusyhteyksissä) |
| Oksettavuusluokitus | Matala |
| Seurantakohteet | Verenkuva, maksa-arvot ja bilirubiini, haiman entsyymit, elektrolyytit (kalium, kalsium, fosfori), verensokeri, EKG (QT-aika) |
| Käsittelysuojaus | Tarkempi ohjeistus: katso valmisteyhteenvedon varoitukset ja varotoimet |

---

## Turvallisuushuomiot

- **Tiedossa olevat sairausriskit (tietämyskaaviosta, ei valmisteyhteenvedosta):** Mallin tietämyskaavio liittää nilotinibin vasta-aihe- tai varovaisuusyhteyksiin seuraavissa tiloissa: pitkä QT-oireyhtymä ja familiaalinen pitkä QT-oireyhtymä, torsades de pointes, hypertensio, maksasairaus, sappirakon sairaus, haimatulehdus, trombosytopenia, neutropenia, agranulosytoosi, anemia, hyperglykemia, diabetes ja diabeettinen ketoasidoosi, kaliumin puutos, hyperkalsemia, nefrokalsinoosi, fosforiaineenvaihdunnan häiriöt, hypofosfatemia, hyperbilirubinemia ja Gilbertin oireyhtymä. Nämä perustuvat tietämyskaavioon, eivät virallisiin valmistetietoihin.
- **Lääkeinteraktiot:** Tarkastettu 100 yhteisvaikutusta. Merkittäviä (Major) ovat mm. deksametasoni, klaritromysiini, pikosulfaatti ja polyetyleeniglykoli (elektrolyyttien kanssa). Kohtalaisia (Moderate) ovat mm. protonipumpun estäjät (omepratsoli, rabepratsoli), H2-salpaajat (famotidiini, ranitidiini, simetidiini), hydrokortisoni, budesonidi, betametasoni, triamsinoloni, pioglitatsoni, loperamidi, bupropioni, aprepitantti, bisakodyyli ja saksagliptiini.

Varoitusten ja vasta-aiheiden osalta katso valmisteyhteenveto.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Ennuste perustuu uskottavaan PDGFR-mekanismiin ja korkeaan TxGNN-pisteeseen, mutta kliinisiä tutkimuksia ei ole ja kirjallisuusnäyttö rajoittuu yhteen yleiseen katsaukseen. Näytön taso on L4. Valmisteyhteenvedon turvallisuustiedot puuttuvat.

<!-- review:begin fi-lic-20261106-nilotinib-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lisäksi lääkkeellä ei ole voimassa olevaa myyntilupaa Suomessa, ja valmisteyhteenvedon turvallisuustiedot puuttuvat.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 2 myyntilupaa, joista 2 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-nilotinib-1 -->

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimeasta (estää turvallisuusseulonnan etenemisen)
- Vaikutusmekanismitietojen täydentäminen DrugBankista
- DFSP-spesifisen kliinisen ja prekliinisen näytön kartoitus, erityisesti imatinibille resistentit tai sitä sietämättömät potilaat
- Selvitys nilotinibin saatavuudesta ja myyntiluvan tilasta Suomessa
- QT-ajan, maksa- ja haimariskien sekä yhteisvaikutusten seurantasuunnitelma

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi lääkkeellä ei ole voimassa olevaa myyntilupaa Suomessa, ja v” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: 2 myyntilupaa (Tasigna (EMEA/H/C/000798), Nilotinib Accord (EMEA/H/C/006315)) ovat voimassa, ei peruutettuja | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

