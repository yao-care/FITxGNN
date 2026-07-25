---
layout: default
title: Kohtalainen näyttö (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "FITxGNN:n L3–L4-tason uudelleensijoitteluehdokkaat, joita tukee havainnoiva tai prekliininen näyttö."
---

# Kohtalainen näyttö (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Ehdokkaat, joilla on alustavaa näyttöä ja jotka vaativat lisävahvistusta
</p>

---

## Kriteerit

| Taso | Määritelmä | Kliininen merkitys |
|-------|------------|------------------|
| **L3** | Havainnoivat tutkimukset / laajat tapaussarjat | Alustava tuki; vaatii lisävahvistusta |
| **L4** | Prekliiniset / mekanistiset tutkimukset | Teoreettinen tuki; kaukana kliinisestä käytöstä |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} lääkettä)

| Lääke | Käyttöaiheet | Linkki |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Näytä raportti]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} lääkettä)

| Lääke | Käyttöaiheet | Linkki |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Näytä raportti]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Vastuuvapauslauseke</strong><br>
Tämä raportti on tarkoitettu ainoastaan akateemisen tutkimuksen tausta-aineistoksi, eikä se <strong>ole lääketieteellinen neuvo</strong>. Noudata aina lääkärisi ohjeita äläkä koskaan muuta lääkitystäsi omin päin. Kaikki lääkkeiden uudelleensijoittelua koskevat päätökset edellyttävät täydellistä kliinistä validointia ja viranomaisarviointia.
<br><br>
<small>Tarkastanut: 藥提醒科技有限公司 (yao.care)</small>
</div>
