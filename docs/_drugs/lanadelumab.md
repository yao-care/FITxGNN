---
layout: default
title: Lanadelumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Lanadelumab: Näyttöpaketti epätäydellinen – Lääkkeen uudelleenkäyttöarviointi kesken

## Yhden lauseen yhteenveto

Lanadelumab (DrugBank: DB14597) on käyty läpi tietolinja-alustan kautta, mutta nykyisessä Näyttöpaketissa ei ole **alkuperäisiä indikaatiotietoja**, **TxGNN:n ennustamia indikaatioita** eikä **kahta ratkaisematonta tietovajausta** (yksi kriittinen, yksi korkea vakavuus). Täydellistä lääkkeen uudelleenkäyttöarviointia ei voi valmistua ennen näiden vajauksien korjaamista – tämä raportti dokumentoi nykyisen tietojen tilan ja esittelee etenemiseen tarvittavat vaiheet.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | — (tietoja ei haettu) |
| Ennustettu uusi indikaatio | — (TxGNN-ennusteita ei ole vielä luotu) |
| TxGNN-ennustepiste | — |
| Näyttöjen taso | N/A — ennustelinja ei ole tuottanut tuloksia |
| Suomen markkinatilanne | Ei markkinoilla (0 myyntilupaa) |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | **Pidätys** |

---

## Miksi mekaniikan analyysi ei ole mahdollista

Tällä hetkellä Lanadelumabin yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla tässä Näyttöpaketissa.

Kaksi tietovajausta estävät mekanistisen päättelyvaiheen:

- **DG002 (korkea vakavuus)** — MOA puuttuu DrugBank-kyselytulosteista. Ilman tätä on mahdotonta muodostaa mekaanista yhteyttä minkä tahansa alkuperäisen indikaation ja ennustetun uuden indikaation välille.
- **DG001 (kriittinen vakavuus)** — TFDA-pakkauksen sisällön varoituksia ja vasta-aiheita ei ole jäsennetty. Tämä estää pakollisen turvallisuuden esikyselyn (S1) suorittamisen.

Kunnes DG001 on ratkaistu, prosessi **ei voi edetä turvallisuuden arviointiin**. Kunnes DG002 on ratkaistu, yhtään ennustettua indikaatiota ei voida arvioida biologisen uskottavuuden näkökulmasta.

---

## Suomen markkinatiedot

Lanadelumab ei ole tällä hetkellä markkinoilla Suomessa. Myyntilupoja ei löytynyt sääntelyhallinnon kyselystä, joka toteutettiin 2026-03-29.

---

## Turvallisuusnäkökohtia

Turvallisuu­stiedot löytyvät pakkauksen sisällöstä.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätys**

**Perustelut:**
Näyttöpaketissa on nolla ennustettua indikaatiota ja se sisältää kriittisen vakavuuden tietovajauden (puuttuvat sääntelyturvallisuustiedot), mikä tekee teknisesti ja eettisesti ennenaikaiseksi antaa mitään lääkkeen uudelleenkäyttösuositusta.

**Etenemiseen tarvitaan seuraavaa:**

1. **[DG001 — kriittinen]** Lataa Lanadelumabin TFDA-pakkauksen sisältö PDF-muodossa ja jäsennä varoitukset, vasta-aiheet ja erityisväestöjen rajoitukset. Tämä on edellytys, ennen kuin mitään turvallisuuden esiarviointia voidaan suorittaa.
2. **[DG002 — korkea]** Kyselytä DrugBank API:ta (`/drugs/DB14597`) noutaaksesi vaikutusmekanismin, farmakodynamiikan ja lääkkeen luokat. Tämä vaaditaan mekanistisen uskottavuuden analyysia varten.
3. **Suorita TxGNN-ennustelinja uudelleen** DB14597:lle tuottaaksesi `predicted_indications` pisteillä, niihin liittyvät kliiniset tutkimukset ja kirjallisuuden.
4. Kun ennusteet ovat saatavilla, luo Näyttöpaketti uudelleen (v5+) ja suorita täydellinen L1–L5-näytönarviointti.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

