---
layout: default
title: Imatinib
parent: Kohtalainen näyttö (L3-L4)
nav_order: 191
evidence_level: L4
indication_count: 10
---

# Imatinib
{: .fs-9 }

Näytön taso: **L4** | Ennustetut käyttöaiheet: **10** kpl
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

# Imatinibi: Kroonisesta myelooista leukemiasta sydämen fibroosarkoomain

## Yhden lauseen yhteenveto

> Imatinibi on tyrosiinikinaasin estäjä, joka on alun perin kehitetty kroonisen myeloisen leukemian (CML) ja gastrointestinaalisten stroomeaalisten tumorien (GIST) hoitoon.
> TxGNN-mallin huipulla oleva ennuste tälle lääkkeelle on **sydämen fibroosarkooma**,
> mutta tätä spesifistä kandidaattia tukee tällä hetkellä vain **1 julkaisu** ja **ei kliinisiä tutkimuksia** — näyttö perustuu oleellisesti vain malliin.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Krooninen myeloinen leukemia (CML) / GIST *(yleinen tieto — ei peräisin tästä näyttöpaketista; Fimean pakkausesite-tekstiä ei ole saatavilla)* |
| Ennustettu uusi käyttöaihe | Sydämen fibroosarkooma |
| TxGNN-ennustuspistemäärä | 99.94% (rank 952) |
| Näyttötaso | L4 |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Hold |

## Miksi tämä ennuste on kohtuullinen?

Yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla tässä näyttöpaketissa (vaikutusmekanismi merkitty tietovajeena). Yleisen tiedon perusteella imatinibi on pieni-molekyylinen tyrosiinikinaasin estäjä, joka kohdistuu BCR-ABL:lle, KIT:ille ja PDGFR/PDGFRB:lle — mekanismi, joka on hyvin vakiintunut CML:n ja GIST:n yhteydessä, ja mekanistisesti se voi laajentua PDGFRB-fuusion ohjaamiin tumoreihin.

Kuitenkin spesifinen yhteys **sydämen fibroosarkoomain** on heikko. Näyttöpaketin omien perusteluiden mukaan: *"PDGFRB-fuusion ohjaamaan fibroosarkooma-perheeseen on teoreettinen laajennus, mutta primaarinen sydämen fibroosarkooma on äärimmäisen harvinainen, eikä eliminiin-spesifinen mekanistinen näyttö tue tätä yhteyttä."* Tumorin genotyypin määritystiedot eivät vahvista PDGFRB:n osallisuutta tässä spesifissä, äärimmäisen harvinaisessa sydämen tumorin alaryhmässä.

Huomionarvoista on, että muut TxGNN:n ennustamat ehdokkaat samassa fibroosarkooma/fibroblastinen-neoplaasia-perheessä osoittavat huomattavasti vahvempia näyttöä — erityisesti "fibroblastinen neoplaasia" (rank 2, vastaa suurelta osin dermatofibrosarcoma protuberansia), jossa COL1A1-PDGFB-fuusio on oppikirjaesimerkki imatinibin kohteesta L2-näytöllä ja "Proceed with Guardrails" -suosituksella. Tämä antaa epäsuoraa, luokka-tasolla uskottavuutta PDGFR-ohjaamalle mekanismille, mutta se ei korvaa suoraa näyttöä sydämen fibroosarkooman tapauksessa.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröity vastaavia kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeiset havainnot |
|------|------|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Kommentti | Prescrire international | Arvioi imatinibin asteittain laajenevaa käyttöaiheita CML:n ja GIST:n ulkopuolella (esim. Ph+ ALL); päättelee näyttöä uusille käyttöaiheille olevan "ei vahva". Ei käsittele sydämen fibroosarkooomaa erityisesti. |

## Suomen markkinatiedot

Imatinibi:lla ei ole tällä hetkellä myyntilupien tietoja Suomessa tässä tietojoukossa (markkinatilanne: ei markkinoilla; 0 hyväksyntää).

## Sytotoksisuus

| Kohde | Sisältö |
|------|------|
| Sytotoksisuuden luokittelu | Kohdistettu lääkitys (tyrosiinikinaasin estäjä; ei perinteinen sytotoksinen aine) |
| Boniytimen tukahduttamisen riski | Katso pakkausesite varoitukset ja varotoimet |
| Emetogeniteetin luokittelu | Katso pakkausesite varoitukset ja varotoimet |
| Seurantakohdat | Katso pakkausesite varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausesite varoitukset ja varotoimet |

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausesitteestä.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold**

**Perustelut:**
TxGNN-pistemäärä on korkea, mutta tälle spesifiselle käyttöaiheelle (sydämen fibroosarkooma) on vain yksi ei-spesifinen kommenttiartikel ja nolla kliinisiä tutkimuksia. Primaarinen sydämen fibroosarkooma on äärimmäisen harvinainen, eikä mikään eliminiin- tai tumoriin-spesifinen mekanistinen näyttö (esim. PDGFRB-fuusion tila) tue yhteyttä — tämä on tällä hetkellä vain mallin ennustussignaali (johdonmukainen paketin omien L4/Hold-pisteytysten kanssa).

**Jatkamista varten tarvitaan seuraavaa:**
- TFDA/Fimean pakkausesite-tiedot (tällä hetkellä esto — DG001)
- Yksityiskohtainen vaikutustavan vahvistus (tällä hetkellä vakava puute — DG002)
- Tapausraportteja tai prekliinisiä tietoja, jotka vahvistavat PDGFR/KIT/BCR-ABL-polun aktiviteetin erityisesti sydämen fibroosarkooman tapauksessa
- Harkitse saman ennustusjoukon korkeamman näyttötason ehdokkaan ("fibroblastinen neoplaasia"/DFSP, L2, Proceed with Guardrails) uudelleenarviointi toimintakelpoisempana lähiajan uudelleenkäyttötavoitteena

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

