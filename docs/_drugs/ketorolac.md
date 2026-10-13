---
layout: default
title: Ketorolac
parent: Vahva näyttö (L1-L2)
nav_order: 242
evidence_level: L1
indication_count: 3
---

# Ketorolac
{: .fs-9 }

Näytön taso: **L1** | Ennustetut käyttöaiheet: **3** kpl
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

# Ketorolaakki: Leikkauksen jälkeisestä kivusta päänsärkyhäiriöön

## Yhden lauseen yhteenveto

Ketorolaakki on tulehduskipulääke (NSAID), jonka hyväksytty käyttöaihe on silmänsisäisen linssi-implantaation yhteydessä ja leikkauksen jälkeisen kivun hoidossa. TxGNN-malli ennustaa sen voivan tehota **päänsärkyhäiriöihin**, joista tärkeimpiä ovat migreeni ja jännityspäänsärky. Ennustetta tukee tällä hetkellä **16 kliinistä tutkimusta** ja **19 julkaisua**, ja näyttöä pidetään vahvana.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Silmänsisäinen linssi-implantaatio; leikkauksen jälkeinen kipu |
| Ennustettu uusi käyttöaihe | Päänsärkyhäiriö (headache disorder) |
| TxGNN-ennusteen pistemäärä | 99,43 % |
| Näytön taso | L1 |
| Markkinatilanne Suomessa | Vain peruutettu myyntilupa |
| Myyntilupien määrä | 1 |
| Suositeltu päätös | Proceed with Guardrails (eteneminen suojatoimin) |

---

## Miksi ennuste on perusteltu?

Tässä raportissa käytettyyn aineistoon ei sisälly yksityiskohtaista vaikutusmekanismitietoa. Ketorolaakki on kuitenkin tunnetusti epäselektiivinen COX-1/COX-2-estäjä. Se estää prostaglandiinien synteesiä, mikä vähentää perifeeristä ja keskushermostollista herkistymistä sekä neurogeenistä tulehdusta. Nämä mekanismit liittyvät migreenin ja jännityspäänsäryn kipuun. Tämä kuvaus perustuu vakiintuneeseen farmakologiseen tietoon, ei raportin lähdeaineistoon.

Alkuperäinen käyttöaihe eli leikkauksen jälkeinen kipu ja uusi käyttöaihe eli akuutti päänsärky ovat molemmat tilanteita, joissa tarvitaan nopeaa kivunlievitystä. Ketorolaakin parenteraaliset ja nenänsisäiset valmisteet vaikuttavat nopeasti, mikä sopii päivystyspoliklinikan akuuttihoitoon.

Ennustettu käyttö on myös kliinisessä käytössä: kirjallisuuden mukaan ketorolaakkia käytetään ensilinjan akuuttihoitona migreenissä erityisesti lapsilla.

Toinen ennuste, **tihkuvastaanotto: trigeminaalinen autonominen päänsärky** (esim. cluster-päänsärky), on teoreettisesti perusteltu, mutta suora näyttö on heikkoa. Ennuste **ruusufinnin sidekalvotulehdus** perustuu pelkkään mallin pistemäärään (99,40 %) ilman tutkimuksia tai julkaisuja.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Vaihe 4 | Päättynyt | 56 | Suonensisäinen ketorolaakki + metoklopramidi lasten migreenissä päivystyksessä |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Vaihe 4 | Päättynyt | 72 | Ketorolaakkinenäsumute vs. sumatriptaaninenäsumute vs. lumelääke akuutissa migreenissä |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Vaihe 4 | Päättynyt | 123 | Metoklopramidi/difenhydramiini vs. pelkkä ketorolaakki jännityspäänsäryssä |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Vaihe 2 | Päättynyt | 173 | Satunnaistettu, kaksoissokkoutettu, lumekontrolloitu tutkimus nenänsisäisestä ketorolaakista akuutissa migreenissä |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Vaihe 3 | Päättynyt | 59 | Nenänsisäinen vs. suonensisäinen ketorolaakki lasten migreenissä (non-inferiority) |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Vaihe 4 | Päättynyt | 330 | Suonensisäinen valproaatti vs. metoklopramidi vs. ketorolaakki akuutissa migreenissä |
| [NCT05641363](https://clinicaltrials.gov/study/NCT05641363) | Vaihe 3 | Päättynyt | 171 | Ketorolaakin kolme annosta lasten akuutissa kivussa |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Vaihe 2 | Keskeytetty | 41 | Nenänsisäinen ketorolaakki-yhdistelmä vs. suonensisäinen ketorolaakki lasten migreenissä |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Vaihe 4 | Tila tuntematon | 60 | Ketamiini vs. ketorolaakki jännityspäänsäryssä |
| [NCT03066544](https://clinicaltrials.gov/study/NCT03066544) | Vaihe 1/2 | Tila tuntematon | 50 | Status migrainosuksen hoitovasteen selvittäminen tavanomaisessa kliinisessä hoidossa |

Huomio: tutkimuksissa ketorolaakki on usein osa yhdistelmähoitoa tai vertailuvalmiste, joten sen yksittäistä vaikutusta on vaikea erottaa. Useat tutkimukset ovat pieniä.

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systemaattinen katsaus ja meta-analyysi | Acad Emerg Med | Parenteraalisen ketorolaakin teho akuutissa migreenikohtauksessa |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Systemaattinen katsaus | Headache | Parenteraalisen ketorolaakin vaikuttavuus akuutissa migreenissä; näyttö osin ristiriitaista |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systemaattinen katsaus ja meta-analyysi | Adv Clin Exp Med | Suonensisäinen ketorolaakki vs. metoklopramidi aikuisten migreenissä |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | Satunnaistettu koe | Headache | Metoklopramidi vs. metoklopramidi + ketorolaakki lasten migreenissä päivystyksessä |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Ohje | Headache | American Headache Societyn päivitetty ohje migreenin parenteraalisesta akuuttihoidosta päivystyksessä |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Ohje / näytön arviointi | Headache | Akuutin migreenilääkityksen näytön arviointi |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systemaattinen katsaus ja suositukset | Cephalalgia | Kanadan päänsärkyseuran suositukset migreenikivun hoidosta päivystyksessä |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Systemaattinen katsaus | Headache | Episodisen jännityspäänsäryn parenteraalinen hoito |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Systemaattinen katsaus | Headache | Lasten migreenin akuuttihoidot päivystyksessä |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | Satunnaistettu koe | Ann Emerg Med | Lihaksensisäinen ketorolaakki vs. meperidiini ja hydroksitsiini akuutissa migreenissä |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/003702 | Omidria | – | Silmänsisäinen linssi-implantaatio; leikkauksen jälkeinen kipu (tila: peruutettu) |

---

## Turvallisuusnäkökohdat

- **Lääkeyhteisvaikutukset:** Yhteisvaikutuksia on tunnistettu yhteensä 100. Merkittävimpiä:
  - **Vakava (Major):** asetyylisalisyylihappo
  - **Kohtalainen (Moderate):** kortikosteroidit (beetametasoni, budesonidi, deksametasoni, hydrokortisoni), sulfonyyliureat (asetoheksamidi, klooripropamidi, glimepiridi, glipitsidi, glyburidi), eksenatidi, balsalatsidi, kanamysiini, levofloksasiini, fenfluramiini ja deksfenfluramiini
  - **Lievä (Minor):** famotidiini, ranitidiini, simetidiini, linaklotidi
- **Tietämysgraafin perusteella tunnistetut sairaudet, joissa käyttöön liittyy vasta-aihe tai varovaisuus** (ei perustu valmisteyhteenvetoon): mm. mahahaava ja aktiivinen peptinen haavauma, tulehduksellinen suolistosairaus, maksasairaus, munuaisten vajaatoiminta, verenvuotohäiriöt (mm. hemofilia), aivohalvaus ja aivoverenkiertohäiriöt, sydäninfarkti, sydän- ja verisuonitaudit, verenpainetauti, astma, diabetes ja kuiva silmä -oireyhtymä.
- **Lisähuomiot:** Lasten annostelussa tarvitaan varovaisuutta. Yksittäisessä tapausselostuksessa ketorolaakin on raportoitu aiheuttaneen litiumtoksisuutta (PMID 7928331), mikä on merkityksellistä, koska litiumia käytetään cluster-päänsäryn hoidossa. Ruusufinnin sidekalvotulehduksessa NSAID-lääkkeisiin liittyy sarveiskalvoriskejä (viivästynyt paraneminen, sarveiskalvon sulaminen).

Valmisteyhteenvedon varoitukset ja vasta-aiheet puuttuvat tästä raportista, joten niihin on perehdyttävä valmisteyhteenvedosta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Proceed with Guardrails (eteneminen suojatoimin)**

**Perustelut:**
- Päänsärkyhäiriön (erityisesti migreenin ja jännityspäänsäryn) osalta on useita päättyneitä vaiheen 2–4 tutkimuksia, systemaattisia katsauksia, meta-analyysi ja kansainvälisiä hoito-ohjeita, jotka tukevat ketorolaakin käyttöä. Näytön taso on L1. Suomessa ainoa myyntilupa (Omidria) on kuitenkin peruutettu, eikä kyseinen valmiste ole päänsäryn hoitoon tarkoitettu.
- Ennusteet ruusufinnin sidekalvotulehdukseen (L5) ja trigeminaaliseen autonomiseen päänsärkyyn (L4) ovat tässä vaiheessa Hold-tasolla.

**Jatkoon tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden kokoaminen (estää etenemisen turvallisuusseulontaan)
- Yksityiskohtaiset vaikutusmekanismitiedot
- Selvitys Suomessa saatavilla olevista ketorolaakkivalmisteista ja antoreiteistä (parenteraalinen, nenänsisäinen) päänsärkykäyttöön
- Turvallisuuden seurantasuunnitelma: ruoansulatuskanavan verenvuoto, munuaisten toiminta, sydän- ja verisuoniriski, antikoagulanttien käyttö sekä annos- ja hoitoajan rajat
- Lasten annostelun ja yhteisvaikutusten (erityisesti asetyylisalisyylihappo) tarkempi arviointi
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

