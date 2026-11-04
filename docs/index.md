---
layout: default
title: "L\u00e4\u00e4kkeiden Uudelleensijoittelun Ennusteet \u2014 Suomi"
nav_order: 1
description: "Tekoälyyn perustuvat lääkkeiden uudelleenkäytön ennusteet Suomelle. Näyttöön perustuva analyysi hyväksyttyjen lääkkeiden mahdollisista uusista käyttöaiheista."
permalink: /
---

# Lääkkeiden uudelleenkäytön ennusteet — Suomi

Tämä projekti käyttää TxGNN-graafineuroverkkoa ennustamaan Suomessa hyväksyttyjen lääkkeiden mahdollisia uusia terapeuttisia käyttöaiheita.

**Vastuuvapauslauseke**: Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön, eikä se ole lääketieteellinen neuvo. Kaikki lääkkeiden uudelleensijoittelua koskevat ennusteet edellyttävät kliinistä validointia ennen käyttöä.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Suomi: sivuston kattavuus

Sivustolla on julkaistu raportit **{{ site.data.drug_stats.total_drugs }}** lääkkeestä, joilla on EU:n keskitetty myyntilupa ([EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), voimassa myös Suomessa).

Aineisto: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); se ladataan ja verrataan automaattisesti joka viikko (maanantaisin). Lisätietoja: [Tietolähteet]({{ '/sources/' | relative_url }}).

Raportit näytön tason mukaan:

| Näytön taso | Raportit | Osuus |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

### Sivuston vahvimman näytön lääkkeet

| Lääke | Näytön taso |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Grazoprevir](/drugs/grazoprevir/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Brentuximab Vedotin](/drugs/brentuximab-vedotin/) | L2 |
| [Ledipasvir](/drugs/ledipasvir/) | L2 |

<!-- local-home:end -->

## Kehittäjästä

Tämän alustan on kehittänyt ja sitä ylläpitää **藥提醒科技有限公司** (yao.care). Yhtiön tiedot, TxGNN-mallin
tausta ja tuotelinjan kaikki sivustot löytyvät <a href="{{ '/about/' | relative_url }}">Tietoa</a>-sivulta.
