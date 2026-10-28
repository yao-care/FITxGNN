---
layout: default
title: Trametinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 449
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Trametinib: ennustettu uusi käyttöaihe Choroideremia (sijalla 1). Käytännössä merkityksellisin vaihtoehto: e… (näytön taso L5). Alkuperäinen käyttöaihe: Melanooma"
monitor_inn: "TRAMETINIB"
predicted_indications: ["choroideremia"]
---

# Trametinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **1** kpl
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

## Trametinibi: choroideremia – ennuste ei ole biologisesti perusteltu
{: .text-alpha }

## Yhden lauseen yhteenveto

Trametinibi on MEK1/2-estäjä, jota käytetään melanooman hoitoon. TxGNN-malli ennustaa sen tehoavan **choroideremiaan** (korkein pistemäärä), mutta tälle ennusteelle ei ole kliinistä tai kirjallisuusnäyttöä (**0 kliinistä tutkimusta ja 0 julkaisua**). Vahvin näyttö liittyy sen sijaan toiseksi sijoittuneeseen ennusteeseen, **ei-ihomelanoomaan**, jota tukee **10 kliinistä tutkimusta**. Mitään julkaisua ei ole haettu tälle kohteelle.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Melanooma |
| Ennustettu uusi käyttöaihe | Choroideremia (sijalla 1). Käytännössä merkityksellisin vaihtoehto: ei-ihomelanooma (sijalla 2) |
| TxGNN-ennustepisteet | 0,9931 (choroideremia) |
| Näytön taso | L5 (choroideremia); L2 (ei-ihomelanooma) |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Hold (choroideremia); Proceed with Guardrails (ei-ihomelanooma) |

## Miksi ennuste on perusteltu (tai ei)?

Tämän raportin käytettävissä olevissa tiedoissa ei ole yksityiskohtaista vaikutusmekanismikuvausta. Tunnetun tiedon perusteella trametinibi on allosteerinen MEK1/2-estäjä (kohteet MAP2K1 ja MAP2K2), ja sen teho BRAF V600 -mutaatiopositiivisessa melanoomassa on osoitettu yhdistelmänä dabrafenibin kanssa.

**Choroideremia:** Tauti on X-kromosomaalinen verkkokalvon rappeumasairaus, jonka aiheuttaa CHM (REP1) -geenin toiminnan menetys. Sillä ei ole tunnettua yhteyttä MAPK/MEK-reitin riippuvuuteen. Korkea pistemäärä (0,9931) on todennäköisesti verkon etenemisen tuottama artefakti, eikä sitä tule pitää biologisena tukena.

**Ei-ihomelanooma:** Limakalvo-, uvea- ja muiden sijaintien melanoomissa on BRAF- tai NRAS-ohjautuvia MAPK-aktiivisia alaryhmiä, joten MEK:n esto on mekanistisesti uskottavaa. Uveamelanooman taustalla ovat pääosin GNAQ/GNA11-muutokset ja niiden alavirran MAPK-signalointi, mikä tukee MEK-estäjäyhdistelmiä. Hyväksytty ihomelanooman käyttöaihe (BRAF V600, yhdessä dabrafenibin kanssa) antaa läheisen biologisen esikuvan. Näyttö on kuitenkin alatyypeittäin heterogeenista ja enimmäkseen pieniä tai varhaisen vaiheen tutkimuksia.

Muut ennustetut kohteet (epiteloidisoluinen, silmäluomen, kivespussin, amelanoottinen, akraalinen lentiginoosi-, lentigo maligna -, pinnallisesti leviävä ja ilmapallosolumelanooma) ovat melanooman histologisia tai sijaintiin perustuvia muunnelmia. Niiden perustelu nojaa pitkälti yleiseen BRAF/MEK-melanoomabiologiaan.

## Kliininen tutkimusnäyttö

Näyttö koskee ennustetta "ei-ihomelanooma" (choroideremialle ei ole tutkimuksia).

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT02296112](https://clinicaltrials.gov/study/NCT02296112) | Vaihe 2 | Valmistunut | 9 | Trametinibi melanoomassa, jossa BRAF non-V600 -mutaatio; suoraan relevantti, mutta hyvin pieni aineisto |
| [NCT02872259](https://clinicaltrials.gov/study/NCT02872259) | Vaihe 1/2 | Valmistunut | 74 | BGB324 yhdessä pembrolitsumabin tai dabrafenibin/trametinibin kanssa; trametinibin osuutta vaikea erottaa |
| [NCT04439292](https://clinicaltrials.gov/study/NCT04439292) | Vaihe 2 | Aktiivinen, ei rekrytoi | 44 | NCI-MATCH H: dabrafenibi + trametinibi BRAF V600 -mutaatiokasvaimissa (ei melanoomaa); kasvainriippumaton, tukee mekanismia |
| [NCT02974725](https://clinicaltrials.gov/study/NCT02974725) | Vaihe 1 | Keskeytetty | 241 | LXH254-yhdistelmät (mm. trametinibi) NRAS-mutaatiomelanoomassa ja keuhkosyövässä; trametinibispesifinen signaali epäselvä |
| [NCT05907304](https://clinicaltrials.gov/study/NCT05907304) | Vaihe 1 | Aktiivinen, ei rekrytoi | 86 | Naporafenibi + trametinibi RAS Q61X -kasvaimissa; varhaisen vaiheen turvallisuus- ja tehotieto |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | Ei sovellettavissa | Valmistunut | 232 | Adjuvanttinen dabrafenibi + trametinibi melanoomassa, havainnointitutkimus; pääosin ihopopulaatio |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Vaihe 4 | Rekrytoi | 100 | Pitkäaikaisturvallisuuden jatkotutkimus; ei tehotietoa tälle käyttöaiheelle |
| [NCT02410863](https://clinicaltrials.gov/study/NCT02410863) | Vaihe 2 | Keskeytetty | 10 | Biopsiaohjattu kohdennetun hoidon optimointi; vähän tulkittavaa dataa |
| [NCT02416232](https://clinicaltrials.gov/study/NCT02416232) | Ei sovellettavissa | Ei enää saatavilla | Ei tiedossa | Laajennettu saatavuusohjelma; ei tehonäyttöä |
| [NCT05275374](https://clinicaltrials.gov/study/NCT05275374) | Vaihe 1/2 | Ei vielä rekrytoi | 221 | XP-102 + trametinibi BRAF V600 -kasvaimissa; ei vielä tuloksia |

Lisäksi tutkimus [NCT07440290](https://clinicaltrials.gov/study/NCT07440290) (vaihe 2/3, rekrytoi, 30 osallistujaa) arvioi dabrafenibi–trametinibiyhdistelmää BRAF V600 -mutaatiopositiivisissa syövissä; relevanssiarviota ei ole vielä tehty.

## Kirjallisuusnäyttö

Choroideremialle, ei-ihomelanoomalle ja kivespussin sekä ilmapallosolumelanoomalle ei löytynyt kirjallisuutta. Alla on muille ennustetuille melanoomamuunnelmille haettu kirjallisuus.

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Katsaus | JAMA | Yleiskatsaus ihomelanoomaan; ilmaantuvuus kasvanut selvästi vuodesta 1975 |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Tapausselostus ja katsaus | Clin Exp Dermatol | Kaksi BRAF-mutatoitunutta sidekalvomelanoomaa (epiteloidisolutyyppi); hoitona vemurafenibi |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Tapausselostus ja katsaus | J Investig Med High Impact Case Rep | Kyynelpussin melanooma, 15 japanilaispotilasta |
| [41209431](https://pubmed.ncbi.nlm.nih.gov/41209431/) | 2026 | Tapausselostus | Oncol Lett | Yhdistetty BRAF/MEK-esto BRAF-mutatoituneiden aivometastaasien hoidossa raskauden aikana |
| [37756677](https://pubmed.ncbi.nlm.nih.gov/37756677/) | 2025 | Tapausselostus | Retinal Cases Brief Rep | Suonikalvon etäpesäkkeen ja subretinaalisen nesteen nopea ja täydellinen väistyminen kohdennetun yhdistelmähoidon jälkeen |
| [41310270](https://pubmed.ncbi.nlm.nih.gov/41310270/) | 2025 | Tapausselostus | Child's Nerv Syst | Harvinainen lapsen keskushermoston amelanoottinen melanooma; kuvantamisen sudenkuopat |
| [42583475](https://pubmed.ncbi.nlm.nih.gov/42583475/) | 2026 | Tapausselostus | Ann Med Surg | Varhain metastasoitunut BRAF V600E -melanooma ilman tunnettua primaarikasvainta |

## Myyntitiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/002643 | Mekinist | – | Melanooma (tila: peruutettu) |

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (MEK-estäjä) |
| Luuydinsuppression riski | Tarkempia tietoja ei ole saatavilla; ks. valmisteyhteenveto |
| Oksettavuusluokitus | Ks. valmisteyhteenveto |
| Seurantaparametrit | Ks. valmisteyhteenveto |
| Käsittelysuojaus | Ks. valmisteyhteenveto |

## Turvallisuusnäkökohdat

**Lääkkeiden yhteisvaikutukset:** Yhteensä 17 kirjattua merkintää, joista 15 on luokiteltu keskivaikeiksi (Moderate). Keskivaikeat yhteisvaikutukset koskevat seuraavia lääkeaineita: fostamatinibi, elagolix, apalutamidi, brigatinibi, dabrafenibi, enkorafenibi, isavukonatsoni, lasmiditaani, midostauriini, sarekykliini, entsalutamidi, erdafitinibi, gilteritinibi, idelalisibi ja tukatinibi. Kaksi muuta merkintää kuvaa lääkeaineen farmakologisia kohteita (MAP2K1 ja MAP2K2).

Muuta turvallisuustietoa varten katso valmisteyhteenveto.

## Johtopäätös ja seuraavat vaiheet

**Päätös:**
- **Choroideremia: Hold**
- **Ei-ihomelanooma: Proceed with Guardrails**

**Perustelut:**
- Choroideremian ennuste on todennäköisesti tilastollinen artefakti: näyttöä ei ole, eikä tunnettua MEK-yhteyttä. Ei-ihomelanoomalle on useita vaiheen 1–2 tutkimuksia ja mekanistisesti uskottava peruste, mutta tutkimukset ovat pieniä ja heterogeenisia. Suomessa trametinibin ainoa myyntilupa on peruutettu.

**Jatkotoimiin tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden selvitys (Fimean verkkosivusto), koska turvallisuusseulontaa ei voi viedä loppuun ilman niitä
- Vaikutusmekanismitiedon täydentäminen (esim. DrugBank)
- Suomen myyntilupatilanteen ja saatavuuden selvitys
- Alatyyppikohtainen tehonäyttö (mutaatiostatuksen mukaan valikoidut potilaat) ei-ihomelanoomassa
- Lääkeyhteisvaikutusten arviointi, erityisesti BRAF-estäjien ja CYP-entsyymeihin vaikuttavien lääkkeiden osalta
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

