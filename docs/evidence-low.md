---
layout: default
title: Pelkkä mallin ennuste (L5)
nav_order: 23
permalink: /evidence-low/
description: "370 lääkettä näytön tasolla L5 tällä sivustolla (Suomi), esim. Denosumab, Metformin, Emtricitabine, kunkin tärkein ennustettu käyttöaihe, keskitettyä EU-myyntilupaa (EMA) ja tarkistusloki."
---

# Pelkkä mallin ennuste (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Sivulla on **{{ site.data.evidence_tier_facts.low.count }}** sivuston **{{ site.data.drug_stats.total_drugs }}** raportoidusta lääkkeestä ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Tasojen L5 mediaaniosuus 30 TxGNN-sivustolla: {{ site.data.evidence_tier_facts.low.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Tämä sivusto on mediaanin yläpuolella.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Tämä sivusto on mediaanin alapuolella.{% else %}Tämä sivusto on mediaanissa.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
Paikallisissa tiedoissa (keskitettyä EU-myyntilupaa (EMA)) **{{ site.data.evidence_tier_facts.low.with_current }}** näistä lääkkeistä on vähintään yksi voimassa olevaa merkintä, **{{ site.data.evidence_tier_facts.low.none_current }}** lääkkeellä on merkintöjä mutta ei yhtään voimassa olevaa, ja **{{ site.data.evidence_tier_facts.low.without_data }}** ei ole paikallisissa tiedoissa. **{{ site.data.evidence_tier_facts.low.with_reviews }}** lääkkeellä on merkintöjä tarkistuslokissa (lupatietojen korjauksia lääkesivulla). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** lääkkeellä on ennustettu käyttöaihe, jota mikään muu TxGNN-sivusto ei mainitse samalle lääkkeelle.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Merkintöjä, mutta ei yhtään voimassa olevaa: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Lääkkeet, joilla on voimassa olevaa paikallinen merkintä, näytetään ensin.
{% endif %}

Kaikkien tasojen määritelmät: [Menetelmät]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} lääkettä)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lääke | Taso | Tärkein ennustettu uusi käyttöaihe | keskitettyä EU-myyntilupaa (EMA): voimassa olevaa / yhteensä | Tarkistusloki | Vain tällä sivustolla |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}kyllä ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
