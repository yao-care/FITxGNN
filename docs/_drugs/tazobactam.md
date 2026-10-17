---
layout: default
title: Tazobactam
parent: Vahva näyttö (L1-L2)
nav_order: 420
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-13
description: "Tazobactam: ennustettu uusi käyttöaihe Keuhkokuume (toissijainen ennuste: virtsatieinfektio) (näytön taso L1). Alkuperäinen käyttöaihe: Bakteeri-infektiot"
monitor_inn: "Tazobactam"
predicted_indications: ["urinary tract infection (disease)"]
---

# Tazobactam
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **2** kpl
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

# Tatsobaktaami: Bakteeri-infektioista keuhkokuumeeseen

> Huom. otsikossa lääkkeen nimi on Tatsobaktaami (Tazobactam).

Korjaus: otsikko alla varsinaisessa muodossa.

# Tazobactam: Bakteeri-infektioista keuhkokuumeeseen

## Yhden virkkeen yhteenveto

Tatsobaktaami (tazobactam) on beetalaktamaasin estäjä, jota on alun perin käytetty bakteeri-infektioiden hoitoon yhdessä beetalaktaamiantibioottien kanssa.
TxGNN-malli ennustaa sen soveltuvan **keuhkokuumeen** hoitoon, ja tätä suuntaa tukee tällä hetkellä **20 kliinistä tutkimusta** ja **20 julkaisua**.
Ennuste on lääkeryhmän sisäinen laajennus eikä uusi vaikutusmekanismi: näyttö koskee vain yhdistelmävalmisteita (esim. keftolotsaani/tatsobaktaami, piperasilliini/tatsobaktaami).

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Bakteeri-infektiot |
| Ennustettu uusi käyttöaihe | Keuhkokuume (toissijainen ennuste: virtsatieinfektio) |
| TxGNN-ennustepistemäärä | 99,46 % |
| Näytön taso | L1 |
| Markkinatilanne Suomessa | Vain peruutettu (ei voimassa olevia myyntilupia) |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Proceed with Guardrails (eteneminen suojatoimin) |

---

## Miksi ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa ei ole tällä hetkellä saatavilla. Tunnetun tiedon perusteella tatsobaktaami on beetalaktamaasin estäjä, joka palauttaa yhdistelmäkumppanin (piperasilliini, keftolotsaani) tehon beetalaktamaasia tuottavia gramnegatiivisia bakteereja vastaan. Sillä ei ole omaa antibakteerista tehoa.

Keuhkokuume, myös sairaalassa hankittu ja ventilaattoriin liittyvä, on bakteeri-infektio. Alkuperäinen käyttöaihe (bakteeri-infektiot) kattaa jo laajasti tämän käytön, joten kyseessä on antibakteerisen luokan sisäinen laajennus. TxGNN-mallin korkea pistemäärä on linjassa olemassa olevan kliinisen näytön kanssa.

Huomioitavaa: markkinatila "vain peruutettu" koskee yksittäistä tuoteluetteloa (Zerbaxa), ei nykyisin käytössä olevia yhdistelmävalmisteita.

---

## Kliininen tutkimusnäyttö

Alla keuhkokuumeen (ensisijainen ennuste) keskeisimmät tutkimukset. Tutkimuksia on yhteensä 20; esitetty on 10 relevantteinta.

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Vaihe 3 | Päättynyt | 726 | Keftolotsaani/tatsobaktaami vs. meropeneemi ventilaattoriin liittyvässä keuhkokuumeessa (ASPECT-NP); ei-huonommuus 28 vrk:n kokonaiskuolleisuudessa |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Vaihe 3 | Päättynyt | 537 | Imipeneemi/relebaktaami vs. piperasilliini/tatsobaktaami sairaalakeuhkokuumeessa |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Vaihe 3 | Päättynyt | 460 | Levofloksasiini vs. piperasilliini/tatsobaktaami lievässä tai keskivaikeassa sairaalakeuhkokuumeessa |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Vaihe 1 | Päättynyt | 41 | Keftolotsaani/tatsobaktaamin turvallisuus ja farmakokinetiikka lapsilla (sairaalakeuhkokuume) |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Vaihe 1 | Päättynyt | 37 | Keftolotsaani/tatsobaktaamin farmakokinetiikka ja keuhkopenetraatio kriittisesti sairailla |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Vaihe 2 | Päättynyt | 80 | Pilottitutkimus asianmukaisesta antibioottihoidosta tehohoidossa |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | Ei määritelty | Päättynyt | 179 | Yksilöllinen annostelu keuhkokuumeen hoidossa tehohoitopotilailla |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | Ei määritelty | Käynnissä (rekrytointi) | 42 | Mallipohjainen piperasilliini/tatsobaktaamin annostelu iäkkäillä |
| [NCT07004049](https://clinicaltrials.gov/study/NCT07004049) | Vaihe 4 | Käynnissä (rekrytointi) | 600 | TREAT-GNB: monilääkeresistenttien gramnegatiivisten infektioiden alustatutkimus |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Vaihe 3 | Keskeytetty | 4 | Keftolotsaani/tatsobaktaami vs. piperasilliini/tatsobaktaami; vain 4 osallistujaa, ei käyttökelpoista näyttöä |

Virtsatieinfektiossa (toissijainen ennuste) merkittävimmät ovat [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) (vaihe 3, 1043 osallistujaa, piperasilliini/tatsobaktaami vertailuhaarana) ja [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) (vaihe 2, 134 lasta, keftolotsaani/tatsobaktaami vs. meropeneemi).

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|------|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: keftolotsaani/tatsobaktaami vs. meropeneemi sairaalakeuhkokuumeessa, vaiheen 3 ei-huonommuustutkimus |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipeneemi/relebaktaami vs. piperasilliini/tatsobaktaami |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Vaiheen 3 ei-huonommuustutkimus: IMI/REL vs. PIP/TAZ HABP/VABP-potilailla |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systemaattinen katsaus | Clin Microbiol Infect | Verkostometa-analyysi empiirisistä antibioottihoidoista sairaalakeuhkokuumeessa |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systemaattinen katsaus | Int J Antimicrob Agents | Uusien beetalaktaamien farmakokinetiikka karbapeneemiresistentissä keuhkokuumeessa |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Katsaus | Eur Respir Rev | Uudet antibiootit gramnegatiivisen keuhkokuumeen hoidossa |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Katsaus | Semin Respir Crit Care Med | Uudet antibiootit HAP/VAP:n hoidossa |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Katsaus | Crit Care | Sairaalakeuhkokuumeen hoidon päivitys tehohoidossa |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Kohorttitutkimus | Clin Infect Dis | Resistenssin kehittyminen: keftatsidiimi-avibaktaami 40 % vs. keftolotsaani/tatsobaktaami 10 % |
| [42129898](https://pubmed.ncbi.nlm.nih.gov/42129898/) | 2026 | Satunnaistettu farmakokineettinen tutkimus | Crit Care | Keftolotsaani/tatsobaktaamin ja keftatsidiimi-avibaktaamin keuhkopenetraatio jatkuvassa infuusiossa |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/003772 | Zerbaxa | – | Bakteeri-infektiot (peruutettu) |

---

## Turvallisuushuomiot

Valmisteyhteenvedon turvallisuustietoja ei ole tällä hetkellä saatavilla; tarkista ne valmisteyhteenvedosta.

Tietämyskaaviosta (ei valmisteyhteenvedosta) tunnistetut mahdolliset vasta-aiheisiin liittyvät sairaudet, jotka vaativat varovaisuutta ja jotka on varmennettava valmisteyhteenvedosta:
- munuaissairaus
- neutropenia ja agranulosytoosi
- veren hyytymishäiriöt
- Clostridium difficile -koliitti
- vastasyntyneen nekrotisoiva enterokoliitti
- tarttuva mononukleoosi ja krooninen Epstein-Barr-virusinfektio
- virtsanjohtimen märkäpesäke (pyoureter)

Lisäksi kirjallisuudessa (PMID 30219824) todetaan, että keftolotsaani/tatsobaktaamin teho voi olla heikentynyt potilailla, joiden kreatiniinipuhdistuma on 30–50 ml/min. Munuaisfunktion mukainen annostus on tärkeää.

Yhteisvaikutustietoja ei löytynyt.

---

## Johtopäätös ja jatkotoimet

**Päätös: Proceed with Guardrails (eteneminen suojatoimin)**

**Perustelut:**
- Useat päättyneet vaiheen 3 satunnaistetut tutkimukset (mm. ASPECT-NP, n=726; RESTORE-IMI 2, n=537) tukevat tatsobaktaamia sisältäviä yhdistelmiä keuhkokuumeessa, ja näyttötaso on L1. Tatsobaktaami ei kuitenkaan toimi yksinään, joten päätös koskee vain yhdistelmävalmisteita. Ennuste on lääkeluokan sisäinen laajennus, ei aidosti uusi käyttöaihe.

**Eteneminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta ja tarkistus (Fimean sivusto); tämä on estävä tietoaukko, jota ilman turvallisuusseulontaan ei voi edetä
- Vaikutusmekanismin tietojen täydentäminen (DrugBank)
- Voimassa olevien yhdistelmävalmisteiden (esim. piperasilliini/tatsobaktaami) myyntilupatilanteen selvittäminen Suomessa
- Munuaisfunktion ja neutropenian seurantasuunnitelma
- ESBL-tuottajien osalta karbapeneemien ensisijaisuuden huomioiminen (NCT03891433 on keskeytetty, eikä tuloksia ole)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

