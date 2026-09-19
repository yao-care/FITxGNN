---
layout: default
title: Golimumab
parent: Kohtalainen näyttö (L3-L4)
nav_order: 180
evidence_level: L4
indication_count: 5
---

# Golimumab
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **5** kpl
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

# Golimumab: TNF-α-inhibitiosta tulehduksellisista niveltaudeista Reumatasolujen vaskaliitiin

## Yhteenveto yhdellä lauseella

Golimumab (DrugBank DB06674) on täysin ihmisen peräisin oleva anti-TNF-α-monoklonaalinen vasta-aine, jonka kirjallisuustiedot osoittavat alkuperäiseksi hyväksytyksi käyttöindikaatioksi olevan reumatoidi nivelrikko (RA), psoriaasisen nivelrikon (PsA) ja ankylosoiva spondyliitti (AS) sekä muut tulehdukselliset niveltaudit; Taiwan-virallinen käyttöindikaatio kokonaisuudessaan puuttuu koska lääkettä ei ole markkinoilla. TxGNN-malli ennustaa sen mahdollisen tehokkuuden **Reumatasolujen vaskaliitiin (Rheumatoid Vasculitis)**, mitä tukee tällä hetkellä vain **3 kliinistä tutkimusta** ja **6 julkaisua**, ja todistusasteikko on heikko (L4), kirjallisuudessa esiintyy samanaikaisesti anti-TNF:n aiheuttaman vaskaliitin ristiriitaisia turvallisuussignaaleja.

> Lisätieto: Tässä Evidence Packissa TxGNN ennustaa yhteensä 5 käyttöindikaatiota, joista sijoitus 3 (inflammatory spondylopathy) ja 5 (polyarticular juvenile rheumatoid arthritis) saavuttavat L1-todistusasteen, mutta nämä ovat olennaisesti golimumabista jo hyväksyttyjen käyttöindikaatioiden laajennuksia eikä varsinaista vanhaa lääkettä uudessa käytössä; sijoitukset 2 ja 4 (häntäluun yliaktiivisuus, Kummel-tauti) puuttuvat minkä tahansa mekanismin tai kliinisen todisteen, määritelty mallin tasoiseksi vääräksi positiiviseksi. Raportti noudattaa muotoiluvaatimuksia ja keskittyy sijoitukseen 1 ennustetuista tuloksista.

## Pika-arvio

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen käyttöindikaatio | Tietovajaus (Taiwan ei markkinoi, virallista käyttöindikaatiota ei ole käytettävissä; kirjallisuuden mukaan golimumab on jo hyväksytty RA:lle, PsA:lle, AS:lle) |
| Ennustettu uusi käyttöindikaatio | Rheumatoid Vasculitis |
| TxGNN ennustepistemäärä | 99,73 % (rank 3425) |
| Todistusaste | L4 |
| Taiwan-markkinatilanne | ✗ Ei markkinoilla |
| Lupakirjojen määrä | 0 |
| Suositeltu päätös | Hold |

## Miksi tämä ennuste on kohtuullinen?

Tällä hetkellä puuttuu yksityiskohtainen toimintamekanismi (MOA) -tieto. Olemassa olevien tietojen perusteella golimumab kuuluu anti-TNF-α täysin ihmisen peräisin olevien monoklonaalisten vasta-aineiden luokkaan, jonka tehokkuus RA:ssa, PsA:ssa, AS:ssa ja muissa tulehduksellisissa niveltaudeissa on jo todistettu, ja mekanistisesti sen käyttö voisi teoriassa laajentua reumatoidin vaskuliittin hoitoon.

Reumatasoinen vaskaliitti on RA:n vakava extraartikulaarinen komplikaatio, joka esiintyy erityisesti seerumin positiivisilla (RF/anti-CCP-positiivisilla) potilailla, ja patologinen mekanismi sisältää TNF-α välittämää vaskulaarisen seinämän tulehdusta ja immuunimompleksien sedimentaatiota. Koska golimumab estää TNF-α-signalointia ja on jo todistettu vähentävän RA:n nivelten rikkoutumista (PMID 31491879, 36 RCT:n verkkoyhteenveto), TNF-α:n estäminen voisi teoriassa myös hidastaa vaskulaarisen seinämän tulehdusta, mikä on mekanistisen laajenemisen kohtuullinen perusta.

Todistus ei kuitenkaan ole yksipuolisen tukevin: kirjallisuus dokumentoi samalla anti-TNF-hoidon ja uusien tai pahentuneiden vaskuliittien välisiä ristiriitaisia signaaleja, esimerkiksi Takayasun arteriitin tapauksia anti-TNF-hoidon aikana (PMID 22999907), sekä golimumab-hoidon aikana kehittyneitä vakavia infektiivisen artriitin tapauksia (PMID 29075910). Nämä ristiriitaiset signaalit liittyvät tunnettuun anti-TNF-aiheuttamaan vaskuliittiin liittyvään turvallisuuskysymykseen, mikä tekee mekanistisen yhteyden suunnasta epäselvää, eikä tällä hetkellä ole reumatoidivaskuliitin tälle taudeille erityisesti suunniteltuja interventiotutkimuksia.

## Kliiniset tutkimukset

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Pääasiallinen havainto |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Rekrytointia ei ole vielä aloitettu | 80 | Arvioidaan reumaatikoiden olkapäännivelleikkauksen edeltävien immunosuppressiivisten lääkkeiden (mukaan lukien TNF-estäjät) lopettamisen aikaista palauttamisen vaikutusta taudin uusiutumiseen, kivuun ja haavakomplikaatioihin; ei ole vaskuliitin-spesifinen tehokkuustutkimus |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Valmis | 184 | Monikansallinen ei-interventio tutkimus, arvioitava Tocilizumab:n käyttäminen RA-potilailla (joilla on huono reaktio DMARD:iin tai yhteen biologiseen lääkkeeseen) kliinisen käytännön malli, tehokkuus ja turvallisuus; kohderyhmä on RA kokonaisuudessaan eikä vaskuliitin-spesifinen |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Tila epäselvä | 750 000 | Suuri tietokantaosio tutkimus arvioi biologisten ja immunosuppressiivisten lääkkeiden hoidon jälkeiset muiden immuuni-välittämien tulehduksellisten sairauksien (IMID) riski, sisältää vaskuliitin kaltaiset turvallisuussignaalit, on havainnoiva tutkimus, ei tehokkuustutkimus |

## Kirjallisuustodisteet

| PMID | Vuosi | Tyyppi | Lehti | Pääasiallinen havainto |
|------|------|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | RCT/Cohort | International Journal of Molecular Sciences | 36 RCT:n verkkoyhteenveto, verrataan 5 TNF-estäjää (mukaan lukien golimumab) niiden vaikutukseen RA:n nivelten rikkoutumisen estämiseen, vahvistaa sen anti-inflammatorisen tehokkuuden perustan |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Katsaus reumasairauksien biologisten lääkkeiden hoidon nykytilanteeseen ja rajoituksiin, sisältää TNF-estäjä-luokan lääkkeiden yleisen tehokkuuden ja turvallisuuden kehyksen |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Seminars in Arthritis and Rheumatism | Tutkii RA-potilaiden terminaalisen munuaisen sairauden (ESRD) esiintymistä, etiologiaa ja hoitoa |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatology International | RA-potilaan, jolle annettiin golimumab-hoitoa, kehittämä gangreenous pyoderma ja purulent arthritis, jotka johtivat vakavaan sepsikseen |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | 2 tapausta Takayasun arteriitin kehittymisestä anti-TNF-hoidon aikana, mikä viittaa anti-TNF aiheuttaman vaskuliitin ristiriitaisiin turvallisuussignaaleihin |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocular Immunology and Inflammation | Golimumab onnistuu hoitamaan Behçet-taudin liittyviä uveiiteja koskevassa tapausraportissa |

## Taiwan markkinatiedot

Tällä hetkellä ei ole lupakirjarekistereitä — golimumab ei ole markkinoilla Taiwanissa (lupakirjojen kokonaismäärä: 0).

## Turvallisuushuomiot

Tutustu pakkausselosteisiin varoituksiin ja varotoimiin. (key_warnings, contraindications, DDI kyselyt eivät ole saatavilla; TFDA pakkausseloste alkuperäisteksti on vielä analysoitava, merkitty DG001 estoavaksi tietovajeeksi.)

## Johtopäätös ja seuraavat suositukset

**Päätös: Hold**

**Perustelu:**
Reumatoidin vaskuliitti näillä näkymin saavuttaa vain L4-todistusasteen (mekanismi/prekliiniset päätelmät tasolla), vailla taudin spesifistä interventiotutkimusta, ja kirjallisuudessa esiintyy anti-TNF aiheuttaman vaskuliitin ristiriitaisia turvallisuussignaaleja, mekanistisen yhteyden suunta on epäselvä, ei riittävä seuraavan vaiheen arviointiinsiirtymiselle.

**Jatkaaksesi sinun on täydennettävä:**
- TFDA pakkausselosteen varoitukset ja kielto kokonaisuudessaan (DG001, estoava aukko, vaikuttaa S1 turvallisuuden alkuarviointiin)
- Golimumab yksityiskohtaiset toimintamekanismi tiedot (DG002, rajoittaa mekanismi-linkki-analyysia)
- Reumatoidin vaskuliitin taudin spesifinen interventiotutkimuksen suunnittelu ja tulokset
- Anti-TNF aiheuttaman vaskuliitin riskien järjestelmällinen turvallisuusarviointi, selvittää mekanistisen suunnan ristiriitaiset signaalit

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

