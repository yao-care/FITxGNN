---
layout: default
title: Azathioprine
parent: Pelkkä mallin ennuste (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: Arviointiraportti — Riittämätön tieto uudelleenkäytön arviointiin

## Yhden lauseen yhteenveto

Azathioprine (DB00993) on ehdokas, joka on toimitettu TxGNN-lääkkeen uudelleenkäyttöarvioinnissa. Kuitenkin tämä Evidence Pack sisältää **ei yhtään ennustettuja uusia indikaatioita**, **ei toimintamekanismin tietoja** ja **ei turvallisuustietoja**, mikä tekee täydellisen uudelleenkäytön arvioinnin mahdottomaksi tässä vaiheessa. Tietojen korjaustoimenpide on tarpeen ennen kuin arviointi voidaan jatkaa.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei saatavilla tässä Evidence Packissa |
| Ennustettu uusi indikaatio | Ei TxGNN-ennusteita luotu |
| TxGNN-ennustepisteet | N/A |
| Todisteiden taso | N/A — Ei ennusteita saatavilla |
| Suomen markkinatilanne | Ei myyntilupia |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | **Pidätä** |

---

## Suomen markkinatiedot

Azathioprinella ei tällä hetkellä ole **myyntilupia** Suomessa 2026-03-29 kerättyjen tietojen perusteella. Tuoteluetteloita, annosmuotoja tai hyväksyttyjä indikaatioita ei ole kirjattu.

---

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustiedot.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Azathiopriinin Evidence Packista puuttuu kaikki kolme osaa, jotka vaaditaan uudelleenkäyttöarvioinnissa: TxGNN-ennusteet, toimintamekanismin tiedot ja turvallisuus-/kontraindikaatiotiedot. Mitään suositusta uudelleenkäytön puolesta tai vastaan ei voida antaa ennen kuin nämä puutteet on ratkaistu.

**Jatkamisen edellytyksenä seuraavat asiat ovat tarpeen:**

- **\[Estävä\] Ennustetut indikaatiot**: `predicted_indications`-matriisi on tyhjä. Suorita TxGNN-putkilinja uudelleen DB00993:lle saadaksesi ehdokas-indikaatiot pistein, tukevia kliinisiä tutkimuksia ja kirjallisuusviitteita.
- **\[Estävä\] Turvallisuustiedot (DG001)**: Tärkeitä varoituksia ja kontraindikaatioita ei haettu. Lataa ja jäsennä pakkausseloste PDF-tiedosto asianosaiselta sääntelyviranomaiselta S1-turvallisuuden esiarvioinnin vaiheen käyttöönottamiseksi.
- **\[Korkea\] Mekanismin toiminta (DG002)**: MOA-tietoja ei ole. Kyselyä DrugBank-API:ta DB00993:lle täyttämään `original_moa`, jota vaaditaan arvioinnin mekanistisen perustelun osassa.
- **\[Suositeltu\] Alkuperäiset indikaatiot**: `original_indications`-kenttä on tyhjä. Täytä tämä DrugBankista tai pakkausselosteesta, jotta voidaan kirjoittaa "X:stä Y:lle" -narratiivi uudelleenkäytössä.

Kun yllä olevat tietojen puutteet on ratkaistu ja Evidence Pack on uudelleen luotu versiossa 5 tai uudempi, täydellinen arviointiraportti voidaan tuottaa.

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

