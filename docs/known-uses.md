---
layout: default
title: "Vain tunnetut käytöt (ei uusia ennusteita)"
nav_order: 24
permalink: /known-uses/
description: "Näiden lääkkeiden kaikki TxGNN-mallin ehdokkaat ovat jo tunnettuja käyttöjä (kirjattu tietograafiin tai myyntilupaan), joten uutta ennustettua käyttöaihett…"
---

# Vain tunnetut käytöt (ei uusia ennusteita)

Näiden lääkkeiden kaikki TxGNN-mallin ehdokkaat ovat jo tunnettuja käyttöjä (kirjattu tietograafiin tai myyntilupaan), joten uutta ennustettua käyttöaihetta ei ole. Jokaisella sivulla on tunnetut käytöt ja paikallinen markkinatilanne.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} lääkettä**

| Lääke | Raportti |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Näytä sivu]({{ drug.url | relative_url }}) |
{% endfor %}
