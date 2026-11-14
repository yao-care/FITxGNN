---
layout: default
title: Pelkkä mallin ennuste (L5)
nav_order: 23
permalink: /evidence-low/
description: "FITxGNN:n L5-tason ehdokkaat: pelkkä mallin ennuste, ilman kliinistä tai kirjallisuusnäyttöä."
---

# Pelkkä mallin ennuste (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Sivulla on **{{ pd_m }}** sivuston **{{ site.data.drug_stats.total_drugs }}** raportoidusta lääkkeestä ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Tasojen määritelmät: [Menetelmät]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Ehdokkaat, joilla on vain mallin ennuste eikä vielä lainkaan näyttöä ihmisillä
</p>

---

## Kriteerit

| Taso | Määritelmä | Kliininen merkitys |
|-------|------------|------------------|
| **L5** | Pelkkä mallin ennuste | Hypoteesivaihe; ei vielä näyttöä ihmisillä |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ l5_drugs.size }} lääkettä)

| Lääke | Käyttöaiheet | Linkki |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Näytä raportti]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
