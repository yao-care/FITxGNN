---
layout: default
title: Pitolisant
parent: Pelkkä mallin ennuste (L5)
nav_order: 348
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "PITOLISANT"
predicted_indications: ["insomnia (disease)", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome"]
description: "Pitolisant: ennustettu uusi käyttöaihe Insomnia (disease) (näytön taso L5). Alkuperäinen käyttöaihe: Sleep Apnea, Obstructive"
---

# Pitolisant
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

## Pitolisant: Insomnia (disease)
{: .text-alpha }

## Yhden lauseen tiivistelmä

Pitolisantti on histamiini H3 -reseptorin käänteisagonisti, jota on käytetty narkolepsian ja obstruktiivisen uniapnean aiheuttaman päiväaikaisen uneliaisuuden hoitoon.
TxGNN-malli ennustaa sen voivan tehota **unettomuuteen** (insomnia), mutta tälle käyttöaiheelle ei ole **yhtään kliinistä tutkimusta** eikä suoraa kirjallisuutta. Lisäksi mekanistinen perustelu on ristiriitainen, koska lääke lisää valppautta.

---

## Pikayhteenveto

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Sleep Apnea, Obstructive; Narcolepsy |
| Ennustettu uusi käyttöaihe | Insomnia (disease) |
| TxGNN-ennustepistemäärä | 0.9971 |
| Näytön taso | L5 (tässä raportissa: käytännössä L5, ei unettomuutta koskevia tutkimuksia) |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 2/2) |
| Myyntilupien määrä | 2 (voimassa: 2) |
| Suositeltu päätös | Hold (odota) |

Huomio: toimitetuissa tiedoissa näytön tasoksi on annettu L4, mutta unettomuudesta ei ole kliinisiä tutkimuksia eikä suoraa kirjallisuutta, joten tason voi perustellusti nähdä olevan L5.

---

## Miksi ennuste on (tai ei ole) uskottava?

Pitolisantti on selektiivinen histamiini H3 -reseptorin antagonisti/käänteisagonisti. Se lisää aivojen histaminergistä välitystä ja edistää valppautta. DrugBankista ei saatu yksityiskohtaista vaikutusmekanismia, mutta kirjallisuus tukee tätä kuvausta.

Unettomuuden hoidossa pyritään yleensä vähentämään vireystilaa. Pitolisantin vaikutus on siis mekanistisesti päinvastainen, ja unettomuus on lääkkeen tunnettu haittavaikutus. Korkea TxGNN-pistemäärä johtuu todennäköisesti tietämysgraafin läheisyysartefaktasta: uni–valve-biologia on yhteistä, mutta se ei tarkoita hoitohyötyä. Käyttö tähän käyttöaiheeseen on mekanistisesti epäuskottavaa ja mahdollisesti haitallista.

Muut ennusteet ovat heikompia tai vain hypoteeseja. ADHD (pistemäärä 0,9936) on mekanistisesti uskottavampi, koska H3-antagonismi lisää histamiinin, asetyylikoliinin, noradrenaliinin ja dopamiinin vapautumista prefrontaalikuorella. Näyttö on kuitenkin epäsuoraa eikä ADHD-kohtaisia kliinisiä tutkimuksia ole. Faciodigitogenitaalinen syndrooma (Aarskog-Scott, 0,9929) on todennäköisesti tietämysgraafin artefakta ilman tukevaa näyttöä.

---

## Kliininen tutkimusnäyttö

Unettomuudesta ei ole tällä hetkellä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Alla olevat julkaisut koskevat pitolisanttia muissa käyttöaiheissa. Yksikään ei osoita tehoa unettomuudessa.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | Vaiheen 3 RCT | The Lancet Neurology | Pitolisantin turvallisuus ja teho vähintään 6-vuotiailla lapsilla, joilla on narkolepsia |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Jäännösuneliaisuus CPAP-hoitoa noudattavilla uniapneapotilailla (ei unettomuus) |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Päiväaikainen uneliaisuus uniapneassa potilailla, jotka kieltäytyvät CPAP-hoidosta (ei unettomuus) |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Tosielämän kohorttitutkimus | Revista de neurologia | WAKE-tutkimus: pitolisantti narkolepsiassa aiempiin hoitoihin vastaamattomilla potilailla |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | Tosielämän kohorttitutkimus | Neurological Sciences | Pitolisantti lasten narkolepsiassa Kiinassa (40 potilasta) |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Katsaus | Drug Des Devel Ther | Pitolisantin profiili narkolepsian hoidossa |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Katsaus | Current Neuropharmacology | Histaminergisen järjestelmän muutokset neuropsykiatrisissa sairauksissa; pitolisantti narkolepsiassa, doksepiini unettomuudessa |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Katsaus | Neurology and Therapy | Lasten uni häiriöiden nykyiset ja uudet hoidot |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Katsaus | Handbook of Clinical Neurology | Histamiinireseptorit, agonistit ja antagonistit terveydessä ja sairaudessa |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Katsaus | Clinical Neuropharmacology | Pitolisantti nuorten narkolepsia-kataplektisessa tilassa |

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005117 | Ozawade | – | Obstruktiivinen uniapnea (peruutettu) |
| EMEA/H/C/002616 | Wakix | – | Narkolepsia (peruutettu) |

---

## Turvallisuushuomiot

**Lääkeyhteisvaikutukset:** Yhteisvaikutuskyselyssä löytyi yhteensä 100 yhteisvaikutusta. Toimitetuista tiedoista keskeisimmät:
- **Merkittävät (Major):** bupropioni, dolasetroni
- **Kohtalaiset (Moderate), esimerkkejä:** famotidiini, simetidiini, metformiini, morfiini, asetyylisalisyylihappo, klaritromysiini, deksametasoni, hydrokortisoni, budesonidi, empagliflotsiini, eliglustaatti, loperamidi

Pakkausselosteen varoituksia ja vasta-aiheita ei ollut saatavilla, joten ne on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Unettomuudesta ei ole kliinisiä tutkimuksia, ja pitolisantin valppautta lisäävä vaikutus on ristiriidassa unettomuuden hoidon kanssa. Korkea ennustepistemäärä on todennäköisesti verkostoartefakta.
- Lisäksi molemmat Suomen myyntiluvat on peruutettu.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (Fimea), jotta turvallisuusarviointi voidaan aloittaa
- Yksityiskohtainen vaikutusmekanismitieto (DrugBank)
- Jos halutaan jatkaa, ADHD on mekanistisesti uskottavampi tutkimuskysymys (suositus: tutkimushypoteesi), mutta se vaatii omat ADHD-kohtaiset tutkimukset
- Myyntilupien peruutuksen syiden selvittäminen ja lääkemuotojen tiedot
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

