---
layout: default
title: Anidulafungin
parent: Pelkkä mallin ennuste (L5)
nav_order: 33
evidence_level: L5
indication_count: 0
---

# Anidulafungin
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

# Anidulafungin: Arviointiraportti — Uudelleenkäyttökohteita ei tunnistettu

## Yhden lauseen yhteenveto

Anidulafungin (DB00362) on ekinokandiini-tyypin antimikoottinen aine, jonka käyttö on hyväksytty useilla markkinoilla kandidemian ja invasiivisen kandida-infektioiden hoitoon. TxGNN-malli ei palauttanut mitään ennustettuja uusia indikaatioita tälle lääkkeelle nykyisessä analyysiajossa. Ennusteiden puuttumisen ja Evidence Pack -tietojen moninaisista puutteista johtuen täydellistä uudelleenkäyttöarviointia ei voida suorittaa tässä vaiheessa.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei tallennettu Evidence Packiin (tunnettu käyttö: kandidemia, ruokatorven kandidiaasin) |
| Ennustettu uusi indikaatio | Ei mikään — TxGNN ei palauttanut kandidaatteja |
| TxGNN-ennusteen pistemäärä | N/A |
| Näyttöaste | L5 — Vain mallin ennuste; ei kandidaatteja arviointiin |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | **Odota** |

---

## Miksi ennustusta ei palautettu

Anidulafunginin Evidence Pack sisältää tyhjän `predicted_indications`-taulukon, mikä osoittaa, että TxGNN-tietämysgraafin neuroverkkomalli ei tunnistanut mitään sairaussolmuja, joilla olisi uudelleenkäyttöpistemäärä raportointikynnysarvon yläpuolella tälle yhdisteelle nykyisessä analyysiajossa.

Kaksi rinnakkaista tietovajaata todennäköisesti rajoittivat mallin kykyä tuottaa ennusteita:

1. **Vaikutusmekanismi (MOA) puuttuu** — Ilman strukturoituja MOA-tietoja DrugBank-muodossa (esim. entsyymien kohteet, reseptorikytkennät, polkuhuomiot), graafi-neuroverkolla on rajoitetut farmakologiset reunat, joita kulkea ja pisteytetään sairaussolmuja vastaan.

2. **Alkuperäisen indikaation luettelo on tyhjä** — Evidence Pack ei sisällä strukturoituja indikaatiomerkintöjä. Jos malli perustuu indikaatiotason kuvaajan ankkurointiin ennustuskulun aloittamiseksi, alkusolmun puuttuminen estäisi kaikki ehdokaspistemäärät.

Nämä kaksi vajausta yhdessä edustavat yhdistettyä epäonnistumista: kumpikaan "mistä" ankkuri (indikaatio) eikä "miksi" signaali (MOA) ei ole käytettävissä mallin päättelyä varten.

---

## Suomen markkinoiden tiedot

Anidulafungin **ei ole tällä hetkellä markkinoilla Suomessa**. Evidence Packissa ei ole tallennettu mitään hyväksyntöjä, tuotenimiä, annosmuotoja tai hyväksyttyjä indikaatioita.

> Vertailun vuoksi, markkinoilla, joissa se on hyväksytty (esim. USA, EU EMA:n kautta tuotenimellä Eraxis), anidulafungin on hyväksytty laskimoon annettavaksi antimikootiksi kandidemian ja invasiivisten Candida-infektioiden hoitoon, mukaan lukien ruokatorven kandidiaasin. Nämä tiedot on annettu vain viiteeksi eivätkä korvaa muodollista sääntelyhaun.

---

## Turvallisuushuomiot

Kaikki nykyisen Evidence Pack -turvallisuuskentät sisältävät tietovajeita. Tärkeitä varoituksia, vasta-aiheita tai lääkkeiden vuorovaikutustietoja ei ole saatavilla raportointia varten.

> Lisätietoja turvallisuudesta saat nykyisestä Summary of Product Characteristics (SmPC) -asiakirjasta tai pakkauksesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelu:**
TxGNN-malli ei palauttanut Anidulafunginin uudelleenkäyttökandidaatteja, ja kriittiset syötetiedot (MOA, strukturoidut alkuperäiset indikaatiot) puuttuvat — mikä tarkoittaa, että prosessilla ei ole vähimmäissyöttöä, joka tarvitaan ennusteen tuottamiseen tai arviointiin. Ilman kandidaatteja uudelleenkäyttöä ei voi perustella.

**Jatkaakseen seuraavaa on tarpeen:**

- **Ratkaise DG002 (MOA):** Kyselyy DrugBank API:a Anidulafunginin mekanistisista tiedoista (kohde: β-1,3-D-glucan synthase; prosessi: sienen seinän synteesi). Täytä `original_moa`-kenttä ja suorita TxGNN uudelleen.
- **Ratkaise DG001 (Turvallisuus):** Lataa Suomen SmPC tai EMA:n tuotemonografia ja pura tärkeimmät varoitukset ja vasta-aiheet. Täytä `key_warnings` ja `contraindications`.
- **Täytä alkuperäiset indikaatiot:** Lisää strukturoidut ICD-10 tai MeSH-sairauksien merkinnät kandidemialle ja ruokatorven kandidiaasille kenttään `original_indications`. Tämä tarjoaa kuvaajaan ankkurin TxGNN:n kulkua varten.
- **Suorita TxGNN-ennusteprosessi uudelleen** tietovajojen korjaamisen jälkeen; arvioi uudelleen, nousevatko kandidaatit alhaisemmalla pistekynnysarvolla, jos vakiokynnysarvo tuottaa edelleen nolla tuloksia.
- **Tarkista, pitääkö Eraxis tai geneerinen EMA:n keskitettyä hyväksyntää**, joka koskisi Suomea — tämä muuttaisi markkinoiden tilan "Ei markkinoilla" muotoon "Markkinoilla (EMA)".

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

