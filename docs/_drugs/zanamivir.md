---
layout: default
title: Zanamivir
parent: Pelkkä mallin ennuste (L5)
nav_order: 476
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Zanamivir: ennustettu uusi käyttöaihe Pyelonefriitti (näytön taso L5). Alkuperäinen käyttöaihe: Ihmisen influenssa"
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **2** kpl
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

# Tsanamiviiri: Influenssasta pyelonefriittiin

## Yhteenveto

Tsanamiviiri (zanamivir) on neuraminidaasin estäjä, jota on alun perin käytetty ihmisen influenssan hoitoon. TxGNN-malli ennustaa sen voivan tehota **pyelonefriittiin** (munuaisaltaan ja munuaisen tulehdus), mutta ennusteen tukena ei ole yhtään kliinistä tutkimusta eikä yhtään aihetta koskevaa julkaisua. Ennuste on siten vain laskennallinen hypoteesi.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Ihmisen influenssa |
| Ennustettu uusi käyttöaihe | Pyelonefriitti |
| TxGNN-ennustepisteet | 99,84 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

Toinen ennustettu käyttöaihe, tyrosiinin aineenvaihdunnan häiriö (pisteet 99,02 %), on myös L5-tasoa, ja sen kolme löydettyä julkaisua käsittelevät influenssan neuraminidaasin estäjiä eivätkä tyrosiinin aineenvaihduntaa. Sillekään ei ole perusteita edetä.

## Miksi ennuste voisi olla perusteltu?

Yksityiskohtaisia tietoja tsanamiviirin vaikutusmekanismista ei tätä raporttia varten ollut saatavilla. Tiedetään, että tsanamiviiri on viruksen neuraminidaasia estävä lääke, jonka teho influenzassa on osoitettu.

Pyelonefriitti on useimmiten bakteeri-infektio (tavallisimmin *E. coli*), ja mekanistinen yhteys tsanamiviiriin on heikko. Bakteereilla on kyllä neuraminidaasin kaltaisia entsyymejä (sialidaaseja), mutta tsanamiviirilla ei ole osoitettua antibakteerista tehoa eikä tehoa munuaisinfektioon. Korkea pistemäärä on siksi vain hypoteesia tuottava signaali, ei näyttö tehosta.

## Kliininen tutkimusnäyttö

Toistaiseksi ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Pyelonefriitin osalta aiheeseen liittyvää kirjallisuutta ei ole saatavilla.

Toiseen ennustettuun käyttöaiheeseen (tyrosiinin aineenvaihdunnan häiriö) löytyneet julkaisut eivät tue ennustetta:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [23675925](https://pubmed.ncbi.nlm.nih.gov/23675925/) | 2013 | Katsaus | Infectious Disorders Drug Targets | Oseltamiviirin resistenssin synty (H275Y-mutaatio) sekä influenssan hallinta ennen pandemiaa, sen aikana ja sen jälkeen |
| [25727669](https://pubmed.ncbi.nlm.nih.gov/25727669/) | 2015 | In vitro -menetelmätutkimus | Journal of Molecular Recognition | Pintaplasmoniresonanssimääritys neuraminidaasin eston mittaamiseen; villityypin ja H274Y-mutantin herkkyys tsanamiviirille ja oseltamiviirille |
| [21367898](https://pubmed.ncbi.nlm.nih.gov/21367898/) | 2011 | Prekliininen (virologia/eläin) | Journal of Virology | N294S-mutaation vaikutus H5N1-influenssaviruksen replikaatioon ja patogeenisuuteen |

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004102 | Dectova (peruutettu) | – | Ihmisen influenssa |

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Tietokannasta löytyi 8 mahdollista yhteisvaikutusta. Ainoa luokiteltu on kohtalainen: inhaloitava nopeavaikutteinen ihmisinsuliini. Vakavuusluokaltaan tuntemattomia ovat klaritromysiini, loratadiini, montelukasti, ketotifeeni, feksofenadiini, ibuprofeeni ja diklofenaakki.
- **Tietämysgraafiin perustuvat vasta-aiheet (ei valmisteyhteenvedosta):** epilepsia, krooninen keuhkoahtaumatauti (COPD), vaikea varhain alkava COPD, keuhkoputkisairaus ja delirium. Nämä ovat mallin tuottamia signaaleja, eivät varmennettua valmistetekstin sisältöä.

Valmisteyhteenvedon varoitukset ja vasta-aiheet tulee tarkistaa erikseen.

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteen tukena on vain korkea TxGNN-pistemäärä. Kliinistä tai kirjallista näyttöä ei ole, mekanistinen yhteys bakteeriperäiseen pyelonefriittiin on heikko, ja Suomessa ainoa myyntilupa on peruutettu.

**Eteneminen edellyttää:**
- Vaikutusmekanismin tietojen täydentämistä
- Valmisteyhteenvedon turvallisuustietojen hankkimista (estää turvallisuusseulonnan)
- Prekliinistä näyttöä tsanamiviirin vaikutuksesta uropatogeeneihin tai munuaisinfektiomalleihin
- Selvitystä lääkemuodosta ja antoreitistä (pyelonefriitti edellyttäisi todennäköisesti systeemistä altistusta)
- Arviota siitä, onko valmiste ylipäätään saatavilla Suomessa myyntiluvan peruutuksen jälkeen
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

