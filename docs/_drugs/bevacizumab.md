---
layout: default
title: Bevacizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "BEVACIZUMAB"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
description: "Bevacizumab: ennustettu uusi käyttöaihe Epiglottiksen kasvain (näytön taso L5). Alkuperäinen käyttöaihe: Paksusuolen ja peräsuolen kasvaimet, rintasyöpä…"
---

# Bevacizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

# Bevasitsumabi: Alkuperäisistä syöpäindikaatioista ennustettuun kystiseen neoplasiaan

## Yhden lauseen yhteenveto

Bevasitsumabi on VEGF-vasta-aine, jota on alun perin käytetty paksusuolen ja peräsuolen syövän, rintasyövän, ei-pienisoluisen keuhkosyövän, munuaissolusyövän, munasarjasyövän ja kohdunkaulan syövän hoitoon sekä kosteaan silmänpohjan ikärappeumaan. TxGNN-malli ennustaa sen mahdollisesti tehokkaaksi **epiglottiksen kasvaimessa**, mutta tälle indikaatiolle ei ole kliinisiä tutkimuksia eikä kirjallisuutta. Kaikista kymmenestä ennustetusta indikaatiosta parhaiten tuettu on **kystinen neoplasia** (**5 kliinistä tutkimusta** ja **21 julkaisua**), mutta se kattaa pääosin jo hyväksytyn munasarjasyöpäindikaation.

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Paksusuolen ja peräsuolen kasvaimet, rintasyöpä, ei-pienisoluinen keuhkosyöpä, munuaissolusyöpä, kohdunkaulan kasvaimet (sekä munasarjan, munanjohtimen ja vatsakalvon kasvaimet) |
| Ennustettu uusi indikaatio (sijalla 1) | Epiglottiksen kasvain |
| TxGNN-ennustepisteet | 99,90 % |
| Näytön taso | L5 (sijalla 1); parhaiten tuettu ennuste, kystinen neoplasia, on L1 |
| Markkinatilanne Suomessa | Vain peruutetut myyntiluvat |
| Myyntilupien määrä | 10 (kaikki peruutettu) |
| Suositeltu päätös | Hold (odotetaan) |

## Miksi ennuste on perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa ei ole tämän raportin aineistossa saatavilla. Tunnetun tiedon perusteella bevasitsumabi neutraloi VEGF-A:n ja estää kasvaimen verisuonten muodostusta (angiogeneesiä). Sen teho useissa kiinteissä kasvaimissa on osoitettu, ja mekanistisesti se voi soveltua myös muihin voimakkaasti verisuonittuneisiin kasvaimiin.

Epiglottiksen kasvaimen kohdalla mekanismi on uskottava pään ja kaulan alueen kasvaimissa, mutta ennuste perustuu vain mallin laskemaan pisteeseen. Aineistossa ei ole yhtään tutkimusta tai julkaisua tästä taudista, joten korkea pistemäärä (0,999) ei yksin riitä perusteeksi.

Kystisen neoplasian kohdalla yhteys on selvempi: bevasitsumabi on jo hyväksytty munasarjasyövän hoitoon, joten kyse ei ole varsinaisesti uudesta käyttöaiheesta. Taudin nimike on laaja, ja sen kytkeminen tiettyihin munasarjan kasvaintyyppeihin on epätarkkaa.

## Kliininen tutkimusnäyttö

Sijan 1 ennusteelle (epiglottiksen kasvain) ei ole rekisteröityjä kliinisiä tutkimuksia. Alla on parhaiten tuetun ennusteen (kystinen neoplasia) tutkimukset.

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Vaihe 3 | Aktiivinen, ei rekrytoi | 1052 | Karboplatiini ja paklitakseli (tai gemsitabiini) bevasitsumabin kanssa tai ilman uusiutuneessa, platinaherkässä munasarja-, vatsakalvo- ja munanjohdinsyövässä |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Vaihe 2 | Aktiivinen, ei rekrytoi | 133 | Atesolitsumabin ja bevasitsumabin yhdistelmä harvinaisissa kiinteissä kasvaimissa, ei vertailuryhmää |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Vaihe 1/2 | Päättynyt | 66 | Erlotinibin, setuksimabin ja bevasitsumabin yhdistelmä; ei kohdespesifinen |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Vaihe 1 | Päättynyt | 39 | Bevasitsumabi, fluorourasiili ja hydroksiurea sädehoidon kanssa pään ja kaulan syövässä; turvallisuus ja annostus |
| [NCT00492089](https://clinicaltrials.gov/study/NCT00492089) | Vaihe 2 | Päättynyt | 11 | Bevasitsumabi aivojen sädevaurion hoidossa; eri kliininen kysymys |

Huomautus: tutkimuksen NCT00565851 otsikko oli aineistossa katkaistu, joten bevasitsumabihaara on syytä varmistaa.

## Kirjallisuusnäyttö

Alla on valikoima kystisen neoplasian (munasarjatyypit) kirjallisuudesta. Sijan 1 ennusteelle ei ole kirjallisuutta.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | Systemaattinen katsaus | Current Oncology | Bevasitsumabi matala-asteisessa seroosissa munasarjasyövässä; jonkin verran vaikutusta, näyttö rajallista |
| [40700681](https://pubmed.ncbi.nlm.nih.gov/40700681/) | 2025 | RCT | J Clin Oncol | Alpelisibi + olaparibi vs. solunsalpaaja platinaresistentissä korkea-asteisessa seroosissa munasarjasyövässä (ei bevasitsumabitutkimus) |
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Retrospektiivinen | Future Oncology | Bevasitsumabi matala-asteisessa seroosissa munasarjasyövässä: objektiivinen vasteosuus 54,1 % (51 potilasta) |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | 2025 | RCT:n osa-analyysi | Eur J Cancer | BRCA1/RAD51C-metylaation ennustearvo PAOLA-1-tutkimuksessa (bevasitsumabi + olaparibi) |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | Katsaus | Curr Oncol Rep | Ppitkälle edenneen korkea-asteisen seroosin munasarjasyövän ensilinjan hoito, VEGF-estäjät mukaan lukien |
| [27498762](https://pubmed.ncbi.nlm.nih.gov/27498762/) | 2016 | Kohortti/translationaalinen | Sci Rep | VEGF-riippuvainen geenisignatuuri ennustaa potilaiden ennustetta mesenkymaalisessa munasarjasyövässä |
| [29752717](https://pubmed.ncbi.nlm.nih.gov/29752717/) | 2018 | Prekliininen | Int J Cancer | Bevasitsumabin lisääminen tiheään tai tavanomaiseen paklitakseli-sisplatiinihoitoon munasarjasyövän malleissa |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | Hoitotulossarja | Clin Colorectal Cancer | Mitomysiini-C, metronominen kapesitabiini ja bevasitsumabi umpilisäkeperäisessä pseudomyxoma peritonei -taudissa |

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty indikaatio |
|---------|------|------|-----------|
| EMEA/H/C/000582 | Avastin | – | Ei-pienisoluinen keuhkosyöpä, rintasyöpä, munasarjasyöpä, paksusuolen ja peräsuolen syöpä, munuaissolusyöpä... |
| EMEA/H/C/004697 | Zirabev | – | Paksusuolen ja peräsuolen kasvaimet, rintasyöpä, ei-pienisoluinen keuhkosyöpä, munuaissolusyöpä... |
| EMEA/H/C/004728 | Mvasi | – | Munuaissolusyöpä, vatsakalvon kasvaimet, munasarjasyöpä, rintasyöpä... |
| EMEA/H/C/005723 | Lytenava | – | Kostea silmänpohjan ikärappeuma |
| EMEA/H/C/005534 | Vegzelma | – | Paksusuolen ja peräsuolen kasvaimet, rintasyöpä, munasarjasyöpä, munanjohdinsyöpä... |

Kaikki kymmenen myyntilupaa on merkitty peruutetuiksi.

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (VEGF:ää estävä monoklonaalinen vasta-aine), ei perinteinen solunsalpaaja |
| Luuydinlamaus | Kohdennetun hoidon luonteen vuoksi tyypillisesti pieni; riski liittyy usein samanaikaiseen solunsalpaajahoitoon. Tarkempaa tietoa ei ole saatavilla |
| Oksentelua aiheuttava vaikutus | Pieni |
| Seurattavat parametrit | Verenkuva, maksa- ja munuaisarvot, verenpaine, virtsan valkuaisaine |
| Käsittelysuojaus | Noudatettava valmisteyhteenvedon ja sairaalan ohjeita; tarkempaa tietoa ei ole saatavilla |

## Turvallisuusnäkökohdat

Lääkkeiden yhteisvaikutuksia on löytynyt yhteensä 22. **Vakavia (Major)** yhteisvaikutuksia ovat:
- deferiproni
- samarium (153Sm) leksidronaami
- panitumumabi
- sunitinibi
- talidomidi

**Kohtalaisia (Moderate)** yhteisvaikutuksia ovat muun muassa bisfosfonaatit (alendronihappo, risedronihappo, etidronihappo, ibandronaatti, pamidronihappo, tiludronihappo), kasvutekijät (filgrastiimi, pegfilgrastiimi, sargramostiimi), palifermiini, idelalisibi, romosotsumabi, strontium-89, radium-223 ja radioaktiivinen fosfori (P32).

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla; ne on tarkistettava valmisteyhteenvedosta.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odotetaan)**

**Perustelut:**
- Ykkössijan ennusteelle (epiglottiksen kasvain) ei ole kliinistä eikä kirjallisuusnäyttöä, joten korkea pistemäärä on pelkkä mallin ennuste. Muista ennusteista vain kystinen neoplasia yltää tasolle L1, mutta se kattaa pääosin jo hyväksytyn munasarjasyöpäindikaation eikä ole aitoa uudelleenkäyttöä.
- Kaikki myyntiluvat Suomessa on peruutettu, ja turvallisuustiedot puuttuvat.

**Eteneminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivuilta (estävä tietoaukko).
- Vaikutusmekanismitietojen täydentäminen DrugBankista.
- Epiglottiksen kasvaimen ja muiden pään ja kaulan kasvainten kohdespesifisen kliinisen ja prekliinisen näytön kartoitus.
- Kystisen neoplasian osalta taudin tarkentaminen tiettyihin munasarjahistologioihin ja tutkimuksen NCT00565851 bevasitsumabihaaran varmistaminen.
- Markkinatilanteen selvittäminen, koska kaikki myyntiluvat on peruutettu.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

