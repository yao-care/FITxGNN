---
layout: default
title: Rimegepant
parent: Pelkkä mallin ennuste (L5)
nav_order: 325
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Rimegepantti: Migreenihoitojen indikaatiosta aivovartalon aura-migreenihoitoon

## Yhden lauseen tiivistelmä

Rimegepantti on pienimolekyylinen kalsitoniigeeni-sukulaispeptidi (CGRP) reseptorin antagonisti (gepantti-luokka), joka kehitettiin alun perin ja joka on hyväksytty migreenin akuuttiin hoitoon (auroilla tai ilman auroja) ja episodisen migreenin ehkäisyyn.
TxGNN-malli ennustaa sen voivan olla tehokas **aivovartalon aura-migreenin** hoidossa, migreenin alatyypissä, jossa tripitaanit ovat tyypillisesti kontraindisoituja,
sisältäen **0 omistettua kliinistä tutkimusta** mutta **14 tukevan julkaisun** rimegepantin yleisestä migreenihoitojen tehokkuudesta ja verisuoniston turvallisuusprofiilista.

## Pikakatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Migreeni (akuutti hoito ilman auroja tai auroilla; episodisen migreeni ehkäisy) — ei Suomen lisensointitiedoista, koska lääke ei ole tällä hetkellä markkinoilla siellä |
| Ennustettu uusi indikaatio | Aivovartalon aura-migreeni |
| TxGNN ennustuspistemäärä | 99.94% |
| Todistusvoimakkuus | L1 (perustuu kattavaan rimegepantin/migreenin todistusbääriin; ei tutkimuksiin, jotka olisivat erityisiä aivovartalon aura alatyypille) |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksilla |

## Miksi tämä ennuste on järkevä?

Rimegepantin yksityiskohtainen vaikutusmekanismi on tällä hetkellä merkitty tietovajeeksi tässä todistuspakkauksessa. Tukevan kirjallisuuden perusteella rimegepantti on erittäin selektiivinen, pienimolekyylinen kalsitoniigeeni-sukulaispeptidi (CGRP) reseptorin antagonisti — CGRP on migreeni patofysiologian keskeinen välittäjä, ja rimegepantti estää sen signaloinnin ilman tripitaaneissa nähtävää vasokonstriktiiivistä aktiivisuutta.

Aivovartalon aura-migreeni (aiemmin "basilaarityyppin migreeni") on migreenin alatyyppi, jossa tripitaaneja tyypillisesti vältetään tai joissa ne ovat kontraindisoituja, koska niiden vasokonstriktiiivinen mekanismi sisältää teoreettisen riskin vertebrobaasilaarisen verenkierron osalta. Koska rimegepantin mekanismi ei perustu vasokonstriktion — piste, jonka vahvistaa pituussuuntainen magneettiresonanssiangiografiaa (MRA) tutkimus (PMID 41574090), joka osoittaa, että se ei aiheuta aivoja koskevien tai aivon ulkoisten valtimoiden supistumista migreeni-iskujen aikana — on mekanistisesti uskottavaa, että rimegepanttia voitaisiin käyttää turvallisesti tässä alatyypissä, jossa tripitaanit eivät ole käyttökelpoisia.

Tämä tulisi ymmärtää indikaation tarkennusennusteena pikemmin kuin uutena terapeuttisena hypoteesina: rimegepantti on jo hyväksytty laajasti migreeniin, ja malli korostaa spesifistä, mekanistisesti hyvin tuettua alaryhmää (aivovartalon aura), joka hyötyisi ei-vasokonstriktiiivisen akuuttihoidon vaihtoehdosta. Yksikään tutkimus ei ole vielä suoraan ottanut tätä erityistä alaryhmää osallistujiksi tai raportoinut tuloksia aivovartalon aura-potilaille.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröitynä kliinisiä tutkimuksia, jotka koskisivat erityisesti aivovartalon aura-migreeniä.

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Katsaus/Sääntelytieto (ensimmäinen hyväksyntä) | Drugs | Vahvistaa rimegepantin ensimmäisen FDA:n hyväksynnän CGRP-reseptorin antagonistina akuutin migreenin hoitoon, tablettilääkkeella tutkitaan ehkäisyä ja refraktaarista trigeminaali hermosärkyä |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Vaiheen 3 avoin pitkäaikaisen turvallisuuden tutkimus | Cephalalgia | Pitkäaikainen turvallisuus, siedettävyys ja rimegepantin 75 mg ODT:n tehokkuus akuutin migreenin hoitoon kiinalaisilla aikuisilla |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | Satunnaistettu lumelääke-kontrolloitu tutkimus (vaiheen 1 PK/turvallisuus) | Clin Pharmacol Drug Dev | Vahvistaa rimegepantin 75 mg ODT:n yksittäisen ja toistetun annoksen farmakokinetiikan ja turvallisuuden terveillä kiinalaisilla aikuisilla |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Verkon meta-analyysi | J Headache Pain | Epäsuora vertailu lasmiditaanin, rimegepantin ja ubrogepantin akuutin migreenin hoidon vaikuttavuuden alkamisnopeudesta |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Vaiheen 4 avoin turvallisuustutkimus | J Headache Pain | 24 viikon tutkimus kerran päivässä annettavasta 75 mg rimegepantista episodisen migreenin ehkäisyyn osoittaa hyvää pitkäaikaisiedettävyyttä |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Pituussuuntainen magneettiresonanssiangiografia-tutkimus | Brain Communications | Tutkii suoraan rimegepantin vaikutusta aivoja koskeviin ja aivon ulkoisiin valtimoihin migreeni-iskujen aikana, tukien sitä ei-vasokonstriktiiivisena vaihtoehtona tripitaaneille — mekanistisesti merkityksellisimmät aivovartalon aura-hypoteesia |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospektiivinen kohortti | Headache | Arvioi rimegepantin off-label käytön siedettävyyttä ja tehokkuutta akuutin migreenin hoitoon nuorilla aikuisilla |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Katsaus | CNS Drugs | Kattava katsaus rimegepantista akuutin ja ehkäisevän migreenin hoidossa, huomioiden sen ylivoiman lumelääkkeeseen nähden vaiheen 3 tutkimuksissa |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Katsaus | Handbook of Clinical Neurology | Arvioi toisen sukupolven gepanttien (rimegepantti, ubrogepantti) farmakologiaa vertaisten ensimmäisen sukupolven hepatotoksisuushuoliin |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Katsaus | Pain Management | Arvioi rimegepantin roolia uusien akuutin migreenin hoitovaihtoehtojen (lasmiditaani, rimegepantti, ubrogepantti) joukossa |

## Turvallisuushuomioon ottamisen

Viitaa pakkausselosteeseen turvallisuustiedoista. TFDA/EMA:n erityisiä varoituksia, kontraindikaatioita ja lääke-lääke-yhteisvaikutusten tietoja ei ollut saatavilla tässä todistuspakkauksessa.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksilla**

**Perustelut:**
Mekanistinen perusteltu on vahva — rimegepantin ei-vasokonstriktiiivinen CGRP-reseptorin antagonismi osoittaa uskottavasti tripitaanien erityisen turvallisuusrajoituksen aivovartalon aura-migreenin osalta, ja tätä tukee laaja yleinen todistusbääri (14 julkaisua, sisältäen suorat verisuoniston vaikutusta koskevat tiedot). Kuitenkaan yksikään tutkimus ei ole vielä ottanut tätä erityistä alaryhmää osallistujiksi, eikä lääke ole vielä markkinoilla Suomessa, joten todellisen maailman sääntelyä ja turvallisuustietoja ei ole saatavilla.

**Jatkamiseksi seuraava on välttämätöntä:**
- TFDA/EMA pakkausseloste-tiedot varoituksista ja kontraindikaatioista (tällä hetkellä este-merkinnyn tietoväli — vaaditaan ennen mitään S1-turvallisuuden arviointia)
- Vahvistettu vaikutusmekanismi-dokumentaatio DrugBankista (tällä hetkellä tietoväli)
- Omistettu tutkimus tai alaryhmäanalyysi potilaissa, joilla on aivovartalon aura-migreeni, pikemmin kuin yleisen migreenin tutkimustietojen ekstrapolointiin perustuva
- Suomen/EU markkinoiden hyväksyntä ja rimegepantin lisensointistatus

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

