---
layout: default
title: Vahva näyttö (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "FITxGNN:n L1–L2-tason uudelleensijoitteluehdokkaat, joita tukevat kliiniset tutkimukset tai järjestelmälliset katsaukset."
---

# Vahva näyttö (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Ehdokkaat, jotka voidaan asettaa etusijalle kliinisessä arvioinnissa
</p>

---

## Kriteerit

| Taso | Määritelmä | Kliininen merkitys |
|-------|------------|------------------|
| **L1** | Useita vaiheen 3 RCT-tutkimuksia / järjestelmällisiä katsauksia | Vahva tuki; kliinistä käyttöä voidaan harkita |
| **L2** | Yksittäinen RCT tai useita vaiheen 2 tutkimuksia | Kohtalainen tuki; validointitutkimuksia voidaan suunnitella |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

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
