---
layout: default
title: Bedaquiline
parent: Vahva näyttö (L1-L2)
nav_order: 71
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Bedaquiline: ennustettu uusi käyttöaihe Inaktiivinen tuberkuloosi (latentti tuberkuloosi-infektio / taudin eh… (näytön taso L2). Alkuperäinen käyttöaihe: Monilääkeresistentti tuberkuloosi"
monitor_inn: "Bedaquiline"
predicted_indications: ["tuberculosis, bovine", "tuberculosis, avian", "tuberculous ascites", "tuberculoma", "inactive tuberculosis", "vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "cutaneous tuberculosis", "esophageal candidiasis"]
---

# Bedaquiline
{: .fs-9 }

Näytön taso: **L2** | Ennustetut käyttöaiheet: **10** kpl
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

# Bedakiliini: Monilääkeresistentistä tuberkuloosista latentin tuberkuloosi-infektion ehkäisyyn

## Yhteenveto

Bedakiliini on tuberkuloosilääke, jota on alun perin käytetty monilääkeresistentin tuberkuloosin hoitoon. TxGNN-malli ennustaa sen voivan tehota myös **inaktiiviseen tuberkuloosiin** (latentti infektio ja taudin ehkäisy). Ennusteen tukena on tällä hetkellä **3 kliinistä tutkimusta** ja **19 julkaisua**. Yksikään tutkimus ei ole vielä tuottanut tuloksia kyseisestä käyttötarkoituksesta.

Raportissa käsitellään ensisijaisesti parhaiten tuettua ennustetta (inaktiivinen tuberkuloosi). Muiden ennusteiden lyhyt vertailu on omassa osiossaan.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Monilääkeresistentti tuberkuloosi |
| Ennustettu uusi käyttöaihe | Inaktiivinen tuberkuloosi (latentti tuberkuloosi-infektio / taudin ehkäisy) |
| TxGNN-ennustepistemäärä | 99,96 % |
| Näytön taso | L2 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Etene suojatoimin (Proceed with Guardrails) |

Huomautus: Näytön taso L2 perustuu käynnissä oleviin vaiheen 2/3 tutkimuksiin, joista ei ole vielä tuloksia. Taso on siksi ylärajaa osoittava, ja varsinainen tehonäyttö on vielä saamatta.

---

## Miksi ennuste on perusteltu?

Tällä hetkellä yksityiskohtaista vaikutusmekanismitietoa ei ole käytettävissä kootussa aineistossa. Kirjallisuuden perusteella bedakiliini estää mykobakteerien ATP-syntaasia, joka on keskeinen bakteerin energiantuotannolle. Kyseinen kohde on säilynyt *Mycobacterium tuberculosis* -kompleksin lajeilla.

Alkuperäinen käyttöaihe (monilääkeresistentti tuberkuloosi) ja ennustettu käyttöaihe (tuberkuloosin ehkäisy) liittyvät samaan taudinaiheuttajaan. Bedakiliinin steriloivan vaikutuksen katsotaan tukevan sen käyttöä taudin ehkäisyssä, erityisesti monilääkeresistenttiä tuberkuloosia sairastavien lähikontaktien ja HIV-infektion kanssa elävien ihmisten kohdalla, kun rifamysiini- tai isoniatsidipohjainen ehkäisy ei ole mahdollinen.

Keskeinen rajoite on, että suorin tutkimus (BREACH-TB) on vielä rekrytointivaiheessa. Tehosta ei siis ole vielä tuloksia tässä käyttötarkoituksessa.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Vaihe 2/3 | Rekrytoi | 2530 | BREACH-TB: 4 viikon bedakiliinikuuri verrattuna standardihoitoon tuberkuloosin ehkäisyssä HIV-infektion kanssa elävillä ja suuren riskin lähikontakteilla. Suoraan relevantti, tuloksia ei vielä. |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Vaihe 2/3 | Aktiivinen, ei rekrytoi | 288 | CRUSH-TB: 17 viikon lyhytkuurit (bedakiliini, moksifloksasiini, pyratsiinamidi + rifabutiini tai delamanidi) keuhkotuberkuloosin hoidossa. Epäsuora, koskee aktiivista tautia. |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Vaihe 1 | Ei vielä rekrytoi | 60 | Tuberkuloosilääkkeiden (mm. bedakiliinin) pitoisuudet plasmassa ja rintamaidossa imettävillä naisilla. Ei tehonäyttöä. |

---

## Kirjallisuusnäyttö

Aineistossa ei ole satunnaistettuja kontrolloituja tutkimuksia. Suurin osa on yleisiä katsauksia tuberkuloosin hoidosta. Valikoima tärkeimmistä:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Katsaus | Recent Patents on Anti-Infective Drug Discovery | Bedakiliini mahdollistaa lyhyemmät ja paremmat tuberkuloosihoito-ohjelmat |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Katsaus | Antibiotics (Basel) | *M. tuberculosis* F-ATP-syntaasin estäjät ja kohteet |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Katsaus | Infectious Disorders Drug Targets | Bedakiliinipohjaiset annostelujärjestelmät; lääke voi kohdistua latenttiin muotoon |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Katsaus | Respirology | Tuberkuloosin ajankohtaiskatsaus: tauti on jatkumo, ei vain latentti tai aktiivinen |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Katsaus | Zhejiang Da Xue Xue Bao Yi Xue Ban | Latentin tuberkuloosi-infektion diagnostiikan ja hoidon edistysaskeleet |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Katsaus | Clinical Pharmacology & Therapeutics | Tuberkuloosin hoito: latentti ja aktiivinen tauti vaativat erilaisen hoidon |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Katsaus | International Journal of Molecular Sciences | Tuberkuloosin patogeneesi, nykyiset hoito-ohjelmat ja uudet lääkekohteet |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Katsaus | The Lancet Infectious Diseases | Uudet lääkkeet, hoito-ohjelmat ja isäntään kohdistuvat hoidot |

---

## Muut ennustetut käyttöaiheet (lyhyt vertailu)

| Ennuste | Pistemäärä | Näytön taso | Päätös | Huomio |
|------|------|------|------|------|
| Tuberkuloomi | 99,96 % | L4 | Tutkimuskysymys | Tapausselostuksia BPaL/BPaLM-hoidoista, joissa kliininen tai radiologinen paraneminen. Keskushermoston läpäisy epävarma ja hoidot yhdistelmiä. |
| Naudan tuberkuloosi | 99,96 % | L4 | Odota | Vain in vitro -tutkimus *M. tuberculosis* -kannalla, epäsuora tuki. |
| Lintutuberkuloosi | 99,96 % | L5 | Odota | Pelkkä mallin ennuste, ei tutkimuksia. |
| Tuberkuloottinen askites | 99,96 % | L4 | Odota | Ainoa löydetty julkaisu koskee lääkemaksavauriota, ei tehoa. |
| Ihotuberkuloosi | 99,70 % | L4 | Odota | Julkaisut koskevat lääkkeiden ihohaittoja, eivät tehoa. |
| Vulvovaginaalinen kandidiaasi | 99,88 % | L5 | Odota | Ei mekanistista perustetta; todennäköinen mallin artefakti. |
| Fascioliaasi | 99,88 % | L5 | Odota | Ei mekanistista perustetta. |
| Urea-kiertohäiriö | 99,78 % | L5 | Odota | Ei uskottavaa mekanistista yhteyttä; todennäköinen artefakti. |
| Ruokatorven kandidiaasi | 99,68 % | L5 | Odota | Ei tunnettua sienilääkevaikutusta. |

---

## Myyntiluvat Suomessa

| Myyntilupanumero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002614 | Sirturo | – | Monilääkeresistentti tuberkuloosi (tila: peruutettu) |

Kaikki myyntiluvat ovat peruutettuja, joten valmiste ei tällä hetkellä ole voimassa olevalla myyntiluvalla Suomen markkinoilla.

---

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla kootussa aineistossa, joten ne tulee tarkistaa valmisteyhteenvedosta ennen jatkoa.

**Lääkeinteraktiot:** Interaktioita löytyi yhteensä 100. Aineistossa näkyvistä merkittävimmät (vaikeusaste "Major") ovat:

- deksametasoni
- klaritromysiini
- pikosulfaatti
- polyetyleeniglykoli (3350 elektrolyyttien kanssa)
- dolasetroni
- palonosetroni
- natriumsulfaatti

Lisäksi kohtalaisia (Moderate) interaktioita on mm. doksisykliinin, minosykliinin, tetrasykliinin, famotidiinin, pioglitatsonin, loperamidin, bupropionin, naltreksonin, akarboosin, bisakodyylin, oksandrolonin, oksimetolonin ja kenodeoksikoolihapon kanssa.

Interaktioiden suuri määrä edellyttää huolellista lääkityksen tarkistusta. Etenkin QT-aikaa pidentävien lääkkeiden (esim. dolasetroni, palonosetroni, klaritromysiini) yhteiskäyttöä tulee arvioida, ja QT-seuranta on suositeltava.

---

## Johtopäätös ja seuraavat askeleet

**Päätös: Etene suojatoimin (Proceed with Guardrails)**

**Perustelut:**
- Inaktiivisen tuberkuloosin ennuste on tuettu vaiheen 2/3 tutkimuksella (BREACH-TB), joka testaa suoraan bedakiliinin käyttöä tuberkuloosin ehkäisyssä. Tutkimus on kuitenkin vielä käynnissä eikä tuloksia ole. Muut ennusteet ovat selvästi heikommin tuettuja.

**Jatkoa varten tarvitaan:**
- BREACH-TB-tutkimuksen (NCT06568484) tulosten seuranta
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvitys (tällä hetkellä puuttuu ja estää turvallisuusarvioinnin etenemisen)
- Yksityiskohtaiset vaikutusmekanismitiedot DrugBankista
- QT-seurantasuunnitelma ja lääkeinteraktioiden hallintasuunnitelma
- Käytön rajaaminen monilääkeresistentin tuberkuloosin kontakteihin, joille rifamysiini- tai isoniatsidipohjainen ehkäisy ei sovi
- Myyntiluvan tilanteen selvittäminen Suomessa, koska ainoa myyntilupa on peruutettu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

