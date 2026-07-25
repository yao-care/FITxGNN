---
layout: default
title: Pelkkä mallin ennuste (L5)
nav_order: 23
permalink: /evidence-low/
description: "FITxGNN:n L5-tason ehdokkaat: pelkkä mallin ennuste, ilman kliinistä tai kirjallisuusnäyttöä."
---

# Pelkkä mallin ennuste (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Ehdokkaat, joilla on vain mallin ennuste eikä vielä lainkaan näyttöä ihmisillä
</p>

---

## Kriteerit

| Taso | Määritelmä | Kliininen merkitys |
|-------|------------|------------------|
| **L5** | Pelkkä mallin ennuste | Hypoteesivaihe; ei vielä näyttöä ihmisillä |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

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
