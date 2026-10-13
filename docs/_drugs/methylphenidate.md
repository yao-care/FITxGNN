---
layout: default
title: Methylphenidate
parent: Pelkkä mallin ennuste (L5)
nav_order: 288
evidence_level: L5
indication_count: 4
---

# Methylphenidate
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Metyylifenidaatti: Tarkkaavaisuus- ja ylivilkkaushäiriön hoidosta kohti faciodigitogenitaalista oireyhtymää

## Yhteenveto

Metyylifenidaatti on keskushermostoa stimuloiva lääkeaine, jota käytetään tarkkaavaisuus- ja ylivilkkaushäiriön (ADHD) hoitoon.
TxGNN-malli ennustaa sen tehoavan **faciodigitogenitaaliseen oireyhtymään** (Aarskog-Scottin oireyhtymä), mutta tälle ennusteelle ei ole **yhtään kliinistä tutkimusta eikä julkaisua**. Tutkimusnäyttö on olemassa vain muille, matalammin sijoittuville ennusteille (kehityshäiriöt, dystymia), ja sekin liittyy lähinnä ADHD:hen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Tarkkaavaisuus- ja ylivilkkaushäiriö (ADHD) |
| Ennustettu uusi käyttöaihe | Faciodigitogenitaalinen oireyhtymä |
| TxGNN-ennustepistemäärä | 100,00 % (0,99998) |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla järkevä?

Lääkeaineen tarkkaa vaikutusmekanismia ei ole tämän raportin aineistossa. Farmakologiatiedon mukaan metyylifenidaatti kohdistuu noradrenaliinin kuljettajaproteiiniin (NET, SLC6A2) ja dopamiinin kuljettajaproteiiniin (DAT, SLC6A3). Se estää näiden aineiden takaisinottoa, mikä lisää dopamiinin ja noradrenaliinin pitoisuutta synapsiraossa.

Faciodigitogenitaalinen oireyhtymä on harvinainen geneettinen kehityshäiriö. Joillakin potilailla esiintyy ADHD:n kaltaisia oireita, joten dopaminergisesta tai noradrenergisestä stimulantista voisi teoriassa olla apua näihin oireisiin. Aineisto ei kuitenkaan tue tätä päättelyä: yhteyttä ei ole osoitettu tutkimuksin, ja korkea pistemäärä voi olla pelkkä tietämysgraafin tuottama artefakti.

Muut ennusteet:
- **Spesifinen kehityshäiriö** (pistemäärä 0,99988): kirjallisuus käsittelee pääosin ADHD:n neurobiologiaa ja metyylifenidaatin vaikutuksia kuljettajaproteiineihin, aivojen rakenteeseen ja hoitovasteeseen. Tämä vastaa jo hyväksyttyä ADHD-käyttöaihetta, eikä se osoita uutta käyttöaihetta.
- **Dystymia** (pistemäärä 0,99109): yhteys on heikko ja epäsuora. Relevantein tutkimus (PMID 24045603) koskee ADHD:ta ja samanaikaisia lieviä masennusoireita, ei dystymian hoitoa.
- **Chondromyxoid fibroma** (pistemäärä 0,99991): uskottavaa mekanistista yhteyttä ei ole, sillä kyseessä on harvinainen hyvänlaatuinen rustokasvain.

## Kliiniset tutkimukset

Tällä hetkellä ei ole rekisteröityjä kliinisiä tutkimuksia, jotka liittyisivät ensisijaiseen ennusteeseen (faciodigitogenitaalinen oireyhtymä) tai muihin ennusteisiin.

## Kirjallisuusnäyttö

Ensisijaiselle ennusteelle (faciodigitogenitaalinen oireyhtymä) ei ole kirjallisuutta. Alla on kolme relevanteinta julkaisua toiseksi parhaiten tuettuun ennusteeseen, spesifiseen kehityshäiriöön, ja dystymiaan liittyvä julkaisu (merkitty erikseen).

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Kohorttitutkimus | Prog Neuropsychopharmacol Biol Psychiatry | Kumulatiivinen metyylifenidaattialtistus, aivojen rakenne ja ADHD-oireiden lieventyminen nuorilla (pitkittäinen MRI-tutkimus) |
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Kuvantaminen / mekanistinen | Psychiatry Clin Neurosci | Pitkävaikutteisen metyylifenidaatin vaikutus DAT- ja NET-sitoutumiseen aikuisilla ADHD-potilailla (PET) |
| [41655471](https://pubmed.ncbi.nlm.nih.gov/41655471/) | 2026 | Kohortti / geneettinen assosiaatio | Psychiatry Res | Polygeeninen ennustaminen ADHD-hoitovasteessa usean kohortin meta-analyysissä |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Katsaus | Neuropharmacology | ADHD:n neurobiologia |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Katsaus | J Atten Disord | Metyylifenidaatin teho, turvallisuus ja vaikutukset aikuisen ja nuoren aivoihin |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Havainnoiva tutkimus | Clin EEG Neurosci | Kvantitatiivinen EEG lapsuuden ADHD:ssa ja oppimisvaikeuksissa |
| [24045603](https://pubmed.ncbi.nlm.nih.gov/24045603/) | 2013 | Kohortti / kliininen tutkimus | Clin Neuropharmacol | Metyylifenidaatin vaikutus ADHD:hon ja mielialaan lapsilla ja nuorilla, joilla on lievä masennus (dystymiaan liittyvä ennuste) |

Yksikään julkaisu ei ole satunnaistettu kontrolloitu tutkimus metyylifenidaatista ennustetussa uudessa käyttöaiheessa.

## Myyntiluvat Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005975 | Tuzulby | – | Tarkkaavaisuus- ja ylivilkkaushäiriö (ADHD) (tila: peruutettu) |

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoitus- ja vasta-aihetietoja ei ole tämän raportin aineistossa. Tarkista turvallisuustiedot valmisteyhteenvedosta.

Tietämysgraafin (PrimeKG) vasta-aiheyhteydet, jotka eivät perustu valmisteyhteenvedon tekstiin, viittaavat muun muassa seuraaviin tiloihin:
- **Sydän- ja verisuonitaudit:** verenpainetauti, sepelvaltimotauti, sydäninfarkti, aivohalvaus, aivoinfarkti, sydämen johtumishäiriöt, äkillinen sydänpysähdys
- **Psykiatriset sairaudet:** kaksisuuntainen mielialahäiriö, psykoosit, skitsoaffektiivinen häiriö, päihderiippuvuus, anorexia nervosa
- **Neurologiset sairaudet:** epilepsia
- **Muut:** glaukooma, kilpirauhasen liikatoiminta (Basedowin tauti, tyreotoksikoosi), trombosytopenia, leukopenia, anemia ja hemoglobinopatiat

Lääkeaineiden yhteisvaikutuksista ei ole kliinisiä yhteisvaikutustietoja. Farmakologiahaku tunnisti vain lääkeaineen kohdeproteiinit NET ja DAT.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ensisijaisella ennusteella (faciodigitogenitaalinen oireyhtymä) ei ole kliinisiä tutkimuksia, kirjallisuutta eikä tunnistettua mekanistista yhteyttä, joten näyttö on tasoa L5 (pelkkä mallin ennuste). Lisäksi Suomessa ei ole voimassa olevaa myyntilupaa.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitus- ja vasta-aihetiedot Fimeasta
- Vaikutusmekanismin (MOA) tiedot DrugBankista
- Kirjallisuushaku metyylifenidaatin käytöstä Aarskog-Scottin oireyhtymän ADHD-oireisiin
- Mikäli ADHD-oireiden hoitoa pidetään tavoitteena, arvioitava, tuoko ennuste mitään lisäarvoa jo hyväksyttyyn käyttöaiheeseen verrattuna
- Spesifisen kehityshäiriön ja dystymian ennusteille kontrolloituja tutkimuksia ennen kuin niitä voidaan pitää uusina käyttöaiheina
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

