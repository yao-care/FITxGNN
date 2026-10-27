---
layout: default
title: Leflunomide
parent: Pelkkä mallin ennuste (L5)
nav_order: 257
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Leflunomide: ennustettu uusi käyttöaihe Brakydaktylia-syndaktylia-oireyhtymä (näytön taso L5). Alkuperäinen käyttöaihe: Nivelreuma"
monitor_inn: "LEFLUNOMIDE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Leflunomide
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

## Leflunomidi: Nivelreumasta ja nivelpsoriaasista brakydaktylia-syndaktylia-oireyhtymään
{: .text-alpha }

## Yhteenveto

Leflunomidi on immuunivastetta muokkaava lääke, jota on käytetty nivelreuman ja nivelpsoriaasin hoitoon. TxGNN-malli ennustaa sen voivan tehota **brakydaktylia-syndaktylia-oireyhtymään**, mutta ennuste perustuu pelkästään tietämysgraafiin: **kliinisiä tutkimuksia ei ole lainkaan** eikä **julkaisuja ole yhtään**. Lisäksi ennustetun käyttöaiheen biologinen uskottavuus on heikko.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Nivelreuma; nivelpsoriaasi |
| Ennustettu uusi käyttöaihe | Brakydaktylia-syndaktylia-oireyhtymä |
| TxGNN-ennusteen pistemäärä | 99,93 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 4 (kaikki peruutettuja) |
| Suositeltu päätös | Hold (odota) |

---

## Miksi ennuste voisi olla perusteltu?

Yksityiskohtaista vaikutusmekanismitietoa ei ole tässä raportissa käytettävissä. Yleisen tiedon mukaan leflunomidi estää dihydroorotaattidehydrogenaasi-entsyymiä (DHODH), mikä rajoittaa pyrimidiinisynteesiä ja vaikuttaa nopeasti jakautuviin soluihin, kuten aktivoituneisiin lymfosyytteihin. Tämä päätelmä perustuu yleistietoon, ei raportin aineistoon.

DHODH liittyy myös raajojen kehitykseen: DHODH-geenin mutaatiot aiheuttavat Millerin oireyhtymän, johon kuuluu raajojen epämuodostumia. Graafin läheisyys voi siis heijastaa yhteisiä raajojen kehitykseen liittyviä reittejä. Tämä on kuitenkin vain mahdollinen, todentamaton selitys.

Alkuperäinen käyttöaihe (autoimmuuni nivelsairaus) ja ennustettu käyttöaihe (synnynnäinen luuston epämuodostuma) eroavat toisistaan olennaisesti. Brakydaktylia-syndaktylia-oireyhtymät ovat rakenteellisia kehityshäiriöitä, joille ei tunneta lääkkeellistä korjausta. Leflunomidin aktiivinen metaboliitti teriflunomidi on lisäksi teratogeeninen eli sikiövaurioita aiheuttava. Mekanistinen yhteys on siis spekulatiivinen.

Toinen ennuste, kolobomatoottinen mikroftalmia-rhizomeelinen dysplasia -oireyhtymä (pistemäärä 99,93 %), on samalla tavoin pelkkä graafiennuste ilman tukevaa näyttöä. Siinä on kyse silmän ja raajojen rakenteellisista epämuodostumista, joiden lääkehoito vakiintuneessa sairaudessa on biologisesti epäuskottavaa.

---

## Markkinatiedot Suomessa

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000235 | Arava | – | Nivelreuma; nivelpsoriaasi |
| EMEA/H/C/001129 | Leflunomide Zentiva (aiemmin Leflunomide Winthrop) | – | Nivelreuma; nivelpsoriaasi |
| EMEA/H/C/001227 | Leflunomide medac | – | Nivelreuma |
| EMEA/H/C/002035 | Leflunomide ratiopharm | – | Nivelreuma |

Kaikki neljä myyntilupaa on peruutettu, eikä voimassa olevia myyntilupia ole.

---

## Turvallisuusnäkökohdat

Valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole saatavilla, joten niihin on tutustuttava valmisteyhteenvedosta.

**Tietämysgraafin mukaiset vasta-aihe-ehdotukset** (perustuvat graafin lääke-sairaus-yhteyksiin, eivät valmisteyhteenvetoon):
- Maksa ja sappi: maksan vajaatoiminta, maksasairaus, sappirakon sairaus, krooninen hepatiitti B ja C
- Munuaiset: munuaissairaus
- Veri: trombosytopenia, neutropenia, agranulosytoosi, pansytopenia, anemia, makrosyyttinen anemia sekä useat synnynnäiset neutropenian muodot
- Hermosto: perifeerinen neuropatia, ääreishermoston sairaudet
- Keuhkot ja infektiot: interstitiaalinen keuhkosairaus, pneumokystoosi, aspergilloosi
- Muut: pyoureter

**Lääkeyhteisvaikutukset** (kyselyssä yhteensä 100 yhteisvaikutusta, joista tässä esimerkkejä):
- **Merkittävät (Major):** asetyylisalisyylihappo, hydrokortisoni, deksametasoni, betametasoni, triamsinoloni, budesonidi, pioglitatsoni, akarboosi, bupropioni, klaritromysiini, minosykliini, naltreksoni, kenodeoksikolihappo, oksandroloni, oksimetolonin
- **Kohtalaiset (Moderate):** metronidatsoli, klooripropamidi, asetoheksamidi
- **Lievät (Minor):** sinkkisulfaatti, sinkkiasetaatti

Lisäksi leflunomidin aktiivinen metaboliitti on teratogeeninen, mikä on merkittävä turvallisuusnäkökohta.

---

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennusteilla ei ole kliinistä eikä kirjallisuusnäyttöä (taso L5), ja ennustetut sairaudet ovat synnynnäisiä rakenteellisia epämuodostumia, joiden lääkkeellinen hoito on biologisesti epäuskottavaa. Lisäksi lääke on teratogeeninen ja kaikki Suomen myyntiluvat on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Vaikutusmekanismitietojen täydentämistä (esim. DrugBankista)
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimean sivuilta
- Prekliinistä tai mekanistista näyttöä ennustetuista käyttöaiheista
- Arviota teratogeenisuuden ja ennustetun käyttöaiheen yhteensopivuudesta
- Selvitystä peruutettujen myyntilupien syistä ja nykyisistä saatavuusreiteistä
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

