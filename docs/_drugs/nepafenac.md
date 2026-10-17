---
layout: default
title: Nepafenac
parent: Pelkkä mallin ennuste (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nepafenac: ennustettu uusi käyttöaihe Silmäsairaus (eye disease) (näytön taso L5). Alkuperäinen käyttöaihe: Leikkauksen jälkeinen kipu"
monitor_inn: "NEPAFENAC"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
---

# Nepafenac
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Nepafenaakki: Leikkauksen jälkeisestä kivusta silmäsairauksiin

## Yhden lauseen yhteenveto

Nepafenaakki on paikallisesti silmään annettava tulehduskipulääke, jota on alun perin käytetty leikkauksen jälkeisen kivun ja silmäkirurgian yhteydessä esiintyvän tulehduksen hoitoon.
TxGNN-malli ennustaa sen voivan olla tehokas **silmäsairauksien** hoidossa, ja tätä suuntaa tukee tällä hetkellä **41 kliinistä tutkimusta** ja **20 julkaisua**.
Ennuste on lähellä lääkkeen nykyistä käyttöä, joten kyse on pikemminkin laajennuksesta samalla hoitoalueella kuin kaukaisesta uudelleenkäytöstä.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Leikkauksen jälkeinen kipu; silmäkirurgiset toimenpiteet |
| Ennustettu uusi käyttöaihe | Silmäsairaus (eye disease) |
| TxGNN-ennustepistemäärä | 99,85 % |
| Näytön taso | L1 (ks. huomautus alla) |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Etene suojatoimin (Proceed with Guardrails) |

*Huomautus:* L1-luokitus perustuu laajoihin satunnaistettuihin vaiheen 2 tutkimuksiin, vaiheen 3 tutkimuksiin sekä järjestelmälliseen katsaukseen. Tiukempi arvioija voisi pitää tasoa varovaisemmin L2:na, mikäli vaaditaan vahvistettuja vaiheen 3 tuloksia juuri tästä käyttöaiheesta.

---

## Miksi ennuste on perusteltu?

Nepafenaakki on esilääke (prodrug), jonka silmäkudoksen hydrolaasientsyymit muuttavat aktiiviseksi amfenaakiksi. Amfenaakki estää syklo-oksigenaasientsyymejä COX-1 ja COX-2, mikä vähentää prostaglandiinien synteesiä ja siten silmän tulehdusta, kipua ja makulaturvotusta. Tutkimusten mukaan amfenaakki jakautuu paikallisen annon jälkeen myös silmän takaosaan.

Alkuperäinen käyttöaihe (kipu ja tulehdus kaihileikkauksen jälkeen) ja ennustettu laaja "silmäsairaus"-luokka ovat pitkälti päällekkäisiä. Vahvin näyttö koskee kaihileikkauksen jälkeistä tulehdusta ja kipua, ja sen lisäksi tutkimuksia on makulaturvotuksen ehkäisystä, diabeettisesta makulaturvotuksesta, verkkokalvon laserhoidon (panretinaalinen fotokoagulaatio) kivusta sekä laserirdotomian jälkeisestä tulehduksesta.

Tässä yhteydessä on huomattava, että mekanistista vaikutustapaa (MOA) koskevia yksityiskohtaisia tietoja ei ole tällä hetkellä saatavilla lääketietokannasta. Edellä kuvattu mekanismi perustuu julkaistuun kirjallisuuteen.

### Muut ennustetut käyttöaiheet

Muiden ennusteiden näyttö on selvästi heikompaa:

- **Optinen papilliitti:** vain prekliininen kaniinitutkimus ja yksi epäsuora tutkimus; näyttö hermon tulehduksen hyödystä puuttuu (taso L4, Hold).
- **Lasiaisirtauma:** yksi vaiheen 4 biomarkkeritutkimus verkkokalvon irtauman yhteydessä (taso L3, tutkimuskysymys).
- **Muut (esim. hiuskatoon, seborrooiseen keratoosiin, lagoftalmukseen liittyvät ennusteet):** pelkkiä malliennusteita ilman tutkimuksia tai uskottavaa mekanismia (taso L5, Hold).

---

## Kliininen tutkimusnäyttö

Alla on valikoima merkityksellisimpiä tutkimuksia (enintään 10).

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Vaihe 3 | Päättynyt | 2120 | Nepafenaakki 0,3 % silmätulehduksen ja kivun ehkäisyssä ja hoidossa kaihileikkauksen jälkeen |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Vaihe 3 | Päättynyt | 881 | Nepafenaakki 0,3 % vs. vehikkeli diabeetikoilla kaihileikkauksen jälkeen |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Vaihe 3 | Päättynyt | 819 | Sama asetelma kuin edellä; kliiniset tulokset diabeetikoilla |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Vaihe 2 | Päättynyt | 1342 | Nepafenaakki 0,3 % vs. 0,1 % vs. vehikkeli tulehduksen ja kivun hoidossa kaihileikkauksen jälkeen |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | Ei sovellettavissa | Päättynyt | 662 | Pseudofakisen kystisen makulaturvotuksen ehkäisy, nepafenaakki 0,3 % vs. lume |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Vaihe 3 | Päättynyt | 448 | Rinnakkaisvalmisteen kliininen ekvivalenssi Ilevroon nähden |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Vaihe 2 | Päättynyt | 263 | Nevanac 0,1 % vs. vehikkeli: makulaturvotuksen ilmaantuvuus diabeettisen retinopatian potilailla kaihileikkauksen jälkeen |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Vaihe 3 | Päättynyt | 260 | Nepafenaakki 0,1 % vs. lume kiinalaisilla potilailla |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Vaihe 3 | Päättynyt | 227 | Nepafenaakki 0,1 % vs. ketorolaakki ja lume Euroopassa |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Vaihe 3 | Keskeytetty | 175 | Makulaturvotuksen vaikeusasteen vähentäminen diabeettisen retinopatian potilailla |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Järjestelmällinen katsaus ja verkostometa-analyysi | Eye | Paikallisten NSAID-lääkkeiden vaikutus makulaturvotukseen ja näöntarkkuuteen faakoemulsifikaation jälkeen |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Nepafenaakki 0,1 % vs. prednisolooni 1 % leikkauksen jälkeisen tulehduksen hoidossa |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenaakki vs. prednisolooniasetaatti laserirdotomian jälkeen: turvallisuus ja teho |
| [41039316](https://pubmed.ncbi.nlm.nih.gov/41039316/) | 2025 | Järjestelmällinen katsaus / verkostometa-analyysi | BMC Ophthalmology | Seitsemän paikallista NSAID-lääkettä verkkokalvon laserhoidon kivun lievityksessä |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Katsaus | Clin Exp Optom | Nepafenaakki kaihileikkauksessa: korkea silmänsisäinen läpäisy ja vähäinen sivuvaikutusprofiili |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Katsaus | Dev Ophthalmol | NSAID-lääkkeet verkkokalvosairauksien hoidossa |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Cochrane-katsaus | Cochrane Database Syst Rev | Paikalliset NSAID-lääkkeet diabeettisessa kystisessä makulaturvotuksessa |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Prekliininen / farmakokinetiikka | Exp Eye Res | Nepafenaakin ja amfenaakin jakautuminen silmän takaosaan |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Prekliininen | Diabetes | Paikallinen nepafenaakki esti diabeettista verkkokalvon mikroverisuonisairautta rotilla |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Tapausselostus | J Cataract Refract Surg | Sarveiskalvon sulaminen (corneal melt) nepafenaakin käytön yhteydessä potilaalla, jolla oli graft-versus-host-tauti |

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000818 | Nevanac | – | Leikkauksen jälkeinen kipu; silmäkirurgiset toimenpiteet (tila: peruutettu) |

Ainoa myyntilupa (Novartis Europharm Limited) on peruutettu, joten tuotteen saatavuus on tarkistettava.

---

## Turvallisuusnäkökohdat

- **Tietämyskuvaajaan perustuvat vasta-aiheet:** TxGNN-tietämyskuvaajan (PrimeKG) mukaan lääkkeeseen liittyy mahdollisia vasta-aihe-yhteyksiä seuraavissa tiloissa: nivelreuma, diabetes, diabeettinen ketoasidoosi, veren hyytymishäiriöt, keratiitti, keratokonjunktiviitti, kuivasilmäisyys, kserooftalmia ja sarveiskalvon haava. Nämä eivät perustu valmisteyhteenvetoon, vaan ne on varmennettava erikseen.
- **Kirjallisuudessa raportoitu riski:** Sarveiskalvon sulamisesta on kuvattu tapaus potilaalla, jolla oli graft-versus-host-tauti (PMID 17964407), mikä on linjassa sarveiskalvon sairauksiin liittyvien varoitusten kanssa.

Muuten turvallisuustiedot on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Etene suojatoimin (Proceed with Guardrails)**

**Perustelut:**
- Nepafenaakin teho kaihileikkauksen jälkeisen tulehduksen, kivun ja makulaturvotuksen ehkäisyn hoidossa on tukena useissa suurissa satunnaistetuissa tutkimuksissa ja systemaattisessa katsauksessa, ja ennuste on lähellä alkuperäistä käyttöaihetta. Muut ennustetut käyttöaiheet (esim. optinen papilliitti) tulee pitää odotustilassa (Hold) näytön puutteen vuoksi.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet Fimean lähteistä (nykyinen tietoaukko estää turvallisuusarvioinnin)
- Yksityiskohtaiset vaikutusmekanismitiedot (MOA) lääketietokannasta
- Saatavuuden varmistaminen, koska Suomen myyntilupa on peruutettu (mahdolliset muut valmisteet, esim. 0,3 % vahvuus)
- Sarveiskalvon sairauksien ja diabeteksen riskipotilaiden turvallisuusseurantasuunnitelma
- Arvio siitä, kuinka laajasti "silmäsairaus"-ennuste on tarkennettava konkreettisiin käyttöaiheisiin (esim. makulaturvotus)
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

