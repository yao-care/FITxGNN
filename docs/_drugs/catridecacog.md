---
layout: default
title: Catridecacog
parent: Pelkkä mallin ennuste (L5)
nav_order: 92
evidence_level: L5
indication_count: 3
---

# Catridecacog
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaseutin arviointiraportti

</div>

# Catridecacog: määrittämättömästä alkuperäisestä käyttöaiheesta verihiutaleiden primaarisen vapautumishäiriöön

## Yhden lauseen tiivistelmä

Catridecacog (DrugBank DB09310, rekombinantti-koagulaatiotekijä XIII A-yksikkö) on nykyisessä näyttöpaketissa ilman alkuperäisen käyttöaiheiston ja vaikutusmekanismin tietoja. TxGNN-malli ennustaa mahdollisen yhteyden **verihiutaleiden primaarisen vapautumishäiriöön**, ennuste-pistemäärällä **99,29 %**, mutta tätä suuntaa tukee tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua**.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen käyttöaihe | Ei saatavilla näyttöpaketista (ei Suomen myyntilupa-tietoja, `original_indications` tyhjä) |
| Ennustettu uusi käyttöaihe | Verihiutaleiden primaarinen vapautumishäiriö |
| TxGNN ennuste-pistemäärä | 99,29 % |
| Todistusaineiston taso | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä catridecacogin yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla nykyisessä näyttöpaketissa, eikä alkuperäistäkään käyttöaihetta ole dokumentoitu (DrugBank-haku ei palauttanut `original_moa`-tietoja, eikä Taiwan/Suomen myyntilupaa ole käytettävissä hyväksytyn käytön päättelemiseen).

Lääkkeen identiteetin perusteella rekombinantti-koagulaatiotekijä XIII A-yksiköstä ja TxGNN-ennusteen mukaan toimitetusta mekanistisesta perustelusta biologinen yhteys ennustettuun käyttöaiheseen on heikko eikä vahva:

Verihiutaleiden primaarinen vapautumishäiriö johtuu verihiutaleiden granuulien (tiheät granuulit/alfa-granuulit) vapautumisen häiriöstä, joka heikentää verihiutaleen aktivaation signaloinnin toisioamplifikaatiota — primaarisen hemostaasin häiriö. Koagulaatiotekijä XIII puolestaan vaikuttaa koagulaatiokaskadin viimeisessä vaiheessa, ristiinkytkien fibriinin monomeereita jo muodostuneen hyytymen stabilisoimiseksi. Sillä ei ole suoraa biokemiallista suhdetta verihiutaleiden granuulien vapautumismekanismiin; enintään se voisi vaikuttaa epäsuorasti hyytymen yleisellä stabilisaatiolla. **Lääkkeen ja ennustetun käyttöaiheeseen välinen mekanistinen yhteys on eksplisiittisesti arvioitu heikoksi.**

Tämä tarkoittaa, että ennustetta tulisi lukea mallin hypoteesin generoivana signaalina pikemminkin kuin mekanistisesti hyvin tuetuksi uusien käyttöaiheisiin ehdotukseksi.

---

## Kliinisten tutkimusten todistusaineisto

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia

---

## Kirjallisuustodistusaineisto

Tällä hetkellä ei ole saatavilla asiaan liittyvää kirjallisuutta

---

## Turvallisuusasiat

Katso pakkausselosteen turvallisuustiedot.

*(Huomio: TFDA-pakkausselosteen varoitukset/vasta-aiheet on merkitty **estäväksi** tietovajeeksi (DG001) tässä näyttöpaketissa — tämä on ratkaistava ennen S1-turvallisuusarviointia.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Ennuste perustuu yksinomaan TxGNN-mallin pistemäärään (L5-todistusaineiston taso) ilman kliinisten tutkimusten tai kirjallisuuden tukea. Toimitettu mekanistinen perustelu arvioi biologisen yhteyden heikoksi — koagulaatiotekijä XIII:n fibriinin ristiinkytkentärooli ei suoraan käsittele verihiutaleiden granuulien vapautumisen häiriötä, joka on tämän käyttöaiheeseen taustalla.

**Etenemiseksi tarvitaan seuraavaa:**
- TFDA-pakkausseloste (varoitukset/vasta-aiheet) — estää tällä hetkellä (DG001)
- Vaikutusmekanismin tieto (MOA) DrugBank API:n kautta — korkean vakavuusasteen tietovajeessa (DG002)
- Prekliiniset tai tapaus-tasoisen todistusaineistot, jotka erityisesti linkittävät koagulaatiotekijä XIII:n lisäämisen verihiutaleiden vapautumishäiriöihin, pseudo-von Willebrandi-tautiin tai Glanzmannin trombasteniaan (tämän näyttöpakkauksen kaksi muuta kandidaattia sisältävät saman L5/Pidätä-statuksen ja yhtä heikkoja mekanistisia linkkejä)
- Vahvistus koagulaatiotekijä XIII:n alkuperäisestä hyväksytystä käyttöaihesesta, koska mitään ei ole tällä hetkellä tiedostossa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

