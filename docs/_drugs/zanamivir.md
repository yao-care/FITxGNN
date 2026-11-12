---
layout: default
title: Zanamivir
parent: Pelkkä mallin ennuste (L5)
nav_order: 476
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
description: "Zanamivir: ennustettu uusi käyttöaihe Pyelonephritis (näytön taso L5). Alkuperäinen käyttöaihe: Influenza, Human"
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

<div id="pharmacist" markdown="1">

## Farmaseutin arviointiraportti

</div>

## Zanamivir: Pyelonephritis
{: .text-alpha }

## Yhteenveto

Tsanamiviiri (zanamivir) on neuraminidaasin estäjä, jota on alun perin käytetty ihmisen influenssan hoitoon. TxGNN-malli ennustaa sen voivan tehota **pyelonefriittiin** (munuaisaltaan ja munuaisen tulehdus), mutta ennusteen tukena ei ole yhtään kliinistä tutkimusta eikä yhtään aihetta koskevaa julkaisua. Ennuste on siten vain laskennallinen hypoteesi.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Influenza, Human |
| Ennustettu uusi käyttöaihe | Pyelonephritis |
| TxGNN-ennustepisteet | 0.9984 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

Toinen ennustettu käyttöaihe, tyrosiinin aineenvaihdunnan häiriö (pisteet 0.9902), on myös L5-tasoa, ja sen kolme löydettyä julkaisua käsittelevät influenssan neuraminidaasin estäjiä eivätkä tyrosiinin aineenvaihduntaa. Sillekään ei ole perusteita edetä.

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
| EMEA/H/C/004102 | Dectova (voimassa) | – | Ihmisen influenssa |

<!-- review:begin fi-row-20261112-zanamivir-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/004102 / Dectova (peruutettu) / – / Ihmisen influenssa” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntilupa Dectova (EMEA/H/C/004102) on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-zanamivir-1 -->

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Tietokannasta löytyi 8 mahdollista yhteisvaikutusta. Ainoa luokiteltu on kohtalainen: inhaloitava nopeavaikutteinen ihmisinsuliini. Vakavuusluokaltaan tuntemattomia ovat klaritromysiini, loratadiini, montelukasti, ketotifeeni, feksofenadiini, ibuprofeeni ja diklofenaakki.
- **Tietämysgraafiin perustuvat vasta-aiheet (ei valmisteyhteenvedosta):** epilepsia, krooninen keuhkoahtaumatauti (COPD), vaikea varhain alkava COPD, keuhkoputkisairaus ja delirium. Nämä ovat mallin tuottamia signaaleja, eivät varmennettua valmistetekstin sisältöä.

Valmisteyhteenvedon varoitukset ja vasta-aiheet tulee tarkistaa erikseen.

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteen tukena on vain korkea TxGNN-pistemäärä. Kliinistä tai kirjallista näyttöä ei ole, mekanistinen yhteys bakteeriperäiseen pyelonefriittiin on heikko.

<!-- review:begin fi-lic-20261106-zanamivir-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Kliinistä tai kirjallista näyttöä ei ole, mekanistinen yhteys bakteeriperäiseen pyelonefriittiin on heikko, ja Suomessa ainoa myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-zanamivir-1 -->

**Eteneminen edellyttää:**
- Vaikutusmekanismin tietojen täydentämistä
- Valmisteyhteenvedon turvallisuustietojen hankkimista (estää turvallisuusseulonnan)
- Prekliinistä näyttöä tsanamiviirin vaikutuksesta uropatogeeneihin tai munuaisinfektiomalleihin
- Selvitystä lääkemuodosta ja antoreitistä (pyelonefriitti edellyttäisi todennäköisesti systeemistä altistusta)

<!-- review:begin fi-lic-20261106-zanamivir-2 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Selvitystä lääkemuodosta ja antoreitistä (pyelonefriitti edellyttäisi todennäköisesti systeemistä altistusta) / Arviota siitä, onko valmiste ylipäätään saatavilla Suomessa myyntiluvan peruutuksen jälkeen” Poistettu: väite oli ristiriidassa myyntilupatietojen kanssa (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-zanamivir-2 -->

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen.

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”ja Suomessa ainoa myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Poistettu: ”Arviota siitä, onko valmiste ylipäätään saatavilla Suomessa myyntiluvan peruutuksen jälkeen” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Dectova (EMEA/H/C/004102) on voimassa, ei peruutettu | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

