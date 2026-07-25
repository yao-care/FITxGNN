---
layout: default
title: Tietolähteet
nav_order: 93
permalink: /sources/
description: "FITxGNN:n taustalla olevat tietolähteet: Fimean myyntilupatiedot, TxGNN, ClinicalTrials.gov, PubMed ja DrugBank."
---

# Tietolähteet

<div class="key-takeaway">
Jokainen johtopäätös on jäljitettävissä julkiseen tietolähteeseen — mikään ei ole musta laatikko.
</div>

---

## Lähteiden yleiskatsaus

<table class="comparison-table">
<thead>
<tr><th>Tyyppi</th><th>Lähde</th><th>Käyttötarkoitus</th></tr>
</thead>
<tbody>
<tr><td>Myyntilupatiedot</td><td><a href="https://fimea.fi/">Fimea</a></td><td>Suomessa hyväksyttyjen lääkkeiden luettelo ja vaikuttavat aineet</td></tr>
<tr><td>Ennustemalli</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Lääkkeen ja sairauden välisen yhteyden ennustaminen</td></tr>
<tr><td>Kliiniset tutkimukset</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Näytön luokittelu (NCT)</td></tr>
<tr><td>Kirjallisuus</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Näytön luokittelu (PMID)</td></tr>
<tr><td>Lääketiedot</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Vaikuttavien aineiden kohdennus ja kohdemolekyylitiedot</td></tr>
<tr><td>Yhteisvaikutukset</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Lääkkeiden välisten yhteisvaikutusten tiedot</td></tr>
</tbody>
</table>

---

## Lisensointi

Jokaisella lähteellä on oma lisenssinsä — tarkista se ennen viittaamista:

- **TxGNN**: akateeminen käyttö; viittaa julkaisuun Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: Yhdysvaltain NIH:n julkista dataa
- **DrugBank**: ei-kaupallinen käyttö lisenssiehtojen mukaisesti
- **Fimea**: Suomen lääkeviranomaisen avoimen datan ehtojen alainen

---

## Päivitystiheys

| Tiedot | Tiheys |
|------|-----------|
| Myyntilupatiedot | Viranomaisen julkaisurytmin mukaan |
| Tutkimus- ja kirjallisuusnäyttö | Kerätään uudelleen säännöllisesti |
| Yhteisvaikutustiedot | Tarkistetaan neljännesvuosittain |

---

## Tieteellinen viittaus

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Kehittäjästä

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care, yritysrekisterinumero
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

FITxGNN on yhtiön "TxGNN Drug Repurposing" -tuotelinjan Suomen sivusto.
Sama järjestelmä on otettu käyttöön 30 maassa ja alueella, kukin nimellä `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN ja niin edelleen) osoitteessa `{cc}txgnn.yao.care`.
Tuotteen yleiskuvaus: <https://www.yao.care/medical/txgnn/>.

Itse TxGNN-mallin on kehittänyt Zitnik Lab Harvard Medical Schoolissa, ja se on julkaistu
*Nature Medicine* -lehdessä. Tämä alusta on tuotantojärjestelmä, jonka 藥提醒科技有限公司 on rakentanut
kyseisen mallin päälle. Se kattaa kansallisten lääkerekisteritietojen integroinnin, tietograafiin ja
syväoppimiseen perustuvan kaksoisennusteen, PubMed- ja ClinicalTrials-näytön luokittelun sekä
SMART on FHIR -integraation potilastietojärjestelmiin.

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
