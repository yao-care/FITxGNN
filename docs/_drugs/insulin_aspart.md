---
layout: default
title: Insulin Aspart
parent: Vahva näyttö (L1-L2)
nav_order: 196
evidence_level: L1
indication_count: 10
---

# Insulin Aspart
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

# Insulin-aspartat: Tyypin 1 diabetes mellitus — olemassa oleva indikaatio, ei uusi lääkkeen uudelleenkäytön signaali

## Yhden lauseen yhteenveto

Insulin-aspartat (DrugBank ID DB01306) on nopeasti vaikuttava insuliini-analogi; tällä todistusaineistolla ei ole tietoja sen alkuperäisestä indikaatiosta tai MOA:sta (tietoaukko). TxGNN:n parhaiten sijoittuva ennuste, **Tyypin 1 diabetes mellitus**, on tuettu **50 kliinisellä tutkimuksella** ja **20 julkaisulla** — mutta tämä todistusmäärä heijastaa insulin-aspartatin jo vakiintunutta standardihoidon roolia T1DM:ssä, ei aidon uuden käytön löytöä.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei annettu todistusaineistossa (`original_indications` on tyhjä) |
| Ennustettu uusi indikaatio | Tyypin 1 diabetes mellitus |
| TxGNN-ennustepistemäärä | 99,95% |
| Todisteiden taso | L1 |
| Suomen markkinoinnin asema | Ei markkinoitu |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Etene varauksilla |

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismin tietoa ei ole käytettävissä tässä todistusaineistossa. Tunnetun farmakologisen luokittelun perusteella insulin-aspartat on nopeasti vaikuttava uudelleenyhdistelmä-ihmisen insuliini-analogi, joka on suunniteltu nopeampaa subkutaanista imeytymistä varten kuin tavallinen ihmisen insuliini; sen rooli on endogeenisen insuliinin suora korvaaminen verensokerin hallintaan.

Kriittisesti todistusaineiston oma analyysi korostaa tärkeää varausta: Tyypin 1 diabetes mellitus ei todellakaan ole insulin-aspartatin *uusi* ennustettu indikaatio — se on lääkkeen todellinen, pitkäaikainen, opasmukainen indikaatio. Se, että `original_indications` on tyhjä ja `market_status` näyttää "Ei markkinoitu" Suomessa, näyttää heijastavan taustalla olevan sääntelytietokannan aukkoja pikemminkin kuin kliinistä todellisuutta, sillä insulin-aspartat-tuotteet (esim. NovoRapid/NovoLog, Fiasp) ovat laajalti käytössä T1DM:n verensokerin hallintaan kansainvälisesti.

Mekanistisesti T1DM johtuu pankreaan beetasolujen autoimmunista tuhoamisesta ja absoluuttisesta insuliinipuutteesta — eksogeeninen nopeasti vaikuttava insuliini on lopullinen korvaushoito. Tämä on syy siihen, että malli tuottaa niin korkean pistemäärän ja suuren määrän suoraan asiaan liittyviä tutkimuksia ja kirjallisuutta: TxGNN on pohjimmiltaan löytänyt uudelleen olemassa olevan, todistetun hoitosuhteen pikemminkin kuin identifioineet uusia terapeuttisia hypoteeseja.

## Kliinisten tutkimusten todisteet

| Tutkimuksen numero | Vaihe | Asema | Osallistujien määrä | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Vaihe 3 | Keskeytetty | 596 | Suora vertailu hengitettyä aterioinsuliinia vs. subkutaanista insulin-aspartattia (+ insulin detemir) T1DM:ssä 104 viikon ajan |
| [NCT02546401](https://clinicaltrials.gov/study/NCT02546401) | Vaihe 3 | Valmistunut | 22 | Testattiin aterian ennen/jälkeen insuliini-aspartatin bolus-ajoitusta insuliinipumpulla T1DM-potilailla |
| [NCT05413369](https://clinicaltrials.gov/study/NCT05413369) | Vaihe 3 | Valmistunut | 582 | Suuri monikeskuksinen tutkimus vertailemassa iGlarLixi:tä IDegAsp:iin (insuliini degludek/aspartat) oraalilääkkeillä riittämättömästi hallitussa diabeteksessa |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Vaihe 3 | Valmistunut | 26 | Dapagliflozin-lisä liraglutidiin ja insuliiniin T1DM:ssä; insuliini (ml. aspartat) taustahoidoksi |
| [NCT03800875](https://clinicaltrials.gov/study/NCT03800875) | Vaihe 2 | Valmistunut | 24 | Kaksoishormoni (insuliini-pramlintidi) suljetun silmukan toimitus ilman hiilihydraatin laskemista T1DM-aikuisilla |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Vaihe 3 | Valmistunut | 59 | HMR1964:n vs. insulin-aspartatin turvallisuusvertailu jatkuvan subkutaanisen insuliinin infuusion kautta T1DM:ssä |
| [NCT01513590](https://clinicaltrials.gov/study/NCT01513590) | Vaihe 3 | Valmistunut | 394 | 26 viikon tutkimus vertailemassa insuliini degludek/aspartattia (IDegAsp) vs. kaksivaiheista insuliini-aspartattia 30, molemmat metformiinin kanssa |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Vaihe 3 | Valmistunut | 347 | Insuliini detemir vs. NPH-insuliini, molemmat yhdistettynä aterioinsuliini-aspartaatin kanssa, lapsilla/nuorilla T1DM:n kanssa |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Vaihe 3 | Valmistunut | 470 | Insuliini detemir vs. NPH-insuliini yhdistettynä insuliini-aspartatin bolus-annostukseen raskailla naisilla T1DM:n kanssa |
| [NCT00082407](https://clinicaltrials.gov/study/NCT00082407) | Vaihe 3 | Valmistunut | 505 | Exenatidi vs. kahdesti päivässä annettava kaksivaiheinen insuliini-aspartat diabeteksessa sulfonyyluurean/metformiinin käyttäjillä |

*40 lisätutkimusta palautettiin, mutta niitä ei näytetä; useimmat käyttävät insulin-aspartattia taustahoidoksi/vertailuryhmänä laite- tai yhdistelmätutkimuksissa.*

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT (systemaattisen katsauksen perusteella) | Diabetes & Metabolism | Nopeasti vaikuttavan insuliini-aspartatin tehokkuus/turvallisuus vs. tavallinen ihmisen insuliini T1DM:ssä/T2DM:ssä |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT (Vaihe 3a) | Lancet | ONWARDS 6: kerran viikossa annettava insuliini icodec vs. kerran päivässä annettava degludek T1DM:n basal-bolus-skeemassa |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT-tutkimus: insuliini degludec vs. detemir, molemmat insuliini-aspartatin kanssa raskailla naisilla T1DM:n kanssa |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Katsaus | Lancet Diabetes & Endocrinology | T1DM:n hallinta raskauden aikana — elämäntapa, farmakologinen hoito, glykeemisen hallinnon tavoitteet |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Katsaus | JAMA | Tyypin 1 diabetes yleiskatsaus — autoimmuni beetasolujen tuhoaminen, epidemiologia, komplikaatiot |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Katsaus | Treatments in Endocrinology | Insulin-aspartaatin merkitys T1DM:ssä/T2DM:ssä — alempi HbA1c ja parantunut ateriajälkeinen hallinta vs. tavallinen insuliini |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Katsaus | Drugs | Insuliini-aspartatin käyttökatsaus T1DM:n/T2DM:n hallinnassa |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Katsaus | Expert Opinion on Pharmacotherapy | Kaksivaiheinen insuliini-aspartat 30 T1DM:n hoitoon |
| [35746893](https://pubmed.ncbi.nlm.nih.gov/35746893/) | 2023 | Meta-analyysi | Diabetes & Metabolism Journal | Nopeasti vaikuttava aspartat vs. aspartat insuliinipumpun kautta T1DM:ssä |
| [31345519](https://pubmed.ncbi.nlm.nih.gov/31345519/) | 2019 | Katsaus | Endocrinology and Metabolism Clinics of North America | Tyypin 1 diabetes raskauden aikana — glykeemisen hallinnon haasteet ja teknologian edistysaskeleet |

*10 lisäjulkaisua palautettiin, mutta niitä ei näytetä.*

## Suomen markkinatiedot

Insulin-aspartat näyttää tällä hetkellä olevan **ilman markkinointilupia** tässä todistusaineistossa (`market_status`: Ei markkinoitu, `total_licenses`: 0). Koska insulin-aspartatin laaja kliininen käyttö ja tutkimuspohja näytetään yllä, tämä todennäköisesti heijastaa aukkoa taustalla olevan sääntelytietokannan sijaan kuin todellista markkinapuutetta, ja se tulisi uudelleen tarkistaa Fimean virallisessa rekisterissa.

## Turvallisuusnäkökohdat

Lisätietoja turvallisuudesta on pakkausselosteessa.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Etene varauksilla**

**Perustelut:**
- Vaihe 3 tutkimusten ja kirjallisuuden todisteiden määrä (L1) vahvistaa insulin-aspartatin tehokkuuden T1DM:lle, mutta tämä johtuu siitä, että T1DM on jo sen vakiointunut indikaatio — ei aidon lääkkeen uudelleenkäytön löytö. Tämä kandidaatti tulisi käsitellä tiedon laadun korjauksena, ei uutena mahdollisuutena, ennen kuin mitään myöhempää toimintaa tehdään.
- Erikseen, kaksi muuta TxGNN-signaalia tälle lääkkeelle (lääkeindusoitu paikallinen lipodystrofia, keskipakoinen lipodystrofia) näyttävät olevan käänteisen kausaalisuuden — insuliini-injektio on tunnettu *syy* paikalliselle lipoodystrifialle, ei hoito sille — ja ne tulisi merkitä turvallisuusarvioinnin kohteiksi pikemminkin kuin lääkkeen uudelleenkäytön kandidaateiksi.

**Edetäkseen seuraava on tarpeen:**
- TFDA/Fimean pakkausseloste (varoitukset ja vasta-aiheet) — tällä hetkellä estävä tietoaukko (DG001)
- DrugBank:in toimittama vaikutusmekanismin vahvistus (DG002)
- `original_indications`- ja `market_status`-kenttien korjaus lähdetietokannassa vastaamaan insulin-aspartatin todellista hyväksyttyä indikaatiota ja markkinoinnin asemaa Suomessa
- Tämän kandidaatin uudelleenluokittelu putkessa "ennustettu uusi indikaatio":sta "olemassa oleva indikaatio — tietokannan aukko"

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

