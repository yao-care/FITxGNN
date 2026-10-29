---
layout: default
title: Pemetrexed
parent: Pelkkä mallin ennuste (L5)
nav_order: 338
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-29
monitor_inn: "PEMETREXED"
predicted_indications: ["pleural adenomatoid tumor", "pericardium cancer", "iminoglycinuria"]
description: "Pemetrexed: ennustettu uusi käyttöaihe Pleural adenomatoid tumor (näytön taso L5). Alkuperäinen käyttöaihe: Mesothelioma"
---

# Pemetrexed
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **3** kpl
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

## Pemetrexed: Pleural adenomatoid tumor
{: .text-alpha }

## Yhteenveto

Pemetreksedi on monikohteinen antifolaatti, jota on alun perin käytetty mesoteliooman ja ei-pienisoluisen keuhkosyövän hoitoon.
TxGNN-malli ennustaa sen voivan tehota myös **vatsakalvon pahanlaatuiseen mesotelioomaan**,
ja tätä suuntaa tukee tällä hetkellä **7 kliinistä tutkimusta** ja **20 julkaisua**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Mesothelioma;Carcinoma, Non-Small-Cell Lung; Carcinoma, Non-Small-Cell Lung;Mesothelioma |
| Ennustettu uusi käyttöaihe | Pleural adenomatoid tumor |
| TxGNN-ennusteen pistemäärä | 0.9999 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 3/4) |
| Myyntilupien määrä | 4 (voimassa: 3) |
| Suositeltu päätös | Etene suojatoimin (Proceed with Guardrails) |

---

## Miksi ennuste on perusteltu?

Tämän raportin tietoihin ei sisälly yksityiskohtaista vaikutusmekanismitietoa lääkeaineen perustiedoista. Tunnetun tiedon perusteella pemetreksedi estää useita folaattiriippuvaisia entsyymejä (tymidylaattisyntaasi, DHFR ja GARFT), jolloin nopeasti jakautuvien kasvainsolujen puriini- ja pyrimidiinisynteesi häiriintyy.

Vatsakalvon ja keuhkopussin mesotelioma ovat histologialtaan ja solunsalpaajaherkkyydeltään samankaltaisia. Siksi pleuraalisen taudin hoidon ulottaminen vatsakalvoon on biologisesti uskottavaa. Pemetreksedin ja platinan yhdistelmää käytetään käytännössä vatsakalvon mesoteliooman systeemisenä vakiohoitona.

Näyttö vatsakalvon kohdalta perustuu kuitenkin vaiheen 2 tutkimuksiin, retrospektiivisiin aineistoihin ja sekaryhmiin (keuhkopussi ja vatsakalvo), ei vatsakalvokohtaisiin vaiheen 3 tutkimuksiin.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Vaihe 2 | Päättynyt | 48 | Pemetreksedi + gemsitabiini ensilinjan hoitona pleuraalisessa tai peritoneaalisessa mesotelioomassa |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Vaihe 2 | Rekrytoi | 66 | Satunnaistettu: karboplatiini, pemetreksedi ja bevasitsumabi ± atetsolitsumabi vatsakalvon mesotelioomassa; tuloksia ei vielä saatavilla |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Vaihe 2 | Keskeytetty | 66 | PIPAC + systeeminen solunsalpaajahoito (sisplatiini + pemetreksedi) vs. pelkkä systeeminen hoito |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Vaihe 2 | Rekrytoi | 28 | Yhden haaran tutkimus: sintilimabi + bevasitsumabi + pemetreksedi + sisplatiini |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Vaihe 2 | Rekrytoi | 64 | Satunnaistettu: vatsakalvonsisäinen vs. laskimonsisäinen solunsalpaajahoito leikkauksen ja HIPEC:n jälkeen; pemetreksedin rooli epäselvä |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Vaihe 1/2 | Aktiivinen, ei rekrytoi | 30 | TRC102 + sisplatiini + pemetreksedi edenneissä kasvaimissa; ei sairauskohtainen |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Vaihe 1 | Päättynyt | 19 | Sisplatiini + pemetreksedi + imatinibi mesotelioomassa; lähinnä turvallisuustutkimus |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Katsaus | J Natl Compr Canc Netw | Suositellut ensilinjan vaihtoehdot: nivolumabi + ipilimumabi tai pemetreksedi-pohjainen solunsalpaajahoito; suositukset perustuvat pleuraalisiin tutkimuksiin |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Retrospektiivinen vertailu | Clin Med Insights Oncol | Pemetreksedi-platina vs. gemsitabiini-platina ensilinjassa |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospektiivinen | Jpn J Clin Oncol | Pemetreksedi + sisplatiini ensilinjassa edenneessä vatsakalvon mesotelioomassa |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospektiivinen | Expert Rev Anticancer Ther | Ensilinjan pemetreksedi + sisplatiini vatsakalvon mesotelioomassa |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | Yhden keskuksen kokemus | Tumori | Pemetreksedi-sisplatiini-yhdistelmän teho ja turvallisuus aiemmin hoitamattomilla |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Monikeskustutkimus | Ann Surg Oncol | Hoitostrategiat ja tulokset vatsakalvon mesotelioomassa |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Katsaus | Cancers | Diagnostiikka ja hoitopolku; sytoreduktiivinen leikkaus + HIPEC tuottaa parhaan eloonjäämisen |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Katsaus | J Clin Med | Vatsakalvon mesoteliooman hoito |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Katsaus | Transl Lung Cancer Res | Harvinainen kasvain, huono ennuste |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Tapausselostus | BMJ Case Rep | Nivolumabi vatsakalvon mesotelioomassa solunsalpaajahoidon jälkeen |

---

## Myyntiluvat Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000564 | Alimta | – | Mesotelioomaa; ei-pienisoluinen keuhkosyöpä (peruutettu) |
| EMEA/H/C/003905 | Pemetrexed medac | – | Ei-pienisoluinen keuhkosyöpä; mesotelioma (peruutettu) |
| EMEA/H/C/003895 | Pemetrexed Fresenius Kabi | – | Ei-pienisoluinen keuhkosyöpä; mesotelioma (peruutettu) |
| EMEA/H/C/003970 | Pemetrexed Pfizer (aiemmin Pemetrexed Hospira) | – | Ei-pienisoluinen keuhkosyöpä; mesotelioma (peruutettu) |

---

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Perinteinen sytotoksinen lääke (antifolaatti) |
| Luuydinsuppression riski | Korkea: tietograafin vasta-aihetiedoissa mainitaan neutropenia, trombosytopenia, agranulosytoosi ja anemia |
| Oksettavuusluokitus | Tietoa ei ole saatavilla; ks. valmisteyhteenveto |
| Seurattavat kohteet | Verenkuva (erittelylaskenta), munuaisten ja maksan toiminta |
| Käsittelysuojaus | Noudatettava sytotoksisten lääkkeiden käsittelyohjeita |

---

## Turvallisuusnäkökohdat

- **Tietograafin mukaiset vasta-aiheisiin liittyvät sairaudet** (eivät perustu valmisteyhteenvetoon): munuaissairaus, heikentynyt munuaisten toiminta, pyoureter, trombosytopenia, neutropenia, agranulosytoosi, anemia ja makrosyyttinen anemia.
- **Yhteisvaikutukset:** Tietoihin sisältyy 100 yhteisvaikutusta, joista näytetyt ovat kaikki merkittävyydeltään kohtalaisia. Keskeisiä ovat mm. H2-salpaajat (famotidiini, ranitidiini, simetidiini), metformiini, asetyylisalisyylihappo, amfoterisiini B:n eri muodot, aminoglykosidit ja muut munuaistoksiset tai munuaisten kautta erittyvät lääkkeet (vankomysiini, kanamysiini, neomysiini, polymyksiini B), levofloksasiini, amoksisilliini sekä mesalatsiini ja sen johdokset.

Muilta osin turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Etene suojatoimin (Proceed with Guardrails)**

**Perustelut:**
- Pemetreksedi-platina on käytännössä vakiintunut vatsakalvon mesoteliooman systeeminen hoito, ja näyttöä on vaiheen 2 tutkimuksista ja retrospektiivisistä aineistoista. Vatsakalvokohtaisia vaiheen 3 tutkimuksia ei kuitenkaan ole, joten näytön taso on L2.
- Kaikki neljä suomalaista myyntilupaa on peruutettu, joten saatavuus on selvitettävä.

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (tällä hetkellä puuttuvat; estävä tietoaukko)
- Vaikutusmekanismin tiedot lääketietokannasta
- Myyntilupatilanteen ja valmisteiden saatavuuden selvitys Suomessa
- Satunnaistettujen vatsakalvotutkimusten (mm. NCT05001880) tulokset
- Munuaistoiminnan, verenkuvan ja yhteisvaikutusten seurantasuunnitelma

---

## Muut ennustetut käyttöaiheet (lyhyesti)

Samoista tiedoista nousi esiin myös muita ennusteita:
- **Keuhkopussin mesotelioma (L1):** alkuperäinen käyttöaihe, ei varsinainen uudelleenkäyttö. Pemetreksedi + sisplatiini on vakiohoito (vaiheen 3 tutkimus, PMID 12860938).
- **Epiteloidi mesotelioma (L1):** tuki perustuu pääosin yleisiin mesotelioomatutkimuksiin.
- **Sarkomatoidi- ja bifaasinen mesotelioma (L2):** tutkimustyön aihe; alatyyppikohtainen näyttö niukkaa.
- **Sydänpussin syöpä (L4):** vain tapausselostuksia, tutkimustyön aihe.
- **Hyvin erilaistunut papillaarinen mesotelioma, lymfohistiosytoidi mesotelioma, pleuraalinen adenomatoidikasvain ja iminoglysinuria:** odota (Hold); näyttö puuttuu tai mekanistinen peruste on heikko.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

