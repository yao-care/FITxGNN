---
layout: default
title: Alirocumab
parent: Vahva näyttö (L1-L2)
nav_order: 23
evidence_level: L1
indication_count: 10
---

# Alirocumab
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

# Alirokumabi: Hyperkolesterolemiaasta kolesterolin kataboliseen prosessin sairauteen

## Yhden lauseen yhteenveto

Alirokumabi on PCSK9-inhibiittori monoklonaalinen vasta-aine, jota alun perin käytetään LDL-kolesteriinin alentamiseen ja sydän- ja verisuonisairauksien riskin vähentämiseen hyperkolesterolemian potilailla. TxGNN-malli ennustaa, että se saattaa olla tehokas myös **Cholesterol Catabolic Process Disease** -sairaudelle (kategoria, joka sisältää homozygottisen familiarisen hyperkolesterolemian, HoFH), ja sille on saatavilla **1 valmistunut Phase 3 -suhteinen kliininen tutkimus** sekä **19 julkaisua**, jotka tukevat tätä suuntaa. Tämä kandidaatti on pohjimmiltaan alirokumabbin ydinmekanismin jatke eikä mekanistinen harppaus, mikä näkyy sen poikkeuksellisen vahvasta näyttöpohjasta verrattuna lääkkeen muihin ennustettuihin indikaatioihin.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Hyperkolesterolemia / sydän- ja verisuonisairauksien riskin vähentäminen (PCSK9:n esto) — *virallisen hyväksynnän teksti ei ole saatavilla; katso tietoaukko-huomio alla* |
| Ennustettu uusi indikaatio | Cholesterol Catabolic Process Disease (sisältää homozygottisen familiarisen hyperkolesterolemian) |
| TxGNN-ennusteen pistemäärä | 99.36% |
| Näytön taso | L1 |
| Suomen markkina-asema | ✗ Ei markkinoilla |
| Lupamääräysten lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksilla |

---

## Miksi tämä ennuste on perusteltu?

Virallinen DrugBank vaikutusmekanismi -teksti on tällä hetkellä tietoaukko tälle tietueelle. Tässä paketissa kerätyn kirjallisuuden näytön perusteella alirokumabi on ihmisen monoklonaalinen vasta-aine, joka sitoutuu verenkierron PCSK9:ään (proproteinaasi konvertaasi subtilisiiniksi/keksinimuotoiseksi tyypiksi 9) ja estää sen sitoutumisen maksaan LDLR:ään (LDL-reseptori). Estämällä PCSK9:n välittämää LDLR:n hajoamista enemmän LDLR:ää kierrätetään hepatosyytin pinnalle, mikä lisää veresta LDL-kolesteriinin selvittämistä (PMID 39947256, 38185721).

Ennustettu uusi indikaatio, "kolesterolin katabolisen prosessin sairaus", ei ole kaukaa haettu tai spekulatiivinen kohde — se kuvaa kolesteriinin käsittelyn ja selvittämisen häiriöitä, mukaan lukien homozygottinen familiaarinen hyperkolesterolemia (HoFH), sairaus, jota määrittelee vaikeasti heikentynyt LDLR:n toiminta. Koska alirokumabbin koko farmakologia perustuu LDLR:n välittämän selvittämisen parantamiseen, tämä indikaatio sijaitsee suoraan mekanismilla eikä vaadi uutta biologista hypoteesia. Tämä on johdonmukainen sen kanssa, miksi näytön taso täällä (L1) on paljon vahvempi kuin lääkkeen muille TxGNN-ennustetuille indikaatioille (esim. ihtyyoosi, ksantomatoosi tai diafyysinen dyspasia), jotka sisältävät mekanistisesti liittymättömiä tai epäsuoria graafisen yhteyden.

Tämä tukee, että kirjallisuusperusta sisältää sekä dedikoidut HoFH-hoito-arviot (PMID 39751968) että suuret, pitkäaikaiset turvallisuustiedot ODYSSEY OUTCOMES -ohjelmasta (47,296 potilaan-vuotta, PMID 38658193), mikä osoittaa, että lääke-sairaus -suhde on jo hyvin karakterisoitu todellisen maailman ja kontrolloiduissa asetuksissa, vaikka sitä ei ole arvioitu täällä de novo "uuden indikaation" tutkimuksena.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Rekrytointi | Keskeisiä löydöksiä |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Valmistunut | 118 | EPIC-HIV -tutkimus: arvioi PCSK9:n estotyön vaikutusta sydän- ja verisuonisairauksien riskiin ja aterosklerootiseen plaakkiin HIV-positiivisilla dyslipideemiapotilailla; testaa suoraan PCSK9:n estotyön vaikutusta kolesteriinin metaboliaan liittyviin kardiovaskularisiin tuloksiin. |

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeisiä löydöksiä |
|------|-----|------|------|---------|
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Katsaus | Current Atherosclerosis Reports | Tarkastelee uusia farmakologisia hoitoja, mukaan lukien PCSK9-inhibiittorit, homozygottiseen familiariseen hyperkolesterolemiaan (HoFH). |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Katsaus (RCT-synteesi) | Kardiologia Polska | Syntetisoi näyttöä PCSK9-inhibiittorien vaikutuksesta lipidiparametreihin ja kardiovaskulaaristen tapahtumien vähentämiseen. |
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Turvallisuus/Observaatiotutkimus | European Heart Journal - Cardiovascular Pharmacotherapy | Alirokumabbin turvallisuusanalyysi ODYSSEY OUTCOMES -ohjelmasta, kattaen 47,296 potilaan-vuotta havainnointia. |
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | Post hoc RCT-analyysi | Diabetes Care | ODYSSEY OUTCOMES post hoc -analyysi alirokumabbin vaikutuksesta lipoproteini(a):lle, LDL-C:lle ja diabeteksen riskille. |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Katsaus | Signal Transduction and Targeted Therapy | Kattava katsaus PCSK9-biologiasta ja sen terapeuttisesta kohdentamisesta lipidi- ja ei-lipidisairauksissa. |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Katsaus | Current Opinion in Lipidology | Päivitys PCSK9:n suhteen kohdennetuista terapioista ja niiden erilaisista vaikutusmekanismeista. |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Katsaus | Medicina (Kaunas) | Tarkastelee familiarisen hyperkolesterolemian diagnostiikkaa ja hoitoa, mukaan lukien PCSK9:n kohdentavat vaihtoehdot. |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | Katsaus | Pharmacotherapy | Tämänhetkinen katsaus nykyisistä ja nousevista PCSK9:n suhteen kohdennetuista terapioista sydän- ja verisuonisairauksien riskin vähentämiseksi. |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Katsaus (mekanismi) | Pharmacology & Therapeutics | Vertaa solunsisäisen vs. solunulkoisen PCSK9:n kohdentamisstrategioita, käsittelee alirokumabbia erityisesti. |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Katsaus | International Journal of Molecular Sciences | Tarkastelee nykyisiä dyslipideemian hoitomenetelmiä, mukaan lukien PCSK9-esto. |

---

## Suomen markkina-informaatio

Tällä hetkellä alirokumabille ei ole saatavilla myyntilupaa koskevaa tietoa Suomessa (markkina-asema: **Ei markkinoilla**, tiedostossa on 0 valtuutusta).

---

## Turvallisuusnäkökohdat

Turvallisuustietoja saatavilla pakkausselosteesta. Tälle tietueelle ei ole tällä hetkellä saatavilla jäsenneltyjä varoituksia, vasta-aiheita tai lääkkeen yhteisvaikutustietoja — erityisesti virallista TFDA/Fimea-pakkausselostetta (varoitukset ja vasta-aiheet) ei ole vielä haettu, mikä on merkitty Estäviksi tietoaukoksi ja estää tätä ehdokasta saattamasta loppuun lääkintöturvallisuuden esiarviointia (S1) lääkkeen tasolla.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksilla**

**Perustelut:**
Ennustettu indikaatio on mekanistisesti hyvin sopusoinnussa alirokumabbin vakiintuneen farmakologian kanssa (PCSK9:n esto → LDLR:n välittämä kolesteriinin selvittäminen), ja sitä tukevat valmistunut Phase 3 -suhteinen tutkimus sekä merkittävä kirjallisuusperusta, mukaan lukien pitkäaikaiset turvallisuustiedot ODYSSEY OUTCOMES -ohjelmasta. Lääkkeen turvallisuusarvio jää kuitenkin estoon puuttuvan virallisen pakkausselosteen vuoksi, joten varauksilla on oltava ennen jatkotoimia.

**Edistymiseksi tarvitaan seuraavaa:**
- Hae virallinen TFDA/Fimea-pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä tietoaukko (DG001)
- Hanki virallinen DrugBank vaikutusmekanismi -dokumentaatio korvaamaan nykyisen tietoaukon (DG002)
- Selvitä, vastaako "kolesterolin katabolisen prosessin sairaus" TxGNN:n arvioimana todella uutta indikaatiota vai päällekkäin merkittävästi alirokumabbin nykyisen hyväksynnän kanssa HoFH/hyperkolesterolemialle
- Vahvista antoreitin yhteensopivuus kohdeväestölle (tällä hetkellä merkitty "vireillä")
- Huomio: muut tämän lääkkeen TxGNN-ennustamat indikaatiot (esim. ksantomatoosi, ihtyyoosi, diafyysinen dyspasia) sisältävät vain L4–L5 -näyttöä ja jäävät **Odotukseen** vahvemman mekanistisen tai kliinisen tuen odotuksella; ne eivät ole osa tätä suositusta.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

