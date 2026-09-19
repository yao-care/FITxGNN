---
layout: default
title: Aztreonam
parent: Pelkkä mallin ennuste (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: Lääkkeen uudelleenkäyttötarkoituksen arviointi — riittämättömät tiedot jatkamiseen

## Yhden lauseen yhteenveto

Aztreonam (DB00355) on gramnegatiivisia bakteeri-infektioita hoitava monobaktaami-β-laktaami-antibiootti. Nykyinen Evidence Pack ei sisällä **TxGNN-ennustettuja indikaatioita**, ja kriittiset tiedot — mukaan lukien alkuperäiset indikaatiot, vaikutusmekanismi ja turvallisuusvaroitukset — eivät ole vielä täytetty. Muodollista uudelleenkäyttötarkoituksen arviointia ei voida viimeistellä, ennen kuin nämä tietovajeet korjataan.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei saatavilla (sääntelyä koskevaa tietoa ei haettu) |
| Ennustettu uusi indikaatio | Ei saatavilla (ei TxGNN-tulosta) |
| TxGNN-ennusteen pistemäärä | N/A |
| Todisteen taso | N/A — ennusteita ei ole luotu |
| Suomen markkinatilanne | ✗ Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi arviointia ei voida jatkaa

Aztreonamia koskevassa Evidence Pack -asiakirjassa puuttuu kolme tiedon luokkaa, jotka ovat kaikki välttämättömiä ennen kuin uudelleenkäyttötarkoitusta voidaan arvioida:

**1. TxGNN-ennusteita ei ole luotu.** `predicted_indications`-taulukko on tyhjä. Ilman mallin ennustamaa kohdeindikaatiota ei ole kandidaattihypoteesia arvioitavaksi — jokainen myöhempi osio (todisteiden tarkistus, mekanistiset perustelut, kliinisen tutkimuksen kartoitus) riippuu tästä tuloksesta.

**2. Vaikutusmekanismia ei ole tallennettu.** `original_moa`-kenttä on merkitty korkean vakavuuden tievajeksi. Vaikka ennusteita olisikin saatavilla, mekanistinen uskottavuus — lääkkeen uudelleenkäyttötarkoituksen perusteluiden keskeinen tekijä — ei voi olla arvioitavissa ilman tietoa siitä, miten lääke vaikuttaa molekyylitasolla.

**3. Alkuperäisen indikaation tietoja ei ole strukturoitu.** `original_indications`-taulukko on tyhjä, eikä Suomea (Fimea) koskevia markkinoille pääsemisen hyväksynnöistä ole olemassa. Vaikka Aztreonam tunnetaan yleisesti monobaktaami-antibiootiksi, joka vaikuttaa aerobisten gramnegatiivisten bakteerien vastaisesti, tämä Evidence Pack ei sisällä jäsenneltyä tai sääntelyä koskevaa indikaation tekstiä, johon uudelleenkäyttötarkoituksen analyysi voitaisiin ankkuroida.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole saatavilla liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla liittyviä kirjallisuuslähteitä.

---

## Suomen markkinatiedot

Aztreonam ei ole tällä hetkellä markkinoitu Suomessa. Fimealla ei ole merkintöjä nollasta markkinoille pääsemisen hyväksynnöistä.

---

## Turvallisuusnäkökulmat

Katso pakkausselosteesta turvallisuustietoja.

*(Turvallisuusvaroitukset ja vasta-aiheet on merkitty estäväksi tievajeksi; DDI-kysely ei tuottanut tuloksia.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Evidence Pack ei sisällä TxGNN-ennusteita ja siinä on kolme ratkaisematonta tievajetta (Estävä: turvallisuusvaroitukset; Korkea: vaikutusmekanismi; Rakenteellinen: alkuperäiset indikaatiot). Ei ole uudelleenkäyttötarkoituksen hypoteesia arvioitavaksi, eikä turvallisuutta voida arvioida millekään uudelle indikaatiolle.

**Jatkamiseksi tarvitaan seuraavat:**

- **TxGNN-mallin tulos** — suorita uudelleen ennusteen putkisto DB00355:lle ja täytä `predicted_indications` pisteytetyillä kandidaateilla
- **Vaikutusmekanismi** — kysy DrugBank API:sta Aztreonamin farmakodynamiikkaa ja kohdeproteiineja
- **Pakkausselosteesta turvallisuustiedot** — lataa ja jäsentele Fimean tai TFDA:n pakkausseloste turvallisuusvaroitusten, vasta-aiheet ja erityispopulaation ohjeiden poimintaa varten
- **Täsmennä uudelleenkäyttötarkoituksen laajuus** — vahvista, onko tarkoituksena infektiotauti (esim. resistentit gramnegatiiviset patogeenejä, kystiseen fibroosiin tarkoitettu hengitettävä muoto) vai usean terapia-alueen uudelleenkäyttötarkoituksen kokeilu, sillä tämä määrittää, mitä TxGNN-tautinimikkeistöä tulisi kysyä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

