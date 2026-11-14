---
layout: default
title: Vahva näyttö (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "FITxGNN:n L1–L2-tason uudelleensijoitteluehdokkaat, joita tukevat kliiniset tutkimukset tai järjestelmälliset katsaukset."
---

# Vahva näyttö (L1-L2)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L1 | plus: site.data.drug_stats.level_counts.L2 %}
Sivulla on **{{ pd_m }}** sivuston **{{ site.data.drug_stats.total_drugs }}** raportoidusta lääkkeestä ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Tasojen määritelmät: [Menetelmät]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Ehdokkaat, jotka voidaan asettaa etusijalle kliinisessä arvioinnissa
</p>

Millä näistä lääkkeistä on tutkimusnäyttöä ennustetulle uudelle käyttöaiheelle, ja kuinka moneen rekisteröityyn tutkimukseen viitataan? Katso [Lääkkeet, joiden uudelle käyttöaiheelle on kliinistä tutkimusnäyttöä]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Kriteerit

| Taso | Määritelmä | Kliininen merkitys |
|-------|------------|------------------|
| **L1** | Useita vaiheen 3 RCT-tutkimuksia / järjestelmällisiä katsauksia | Vahva tuki; kliinistä käyttöä voidaan harkita |
| **L2** | Yksittäinen RCT tai useita vaiheen 2 tutkimuksia | Kohtalainen tuki; validointitutkimuksia voidaan suunnitella |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ l1_drugs.size }} lääkettä)

| Lääke | Käyttöaiheet | Linkki |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Näytä raportti]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} lääkettä)

| Lääke | Käyttöaiheet | Linkki |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Näytä raportti]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
