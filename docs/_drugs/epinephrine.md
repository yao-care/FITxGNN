---
layout: default
title: Epinephrine
parent: Pelkkä mallin ennuste (L5)
nav_order: 169
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Epinephrine: ennustettu uusi käyttöaihe Obstruktiivinen keuhkosairaus (näytön taso L1). Alkuperäinen käyttöaihe: Anafylaksia"
monitor_inn: "EPINEPHRINE"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
---

# Epinephrine
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

## Epinefriini: Obstruktiivinen keuhkosairaus
{: .text-alpha }

## Yhden virkkeen yhteenveto

Epinefriini on adrenerginen agonisti, jota on alun perin käytetty anafylaksian hoitoon.
TxGNN-malli ennustaa sen voivan tehota **obstruktiiviseen keuhkosairauteen** (astma, keuhkoahtaumatauti ja bronkioliitti),
ja tätä suuntaa tukee tällä hetkellä **15 kliinistä tutkimusta** ja **20 julkaisua**.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Anafylaksia |
| Ennustettu uusi käyttöaihe | Obstruktiivinen keuhkosairaus |
| TxGNN-ennusteen pistemäärä | 0,9971 |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Markkinoilla (voimassa olevia lupia: 1/1) |
| Myyntilupien määrä | 1 (voimassa: 1) |
| Suositeltu päätös | Proceed with Guardrails (eteneminen suojatoimin) |

---

## Miksi ennuste on perusteltu?

Epinefriini on epäselektiivinen adrenerginen agonisti. Beta-2-reseptorien aktivoituminen rentouttaa keuhkoputkien sileää lihaksistoa ja laajentaa keuhkoputkia. Alfa-1-reseptorien aktivoituminen supistaa verisuonia ja vähentää limakalvojen turvotusta. Tämä sopii suoraan palautuvaan hengitysteiden ahtautumiseen (astma) ja pienten hengitysteiden tulehdukselliseen ahtautumiseen (bronkioliitti).

Alkuperäinen käyttöaihe, anafylaksia, ja ennustettu käyttöaihe jakavat saman farmakologisen perustan: molemmissa hoidon tavoitteena on keuhkoputkien laajentaminen ja hengitysteiden turvotuksen vähentäminen. Yksityiskohtaista vaikutusmekanismitietoa ei ole tähän raporttiin koottu tietokannasta, mutta edellä kuvattu mekanismi on yleisesti tunnettu.

Systeemisen adrenergisen vaikutuksen sydän- ja verisuonihaittoja (takykardia, verenpaineen nousu) on seurattava, erityisesti potilailla, joilla on keuhkoahtaumatauti ja sydänsairauksia.

---

## Kliininen tutkimusnäyttö

| Tutkimusnumero | Vaihe | Tila | Osallistujia | Keskeiset havainnot |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Vaihe 3 | Päättynyt | 373 | Epinefriini-inhalaatioaerosolin (HFA-MDI) teho ja turvallisuus astmassa vs. lume ja Primatene Mist |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Vaihe 3 | Päättynyt | 208 | 3 kuukauden kaksoissokkoutettu turvallisuuslaajennus astmapotilailla |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Vaihe 3 | Päättynyt | 70 | E004-inhalaatioaerosolin teho ja turvallisuus lasten astmassa (4 viikkoa) |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Vaihe 3 | Päättynyt | 28 | Kerta-annos E004:ää 4–11-vuotiailla astmalapsilla, satunnaistettu ristikkäisasetelma |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Vaihe 4 | Päättynyt | 49 | Lihaksensisäinen epinefriini lisähoitona lasten vaikeassa astman pahenemisvaiheessa |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Vaihe 4 | Päättynyt | 120 | Epinefriini, deksametasoni ja hypertoninen keittosuola lasten bronkioliitissa (yhdistelmähoito) |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Vaihe 4 | Tuntematon | 500 | Optimaalinen inhalaatiohoito alle 12 kk:n ikäisten bronkioliitissa |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Vaihe 4 | Päättynyt | 28 | Primatene Mistin systeeminen altistus verrattuna lihaksensisäiseen epinefriiniin terveillä |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Vaihe 2 | Päättynyt | 24 | Epinefriini-inhalaatioaerosolin farmakokinetiikka terveillä vapaaehtoisilla |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | Ei määritelty | Tuntematon | 600 | Epinefriinin ja albuterolin vertailu bronkioliitissa |

---

## Kirjallisuusnäyttö

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset havainnot |
|---------|-----|------|------|---------|
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Verkostometa-analyysi | Pediatrics | Bronkioliitin hoitojen vertaileva teho akuuttihoidossa |
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | The Journal of Pediatrics | Kortikosteroidien ja inhaloidun epinefriinin yhdistelmä lasten teho-osastolla bronkioliitissa |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systemaattinen katsaus (Cochrane) | Cochrane Database Syst Rev | Epinefriini bronkioliitissa |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systemaattinen katsaus (Cochrane) | Cochrane Database Syst Rev | Bronkodilataattorit tuottavat lievän lyhytaikaisen hyödyn lievässä tai keskivaikeassa bronkioliitissa |
| [22389988](https://pubmed.ncbi.nlm.nih.gov/22389988/) | 2011 | Satunnaistettu tutkimus | Turk J Pediatr | Nebulisoidun epinefriinin ja salbutamolin vertailu akuutissa bronkioliitissa päivystyksessä (75 potilasta) |
| [40378135](https://pubmed.ncbi.nlm.nih.gov/40378135/) | 2025 | Bayesilainen analyysi | PLoS One | Epinefriinin ja deksametasonin vaikutus bronkioliitin sairaalahoitoon (CanBEST-aineisto) |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Katsaus | Emerg Med Clin North Am | Astman ja keuhkoahtaumataudin pahenemisvaiheiden arviointi ja hoito päivystyksessä |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Katsaus | Expert Rev Respir Med | Rasemisen epinefriinin, kortikosteroidien, hypertonisen keittosuolan ja high-flow-hapen rooli bronkioliitissa |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Katsaus | Duodecim | Bronkioliitti Suomessa; rasemista epinefriiniä tarvittaessa inhalaationa |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Kustannusvaikuttavuusanalyysi | Pediatrics | Epinefriinin ja deksametasonin kustannusvaikuttavuus bronkioliitissa |

---

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/006139 | Eurneffy | – | Anafylaksia (myyntilupa peruutettu) |

---

## Turvallisuushuomiot

- **Mahdolliset vasta-aiheet (tietämysgraafista, ei valmisteyhteenvedosta):** Tietämysgraafi liittää epinefriiniin mm. seuraavat sairaudet: hypertensio, sepelvaltimotauti, sydäninfarkti, eteisvärinä, sydämen johtumishäiriöt, sydänsairaudet, kilpirauhasen liikatoiminta, diabetes ja diabeettinen ketoasidoosi, ahdaskulmaglaukooma, epilepsia, munuaisten ja maksan sairaudet, myasthenia gravis sekä hengitysvajaus.
- **Lääkeyhteisvaikutukset:** Yhteisvaikutuksia löytyi yhteensä 100. Vakavia (Major) ovat mm. amitriptyliini ja amoksapiini. Kohtalaisia (Moderate) ovat mm. beetasalpaajat (asebutololi, atenololi, betaksololi), beeta-2-agonistit (formoteroli, salbutamoli, arformoteroli), metyylifenidaatti, amfetamiini, atomoksetiini, aripipratsoli, amisulpridi sekä diabeteslääkkeet (akarboosi, alogliptiini, albiglutidi).

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla, joten ne on tarkistettava valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Proceed with Guardrails (eteneminen suojatoimin)**

**Perustelut:**
- Useat päättyneet vaiheen 3 tutkimukset tukevat inhaloidun epinefriinin tehoa ja turvallisuutta astmassa, ja bronkioliitista on satunnaistettuja tutkimuksia sekä Cochrane-katsauksia. Mekanismi sopii hyvin hengitysteiden ahtautumiseen. Bronkioliitissa näyttö on kuitenkin ristiriitaista ja osin yhdistelmähoitoihin perustuvaa, ja sydän- ja verisuoniriskit vaativat rajauksia.
- Suomessa ainoa myyntilupa on peruutettu, joten valmistetta ei tällä hetkellä ole markkinoilla.

**Eteneminen edellyttää seuraavaa:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkiminen Fimean sivuilta (estävä tietoaukko turvallisuusseulonnalle).
- Yksityiskohtaisten vaikutusmekanismitietojen täydentäminen DrugBankista.
- Annostelureitin ja lääkemuodon arviointi (inhalaatio vs. lihaksensisäinen) sekä myyntiluvan tilanteen selvittäminen.
- Sydän- ja verisuoniturvallisuuden seurantasuunnitelma erityisesti keuhkoahtaumatautia sairastaville ja sydänsairaille potilaille.

---

*Muut ennustetut käyttöaiheet:* ruokaperäinen rasitusanafylaksia (L4, tutkimuskysymys; käytännössä nykyisen anafylaksiaindikaation laajennus ilman erillisiä tutkimuksia), hengitysteiden epämuodostuma (L3, tutkimuskysymys; vaikutus oireenmukainen, yhteys epäsuora) ja Rienhoffin oireyhtymä (L5, Hold; ei tutkimus- tai kirjallisuusnäyttöä, pelkkä mallin ennuste).
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

