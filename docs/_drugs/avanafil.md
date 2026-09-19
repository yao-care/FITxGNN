---
layout: default
title: Avanafil
parent: Pelkkä mallin ennuste (L5)
nav_order: 49
evidence_level: L5
indication_count: 0
---

# Avanafil
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **0** kpl
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

# Avanafil: Lääkkeen uudelleenkäytön arviointi — Epätäydellinen näyttöpaketti

## Yhden lauseen yhteenveto

Avanafil (DrugBank: DB06237) on lääke, jota ei tällä hetkellä ole rekisteröity Taiwanissa, ja tämä näyttöpaketti sisältää **ei yhtään TxGNN-ennustamaa indikaatiota** sekä useita kriittisiä tietojen puutteita. Muodollista lääkkeen uudelleenkäytön arviointia ei voida saattaa loppuun tässä vaiheessa; suositeltu toimenpide on **Odottaa** puuttuvien tietojen korjaamisen saaksi.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu tässä näyttöpaketissa |
| Ennustettu uusi indikaatio | Ei saatavilla |
| TxGNN-ennusteen pisteet | N/A |
| Näytön taso | L5 — Mallin ennustamisen vaihetta ei saavutettu |
| Taiwanin markkinatilanne | Ei myytävänä（Ei myytävänä） |
| Autorisaatioiden lukumäärä | 0 |
| Suositeltu päätös | **Odottaa** |

---

## Miksi arviointia ei voi saattaa loppuun

TxGNN-putki palautti **nolla ennustettua indikaatiota** Avanafilillle tässä näyttöpaketissa. Kaksi kriittistä tietojen puutetta ovat suoraan vastuussa:

**1. Puuttuva toimintamekanismi (DG002 — Korkea vakavuus)**
Toimintamekanismin tiedot puuttuvat näyttöpaketista. Toimintamekanismi on keskeinen syöte TxGNN:n knowledge-graph-upotukselle. Ilman sitä lääke-sairaus-reunojen painoja ei voida laskea, ja malli ei ehkä pysty tuottamaan kandidaatti-indikaatioita.

**2. Puuttuva TFDA-pakkausselosteen varoitukset ja vasta-aiheet (DG001 — Estävä vakavuus)**
Taiwan TFDA -etiketin tiedot vaaditaan S1-turvallisuuden esi-seulontakerroksen täyttämiseen. Tämä puute on luokiteltu estäväksi, mikä tarkoittaa, että myöhemmät arviointivaiheet ovat riippuvaisia sen ratkaisusta.

Koska `predicted_indications` on tyhjä, seuraavia vakioosioita ei voida luoda, joten ne jätetään raportointisääntöjen mukaan pois: *Clinical Trial Evidence*, *Literature Evidence* ja *Taiwan Market Information*.

---

## Turvallisuusnäkökohdat

Katso pakkausselosteen turvallisuustietoja.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odottaa**

**Perustelut:**
Näyttöpaketti on rakenteellisesti epätäydellinen — ei ole TxGNN-ennustamia indikaatioita, ja kaksi kriittisin tietokohdista (toimintamekanismi ja TFDA-pakkausseloste) puuttuvat. Mielekästä uudelleenkäytön signaalia ei voida arvioida tai kertoa, kunnes nämä puutteet on korjattu.

**Seuraavaa vaihetta varten tarvitaan:**

- **[DG001 — Estävä]** Lataa ja analysoi TFDA-pakkausselosteen PDF Avanafilille hyväksyttyjen indikaatioiden, varoituksien ja vasta-aiheisten purkamiseksi; tämä avaa S1-turvallisuusseulonnan portin
- **[DG002 — Korkea]** Kysy DrugBank API:ta (`/drugs/DB06237`) toimintamekanismin hakemiseksi; tämä palauttaa täyden knowledge-graph-upotuksen kattavuuden
- Suorita TxGNN-näyttöputki uudelleen täydennetyllä lääkkeen profiililla luodaksesi sijoitetut ennustetut indikaatiot
- Vahvista DDI-tiedot vaihtoehtoisesta lähteestä (esim. DrugBank-vuorovaikutuspääte tai kliinisen farmakologian tietokanta), koska nykyinen DDI-kysely palautti `not_found`
- Kun ennustetut indikaatiot ovat käytettävissä, aloita tämä raportti uudelleen täytetyllä näyttöpaketilla (v5+)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

