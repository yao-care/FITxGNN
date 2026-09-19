---
layout: default
title: Leflunomide
parent: Pelkkä mallin ennuste (L5)
nav_order: 222
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Leflunomidi: Lääkkeen uudelleenkäytön ehdokas — Arviointi keskeytettynä

## Yhden lauseen yhteenveto

Leflunomidi on immunomoduloiva tautia muokkaava reumaatinen lääke (DMARD), joka tunnetaan kliinisessä käytännössä reumatoidiartriitista ja psoriaattisesta artriitista.
Nykyinen Evidence Pack ei kuitenkaan sisällä **TxGNN:n uudelleenkäytön ennusteita** tälle lääkkeelle, ja keskeiset tietokentät, joihin kuuluvat vaikutusmekanismi, turvallisuusvaroitukset ja alkuperäisten indikaatioiden tietueet, puuttuvat.
Ilman arvioitavaa ennustettua indikaatiota tämä raportti dokumentoi tietoaukot ja suosittelee lykkäyksen päätöstä tietojen korjaamisen odotuksissa.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei kirjattu nykyisessä Evidence Packissa |
| Ennustettu uusi indikaatio | Ei mikään — TxGNN ei palauttanut ennusteita |
| TxGNN-ennusteen pistemäärä | N/A |
| Näytön taso | L5 (mallin ennuste ei saatavilla; ei tukevia tutkimuksia) |
| Myyntistatus | Ei myynnissä (Ei myynnissä) |
| Lupien määrä | 0 |
| Suositeltu päätös | **Lykkää** |

---

## Miksi ennuste ei ole saatavilla

Leflunomidin Evidence Pack (DrugBank ID: DB01097) palautti tyhjän `predicted_indications`-taulukon. Kaksi mahdollista selitystä on olemassa:

1. **Putkilinjan alkupään epäonnistuminen**: Jos lääkkeen solmu DB01097:lle ei ollut läsnä tai ei ollut asianmukaisesti upotettu TxGNN:n käyttämään tietokaaviin, malli ei tuottaisi sijoitettuja ehdokkaita.
2. **Suodatettu tulos**: Ennusteita on voitu luoda, mutta ne jäivät jälkikäsittelyn aikana käytetyn luottamustason kynnyksen alapuolelle.

Kunnes juurisyy vahvistetaan, mitään uudelleenkäytön hypoteesia ei voida arvioida. Evidence Packissa kirjatut tietoaukot (DG001: TFDA:n pakkausselosteen varoitukset; DG002: vaikutusmekanismi) rajoittavat myös turvallisuuden ja mekanismin arviointia, joka normaalisti liittyisi mihin tahansa ennustettuun indikaatioon.

---

## Markkinatiedot

Leflunomidi **ei ole myynnissä** minkään nykyisen paikallisen luvan alaisena. Sääntelykysely palautti nolla lisenssiä (total_licenses: 0), eikä doseerausmuodosta tai hyväksytystä indikaatiotiedosta ole tietoja tiedostoissa.

> Huomio: Sekä DrugBank-kysely (kyselylokin tunnus 3) että TFDA:n pakkausselosteen kysely (kyselylokin tunnus 4) palautti result_count ≥ 1, mikä osoittaa lähdetietueiden olevan olemassa. Kuitenkin tämän Evidence Packin jäsennellyt kentät eivät olleet täytettyjä näistä tuloksista. Korjauksessa tulisi uudelleen purkaa hyväksytyn indikaation teksti ja turvallisuusvaroitukset näistä vahvistetuista lähteistä.

---

## Turvallisuusnäkökohdat

Kaikki nykyisen Evidence Packin turvallisuuskentät on merkitty tietoaukoksi:

- Keskeiset varoitukset: ei saatavilla
- Vasta-aiheet: ei saatavilla
- Lääke-lääke-vuorovaikutukset: kysely ei palauttanut tuloksia

Tutustu pakkausselosteeseen ja DrugBank-tietueeseen (DB01097) turvallisuustiedoille ennen kuin jatkat arviointia.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Lykkää**

**Perustelut:**
Evidence Pack ei palauttanut TxGNN-ennusteita, ja kaksi korkean/estävän prioriteetin tietoaukkoa (MOA ja TFDA:n turvallisuusvaroitukset) eivät ole ratkenneet. Tällä hetkellä ei ole arvioitavaa uudelleenkäytön hypoteesia.

**Jatkamista varten tarvitaan seuraavaa:**

- **Suorita TxGNN uudelleen** DB01097:lle ja vahvista, onko lääkkeen solmu läsnä tietokaavissa; jos ei, lisää se ja upota uudelleen.
- **Ratkaise DG002 (MOA)**: Kysy DrugBank API:ta vaikutusmekanismista ja farmakologisesta luokasta DB01097:lle.
- **Ratkaise DG001 (turvallisuus)**: Lataa ja jäsennä TFDA:n pakkausselose-PDF purkamalla varoitukset ja vasta-aiheet; täytä `key_warnings` ja `contraindications`-kentät.
- **Täytä uudelleen original_indications**: TFDA:n pakkausselose-kysely (lokin tunnus 4) vahvisti tuloksen olevan olemassa — pura hyväksytyn indikaation teksti ja täytä kenttä ennen seuraavaa arviointisykliä.
- Kun ennustettu indikaatio on saatavilla, luo raportti uudelleen käyttämällä täyttä Evidence Pack -mallia.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

