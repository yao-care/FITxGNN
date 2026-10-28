---
layout: default
title: Roxadustat
parent: Pelkkä mallin ennuste (L5)
nav_order: 389
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Roxadustat: ennustettu uusi käyttöaihe Kuivasilmäisyys (dry eye syndrome) (näytön taso L5). Alkuperäinen käyttöaihe: Anemia"
monitor_inn: "ROXADUSTAT"
predicted_indications: ["dry eye syndrome", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma"]
---

# Roxadustat
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
{: .fs-6 .fw-300 }

---

## Sisällysluettelo
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

## Roksadustaatti: Kuivasilmäisyys
{: .text-alpha }

## Yhden lauseen yhteenveto

Roksadustaatti on HIF-prolyylihydroksylaasin estäjä, jota on alun perin käytetty kroonisen munuaisten vajaatoiminnan aiheuttaman anemian hoitoon.
TxGNN-malli ennustaa sen voivan olla tehokas **kuivasilmäisyyden** hoidossa, mutta ennusteen tueksi ei ole toistaiseksi **yhtään kliinistä tutkimusta eikä julkaisua**. Ennuste perustuu pelkästään mallilaskentaan.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Anemia; krooninen munuaisten vajaatoiminta |
| Ennustettu uusi käyttöaihe | Kuivasilmäisyys (dry eye syndrome) |
| TxGNN-ennusteen pistemäärä | 0,9951 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on perusteltu?

Roksadustaatti estää HIF-prolyylihydroksylaasientsyymejä (mm. EGLN2) ja vakauttaa siten HIF-1/2-alfa-tekijöitä. Tarkempaa mekanismitietoa ei ole tällä hetkellä saatavilla tähän raporttiin koottujen tietojen perusteella, joten mekanistinen arvio on rajallinen.

HIF-signalointi vaikuttaa tulehdukseen, hypoksiavasteisiin sekä epiteelin ja sarveiskalvon korjautumiseen. Siksi teoreettinen yhteys silmän pinnan sairauksiin on olemassa. Alkuperäinen käyttöaihe (anemia) ja kuivasilmäisyys ovat kuitenkin kliinisesti hyvin kaukana toisistaan, eikä yhtäläisyyttä alkuperäiseen käyttöaiheeseen ole arvioitu.

Vaikutus on lisäksi kontekstiriippuvainen: HIF:n aktivointi voi edistää uudissuonittumista ja vaikuttaa tulehdukseen kumpaankin suuntaan. Korkea pistemäärä (0,9951) on laskennallinen ennuste, ei näyttöä tehosta.

### Muut mallin ennustamat käyttöaiheet

| Sija | Käyttöaihe | Pistemäärä | Näytön taso | Huomio |
|------|------|------|------|------|
| 2 | Luun Pagetin tauti | 0,9912 | L5 | Spekulatiivinen yhteys luun uudelleenmuovautumiseen; vaikutussuunta epävarma (HIF voi lisätä myös osteoklastogeneesiä). Vakiohoitona bisfosfonaatit. |
| 3 | Dentinogenesis imperfecta | 0,9906 | L5 | Geneettinen rakenneproteiinivika (pääosin DSPP); mekanistinen yhteys heikko. |
| 4 | Levyepiteelisyöpä | 0,9902 | L5 | HIF-aktivaatio liittyy kasvaimen etenemiseen ja hoitoresistenssiin, joten kyse on pikemminkin turvallisuushuolesta kuin hoitoperusteesta. |

## Kliininen tutkimusnäyttö

Toistaiseksi ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Toistaiseksi ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004871 | Evrenzo (Astellas Pharma Europe B.V.) | – | Anemia; krooninen munuaisten vajaatoiminta (tila: peruutettu) |

## Turvallisuushuomiot

- **Lääkeyhteisvaikutukset ja farmakologia**: Yhteisvaikutushaussa löytyi yksi farmakologinen kohde: roksadustaatti estää EGLN2-entsyymiä (egl-9 family hypoxia inducible factor 2). Kyse on lääkkeen vaikutuskohteesta, ei kliinisestä yhteisvaikutuksesta, eikä vakavuusluokkaa ole annettu.
- **Teoreettinen turvallisuushuoli**: HIF:n vakauttaminen voi edistää kasvaimen etenemistä ja uudissuonittumista, mikä on tärkeää huomioida erityisesti syöpäkäyttöaiheissa ja silmän alueella.

Muilta osin tarkemmat turvallisuustiedot, varoitukset ja vasta-aiheet löytyvät valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkkään mallilaskentaan (L5): kliinisiä tutkimuksia ja julkaisuja ei ole, mekanismitieto puuttuu ja Suomessa valmisteen myyntilupa on peruutettu.

**Jatkotoimiin tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kokoaminen (turvallisuusarvion estävä puute)
- Tarkempi vaikutusmekanismitieto
- Prekliininen näyttö HIF-estäjän vaikutuksesta silmän pinnan sairausmalleissa
- Antoreittien soveltuvuuden arviointi (esim. paikallinen silmään annettava valmiste, sillä tähän ei ole tietoa)
- Turvallisuusarvio uudissuonittumiseen ja kasvainriskiin liittyen ennen mitään jatkotyötä
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

