---
layout: default
title: Axicabtagene Ciloleucel
parent: Pelkkä mallin ennuste (L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Axicabtagene Ciloleucel
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

# Aksikabtageen siloleuseeli: Uudelleenkäyttöarviointi — riittämätön näyttöpaketti

## Yhden lauseen yhteenveto

Aksikabtageen siloleuseeli (DB13915) on CD19-suunnattu CAR-T-soluimmunoterapia; nykyisen näyttöpaketin sisältö ei kuitenkaan sisällä alkuperäisen indikaation tietoja, ei TxGNN-ennustettuja indikaatioita eikä toimintamekanismin tietoja.
Ilman ennustettua uutta indikaatiota tavanomaista uudelleenkäyttöarviointia **ei voida suorittaa tällä hetkellä**.
Suositeltu toimenpide on korjata kaikki estävät/korkean vakavuuden tietoaukot ennen prosessin uudelleenkäyttöä.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei tallennettu näyttöpaketissa |
| Ennustettu uusi indikaatio | Ei mitään — TxGNN ei palauttanut ennusteita |
| TxGNN-ennusteen pistemäärä | N/A |
| Näyttötaso | N/A (ei ennusteita luotu) |
| Suomen markkinatilanne | Ei markkinoilla (0 hyväksyntää) |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Pidätys** |

---

## Miksi ennustetta ei ole saatavilla

Näyttöpaketin `predicted_indications`-taulukko on tyhjä. Tämä tapahtuu tyypillisesti yhdestä kahdesta syystä:

1. **Mallin laajuus**: TxGNN-tietokanta ei välttämättä sisällä DrugBank-solmua `DB13915`:lle (aksikabtageen siloleuseeli), koska CAR-T-solujen terapiat ovat eläviin soluihin perustuvia tuotteita, joiden esitys tietokannassa eroaa pienimolekyylilääkkeiden esityksestä.
2. **Prosessin aukko**: Ennustevaihetta ei välttämättä ole suoritettu, tai tautikartitusvaihe (KG → MeSH/ICD) ei tuottanut yhtään vastaavia ehdokkaita kynnysarvon yläpuolella.

Tällä hetkellä yksityiskohtaiset toimintamekanismin tiedot eivät myöskään ole saatavilla. Tunnettujen tietojen perusteella aksikabtageen siloleuseeli kuuluu CD19-kohdentavien CAR-T-soluterapioiden luokkaan; sen teho relapsseissa/refraktaarisessa laajassa B-solutahdissa on osoitettu rekisteröintiinterventiossa, ja mekanismisesti lähestymistapa voisi periaatteessa laajentua muihin CD19-ilmaiseviin hematologisiin maligniteetteihin — mutta **tätä ei voida muodollisesti arvioida ilman näyttöpaketin tietoja**.

---

## Kliiniset tutkimukset

Näyttöpaketissa ei ole tällä hetkellä siihen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuusväitteet

Näyttöpaketissa ei ole tällä hetkellä aiheeseen liittyviä kirjallisuuslähteitä.

---

## Suomen markkinatiedot

Tässä näyttöpaketissa ei ole aksikabtageen silolesueelille merkittyjä markkinointihyväksynnän tietoja.

---

## Sytotoksisuus

Aksikabtageen siloleuseeli on kasvainsytostaattinen solutuote (CD19:tä kohdennettu CAR-T-immuuniterapia). Seuraavat tiedot on huomioitu tässä ajossa haetussa DrugBank-tietueesta; yksityiskohtaisia pakkausesite-toksisuustietoja ei jäsennetty näyttöpaketiksi.

| Kohde | Sisältö |
|------|---------|
| Sytotoksisuuden luokittelu | Soluimmuuniterapia (CAR-T; ei tavanomainen sytotoksinen) |
| Ydinliemen sortumisenriski | Korkea — sytokiinin vapautumisen oireyhtymä ja hematologinen toksisuus ovat CAR-T-terapioiden luokan vaikutuksia |
| Emetisyysluokittelu | Alhainen (ensisijainen toksisuus on CRS/neurotoksisuus, ei pahoinvointia) |
| Seurantakohteet | Täydellinen verikuvio differentiaalilla, maksanfunktio, munuaisten toiminta, neurologinen asema, ferritiini, CRP (CRS-seuranta) |
| Käsittelyn varotoimet | On noudatettava genetiikasti muunnettujen solutuotteiden käsittelyä koskevia ohjeita; tavanomaiset sytotoksisten aineiden käsittelyvarotoimet soveltuvat |

> **Huomio:** Yllä oleva perustuu CAR-T-luokan tietoihin. Katso täydelliset pakkausesite-tiedot (Yescarta® SmPC) tuottekohtaisista varoituksista ja varotoimista.

---

## Turvallisuusnäkökohdat

Katso pakkausesite-turvallisuustietoja.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätys**

**Perustelut:**
Näyttöpaketti ei sisällä ennustettuja indikaatioita, alkuperäisen indikaation tietoja eikä toimintamekanismin tietoja; lääkkeen uudelleenkäyttöarviointia ei voida mielekkäällä tavalla suorittaa tai pisteyttää ilman näitä syöttötietoja.

**Jatkamista varten tarvitaan seuraavat:**

- **[DG001 — Estävä]** Hae TFDA:n (tai EMA:n/FDA:n) pakkausesite-PDF ja jäsennä varoitukset, vasta-aiheet ja hyväksytyt indikaatiot
- **[DG002 — Korkea]** Kysy DrugBank API:sta MOA-, farmakologisia ja lääkkeiden luokittelutietoja `DB13915`:lle
- **Suorita TxGNN-prosessi uudelleen** sen jälkeen kun olet vahvistanut, että `DB13915`-solmu on olemassa tietokannassa ja että ennuste- ja tautikartitusvaihe saa päätökseen
- **Vahvista KG-solmun tyyppi**: Vahvista, onko aksikabtageen siloleuseeli mallinnettu pienimolekyyliseksi solmuksi vai biologia/soluterapia-solmuksi TxGNN-graafissa, koska tämä vaikuttaa ennusteen kattavuuteen
- Kun ennusteet ovat saatavilla, luonti uudelleen tämä näyttöpaketti (v5+) ja uudelleenkäyttö arviointi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

