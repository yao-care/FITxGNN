---
layout: default
title: Pantoprazole
parent: Vahva näyttö (L1-L2)
nav_order: 284
evidence_level: L1
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **6** kpl
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

# Pantoprazoli: dokumentoimattomasta alkuperäisestä indikaatiosta aktiiviseen peptiseen haavaan

## Yhden lauseen yhteenveto

Pantoprazoli on protonienpumppuinhibiittori (PPI); sen virallisesti rekisteröity alkuperäinen indikaatio puuttuu tästä näytöstä (`original_indications` on tyhjä ja `original_moa` on merkitty tietovajeeksi). TxGNN:n paras ennuste on **aktiivinen peptinen haava** (pistemäärä **99,69%**), jota tukee **3 kliinistä tutkimusta** ja **20 julkaisua** — mutta näytön oman analyysin mukaan tämä johtuu todennäköisesti puuttuvan alkuperäisen indikaation tiedon aiheuttamasta virheestä, ei todellisesta uudesta käyttötarkoituksesta, sillä peptinen haava on jo vakiintunut ja PPI:lle merkittyyn indikaatioon kuuluva käyttötarkoitus.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei tietueissa (0 Suomen lupaa); PPI-luokan lääkkeet ovat yleensä indikoituja refluksitaudissa/eroosiivisessa ruokatorvtulehduksessa ja peptisessä haavassa |
| Ennustettu uusi indikaatio | Aktiivinen peptinen haava |
| TxGNN-ennusteen pistemäärä | 99,69% |
| Näyttöaste | L1 |
| Suomen markkinatila | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Jatka varauksilla |

---

## Miksi tämä ennuste on perusteltu?

`original_moa` on tässä näytössa nimenomaisesti merkitty tietovajeeksi (DG002, vakavuusaste: Korkea). Kuitenkin tälle ehdokkaalle liitetty uudelleentarkoitusperustelu sisältää mekanistisia yksityiskohtia: Pantoprazoli on protonienpumppuinhibiittori, joka sitoutuu peruuttamattomasti ja spesifisesti mahassa olevan paretallisolun H+/K+-ATPaasiin, estäen gastrin hapon eritytykseen liittyvän viimeisen yhteisen vaiheen — vakiintuneen ensimmäisen linjan mekanismin happopeptisairauksien paranemiseksi.

Aktiivinen peptinen haava sijaitsee suoraan tämän ydinpharmakoloogisen vaikutuksen alueella. On tärkeää huomata, että näytön oma analyysi merkitsee tätä spesifistä ennustetta todennäköisesti **ei**-aidoksi uuden uudelleentarkoitussignaaliksi: koska taustalla olevan tietokannan `drug.original_indications` on tyhjä, TxGNN näyttää "löytävän uudelleen" käyttötarkoituksen, joka on jo pantoprazolille merkittyyn indikaatioon kuuluva, sen sijaan että paljastaisi uutta terapeuttista aluetta. Erittäin korkea pistemäärä (99,69%) on yhdenmukainen tämän kanssa — se näyttää enemmän tietojen täydellisyyden ongelmalta kuin todelliselta uudelleentarkoitusintuitiolta.

Sama huomautus pätee myös tämän näytön kuudennelle ehdokkaalle ("kaksitostasormisuolen haava", myös L1), joilla on identtinen mekanistinen peustelu. Loput tämän pakkauksen ehdokkaat (gastrojejunaalinen haava, peptisen haavan perforaatio, duodenogastrinen refluksi, kaksitostasormisuolen obstruksio) kantavat asteittain heikompeneita ja epäsuorempia mekanistisia yhteyksiä (L2–L5), ja ovat todenmukaisempia ehdokkaita todellisen sijainnispesifisen tai lisäyhdistelmähoidon tutkimiselle. Ennen kuin käsitellään mitään näistä kuudesta ennusteesta todellisena "uutena" indikaationa, taustalla oleva `drug.original_indications` -kenttä tulisi täyttää, jotta TxGNN-pistemäärät voidaan oikein tulkita suhteessa tarkkoihin alkuperäisiin arvoihin.

---

## Kliinisen tutkimuksen näyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujamäärä | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Vaihe 3 | Valmistunut | 323 | Monitapauksinen satunnaistettu kaksisokkoutettu aktiivista kontrollia käyttävä tutkimus, jossa verrattiin ilaprasoolia ja pantoprasoolia sisältävää kolmoishoitoa (7 päivää) H. pylori -eliminaatiossa mahan ja kaksitostasuolen haavapotilailla — suora tehokkuustieto (merkitsevyysaste A). |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Vaihe 4 | Valmistunut | 320 | Arvioi PPI:n ja statiinien vaikutusta klopidogreeliin liittyvään verihiutaleiden estoon PCI-potilailla, joilla käytetään kaksoisantiplatelet-hoitoa — lääkkeiden vuorovaikutustutkimus, ei haavan paranemisen päätetulosmuuttuja (merkitsevyysaste B). |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Valmistunut | 316 | Selvitti riskitekijöitä, jotka ennustavat huonoa vastetta tai varhaisen uusiintumisen verenvuodossa endoskooppisen hemostaasin ja korkean annoksen PPI:n jälkeen peptisessä haavaverenvuodossa, ohjaamaan valintaa uusintaendoskopiaa varten — kliinisen prosessin tutkimus, vain epäsuorasti liittyvä pantoprazolin tehokkuuteen (merkitsevyysaste C). |

---

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Aikakauslehti | Keskeiset löydökset |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospektiivinen satunnaistettu tutkimus, jossa verrattiin pantoprazolin jatkuvaa ja jaksoittaista infuusiota peptisen haavaverenvuodon uusiintumisen ehkäisyssä endoskooppisen hoidon jälkeen. |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | Journal of Gastroenterology and Hepatology | Prospektiivinen RCT: pantoprazolin infuusio endoskooppisen hoidon lisähoidoksi vähentää uusiintumista peptisen haavaverenvuodossa. |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Alimentary Pharmacology & Therapeutics | Vertaili kolmea pantoprasoolia sisältävää kolmoishoitoskeemaa H. pylori -elinaineiston ja mahan haavan paranemisessa. |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Vertaileva kliininen tutkimus | Hepato-gastroenterology | Vertaili lansoprasoolia ja pantoprasoolia aktiivisen kaksitostasuolen haavan ja H. pylori -elinaineiston hoidossa. |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | RCT | Alimentary Pharmacology & Therapeutics | Kahden viikon pantoprazolihoidon yhdistelmä yksiviikoisen amoksisiiliini/klaritromysiini-hoidon kanssa oli tehokas H. pylori -elinaineistoon ja kaksitostasuolen haavan paranemiseen. |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Monitapauksinen satunnaistettu aktiivisen kontrollin tutkimus tegoprazoista (P-CAB) verrattuna PPI-luokan vertailuaineeseen keinotekoisen endoskooppisen resektion aiheuttaman haavan paranemisessa. |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Kliininen tutkimus | Medical Archives (Sarajevo) | Arvioi PPI:n tehokkuutta endoskooppisen hemostaasin jälkeen verenvuotavassa peptisessä haavassa, mukaan lukien H. pylori -infektioon liittyvä rooli. |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Katsaus | Clinical Drug Investigation | Yleiskatsaus pantoprazolin farmakologiaan: peruuttamaton H+/K+-ATPaasin inhibiitio; todetaan, että kliinisesti merkittäviä lääkkeiden välisiä vuorovaikutuksia ei ole havaittu. |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Katsaus | Pharmacotherapy | Tarkastelee PPI-mekanismia (H+/K+-ATPaasin inhibiitio) ja sen ylivertaisuutta H2-reseptoriantagonisteille magnan hapon eritytyksessä. |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systemaattinen katsaus / Verkko-metaanalyysi | American Journal of Gastroenterology | Vertailee P-CAB:n ja PPI:n tehokkuutta ja turvallisuutta vaikean (Los Angelesin luokka C/D) refluksiesofagiitin paranemisessa. |

---

## Suomen markkinatiedot

Pantoprazoli **ei ole tällä hetkellä markkinoilla Suomessa** (`market_status: Not marketed`, 0 lupaa tietueissa). Tässä näytössa ei ole saatavilla tuotteen lupaa, annosmuotoa tai hyväksytyn indikaation tietoja.

---

## Turvallisuuden huomioitavat asiat

Katso turvallisuustiedot pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Jatka varauksilla**

**Perustelut:**
Pantoprazolin mekaaninen ja kliinisen tutkimuksen näyttö aktiivisesta peptisestä haavasta on vahva (L1, sisältäen suoran vaiheen 3 RCT:n ja useita tukevia RCT:tä haavan paranemisesta/verenvuodon uusiintumisen ehkäisystä), mutta näytön itse merkitsee tätä ennustetta todennäköisesti heijastavan puutteen alkuperäisen indikaation lähtötiedon sijaan kuin todellisen uuden uudelleentarkoitussignaalin — joten sitä tulisi käsitellä tietojen laadun havaintona ensin ja uudelleentarkoituskandidaattina toiseksi, kunnes lähtötiedot on korjattu.

**Jatkamista varten tarvitaan seuraavat tiedot:**
- TFDA:n pakkausseloste (varoitukset/vasta-aiheet) — tällä hetkellä **estävä** tietovahe (DG001); vaaditaan ennen mitään S1-turvallisuusseulontaa
- DrugBank-peräinen vaikutusmekanismi (MOA) — tällä hetkellä **korkea**-vakavuuden tietovahe (DG002)
- `drug.original_indications` -kentän täyttö, jotta tämän ja muiden viiden tämän näytön ehdokkaan (gastrojejunaalinen haava, peptisen haavan perforaatio, duodenogastrinen refluksi, kaksitostasormisuolen obstruksio, kaksitostasormisuolen haava) TxGNN-pistemäärät voidaan oikein erottaa merkityn uudelleenoppimisen virheistä
- Suomen/Taiwanin sääntelyä ja lupaa koskevat tiedot, koska lääkettä ei ole tällä hetkellä markkinoilla (0 lupaa)
- Lääkkeiden väliset vuorovaikutukset (DDI) — nykyinen kyselystatus on "not_found"

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

