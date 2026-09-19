---
layout: default
title: Avelumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Avelumab
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

## Avelumab: Arviointiraportti — Riittämätön tieto täydellisen uudelleenkäyttötarkoituksen analysointiin

## Yhden lauseen yhteenveto

Avelumab (DrugBank: DB11945) on täysin ihmisperäinen anti-PD-L1-monoklonaalinen vasta-aine, joka toimii tarkastuspiste-inhibiittorina, eikä sitä ole tällä hetkellä hyväksytty Taiwanissa.
Tämä todistusnippu ei sisällä TxGNN-ennustettuja indikaatioita, ja kriittiset tietokentät – mukaan lukien alkuperäinen indikaatio, toimintamekanismi ja turvallisuusprofiili – puuttuvat.
Suositellaan pidätys-päätöstä kunnes alla tunnistetut tietoaukot on ratkaistu.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei kirjattu tähän todistusnippuun |
| Ennustettu uusi indikaatio | Ei TxGNN-ennustuksia saatavilla |
| TxGNN-ennustepisteet | N/A |
| Näyttötaso | L5 — Mallin ennustus ei ole saatavilla; tukiarvioita ei ole haettavissa |
| Taiwan-markkinoiden tila | ✗ Ei markkinoilla (0 hyväksyntää) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltava päätös | **Pidätys** |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä tätä osiota ei voida saattaa loppuun. Todistusnippu ei sisällä alkuperäisen indikaation tietoja (`original_indications: []`) tai toimintamekanismin tietoja (`original_moa: [Data Gap]`), ja `predicted_indications`-joukko on tyhjä.

DrugBank-kysely (Kyselylokin tunnus 3) vahvisti, että yksi Avelumab-tietue on olemassa DrugBankissa, mutta jäsenneltyä sisältöä ei välitetty todistusnippuun. Täydellisen DrugBank-merkinnän hakeminen – mukaan lukien farmakologia, kohdemolekyylit ja kategoriat – on edellytys ennen kuin mekanistista perustelua voidaan rakentaa.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä yhtään ennustettua indikaatiota ei ole saatavilla, jotta kliinisiä tutkimuksia voitaisiin liittää siihen. Kliinisen tutkimuksen näyttöjen hakeminen lykätään kunnes TxGNN-ennuste tuottaa tuloksia.

---

## Kirjallisuuden näyttö

Tällä hetkellä yhtään ennustettua indikaatiota ei ole saatavilla, jotta kirjallisuutta voitaisiin liittää siihen. Kirjallisuuden hakeminen lykätään kunnes TxGNN-ennuste tuottaa tuloksia.

---

## Taiwan-markkinoiden tiedot

Avelumabilla ei ole hyväksyttyjä valtuuksia Taiwanissa. TFDA-kysely (Kyselylokin tunnus 1) palautti nolla tuloksia.

---

## Turvallisuuskysymykset

Viitaa pakkausselosteeseen turvallisuustiedoista.

> Huomautus: TFDA-pakkausselosteen kysely (Kyselylokin tunnus 4) palautti 1 tuloksen, mikä osoittaa, että pakkausselostedokumentti saattaa olla olemassa. Jäsenneltyä turvallisuussisältöä – varoituksia, vasta-aiheita ja lääkkeiden välisiä vuorovaikutuksia – ei lisätty tähän todistusnippuun. Lääkkeiden välisen vuorovaikutuksen kysely (Kyselylokin tunnus 2) ei palauttanut tuloksia.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätys**

**Perustelut:**
Tämä todistusnippu on rakenteellisesti epätäydellinen – ei ennustettuja indikaatioita, ei alkuperäisen indikaation tietoja, ei mekanismia (MOA) eikä turvallisuustietoja. Uudelleenkäyttötarkoituksen arviointia ei voida suorittaa ilman näitä tuloja.

**Jatkamista varten tarvitaan seuraavaa:**

- **[Blocking — DG001]** Jäsentele TFDA-pakkausseloste ottaaksesi vasta-aiheet ja päävaroitukset; tämä vaaditaan ennen mitään turvallisuuden seulontaa (S1-portti)
- **[High — DG002]** Hae täysi Avelumab-merkintä DrugBank API:sta toimintamekanismin, farmakologisten kohteiden ja lääkkeen kategorioiden täyttämiseksi
- **[Required]** Suorita TxGNN-ennusteprosessi Avelumabille (DB11945) luodaksesi `predicted_indications` tautipisteet, kliinisen tutkimuksen linkit ja kirjallisuusviitteet
- **[Required]** Vahvista alkuperäinen/-et hyväksytty/-yt indikaatio(t) DrugBankista tai TFDA-pakettiselosteesta ankkuroidaksesi uudelleenkäyttötarkoituksen vertailun
- **[Recommended]** Kun mekanismi on vahvistettu, tarkista täyttääkö Avelumab antineoplastiset/sytotoksiset kriteerit määrittääksesi, vaaditaanko Sytotoksisuus-osio lopullisessa raportissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

