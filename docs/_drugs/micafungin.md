---
layout: default
title: Micafungin
parent: Pelkkä mallin ennuste (L5)
nav_order: 249
evidence_level: L5
indication_count: 1
---

# Micafungin
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

# Micafungin: invasiivisesta kandidiasista virtsatietulehdukseen

## Yhden lauseen yhteenveto

> Micafungin on echinokandiini-antimykootinen lääke, joka on vahvistettu invasiiviseen kandidiasiin ja kandidemiaan. TxGNN-malli ennustaa, että se saattaa olla tehokas **virtsatieinfektioille (Candida UTI/kandiduria)**, ja saatavilla on **0 kliinistä tutkimusta** mutta **13 tukevaa julkaisua** — pääasiassa potilastapauksia ja pieniä tapaussarjoja.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Invasiivinen kandidiaasi / kandidemia (echinokandiini-antimykootinen; ei sisälly tämän todistuspaketin lisenssitietoihin) |
| Ennustettu uusi indikaatio | Virtsatieinfektio (Candida UTI) |
| TxGNN-ennustepisteet | 99.03% |
| Todisteiden tasо | L3 (havainnollinen/retrospektiivinen kohortti + tapaussarjat, ei RCT:itä) |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odota |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä tarkemmat vaikutusmekanismin tiedot eivät ole saatavilla tässä todistuspaketissa (tietovaje). Yleisen farmakologisen tiedon perusteella micafungin kuuluu **echinokandiini**-antimykootisten aineiden luokkaan, joka estää 1,3-β-D-glukaanisyntaasia ja häiritsee sienisolukalvon synteesin. Se on fungisidinen useimmilla *Candida*-lajeilla, mukaan lukien asoli-resistentit kannat, ja sen teho invasiivisessa kandidiasissa/kandidemiassa on hyvin vakiintunut.

Ennustettu uusi indikaatio — Candida-virtsatieinfektio (kandiduria) — on mekanistisesti perusteltu, koska aiheuttavat mikroorganismit ovat suurelta osin samat kuin micafunginin vakiintuneella lääkitysalueella (*C. albicans*, *C. glabrata*, *C. krusei*, *C. auris*). Echinokandiineja on kuitenkin historiallisesti pidetty huonona soveltuvina virtsatieinfektioihin **matalan virtsainerityksen** vuoksi — suurin osa lääkkeestä metaboloituu maksassa hyvin vähäisellä muuttumattomalla munuaisiin erityksellä. Kirjallisuuden todistustepo koostuu pääosin potilastapausista, jotka osoittavat, että mitattavia virtsalääkkeen tasoja ja kliinistä eradikointia *voi* silti tapahtua, erityisesti silloin, kun vakiohoitovaihtoehdot (flukonatsoli, amfoteritiini B) ovat kontraindisoituja tai organismi on resistentti.

Koska tämä uudelleenkäyttöhypoteesi vastustaa tavanomaista PK-opetusta, tukeva todistustepo on tärkeä mutta tällä hetkellä rajoittuu todellisen maailman potilaskokemukseen kontrolloitujen tutkimusten sijaan — tämä heikentää luottamusta huolimatta erittäin korkeasta TxGNN-pisteestä.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeiset löydökset |
|------|-----|------|------|---------|
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospektiivinen kohortti | Int Urol Nephrol | Tutki kandidurian eliminaatioasteita sairaalahoitopotilaissa, joille annettiin micafungiinia |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Tapaussarja | Med Mycol Case Rep | 5 potilasta sai parenteraalista micafungiinia ≥6 päivää; sienierradikointia kaikkien tapausten osalta 30 päivän sisällä |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Tapaussarja | Int J Antimicrob Agents | 6 virtsatieinfektiotapausta (4 flukonatsoli-resistenttiä) hoitettiin onnistuneesti; virtsalääkkeiden seuranta auttoi annoksen määrittelyä |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Tapaussarja | Pediatr Int | Kriittisesti sairaiden PICU-potilaiden, joille annettiin micafungiinia sairaalainfektio-Candida UTI:n vuoksi, tulokset |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Potilastapaus | Front Pediatr | Micafungiinia käytettiin *C. glabrata* virtsatieinfektio hoitoon ennenaikaisesti syntyneellä vastasyntyneellä |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Potilastapaus + kirjallisuuskatsaus | Transpl Infect Dis | Lisäännetyn annoksen micafungin poisti krooniset *C. krusei* UTI maksaan/munuaisen siirron saaneen potilaan osalta |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Potilastapaus | J Pharm Health Care Sci | *C. glabrata* pyelonefriitti/bakteeremia SGLT2-estäjä potilaalla hoidettiin onnistuneesti micafungilla |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Potilastapaus | Med Mycol Case Rep | Yksipuoleinen munuaisiin muodostunut sienipallo (*C. glabrata*, micafungin-herkkä) hoidettiin antimykootisella hoitolla + endoskooppisella poistolla |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Potilastapaus | Cureus | *Candida auris* UTI monisairaalla hoitokodissa olevalla potilaalla |
| [40405904](https://pubmed.ncbi.nlm.nih.gov/40405904/) | 2025 | Potilastapaus | Cureus | Urosepsis *C. glabrata* nefroliittisyydestä immuunikompetentilla potilaalla |

---

## Suomen markkinatiedot

Micafungin ei tällä hetkellä ole markkinoilla Suomessa — tässä todistuspaketissa ei ole käytettävissä hyväksyntätietoja (0 lisenssiä).

---

## Turvallisuusnäkökulmat

Turvallisuustiedot löytyvät pakkausselosteesta. Keskeiset varoitukset, vasta-aiheet ja lääkkeiden väliset yhteisvaikutustiedot eivät olleet saatavilla tässä todistuspaketissa (kyselyiden tila: ei löytynyt).

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Ennuste on tuettu vain potilastapausilla ja yhdellä retrospektiivisellä kohorttitutkimuksella (L3), eikä kliinisiä tutkimuksia, jotka arvioisivat micafungiinia virtsatieinfektiolle. Kriittisemmäksi asiaksi turvallisuustiedot (TFDA/Fimea-pakkausseloste varoitukset ja vasta-aiheet) on merkitty **blokkaajaksi** tietovajeeksi, joka yksinään estää sisäänpääsyn S1-turvallisuuden ennakkoarviointivaiheeseen riippumatta tehokkuustodisteiden vahvuudesta.

**Jatkamiseksi tarvitaan seuraavaa:**
- TFDA/Fimea-pakkausseloste tiedot (varoitukset, vasta-aiheet) — blokkaa väli, vaaditaan ennen S1-turvallisuusarviointia
- Vahvistettu vaikutusmekanismi ja alkuperäinen hyväksytty indikaatio (tällä hetkellä tietovaje)
- Lääkkeiden väliset yhteisvaikutukset (DDI) profiili
- Prospektiiviset tai kontrolloidut tutkimukset, joissa erityisesti arvioidaan micafunginin virtsalääkkeiden farmakokinetiikkaa ja kliinisiä tuloksia kandiduriassa, ottaen huomioon lääkkeen historiallisesti matala muuttumaton munuaisiin erittyminen

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

