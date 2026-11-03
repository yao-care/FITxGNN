---
layout: default
title: Tietolähteet
nav_order: 93
permalink: /sources/
description: "FITxGNN:n taustalla olevat tietolähteet: EMA:n Medicines report (EU:n keskitetyt myyntiluvat), TxGNN, ClinicalTrials.gov, PubMed ja DrugBank."
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
<tr><td>Myyntilupatiedot</td><td><a href="https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx">EMA Medicines report</a> (Euroopan lääkevirasto EMA)</td><td>EU:n keskitetyssä menettelyssä myyntiluvan saaneet lääkkeet (voimassa kaikissa EU/ETA-maissa, myös Suomessa): vaikuttavat aineet ja myyntiluvan tila</td></tr>
<tr><td>Ennustemalli</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Lääkkeen ja sairauden välisen yhteyden ennustaminen</td></tr>
<tr><td>Kliiniset tutkimukset</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Näytön luokittelu (NCT)</td></tr>
<tr><td>Kirjallisuus</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Näytön luokittelu (PMID)</td></tr>
<tr><td>Lääketiedot</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Vaikuttavien aineiden kohdennus ja kohdemolekyylitiedot</td></tr>
<tr><td>Yhteisvaikutukset</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Lääkkeiden välisten yhteisvaikutusten tiedot</td></tr>
</tbody>
</table>

Sivusto ei käytä Fimean kansallista perusrekisteriä, joten pelkästään kansallisella myyntiluvalla
myytävät lääkkeet eivät ole mukana.

---

## Lisensointi

Jokaisella lähteellä on oma lisenssinsä — tarkista se ennen viittaamista:

- **TxGNN**: akateeminen käyttö; viittaa julkaisuun Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: Yhdysvaltain NIH:n julkista dataa
- **DrugBank**: ei-kaupallinen käyttö lisenssiehtojen mukaisesti
- **EMA Medicines report**: Euroopan lääkeviraston julkinen tiedosto, ladattavissa ilman rekisteröitymistä; noudata EMA:n käyttöehtoja

---

## Päivitystiheys

| Tiedot | Tiheys |
|------|-----------|
| Myyntiluvan tila | Päivitetään automaattisesti viikoittain (maanantaisin) EMA:n tiedostosta |
| Tutkimus- ja kirjallisuusnäyttö | Kerätään uudelleen säännöllisesti |
| Yhteisvaikutustiedot | Tarkistetaan neljännesvuosittain |

---

## Tieteellinen viittaus

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Kehittäjästä

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care). Yhtiön tiedot, TxGNN-mallin
tausta ja tuotelinjan kaikki sivustot löytyvät <a href="{{ '/about/' | relative_url }}">Tietoa</a>-sivulta.

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
