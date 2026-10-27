---
layout: default
title: Ezetimibe
parent: Vahva näyttö (L1-L2)
nav_order: 184
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-13
description: "Ezetimibe: ennustettu uusi käyttöaihe Hyperlipoproteinemia (näytön taso L1). Alkuperäinen käyttöaihe: Hyperkolesterolemia, dyslipidemiat"
monitor_inn: "EZETIMIBE"
predicted_indications: ["hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **4** kpl
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

## Ezetimibi: Hyperkolesterolemiasta hyperlipoproteinemiaan
{: .text-alpha }

## Yhden lauseen yhteenveto

Ezetimibi on kolesterolin imeytymisen estäjä, jota on alun perin käytetty hyperkolesterolemian ja dyslipidemioiden hoitoon.
TxGNN-malli ennustaa sen sopivan **hyperlipoproteinemian** hoitoon, ja tätä suuntaa tukee tällä hetkellä **40 kliinistä tutkimusta** ja **20 julkaisua**.
Ennuste on käytännössä lähellä nykyistä käyttöaihetta, joten kyse ei ole varsinaisesta uudelleenkäytöstä.

---

## Pikayhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hyperkolesterolemia, dyslipidemiat |
| Ennustettu uusi käyttöaihe | Hyperlipoproteinemia |
| TxGNN-ennustepistemäärä | 99,63 % |
| Näyttötaso | L1 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Proceed with Guardrails (eteneminen suojatoimin) |

---

## Miksi ennuste on perusteltu?

Ezetimibi estää NPC1L1-välitteistä kolesterolin imeytymistä ohutsuolessa ja alentaa siten LDL-kolesterolia. Yksityiskohtaista vaikutusmekanismitietoa ei ole tällä hetkellä saatavilla kokoamassamme aineistossa, mutta mekanismi on kirjallisuudessa hyvin tunnettu.

Hyperlipoproteinemia on mekanismiltaan sama tila kuin alkuperäinen käyttöaihe, hyperkolesterolemia ja dyslipidemia. Siksi ennuste on päällekkäinen nykyisen käyttöaiheen kanssa. Korkea pistemäärä on tämän mukainen.

Toiseksi sijoittuva ennuste, **familiaalinen hyperkolesterolemia** (pistemäärä 99,38 %), on myös kliinisesti uskottava. Ezetimibi täydentää statiinihoitoa ja sisältyy suosituksiin. Homotsygoottisessa muodossa, jossa LDL-reseptoritoiminta puuttuu, vaste on heikompi, joten hyöty tulee lähinnä statiinin lisälääkkeenä.

Kaksi muuta ennustetta ovat heikosti perusteltuja:
- **Kolesteroli-7α-hydroksylaasin puutoksesta johtuva hyperkolesterolemia** (99,25 %): vain yksi prekliininen tutkimus, ei kliinisiä tutkimuksia (näyttötaso L4, päätös Hold).
- **Kolesteroliesterin siirtäjäproteiinin (CETP) puutos** (99,09 %): tilassa HDL on korkea ja LDL tavallisesti matala tai normaali, joten LDL:ää alentavalle lääkkeelle on vähän perusteita (näyttötaso L5, päätös Hold).

---

## Kliininen näyttö

Taulukossa on hyperlipoproteinemian kannalta tärkeimmät tutkimukset.

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Vaihe 3 | Päättynyt | 511 | Evolokumabi vs. ezetimibi potilailla, jotka eivät siedä statiinia lihashaittojen vuoksi; ezetimibi vertailuvalmiste |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Vaihe 4 | Päättynyt | 40 | Ezetimibi yksin vs. statiini hyperkolesterolemiassa; pieni avoin tutkimus |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Vaihe 4 | Päättynyt | 127 | Ezetimibi/rosuvastatiini ja kandesartaani/amlodipiini potilailla, joilla on verenpainetauti ja hyperlipidemia |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Vaihe 3 | Keskeytetty | 49 | Avoin käyttötutkimus ezetimibillä homotsygoottisessa familiaalisessa hyperkolesterolemiassa tai sitosterolemiassa |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | Ei sovellu | Päättynyt | 1 794 | 52 viikon japanilainen havainnoiva pitkäaikaisturvallisuustutkimus |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Vaihe 3 | Päättynyt | 1 220 | Ezetimibi/simvastatiini ja niasiini IIa- tai IIb-tyypin hyperlipidemiassa |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Vaihe 3 | Päättynyt | 576 | Fenofibraatin ja ezetimibin yhdistelmä sekamuotoisessa hyperlipidemiassa |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Vaihe 3 | Päättynyt | 611 | Ezetimibi/simvastatiini ja fenofibraatti sekamuotoisessa hyperlipidemiassa |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Vaihe 3 | Päättynyt | 720 | ENHANCE: ezetimibi + simvastatiini vs. pelkkä simvastatiini heterotsygoottisessa FH:ssa |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Vaihe 4 | Päättynyt | 245 | Sepelvaltimoplakin regressio ezetimibillä vs. statiinilla (IVUS) |

Familiaalisen hyperkolesterolemian suoraa RCT-näyttöä ovat mm. [NCT00867165](https://clinicaltrials.gov/study/NCT00867165) (vaihe 3, lumekontrolloitu, 138 lasta, ezetimibi-monoterapia) ja [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) (vaihe 3, 50 potilasta, ezetimibi statiinin lisänä homotsygoottisessa FH:ssa). Kahdelle viimeiselle ennusteelle ei ole kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|------|------|------|---------|
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oraalinen PCSK9-estäjä enlisitidi heterotsygoottisessa FH:ssa |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | Inklisiraani homotsygoottisessa FH:ssa (ORION-5) |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Kohorttitutkimus | Lancet | Homotsygoottisen FH:n maailmanlaajuinen kokemus |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Katsaus | J Cardiovasc Pharmacol Ther | Kattava katsaus PCSK9-estäjiin |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Katsaus | Mol Med Rep | Hyperlipidemian lääkehoidon edistysaskeleet |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Katsaus | J Am Coll Cardiol | Uudet LDL-kolesterolia alentavat hoidot statiinien, ezetimibin ja PCSK9-estäjien rinnalla |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Konsensuslausuma | Eur Heart J | FH on alidiagnosoitu ja alihoidettu; suositukset seulontaan ja hoitoon |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Katsaus | Am J Cardiovasc Drugs | Ezetimibin farmakologia: estää kolesterolin ja kasvisterolien imeytymistä suolessa |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Katsaus | Cardiol Clin | FH:n hoitovaihtoehdot, mukaan lukien ezetimibi |
| [34943976](https://pubmed.ncbi.nlm.nih.gov/34943976/) | 2021 | Prekliininen | Cells | NPC1L1:n puutos lisää sappihappovarastoa hiirillä (liittyy CYP7A1-puutosennusteeseen) |

Useimmat julkaisut ovat katsauksia tai tutkimuksia muilla lääkkeillä, joissa ezetimibi on vain taustahoito. Suoraa ezetimibin satunnaistettua näyttöä kirjallisuudesta on vähän.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004959 | Nustendi | Ei tietoa | Hyperkolesterolemia; dyslipidemiat |

Myyntilupa on peruutettu, eikä Suomessa ole voimassa olevia myyntilupia.

---

## Turvallisuushuomioita

- **Lääkeaineyhteisvaikutukset:** Yhteensä 100 mahdollista yhteisvaikutusta löytyi. Kohtalaisiksi luokitellut:
  - kenodeoksikolihappo
  - eluksadoliini
  - rosuvastatiini
  - simvastatiini
  
  Muiden (esim. metformiini, omepratsoli, morfiini, doksisykliini) vaikutusluokka on tuntematon.
- **Tietämysgraafin mukaiset vasta-aiheisiin liitetyt sairaudet** (ei valmisteyhteenvetoteksti): haimatulehdus, maksasairaus, sappirakon sairaus, myopatia, lihassairaudet, rabdomyolyysi, päihteiden väärinkäyttö tai riippuvuus. Nämä on tarkistettava valmisteyhteenvedosta.

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat tästä aineistosta, joten ne on tarkistettava ennen etenemistä.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Proceed with Guardrails (eteneminen suojatoimin)**

**Perustelut:**
- Hyperlipoproteinemia ja familiaalinen hyperkolesterolemia ovat mekanismiltaan samaa kolesterolin imeytymisen estoa kuin nykyinen käyttöaihe. Useat vaiheen 3 tutkimukset tukevat näyttöä (L1). Kaksi muuta ennustetta (CYP7A1-puutos ja CETP-puutos) tulee pitää tilassa Hold, koska kliinistä näyttöä ei ole.
- Suomessa ei ole voimassa olevaa myyntilupaa, ja turvallisuustiedot puuttuvat.

**Etenemiseen tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta (Fimean sivusto), koska tämä estää turvallisuusarvioinnin jatkamisen.
- Vaikutusmekanismitietojen täydentäminen (DrugBank).
- Myyntilupatilanteen selvitys, sillä Nustendi on peruutettu, ja sen selvittäminen, onko muita ezetimibia sisältäviä valmisteita saatavilla.
- Tarkempi arvio ezetimibin omasta vaikutuksesta, koska monissa tutkimuksissa se on vain vertailu- tai taustahoito.
- Yhteisvaikutusten (erityisesti statiinit) ja lihas- ja maksaturvallisuuden seurantasuunnitelma.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

