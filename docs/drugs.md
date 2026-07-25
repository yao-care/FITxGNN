---
layout: default
title: Kaikki lääkkeet
nav_order: 20
permalink: /drugs/
description: "Kaikki lääkkeiden validointiraportit ja näytön tasojen tilastot FITxGNN:ssä."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# Kaikki lääkkeet

{{ site.drugs.size }} lääkkeen validointiraporttia

---

## Näytön tasojen jakauma

| Näytön taso | Lääkkeitä | Kuvaus |
|---------|--------|------|
| **L1** | {{ l1_count }} | Useita RCT-tutkimuksia / järjestelmällisiä katsauksia |
| **L2** | {{ l2_count }} | Yksittäinen RCT / vaiheen 2 tutkimuksia |
| **L3** | {{ l3_count }} | Havainnoivat tutkimukset / laajat tapaussarjat |
| **L4** | {{ l4_count }} | Prekliiniset / mekanistiset tutkimukset |
| **L5** | {{ l5_count }} | Pelkkä mallin ennuste |

---

## Täydellinen lääkeluettelo

{% assign all_drugs = site.drugs | sort: 'title' %}

| Lääke | Näytön taso | Käyttöaiheet |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
