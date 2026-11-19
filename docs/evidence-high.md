---
layout: default
title: Vahva näyttö (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "30 lääkettä näytön tasolla L1–L2 tällä sivustolla (Suomi), esim. Bupropion, Busulfan, Clofarabine, kunkin tärkein ennustettu käyttöaihe, keskitettyä EU-myyntilupaa (EMA) ja tarkistusloki."
---

# Vahva näyttö (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Sivulla on **{{ site.data.evidence_tier_facts.high.count }}** sivuston **{{ site.data.drug_stats.total_drugs }}** raportoidusta lääkkeestä ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Tasojen L1–L2 mediaaniosuus 30 TxGNN-sivustolla: {{ site.data.evidence_tier_facts.high.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Tämä sivusto on mediaanin yläpuolella.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Tämä sivusto on mediaanin alapuolella.{% else %}Tämä sivusto on mediaanissa.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
Paikallisissa tiedoissa (keskitettyä EU-myyntilupaa (EMA)) **{{ site.data.evidence_tier_facts.high.with_current }}** näistä lääkkeistä on vähintään yksi voimassa olevaa merkintä, **{{ site.data.evidence_tier_facts.high.none_current }}** lääkkeellä on merkintöjä mutta ei yhtään voimassa olevaa, ja **{{ site.data.evidence_tier_facts.high.without_data }}** ei ole paikallisissa tiedoissa. **{{ site.data.evidence_tier_facts.high.with_reviews }}** lääkkeellä on merkintöjä tarkistuslokissa (lupatietojen korjauksia lääkesivulla). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** lääkkeellä on ennustettu käyttöaihe, jota mikään muu TxGNN-sivusto ei mainitse samalle lääkkeelle.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Merkintöjä, mutta ei yhtään voimassa olevaa: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Kaikkien tasojen määritelmät: [Menetelmät]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} lääkettä)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lääke | Taso | Tärkein ennustettu uusi käyttöaihe | keskitettyä EU-myyntilupaa (EMA): voimassa olevaa / yhteensä | Tarkistusloki | Vain tällä sivustolla |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}kyllä ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} lääkettä)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lääke | Taso | Tärkein ennustettu uusi käyttöaihe | keskitettyä EU-myyntilupaa (EMA): voimassa olevaa / yhteensä | Tarkistusloki | Vain tällä sivustolla |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}kyllä ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
