---
layout: default
title: Fidaxomicin
parent: Pelkkä mallin ennuste (L5)
nav_order: 190
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "FIDAXOMICIN"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis"]
description: "Fidaxomicin: ennustettu uusi käyttöaihe Stafylokokin aiheuttama kuoriutuva ihosyndrooma (staphylococcal scalded skin syndrome) (näytön taso L5). Alkuperäinen käyttöaihe: Clostridium Infections"
---

# Fidaxomicin
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

## Fidaxomicin: Stafylokokin aiheuttama kuoriutuva ihosyndrooma (staphylococcal scalded skin syndrome)
{: .text-alpha }

## Yhden lauseen yhteenveto

Fidaksomisiini on makrosyklinen, kapeakirjoinen antibiootti, jota on alun perin käytetty Clostridium-infektioiden hoitoon. TxGNN-malli ennustaa sen voivan tehota **stafylokokin aiheuttamaan kuoriutuvaan ihosyndroomaan (SSSS)**, mutta ennusteelle ei ole toistaiseksi **yhtään kliinistä tutkimusta eikä kirjallisuuslähdettä**. Näyttö perustuu pelkästään mallin laskennalliseen pisteytykseen.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Clostridium Infections |
| Ennustettu uusi käyttöaihe | Stafylokokin aiheuttama kuoriutuva ihosyndrooma (staphylococcal scalded skin syndrome) |
| TxGNN-ennustepisteet | 0,9971 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on järkevä – tai ei?

Fidaksomisiini estää bakteerin RNA-polymeraasia, ja sen vaikutus kohdistuu pääosin gram-positiivisiin bakteereihin, kuten *Clostridioides difficile* -bakteeriin. Yhdysvaltain FDA:n hyväksymän valmistetiedon (Prescribing Information) kohtien ”Mechanism of Action” ja ”Microbiology” mukaan valmisteesta Fidaxomicin (epävirallinen käännös): ”Fidaksomisiini on antibakteerinen lääke. […] Fidaksomisiini on fermentaatiotuote, joka saadaan aktinomykeetistä Dactylosporangium aurantiacum. Fidaksomisiini on makrolidiryhmän antibakteerinen lääke, joka estää RNA-synteesiä sitoutumalla RNA-polymeraaseihin. Fidaksomisiini on bakterisidinen C. difficileä vastaan in vitro, ja sillä on C. difficileä vastaan 6–10 tunnin antibioottinen jälkivaikutus.” Englanninkielinen alkuteksti: "Fidaxomicin is an antibacterial drug. […] Fidaxomicin is a fermentation product obtained from the Actinomycete Dactylosporangium aurantiacum. Fidaxomicin is a macrolide antibacterial drug that inhibits RNA synthesis by binding to RNA polymerases. Fidaxomicin is bactericidal against C. difficile in vitro, and demonstrates a post-antibiotic effect vs. C. difficile of 6-10 hrs." ([DailyMed: Dificid (fidaxomicin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb), versio 2024-10-16; haettu 2026-11-19). Tunnetun lääkeluokan perusteella mekanistinen yhteys on kuitenkin mahdollinen: laboratoriokokeissa on raportoitu jonkin verran *Staphylococcus aureus* -tehoa, ja tämä bakteeri tuottaa SSSS:n aiheuttavia eksfoliatiivisia toksiineja.

Ennusteessa on kuitenkin vakavia heikkouksia. Suun kautta annettu fidaksomisiini imeytyy hyvin vähän, joten systeeminen altistus on mitätön. Tämä tekee lääkkeestä epätodennäköisen valinnan systeemiseen, toksiinivälitteiseen sairauteen. Korkea pistemäärä on siis laskennallinen ennuste, jota mikään kliininen tieto ei tue.

### Muut ennustetut käyttöaiheet

Mallin muut ennusteet ovat samansuuntaisia: kaikilla on näytön taso L5 ja suositus Hold.

| Sija | Käyttöaihe | Pisteet | Keskeinen huomio |
|------|------|------|------|
| 2 | Rakkulainen impetigo | 0.9970 | Suun kautta annettu lääke ei saavuta ihokudosta; paikallista valmistetta ei ole; vaihtoehtoja on |
| 3 | Inhalaatiobotulismi | 0.9969 | Toksiinivälitteinen; hoito on antitoksiini ja tukihoito; heikko mekanistinen peruste |
| 4 | Impetigo | 0.9968 | Ei ihoon tarkoitettua valmistetta; tehokkaita paikallislääkkeitä on (mm. mupirosiini, retapamuliini) |
| 5 | Toksiinivälitteinen infektiivinen botulismi | 0.9966 | Teoreettinen peruste suolistoon rajoittuvalle kolonisaatiolle, mutta spekulatiivinen |
| 6 | Vulvovaginaalinen kandidiaasi | 0.9965 | Sieni-infektio; ei tunnettua sienivaikutusta; todennäköisesti mallin artefakti |
| 7 | Rapykkä (hordeolum) | 0.9964 | Ei silmä- tai paikallisvalmistetta; imeytyminen mitätöntä |
| 8 | *Staphylococcus aureus* -keuhkokuume | 0.9921 | Keuhkokudoksen pitoisuudet jäisivät riittämättömiksi; vakiintuneita lääkkeitä on |
| 9 | Pistemäinen epiteliaalinen keratokonjunktiviitti | 0,9902 | Usein virus- tai tulehdusperäinen; ei selvää kohdetta; todennäköisesti mallin artefakti |

## Kliininen tutkimusnäyttö

Tällä hetkellä ei ole aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuusnäyttö

Ensisijaiselle ennusteelle (SSSS) ei ole saatavilla aiheeseen liittyvää kirjallisuutta. Ainoa kirjallisuusviite löytyi sijalla 8 olevalle *S. aureus* -keuhkokuumeelle:

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) | 2019 | Katsaus | Journal of Hospital Medicine | Yleinen sairaalalääketieteen kirjallisuuskatsaus, jossa todetaan mm. vankomysiinin tai fidaksomisiinin olevan ensilinjan hoito *C. difficile* -infektiossa. Ei näyttöä fidaksomisiinin tehosta keuhkokuumeessa. |

## Myyntiluvat Suomessa

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002087 | Dificlir | – | Clostridium-infektiot (tila: voimassa) |

<!-- review:begin fi-row-20261112-fidaxomicin-1 -->

> **Tarkistuskorjaus (2026-11-12)**: Alun perin tässä luki: ”EMEA/H/C/002087 / Dificlir / – / Clostridium-infektiot (tila: peruutettu)” EMA:n keskitetysti myönnettyjen myyntilupien tietojen (2026-11-09) mukaan myyntilupa Dificlir (EMEA/H/C/002087) on voimassa (Authorised). Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-row-20261112-fidaxomicin-1 -->

## Turvallisuusnäkökohdat

### Lääkeyhteisvaikutukset

Tähän raporttiin koottujen tietojen mukaan yhteisvaikutuksia on kirjattu yhteensä 79. Esimerkkejä:

- **Merkittävä (Major):** elävä koleraroksote (*Vibrio cholerae* CVD 103-HgR)
- **Kohtalainen (Moderate):** alpelisibi, apalutamidi, binimetinibi, pikosulfaatti
- **Lievä (Minor):** mm. nifedipiini, amiodaroni, diltiatseemi, verapamiili, siklosporiini, klaritromysiini, erytromysiini, spironolaktoni

Muuta turvallisuustietoa (varoitukset, vasta-aiheet) ei ole saatavilla; tarkista ne valmisteyhteenvedosta.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold**

**Perustelut:**
- Ennuste perustuu pelkkään mallipisteytykseen (L5), eikä sille ole kliinistä tutkimusta tai kirjallisuutta. Lääkkeen vähäinen imeytyminen heikentää uskottavuutta systeemisissä ja kudoskohteissa, ja vakiintuneita hoitoja on olemassa.

<!-- review:begin fi-lic-20261106-fidaxomicin-1 -->

> **Tarkistuskorjaus (2026-11-06)**: Alun perin tässä luki: ”Lääkkeen vähäinen imeytyminen heikentää uskottavuutta systeemisissä ja kudoskohteissa, ja vakiintuneita hoitoja on olemassa. Lisäksi Suomen myyntilupa on peruutettu.” Poistettu: väite, että myyntiluvat olisivat peruttuja, lakanneita tai mitättömiä, ei vastannut myyntilupatietoja (EMA:n keskitetysti myönnetyt myyntiluvat, tilanne 2026-11-06). Tiedoissa (EMA:n keskitetysti myönnetyt myyntiluvat) tälle lääkkeelle on kirjattu 1 myyntilupaa, joista 1 voimassa; ajantasaiset luvut ovat pikakatsauksessa ja markkinatiedoissa. Lähde: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end fi-lic-20261106-fidaxomicin-1 -->

**Etenemiseksi tarvitaan seuraavat tiedot tai toimet:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvittäminen (estää turvallisuusarvioinnin jatkamisen)
- Vaikutusmekanismin (MOA) tiedot
- Prekliiniset tiedot fidaksomisiinin tehosta SSSS:n aiheuttajaa (*S. aureus*) vastaan sekä kudosaltistuksesta
- Arvio mahdollisista antoreiteistä (esim. paikallinen valmiste), sillä nykyinen suun kautta annettava muoto ei sovellu systeemiseen tai ihokohteeseen
- Ennusteiden uudelleenarviointi vasta, kun ensimmäistä tukevaa kliinistä tai kirjallista näyttöä on saatavilla

<!-- review:begin log -->

## Tarkistusloki

Alla on tämän sivun tarkistusloki: väitteet, jotka on tarkistettu virallisista myyntilupatiedoista (EMA:n keskitetysti myönnetyt myyntiluvat). Korjaukset koskevat vain perustietoja; mallin ennusteita, näytön tasoja ja johtopäätöksiä ei ole kirjoitettu uudelleen. Lause, jonka mukaan vaikutusmekanismitietoja ei ollut saatavilla, korvattiin otteella mainitusta virallisesta valmistetiedosta (epävirallisen käännöksen kera).

| Tarkistuspäivä | Kohta | Toimenpide | Lähde |
|------|------|------|------|
| 2026-11-06 | Poistettu: ”Lisäksi Suomen myyntilupa on peruutettu” | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Taulukko: Dificlir (EMEA/H/C/002087) on voimassa, ei peruutettu | Korjattu | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Lause ”vaikutusmekanismitietoja ei ole saatavilla” korvattu otteella yhdysvaltalaisesta valmistetiedosta | Lause puuttuvista vaikutusmekanismitiedoista korvattu lähteellisellä otteella | [DailyMed: Dificid (fidaxomicin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb) |

<!-- review:end log -->

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

