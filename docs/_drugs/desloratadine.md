---
layout: default
title: Desloratadine
parent: Vahva näyttö (L1-L2)
nav_order: 120
evidence_level: L1
indication_count: 6
---

# Desloratadine
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

# Desloratadine: Allergisesta nuhasairauksesta/kroonisesta urtikariasta kylmäurtikariaaksi

## Yhden lauseen yhteenveto

Desloratadine on toisen sukupolven H1-antihistamiini, jota käytetään yleisesti allergisen nuhan ja kroonisen urtikarian hoitoon. TxGNN-malli ennustaa, että se saattaa olla tehokas **kylmäurtikariaalle (Acquired Cold Urticaria, ACU)**, ja tällä hetkellä **3 kliinistä tutkimusta** ja **7 julkaisua** tukevat tätä suuntaa.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Allerginen nuhan/krooninen urtikaria (yleinen toisen sukupolven antihistamiinin käyttö; ei dokumentoitu toimitetussa Suomen sääntelytietokannan aineistossa) |
| Ennustettu uusi indikaatio | Kylmäurtikaria |
| TxGNN-ennusteen pistemäärä | 99.94% |
| Todistusaineiston taso | L1 |
| Markkinatilanne Suomessa | Ei markkinoilla |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | Etene varauksilla |

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaisia virallisia vaikutusmekanismitietoja ei saatu noudettua DrugBankista tässä todistusaineistopaketissa. Tunnetun farmakologian perusteella desloratadine on selektiivinen, perifeerisesti vaikuttava toisen sukupolven H1-reseptoriantagonisti – loratadiinan aktiivinen metaboliitti.

Kylmäurtikaria laukeaa kylmän aiheuttamasta iholle sijoittuneiden mastsolujen degranaulaatiosta, jossa histamiinieritys aiheuttaa papu-punetus-vasteen. Koska desloratadine estää suoraan H1-reseptoria tämän histamiinierityksen jälkeisellä asteella, sen vakiintunut antihistamiini-aktiivisuus vastaa kylmäurtikarian patofysiologiaan mekanistisesti pikemminkin kuin vaatii kokonaan uutta toimintamekanismia.

Tämä näkyy ennusteen mukana toimitetussa uudelleenkäyttötarkoituksen perustelussa: H1-antihistamiinit ovat jo EAACI/GA²LEN urtikariaohjeiden ensimmäisen valinnan hoito kylmäurtikariaassa, ja desloratadiinitoksin annoksen korotusstrategiat on tutkittu. Tämä antaa TxGNN-ennusteelle suoraa, ohjeistokonsistenttia mekanistista tukea pikemminkin kuin puhtaasti päättelevän yhteyden.

## Kliinisten tutkimusten todistusaineisto

| Tutkimuksen numero | Vaihe | Tila | Osallistujamäärä | Keskeiset tulokset |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Valmistunut | 30 | Monikeskuksinen, kaksoissokkoutettu, annosta korotava tutkimus, joka arvioi desloratadiinitasojen (5/10/20 mg) riittävyyttä kylmäurtikarian oireiden estämiseksi. |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Valmistunut | 33 | Satunnaistettu, kaksoissokkoutettu, lumekontrolloitu ristiintutkimus, jossa verrataan 5 mg vs. 20 mg desloratadinia kokeellisesti indusoitujen kylmäurtikarian leesioiden osalta (termografia/volumenometria); tutkii hypoteesia, että annoksen korotus (20 mg) on tehokkaampi kuin vakioannos. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Valmistunut | 150 | Viiden antihistamiinin (mukaan lukien desloratadini) estävän vaikutuksen arviointi urtikariassa; luokkatasolla verrattava todistusaineisto eikä desloratadinikohtainen. |

## Kirjallisuuden todistusaineisto

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeiset tulokset |
|------|-----|------|------|---------|
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | 5 mg desloratadinia 4 päivän ajan testattiin jääkuution provokalla 12 kylmäurtikariapotilaalla ennen ja jälkeen hoitoa. |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Korkea-annoksen desloratadini vähentää papujen tilavuutta ja parantaa kylmäprovokaaation kynnysarvoja vakioannokseen verrattuna ACU-potilailla (satunnaistettu, lumekontrolloitu, ristiintutkimus). |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | H1-antihistamiinin annoksen korotuksen satunnaistettu kontrolloitu tutkimus, jossa käytettiin kriittisen lämpötilan kynnysarvon mittaamista kylmäurtikariaassa. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Katsaus | Drugs | Kroonisen urtikarian etiologia, hoito ja nykyiset/tulevaisuuden hoitovaihtoehdot (mukaan lukien antihistamiiniluokka). |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Katsaus | Allergy | Ebasteenitä koskevan katsaus allergisessa nuhasairauksessa ja kroonisen idiopaattisen urtikarian osalta; luokkatasolla, ei desloratadinikohtainen. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Katsaus/tapaussarja | J Allergy Clin Immunol Pract | Kuvaa ruoka-riippuvaisen kylmäurtikarian fyysisen urtikarian uutena muunnelmana. |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Tapauskertomus | Qatar Med J | Ensimmäinen raportoitu kylmän indusoimaa urtikariaatapaus mustien muurahaisten purema-aiheisen anafylaksian jälkeen. |

## Markkinatiedot Suomesta

Desloratadini ei ole tällä hetkellä markkinoilla Suomessa saatavilla olevan sääntelyaineiston mukaisesti, eikä myyntilupakäyttöä löydetty (0 lupaa kirjautuneena).

## Turvallisuusnäkökohdat

Viitakaa pakkausselosteen turvallisuustietoihin.

## Johtopäätös ja seuraavat askeleet

**Päätös: Etene varauksilla**

**Perustelut:**
Kylmäurtikaria on tuettu L1-tason todistusaineistolla, joka sisältää kaksi valmistunutta Phase 4 -tutkimusta, joissa desloratadini erityisesti annosteltiin ACU-potilaille, sekä kolme muuta julkaistua tutkimusta (Juhlin 2004, Siebenhaar 2009, Magerl 2012) mekanismilla, joka on yhdenmukainen EAACI/GA²LEN ohjeiden suosituksiin. Desloratadini ei kuitenkaan ole tällä hetkellä markkinoilla Suomessa, ja TFDA-vastaavia pakkausselostetietoja/turvallisuustietoja (varoitukset, vasta-aiheet, lääkkeiden väliset vuorovaikutukset) ei saatu noudettua, joten turvallisuuden ja sääntelyreitistä tehdyt varaukset ovat välttämättömiä ennen etenemistä.

**Jatkaaksemme tarvitaan seuraavaa:**
- Virallinen pakkausseloste / merkinnän varoitukset ja vasta-aiheet (tällä hetkellä estävä tietoaukko)
- Vahvistettu lääkkeen välisten vuorovaikutusten profiili
- Virallinen vaikutusmekanismin dokumentaatio DrugBankista
- Sääntelyreitti-arviointi desloratadiiniu kylmäurtikarian merkintää varten markkinoilla, jossa se ei tällä hetkellä ole valtuutettu

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

