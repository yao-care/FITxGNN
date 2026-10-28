---
layout: default
title: Avatrombopag
parent: Pelkkä mallin ennuste (L5)
nav_order: 56
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Avatrombopag: ennustettu uusi käyttöaihe Marcothrombocytopenia with mitral valve insufficiency (näytön taso L5). Alkuperäinen käyttöaihe: Trombosytopenia"
monitor_inn: "Avatrombopag"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "dense granule disease", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "lower motor neuron syndrome with late-adult onset", "Mills syndrome", "monomelic amyotrophy"]
---

# Avatrombopag
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **9** kpl
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

## Avatrombopaagi: Trombosytopeniasta marcothrombocytopenia with mitral valve insufficiency -ennusteeseen
{: .text-alpha }

## Yhden lauseen yhteenveto

Avatrombopaagi on trombopoietiinireseptorin (TPO-R) agonisti, jota on alun perin käytetty **trombosytopenian** hoitoon. TxGNN-malli ennustaa sen voivan tehota ensisijaisesti sairauteen **marcothrombocytopenia with mitral valve insufficiency** (perinnöllinen makrotrombosytopenia, johon liittyy mitraaliläpän vuoto). Ennuste perustuu pelkästään laskennalliseen malliin: **kliinisiä tutkimuksia ja julkaisuja ei ole**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Trombosytopenia |
| Ennustettu uusi käyttöaihe | Marcothrombocytopenia with mitral valve insufficiency |
| TxGNN-ennustepisteet | 1.0000 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on perusteltu?

Avatrombopaagi on suun kautta otettava TPO-R:n (MPL-geeni) agonisti. Se edistää megakaryosyyttien lisääntymistä ja siten verihiutaleiden tuotantoa. Solukokeissa sen EC50-arvo reseptorin aktivaatiolle oli 3,3 nM, ja suurin vaikutus vastasi rekombinantin ihmisen trombopoietiinin vaikutusta. Lääkkeen alkuperäistä vaikutusmekanismia koskevaa yksityiskohtaista tietoa ei ole tässä aineistossa saatavilla.

Alkuperäinen käyttöaihe, trombosytopenia, ja ennustettu käyttöaihe ovat molemmat sairauksia, joissa verihiutaleita on liian vähän. Mekanistinen yhteys on uskottava vain, jos verihiutalepuutos johtuu vähentyneestä tuotannosta ja megakaryosyyttilinja vastaa edelleen TPO-R-signalointiin. Mitraaliläpän vuotoa lääke ei todennäköisesti korjaa.

Muut ennustetut käyttöaiheet ovat heikommin perusteltuja:
- **Hereditary thrombocytopenia with normal platelets** ja **transient neonatal thrombocytopenia**: mekanismi on uskottava, mutta tautinimike on epäselvä (mahdollinen ontologia-artefakti) tai tila paranee itsestään, eikä vastasyntyneiden turvallisuustietoa ole.
- **Dense granule disease**: kyseessä on ensisijaisesti verihiutaleiden toimintahäiriö, joten verihiutalemäärän nosto auttaisi vain osittain.
- **ALS-sairauden ja muiden motoneuronisairauksien** (lower motor neuron syndrome, Mills syndrome, monomelic amyotrophy), sekä **polymicrogyria**: biologista yhteyttä TPO-R-agonismiin ei havaittu. Korkeat pisteet (0.9999) tulevat TxGNN-mallista (deep learning) ja voivat heijastaa mallin oppimia samankaltaisuuksia sairauksien välillä, eivät biologista näyttöä.

---

## Suomen markkinatiedot

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004722 | Doptelet | – | Trombosytopenia (voimassa) |

---

## Turvallisuusnäkökohdat

- **Lääkeaineyhteisvaikutukset**: Tässä aineistossa ei ole lueteltu varsinaisia yhteisvaikutuksia. Ainoa tieto on farmakologinen: avatrombopaagin kohde on trombopoietiinireseptori (MPL).

Tarkemmat turvallisuustiedot, varoitukset ja vasta-aiheet on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteet perustuvat pelkästään laskennalliseen malliin (L5), eikä yhtään kliinistä tutkimusta tai julkaisua tue niitä. Lisäksi Suomessa ainoa myyntilupa on peruttu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hakemista Fimeasta (turvallisuusseulonta ei ole mahdollista ilman niitä)
- Vaikutusmekanismitietojen täydentämistä DrugBankista
- Kirjallisuushakua ja kliinisten tutkimusten rekisterihakua perinnöllisistä makrotrombosytopenioista
- Tautinimikkeiden (esim. "thrombocytopenia with normal platelets") tarkistamista mahdollisten ontologia-artefaktien poissulkemiseksi
- Lapsipotilaiden ja vastasyntyneiden turvallisuustietojen arviointia, jos nämä käyttöaiheet otetaan tarkasteluun
- Myyntiluvan peruuntumisen syyn selvittämistä sekä sen vaikutusta lääkkeen saatavuuteen Suomessa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

