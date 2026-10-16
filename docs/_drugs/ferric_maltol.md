---
layout: default
title: Ferric Maltol
parent: Pelkkä mallin ennuste (L5)
nav_order: 189
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Ferric Maltol: ennustettu uusi käyttöaihe Plummer-Vinsonin oireyhtymä (näytön taso L5). Alkuperäinen käyttöaihe: Raudanpuuteanemia"
---

# Ferric Maltol
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

# Ferrimaltoli: Raudanpuuteanemiasta Plummer-Vinsonin oireyhtymään

## Yhteenveto

Ferrimaltoli on suun kautta otettava rautavalmiste, jota on käytetty raudanpuuteanemian hoitoon.
TxGNN-malli ennustaa, että sillä voisi olla käyttöä **Plummer-Vinsonin oireyhtymän** hoidossa.
Ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**, joten näyttö perustuu pelkästään mallin laskennalliseen ennusteeseen.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Raudanpuuteanemia |
| Ennustettu uusi käyttöaihe | Plummer-Vinsonin oireyhtymä |
| TxGNN-ennustepistemäärä | 99,98 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Tässä raportissa käytetyissä tiedoissa ei ole saatavilla yksityiskohtaista vaikutusmekanismia. Tunnetun tiedon perusteella ferrimaltoli on suun kautta annettava raudankorvaushoito, jonka teho raudanpuuteanemiassa on osoitettu, ja mekanistisesti se voisi soveltua myös Plummer-Vinsonin oireyhtymään.

Plummer-Vinsonin oireyhtymälle (myös Paterson-Brown-Kelly-oireyhtymä) ovat tyypillisiä raudanpuuteanemia, ruokatorven kalvomaiset ahtaumat (esophageal web), nielemisvaikeus ja kielitulehdus. Taustalla olevan raudanpuutteen korjaaminen on tämän tilan hoidon perusperiaate, joten ennuste on mekanistisesti uskottava.

Ennusteeseen on kuitenkin suhtauduttava varovasti. Erittäin korkea pistemäärä johtuu todennäköisesti siitä, että lääkkeellä on jo raudanpuuteanemian käyttöaihe ja että se sijaitsee tietämysgraafissa lähellä tätä tautia, eikä riippumattomasta näytöstä. Ruokatorven ahtauma on lisäksi rakenteellinen ongelma, johon pelkkä rautahoito ei todennäköisesti riitä.

### Muut ennustetut käyttöaiheet

| Sija | Sairaus | TxGNN-pistemäärä | Arvio |
|------|------|------|------|
| 2 | B12- ja foolihaposta riippumaton konstitutionaalinen megaloblastinen anemia | 99,98 % | Mekanistinen perustelu heikko: megaloblastiset muutokset eivät yleensä johdu raudanpuutteesta. Rauta olisi relevanttia vain, jos samanaikainen raudanpuute on todettu. |
| 3 | IRIDA-oireyhtymä (raudalle reagoimaton raudanpuuteanemia) | 99,33 % | Tauti johtuu TMPRSS6-mutaatioista ja liian korkeasta hepsidiinitasosta, joka estää raudan imeytymistä suolesta. Suun kautta annettava rauta on määritelmällisesti yleensä tehotonta. Ferrimaltoli imeytyy eri reittiä kuin rauta(II)suolat, mikä on teoreettinen peruste, mutta se on silti riippuvainen suoliston imeytymisestä. Pelkkä hypoteesi. |

---

## Kliininen tutkimusnäyttö

Ei tällä hetkellä rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä saatavilla aiheeseen liittyvää kirjallisuutta.

---

## Myyntiluvat Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002733 | Feraccru (Norgine B.V.) | – | Raudanpuuteanemia (tila: peruutettu) |

---

## Turvallisuusnäkökohdat

- **Tietämysgraafiin perustuvat vasta-aiheet** (TxGNN-tietämysgraafi, ei valmisteyhteenvedon teksti): perinnöllinen hemokromatoosi, hemosideroosi, raudan aineenvaihdunnan häiriöt ja Wilsonin tauti. Nämä ovat johdonmukaisia rautavalmisteiden yleisten varoitusten kanssa (raudan ylikuormitus), mutta ne tulee varmistaa valmisteyhteenvedosta.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta. Yhteisvaikutuksia ei löytynyt tietokannasta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Kaikki kolme ennustetta perustuvat vain mallin laskennalliseen tulokseen (taso L5) ilman kliinisiä tutkimuksia tai kirjallisuutta. Lisäksi valmisteen ainoa myyntilupa Suomessa on peruutettu, mikä rajoittaa käytännön saatavuutta.

**Jatkoon siirtyminen edellyttää seuraavia:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivuilta (estää turvallisuusarvioinnin etenemisen)
- Vaikutusmekanismin (MOA) tiedot DrugBankista
- Kirjallisuushaku ja kliinisten tutkimusten haku Plummer-Vinsonin oireyhtymästä ja rautahoidosta
- Ennusteen tarkastelu erityisesti Plummer-Vinsonin oireyhtymän osalta, koska se on mekanistisesti uskottavin kandidaatti
- Selvitys valmisteen saatavuudesta, koska myyntilupa on peruutettu
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

