---
layout: default
title: Simvastatin
parent: Vahva näyttö (L1-L2)
nav_order: 345
evidence_level: L1
indication_count: 8
---

# Simvastatin
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **8** kpl
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

# Simvastatin: hyperkolesterolemiaasta perinnölliseen hyperkolesterolemiaaan

## Yhden lauseen yhteenveto

Simvastatin on vakiintunut HMG-CoA reduktaasin inhibiittori (statiini), jota käytetään klassisesti hyperkolesterolemian ja sydän- ja verisuonisairauksien riskin vähentämiseen.
TxGNN-malli ennustaa, että se saattaa olla tehokas **perinnöllisen hyperkolesterolemian (FH)** hoidossa,
ja tällä hetkellä **19 kliinistä tutkimusta** ja **18 julkaisua** tukevat tätä suuntaa — vaikka tämä heijastaa enemmän olemassa olevaa standardihoitokäytäntöä kuin todellista uutta signaalia.

---

## Nopea katsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei saatavilla lähdetiedoissa (Fimean lisenssirekisterit puuttuvat; lääkettä ei ole markkinoitu Suomessa). Simvastatin on yleisesti tunnettu statiini, jota käytetään hyperkolesterolemian/dyslipidemiaan. |
| Ennustettu uusi indikaatio | Perinnöllinen hyperkolesterolemia |
| TxGNN-ennustepistemäärä | 99.63% |
| Näyttötaso | L1 |
| Suomen markkinatilanne | Ei markkinoitu |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksilla |

---

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaiset rakenteelliset toimintamekanismin tiedot (`original_moa`) on merkitty tietovajeeksi, mutta näyttöpaketti esittää mekanistisen perustelun suoraan: simvastatin estää HMG-CoA reduktaasin, alentaa maksan kolesterolisyntesiä ja lisää LDL-reseptorin ilmentymistä, mikä parantaa LDL-C:n klirensia plasmasta.

Perinnöllinen hyperkolesterolemia (FH) — ja sen geneettisen nomenklaturan vastine "autosomaalinen dominantti hyperkolesterolemia" (itsenäisesti ennustettu sijalla 4, myös pisteytetty L1:ksi) — johtuu LDL-reseptorin signalointireitin viallisesta toiminnasta, mikä johtaa heikentyneen LDL-klirenssiin. Statiinin aiheuttama LDL-reseptorin lisääntyminen vastaa suoraan tälle sairaudelle ominaisen mekanismin, minkä vuoksi simvastatin (ja statiinit yleensä) ovat jo ensilinjan standardihoidon perusta FH:n hoidossa, mukaan lukien lapset ja heterotsygoottitilanteet.

Koska tämä suora mekanistinen suhde on olemassa, näyttöpaketti itse tunnistaa tämän oppikirjaesimerkkinä olevaksi mekanismi-indikaatioparityypiksi pelkän TxGNN-mallin löydön sijaan — kaksi itsenäistä, korkealle pisteytettää ennustetta (FH ja sen geneettinen synonyymi) vahvistavat toisiaan mutta eivät edusta uutta kliinistä näkemystä.

---

## Kliinisen tutkimuksen näyttö

| Tutkimuksen numero | Vaihe | Tila | Osallistujamäärä | Tärkeimmät tulokset |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Vaihe 3 | Valmis | 720 | ENHANCE-tutkimus: ezetimiibi + korkean annoksen simvastatin vs. simvastatin yksin kaulavaltimon ateroskleroosin etenemiselle HeFH-potilailla |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Vaihe 3 | Valmis | 248 | Ezetimiibi + simvastatin tehokkuus/turvallisuus/siedettävyys nuorilla HeFH-potilailla |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Vaihe 3 | Valmis | 50 | Ezetimiibi lisätty atorvastatiiniin tai simvastatiiniin homotsygoottisen FH:n (HoFH) potilailla |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Vaihe 3 | Valmis | 44 | Yllä olevan HoFH ezetimiibi + statiini tutkimuksen pitkäaikainen avoin jatko |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Vaihe 3 | Valmis | 442 | Munuaisvaikutukset: rosuvastatin vs. simvastatin FH/dyslipidemia-potilailla |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Vaihe 3 | Valmis | 199 | Niakiini ER + simvastatin vs. atorvastatin lipiidivaikutukset hyperlipidemian potilailla |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Vaihe 4 | Valmis | 194 | Kolesevelami lisänä vakaiselle statiinihoidolle (ml. simvastatin) pediatrisilla HeFH-potilailla |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Vaihe 3 | Valmis | 249 | Aalirokumabi vs. plasebo HeFH-potilailla, joita ei ole saatu kontrolliin peruslääkityksellä (ml. statiinit) |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Vaihe 3 | Valmis | 486 | Aalirokumabi vs. plasebo HeFH-potilailla, joita ei ole saatu kontrolliin peruslääkityksellä (ml. statiinit) |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Valmis | 2089 | VYTORIN:n (ezetimiibi/simvastatin) markkinoinnin jälkeinen uudelleentarkastelu turvallisuudesta ja tehokkuudesta |

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Tärkeimmät tulokset |
|------|-----|------|------|---------|
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Ohjeistus | Circulation | 2026 ACC/AHA dyslipidemiaohjeistus korvaa 2018 verikolesteroolia koskevan ohjeistuksen; statiinit säilyvät perushoitona |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE-tutkimus: simvastatin ± ezetimiibi ateroskleroosin etenemiselle FH:ssa |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Katsaus (Cochrane) | Cochrane Database of Systematic Reviews | Statiinien systemaattinen katsaus lapsilla, joilla on FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Katsaus | Expert Opinion on Drug Safety | Simvastatiinin hyötyjen ja riskien arviointi FH:ssa |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Kohorttitutkimus | Journal of the American College of Cardiology | Statiinihoidolla vähennetään sydän- ja verisuonitapahtumia ja kuolleisuutta heterotsygoottisessa FH:ssa |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Kohorttitutkimus | Journal of Clinical Medicine | Soluttaimen immuunivasteesta johtuvat parametrit lapsilla, joilla on FH ja joita hoidetaan simvastatiinilla |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Kohorttitutkimus | The Pharmacogenomics Journal | Yhdistetty FH:n ja statiinien farmakogeneettinen NGS-tutkimusstrategia |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Katsaus | Drug Safety | Simvastatiinin hyödyt ja riskit FH:n potilailla |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | RCT | International Angiology | Ezetimiibi/simvastatiinin pitkäaikainen tehokkuus ja turvallisuus FH:ssa |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | RCT | Nutrition, Metabolism and Cardiovascular Diseases | Atorvastatin vs. simvastatin LDL-C-tavoitteen saavuttamiselle HeFH:ssa |

---

## Suomen markkinatiedot

Simvastatiinilla ei ole tällä hetkellä rekisteröityä markkinaoikeutta Suomessa (`market_status: Not marketed`, `total_licenses: 0`) näyttöpaketissa — ei lisenssirekisterien tietoja ole saatavilla yhteenvedon tekemistä varten.

---

## Turvallisuushuomiot

Turvallisustiedot löytyvät pakkausselosteesta.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Jatka varauksilla**

**Perustelut:**
FH-indikaatio on tuettu L1-tason näytöllä (19 tutkimusta, mukaan lukien maamerkkitutkimus ENHANCE, 18 julkaisua, mukaan lukien Cochrane-katsaukset ja 2026 ACC/AHA-ohjeistus), ja sitä vahvistaa itsenäinen, yhtä korkealle pisteytetty ennuste samalle taudille sen geneettisen nimen alla ("autosomaalinen dominantti hyperkolesterolemia"). Tämä heijastaa kuitenkin simvastatiinin olemassa olevaa roolia standardihoitona pikemminkin kuin uuden uudelleenkäytön signaalia, ja kaksi estävää/korkean vakavuusasteen tietovajeista jää ratkaisematta.

**Jatkaaksesi, seuraava on tarpeen:**
- TFDA/Fimean pakkausselosteen varoitukset ja vasta-aiheet (DG001, estävä — tällä hetkellä täysin puuttuvat)
- Dokumentoitu toimintamekanismi DrugBankista (DG002)
- Suomen markkinoinnin/rekisteröintitilanteen selventäminen, sillä lääke näyttää tällä hetkellä olevan nolla lisenssillä huolimatta siitä, että se on globaalisti markkinoitu geneerinen lääke
- FH:n ja autosomaalisen dominantti-hyperkolesterolemian ennusteiden sovittaminen yhdeksi indikaatioksi kahden erillisen ehdokkaan sijaan

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

