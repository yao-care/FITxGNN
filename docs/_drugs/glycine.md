---
layout: default
title: Glycine
parent: Pelkkä mallin ennuste (L5)
nav_order: 209
evidence_level: L5
indication_count: 2
---

# Glycine
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

# Glysiini: Vaahterasiirappitaudista nenäontelon sairauteen

## Yhden virkkeen yhteenveto

Glysiini (kauppanimi Maapliv) on aminohappo, jonka alkuperäinen käyttöaihe on vaahterasiirappitauti (MSUD). TxGNN-malli ennustaa sen voivan tehota **nenäontelon sairauteen**, mutta ennustetta tukee vain malliennuste: tietoihin sisältyy **1 kliininen tutkimus** ja **2 julkaisua**, eikä yksikään niistä käsittele glysiiniä.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Vaahterasiirappitauti (MSUD) |
| Ennustettu uusi käyttöaihe | Nenäontelon sairaus |
| TxGNN-ennustepisteet | 99,85 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Tällä hetkellä yksityiskohtaista vaikutusmekanismia koskevia tietoja ei ole saatavilla. Tunnetun tiedon perusteella glysiini on elimistön yleinen aminohappo ja estävä välittäjäaine. Sen tehosta vaahterasiirappitaudissa on myyntilupaan johtanut näyttö, mutta mekanistista yhteyttä nenäontelon sairauksiin ei voida osoittaa.

TxGNN-pistemäärä on hyvin korkea (0,998), mutta se on pelkkä mallipohjainen ennuste. Ennustetta ei voida verrata tunnettuun mekanismiin, eikä aineistossa ole glysiinikohtaista tietoa, joka yhdistäisi sen nenäontelon patologiaan. Ennustetta ei siksi voida pitää uskottavana ilman lisänäyttöä.

Toinen ennustettu käyttöaihe, **akuutti laryngofaryngiitti** (pisteet 99,84 %), on samassa tilanteessa: sille ei ole kliinisiä tutkimuksia eikä julkaisuja.

## Kliininen tutkimusnäyttö

| Tutkimustunnus | Vaihe | Tila | Osallistujamäärä | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Vaihe 1–2 | Päättynyt | 25 | 18F-FPPRGD2-PET-kuvantamistutkimus angiogeneesin merkkiaineesta syöpäpotilailla (glioblastooma, gynekologiset syövät, munuaissyöpä). Diagnostinen kuvantamistutkimus; ei liity glysiiniin, todennäköisesti sattumaosuma. |

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Perustutkimus | Veterinary Pathology | Lektiinihistokemia normaalissa ja herpesviruksen infektoimassa naudan nenän limakalvossa; ei glysiinitietoa. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Perustutkimus | Chemical & Pharmaceutical Bulletin | Oligoarginiini-polymeerit limakalvorokotteen apuaineena hiirten nenäontelossa; ei glysiinitietoa. |

## Myyntiluvat Suomessa

| Myyntilupanumero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv (Recordati Rare Diseases) | Ei tietoa | Vaahterasiirappitauti (peruutettu) |

## Turvallisuushuomioita

Valmisteyhteenvedon varoitus- ja vasta-aihetietoja ei ole saatavilla, joten niihin on tutustuttava erikseen valmisteyhteenvedosta.

Tietämyskuvaajaan (PrimeKG) perustuvat vasta-aiheyhteydet eivät ole valmistekohtaista tekstiä vaan mallin tietopohjaa. Niiden mukaan glysiiniin voi liittyä vasta-aihesuhde mm. seuraaviin tiloihin:
- munuaissairaudet (krooninen munuaisten vajaatoiminta, loppuvaiheen munuaisten vajaatoiminta, nefrokalsinoosi, munuaiskivitauti)
- kalsium- ja fosforiaineenvaihdunnan häiriöt (hyperkalsemia, hyperparatyreoosi, hyperfosfatemia)
- sydän- ja verisuonisairaudet (sydänsairaus, kammiovärinä, digitalismyrkytys)
- fenyyliketonuria ja muut fenyylialaniinin aineenvaihdunnan häiriöt
- sarkoidoosi, ummetus ja hypervitaminoosi

Lääkeyhteisvaikutuksista ei löytynyt tietoja.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkästään TxGNN-mallin pisteisiin (L5). Ainoa löytynyt tutkimus on glysiiniin liittymätön kuvantamistutkimus, kirjallisuus on eläin- ja perustutkimusta ilman glysiinitietoa, eikä mekanistista yhteyttä voida osoittaa. Lisäksi valmisteen myyntiluvat Suomessa on peruutettu.

**Eteneminen edellyttää seuraavaa:**
- Glysiinin vaikutusmekanismin selvittäminen (esim. DrugBankista).
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimeasta (turvallisuusarvioinnin estävä puute).
- Glysiinikohtaisen prekliinisen tai kliinisen näytön löytäminen nenäontelon sairauksista.
- Antoreitin soveltuvuuden arviointi (nenään annettava muoto) sekä munuais- ja aineenvaihduntatilojen vasta-aihesignaalien tarkastelu.
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

