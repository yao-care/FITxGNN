---
layout: default
title: Insulin Glulisine
parent: Vahva näyttö (L1-L2)
nav_order: 200
evidence_level: L1
indication_count: 10
---

# Insulin Glulisine
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

# Insuliini glulisin: diabetuksesta tyypin 1 diabetukseen

## Yhden lauseen yhteenveto

Insuliini glulisin on nopeasti vaikuttava insuliinianalogi, jota käytetään laajasti verensokerin hallintaan diabetes mellituksessa. TxGNN-malli ennustaa, että se saattaa olla tehokas **tyypin 1 diabetukseen**, ja tällä hetkellä **50 kliinistä tutkimusta** ja **19 julkaisua** tukevat tätä suuntaa — kuitenkin tämä ennustettu "uusi" indikaatio on merkittävästi päällekkäinen insuliinin glulisiinin jo vakiintuneen kliinisen käytön kanssa, joten sitä tulisi lukea näyttöjen vahvuuden validointina eikä todellisesti uutena lääkkeen uudelleenkäyttösignaalina.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei dokumentoitu saatavilla olevissa sääntelyaineistoissa (Suomi: ei markkinoilla, ei lupakirjaa); insuliini glulisin on yleensä indikoitu aterian aikaisen verensokerin hallintaan diabetes mellituksessa |
| Ennustettu uusi indikaatio | Tyypin 1 diabetes mellitus |
| TxGNN-ennustuspistemäärä | 99.55% |
| Näyttöjen taso | L1 |
| Markkinatilanne Suomessa | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Etene varautuvin ehdoin |

---

## Miksi tämä ennustus on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla. Tunnettujen tietojen perusteella insuliini glulisin on nopeasti vaikuttava ihmisen insuliinianalogi, joka sitoutuu insuliinireseptoriin ja palauttaa suoraan insuliinin signaloinnin sekä alentaa verensokeria — tämä on peruspharmakolooginen vaikutus, joka on yhteinen kaikille insuliinituotteille, ei uusi mekanismi, jota sovelletaan uusilla tavoilla.

Koska insuliinin korvaaminen on vakiintuneiden hoitokäytäntöjen mukainen hoito absoluuttiselle insuliinin puutokselle, ja tyypin 1 diabetes mellitus määritellään haiman beetasolujen autoimmuuniheikkenemiseksi, joka johtaa täsmälleen tähän puutokseen, lääkkeen ja ennustetun indikaation välinen farmakologinen yhteys on suora ja odotettu eikä tutkiva.

**Tärkeä huomautus:** näyttöpaketin oma uudelleenkäyttöjen perustelut tunnistavat tämän nimenomaisesti — insuliini glulisin on jo hyväksytty käytettäväksi T1DM:ssä useimmilla markkinoilla, joten tämä ehdokas ei edusta todellista "vanha lääke, uusi käyttö" uudelleenkäyttöä. Erittäin vahva TxGNN-pistemäärä ja suuri tutkimus- ja kirjallisuuspohja heijastavat lääkkeen hyvin vakiintunutta roolia T1DM:n hallinnassa, ei äskettäin löydettyä terapeutista soveltamista. Tämä ehdokas tulkitaan parhaiten mallin validointi-/positiivisen kontrollitapauksena eikä putkiston mahdollisuutena.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Phase 4 | Valmis | 289 | Osoitti insuliinin glulisiinin paremmuuden aspartiin ja lispron nähden CSII-pumpulla selittämättömiin hyperglykemioihin/infuusion sarjan tukkeutumiseen liittyen T1DM:ssä |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Valmis | 59 | Monikansallinen glulisiinin (HMR1964) ja aspartin vertailu CSII-pumpun välityksellä; turvallisuuspäätepisteet (tukkeutumiset, HbA1c, hypoglykemia) T1DM:ssä |
| [NCT00115570](https://clinicaltrials.gov/study/NCT00115570) | Phase 3 | Valmis | 572 | 26 viikon tutkimus: glulisin oli yhtä turvallinen ja tehokas kuin lispro lapsissa ja nuorissa T1DM:n kanssa |
| [NCT00545337](https://clinicaltrials.gov/study/NCT00545337) | Phase 3 | Valmis | 60 | 26 viikon kansainvälinen tutkimus glulisiinin + glargiinin tehokkuuden (HbA1c) ja turvallisuuden arvioimiseksi T1DM:ssä |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Valmis | 250 | 28 viikon ei-inferioriteettitutkimus: HMR1964 (glulisin) vs lispro T1DM:ssä |
| [NCT00397553](https://clinicaltrials.gov/study/NCT00397553) | Phase 3 | Valmis | 104 | Paikallinen tehokkuus- ja turvaisuusdata glulisiinille + glargiinin baasaali-insuliinihoidolle T1DM:ssä |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Valmis | 206 | Baasaali-bolus-hoito (glargiini + glulisin) aiemmin huonosti hallituissa T1DM-potilaissa; HbA1c-muutos 24 viikolla |
| [NCT00539448](https://clinicaltrials.gov/study/NCT00539448) | Phase 4 | Valmis | 98 | Avoin monisairaalan tutkimus glargiinin + glulisiinin tehokkuudesta ja annostelusta T1DM:ssä |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Valmis | 68 | Glulisiinin + glargiinin tehokkuus, turvallisuus ja potilaan tyytyväisyys T1DM:ssä |
| [NCT00925977](https://clinicaltrials.gov/study/NCT00925977) | N/A | Lopetettu | 44 | Hoitojen tyytyväisyyden ristiintarkastelu: glargiini + glulisin vs NPH + glulisin uusissa diagnoosissa olleissa lapsissa T1DM:n kanssa (tutkimus lopetettu) |

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Monikansallinen satunnaistettu rinnakkaisryhmä-tutkimus (n=683) glulisiinin ja lispron tehokkuuden ja turvallisuuden vertailussa T1DM:n aikuisissa |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Satunnaistettu 3-suuntainen ristiintarkastelu: glulisin vs aspart vs lispro CSII:lla T1DM:ssä |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | 26 viikon lastentutkimus osoitti glulisiinin ja lispron vertailukelpoista tehokkuutta ja turvallisuutta baasaali-bolus-säännöissä |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | RCT | Diabetes Obes Metab | Glulisiinin ja lispron tehokkuus ja turvallisuus japanilaisissa T1DM-potilaissa käyttämällä glargiinia baasaali-insuliinina |
| [41366610](https://pubmed.ncbi.nlm.nih.gov/41366610/) | 2026 | RCT | Diabetes Obes Metab | Vaiheen III satunnaistettu tutkimus: biosimilaaripohjainen insuliini glulisin (T-Glu) vs alkuperäinen (R-Glu) — immuunigenisiteetti, tehokkuus, turvallisuus T1DM:ssä |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Kohortti | Pediatr Int | Glulisiinin 1 vuoden CSII-käyttö 20 lapsessa T1DM:n kanssa; merkittävä parannus aterian jälkeiseen glukoosin hallintaan |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Katsaus | Drugs | Kattava katsaus insuliinin glulisiinin rooliin diabetes-hallinnassa, mukaan lukien T1DM |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK/PD-tutkimus | Diabetes Care | Glulisiinin farmakokinetika ja aterian aikainen glukoosin hallinta vs säännöllinen ihmisen insuliini lapsissa T1DM:n kanssa |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Katsaus | Clin Pharmacokinet | Insuliinin glulisiinin kliinisen farmakokinetiikan ja farmakodynamiikan katsaus |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Katsaus | Drugs | Glulisiinin verensokerin hallinnan tehokkuuden katsaus vs säännöllinen ihmisen insuliini T1DM:ssä/T2DM:ssä |

---

## Turvallisuusnäkökohdat

Viitattavaksi lääkkeen pakkausmerkintöihin sisältyviin turvaisuustietoihin.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Etene varautuvin ehdoin**

**Perustelut:**
Näyttöjen vahvuus on korkea (L1: useita valmistuneita vaiheen 3 RCT:ita, jotka tutkivat suoraan insuliinia glulisiinia T1DM:ssä), mutta ennustettu indikaatio on merkittävästi päällekkäinen lääkkeen jo vakiintuneen kliinisen käytön kanssa eikä edusta todellista uudelleenkäyttömahdollisuutta — varautumiset ovat tarpeen varmistaakseen, että tämä käsitellään virallisena rekisteröinti-/validointitapauksena eikä uutena terapeutisena hypoteesina.

**Jatkamisen edellytykset:**
- TFDA/Fimea-pakkausmerkinnän sisältämät varoitukset, vasta-aiheet ja lääkkeiden yhteisvaikutustiedot (tällä hetkellä estävät turvallisuuden ennakkoarvioinnin — DG001)
- Vahvistettu vaikutusmekanismin dokumentaatio DrugBankista (DG002)
- Vahvistus siitä, että "ennustettu uusi indikaatio" heijastaa todellista näyttövajetta Suomessa (0 lupaa, ei markkinoilla) vai yksinkertaisesti rekisteröitävää olemassa olevaa käyttöä, jotta voidaan ohjata tämä oikein markkinoille tulemisen tapauksena eikä uudelleenkäyttötapauksena

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

