---
layout: default
title: Evolocumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 183
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Evolocumab: ennustettu uusi käyttöaihe Hemofilian oireinen muoto naispuolisilla kantajilla (näytön taso L5). Alkuperäinen käyttöaihe: Dyslipidemiat"
monitor_inn: "EVOLOCUMAB"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
---

# Evolocumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Evolokumabi: Dyslipidemiasta ja hyperkolesterolemiasta ennustettuun hemofilian oireiseen kantajuuteen

## Yhteenveto

Evolokumabi on PCSK9:ää estävä monoklonaalinen vasta-aine, jota käytetään dyslipidemian ja hyperkolesterolemian hoitoon.
TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **hemofilian oireisen muodon naispuolisilla kantajilla**, mutta ennustetta tukee **0 kliinistä tutkimusta** ja **0 julkaisua**. Ennuste on pelkkä laskennallinen tulos, eikä sille ole tunnistettu biologisesti perusteltua mekanismia.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Dyslipidemiat; hyperkolesterolemia |
| Ennustettu uusi käyttöaihe | Hemofilian oireinen muoto naispuolisilla kantajilla |
| TxGNN-ennustepisteet | 99,82 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettu myyntilupa |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste on (tai ei ole) perusteltu?

Evolokumabi sitoutuu PCSK9-proteiiniin (proproteiinikonvertaasi subtilisiini/keksiini tyyppi 9) ja estää sen vuorovaikutuksen LDL-reseptorin kanssa. Tämä lisää LDL-reseptorien saatavuutta ja alentaa LDL-kolesterolia. Yksityiskohtaisia vaikutusmekanismitietoja ei ole tämän raportin aineistossa saatavilla, joten kuvaus perustuu yleiseen farmakologiseen tietoon ja kohdetietoon (PCSK9).

Hemofilian kantajien oireet johtuvat veren hyytymistekijä VIII:n tai IX:n alentuneesta pitoisuudesta X-kromosomissa periytyvien muutosten vuoksi. Tämä mekanismi ei liity PCSK9:ään eikä LDL-aineenvaihduntaan. Mekanistista yhteyttä alkuperäisen ja ennustetun käyttöaiheen välillä ei ole tunnistettu.

Korkea TxGNN-pistemäärä (0,998) perustuu verkkopohjaiseen ennusteeseen, jota eivät tue tutkimukset, julkaisut tai biologinen perustelu. Pistemäärä yksin ei riitä perustelemaan jatkotoimia.

### Muut ennustetut käyttöaiheet

Aineistossa on myös muita ennusteita, joilla on samoin vain L5-taso ja suositus Hold:

| Sija | Ennustettu käyttöaihe | TxGNN-pisteet | Arvio mekanistisesta yhteydestä |
|------|------|------|------|
| 2 | Familiaalinen apolipoproteiini C-II -puutos | 99,50 % | Epäsuora uskottavuus; evolokumabi laskee pääasiassa LDL-kolesterolia eikä korjaa triglyseridien hajotuksen perusvikaa |
| 3 | Trombosytopeeninen purppura | 99,42 % | Ei selvää yhteyttä; mekanismi liittyy autovasta-aineisiin, ADAMTS13-puutokseen tai verihiutaleiden tuhoutumiseen |
| 4 | Tekijä XI:n puutos | 99,29 % | Ei uskottavaa yhteyttä; evolokumabi ei vaikuta hyytymistekijöihin |
| 5 | Hemofilia A, johon liittyy verisuonianomalia | 99,22 % | Ei uskottavaa yhteyttä; LDL:n lasku ei korjaa tekijä VIII:n puutosta |
| 6 | Katalyyttisen aktiivisuuden sairaus | 99,08 % | Epäspesifinen ontologialuokka, ei määritelty kliininen käyttöaihe |

---

## Kliininen tutkimusnäyttö

Ei tällä hetkellä aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

---

## Kirjallisuusnäyttö

Ei tällä hetkellä aiheeseen liittyvää kirjallisuutta.

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/003766 | Repatha | Ei tietoa | Dyslipidemiat; hyperkolesterolemia |

Myyntilupa on tilassa "peruutettu", eikä voimassa olevia myyntilupia ole.

---

## Turvallisuusnäkökohdat

**Lääkeyhteisvaikutukset:** Yhteisvaikutushaussa löytyi yksi farmakologinen merkintä: evolokumabin kohdeproteiini PCSK9 (vasta-aine, sitoutuu ihmisen PCSK9:ään). Kyse on lääkkeen vaikutuskohteesta, ei kliinisesti merkittävästä lääkeyhteisvaikutuksesta, eikä yhteisvaikutuksen vakavuustasoa ole ilmoitettu.

Muuta turvallisuustietoa ei ole saatavilla. Tarkista varoitukset ja vasta-aiheet valmisteyhteenvedosta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu pelkkään laskennalliseen TxGNN-pistemäärään (L5). Kliinisiä tutkimuksia ja julkaisuja ei ole, eikä biologisesti uskottavaa mekanistista yhteyttä PCSK9:n eston ja hemofilian kantajuuden oireiden välillä ole tunnistettu.
- Lisäksi Suomen myyntilupa on peruutettu, joten valmiste ei ole tällä hetkellä markkinoilla.

**Jatkotoimien edellytyksenä tarvitaan:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankinta Fimeasta (turvallisuusarvioinnin estävä tietoaukko)
- Yksityiskohtaiset vaikutusmekanismitiedot (esim. DrugBankista)
- Prekliininen tai mekanistinen näyttö mahdollisesta yhteydestä hyytymisjärjestelmään
- Selvitys valmisteen saatavuudesta Suomessa myyntiluvan peruutuksen jälkeen
- Jos jatkoanalyysi tehdään, harkitaan ensisijaisesti lipidiaineenvaihdunnan häiriöitä (esim. ApoC-II-puutos), joissa on edes epäsuora biologinen uskottavuus, mutta sekin vaatii suoraa tutkimusnäyttöä
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

