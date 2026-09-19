---
layout: default
title: Basiliximab
parent: Pelkkä mallin ennuste (L5)
nav_order: 63
evidence_level: L5
indication_count: 0
---

# Basiliximab
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

# Basiliximab: Elimistön siirtymisen hylkäämisen estosta — TxGNN-uudelleenkäyttöennusteet eivät ole saatavilla

## Yhden lauseen yhteenveto

Basiliximab (Simulect®) on kimeeerinen monoklonaalinen vasta-aine, joka kohdistuu IL-2-reseptoriin (CD25), ja se on kliinisesti vahvistettu akuutin hylkäämisen estoon munuaisen siirtymisillä.
Nykyinen aineistokokonaisuus sisältää **ei TxGNN-uudelleenkäyttöennusteita** tälle lääkkeelle, mikä tarkoittaa, että uutta indikaatiota ei voida vielä arvioida.
Tämä raportti dokumentoi tietojen tilan ja suosittelee seuraavat vaiheet, jotka tarvitaan ennen kuin uudelleenkäyttöarviointi voidaan aloittaa.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Akuutin elimistön siirtymisen hylkäämisen esto munuaisen siirrosta (IL-2-reseptoritantagonisti, DrugBank DB00074 mukaan) |
| Ennustettu uusi indikaatio | Ei saatavilla — TxGNN-ennuste-pipeline palautti ei kandidaatteja |
| TxGNN-ennustepistemäärä | N/A |
| Todistusaineiston taso | N/A — Ei ennustetta arvioitavaksi |
| Suomen markkinatilantieto | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi ennustetta ei ole saatavilla

Basiliximab on kimeeerinen monoklonaalinen vasta-aine (IgG1κ), joka kohdistuu interleukiini-2-reseptorin (CD25) α-ketjuun ja ilmenee aktivoiduilla T-lymfoyyteillä. Kilpailemalleen estämällä IL-2:n sitoutumista basiliximab tukahduttaa T-solujen klonaalisen leviämisen, mikä vähentää akuutin hylkäämisreaktion allogeneettisen siirtymisen jälkeen.

TxGNN-tietokaavion malli perustuu rikkaaseen farmakologiseen ja sairauden assosiaatiotietoihin uudelleenkäyttökandidaattien luomiseksi. Aineistokokonaisuus osoittaa, että kriittiset syötteet — mukaan lukien lääkkeen toimintamekanismin merkintä ja alkuperäisen indikaation luokittelu — merkittiin tietorakoina pipeline-suorituksen aikana. Näiden jäsenneltyjen syötteiden puuttuminen on todennäköisin syy siihen, että malli palautti tyhjän ennustelistan.

On olemassa nousevia epävirallisia kliinisiä kiinnostuksia basiliximabille **isännän vastaan siirtymisen reaktio (GVHD)** ja steroideja vastustaville tulehduksellisille tiloille, mikä viittaa perustelluun biologiseen perusteluun uudelleenkäytölle, kun pipeline-syötteet viimeistellään ja ajetaan uudelleen.

---

## Suomen markkinatiedot

Basiliximab ei ole tällä hetkellä rekisteröity Suomessa. Markkinointihyväksyntöjä ei löytynyt 29.3.2026 suoritetussa sääntelyhakussa.

> **Huomautus:** Basiliximab (Simulect®) on EMA-hyväksytty akuutin elimistön siirtymisen hylkäämisen estoon de novo -allogeneettisissa munuaisen siirroissa aikuisten ja pediatristen potilaiden osalta, mikä voi toimia perusteena tulevalle suomalaiselle markkinahakemukselle. EMA-dokumentaatioon voidaan viitata vertailulähteinä.

---

## Turvallisuusnäkökohdat

Yksityiskohtaisia turvallisuustietoja (varoitukset, vasta-aiheet, lääkkeiden väliset vuorovaikutukset) ei ollut saatavilla tämän arviointikierroksen aineistokokonaisuudessa. Täydellisten turvallisuustietojen osalta viitatkaa viralliseen pakettitarroihin ja EMA:n tuotetietoihin, mukaan lukien post-siirtymälymfoproliferatiivisen häiriön riski, sytokiinin vapautumisen oireyhtymän varotoimet ja immunosupressio-suhteinen infektioriskit.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
TxGNN-ennuste-pipeline palautti ei kandidaatti-indikaatioita basiliximabille, ja kriittiset syöttökentät (MOA-merkintä, alkuperäisen indikaation luokittelu) merkittiin estäviksi tietorakoiksi. Ilman ennustetavoitetta uudelleenkäytön todistusaineiston arviointia ei voida suorittaa.

**Jatkaaksesi tarvitaan seuraavat:**

1. **Täydennä MOA-tietoraon (DG002):** Kysy DrugBank API:a jäsenneltyjen farmakologian tietojen osalta ja täytä `original_moa`-kenttä niin, että tietokaavio voi rakentaa oikeat solmun upotukset.
2. **Luokittele alkuperäinen indikaatio (DG001):** Kartoita basiliximab jäsennettyyn sairauden ontologian termiin (esim. MONDO tai ICD-10 "munuaisen allosiirron hylkäämisen esto") ja suorita TxGNN-ennuste-pipeline uudelleen.
3. **Suorita TxGNN uudelleen:** Kun ratkaiset yllä olevat raot, suorita ennuste-pipeline; kandidaatti-indikaatiot (esim. GVHD, autoimmunipneumatiikka) odotetaan ilmestyvän.
4. **Hanki turvallisuuden lähdetiedot:** Lataa ja jäsennä EMA/TFDA-pakettitarra-PDF täyttääksesi varoitus- ja vasta-aihe-kentät ennen kuin siirryt turvallisuuden seulontavaiheeseen (S1).
5. **Vahvista Suomen rekisteröintireitti:** Jos uudelleenkäyttökandidaatti tunnistetaan, arvioi, voiko EMA-hyväksytty siirtymisen hylkäämisen esto-indikaatio ankkuroida rivi-laajennushakemuksen Suomessa.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

