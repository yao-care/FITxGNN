---
layout: default
title: Ceritinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Ceritinib
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **10** kpl
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

# Seritinibi: ALK-positiivisesta pieni-solaisesta keuhkosyövästa gingivaaliseen fibromatoosiin

## Yhden lauseen yhteenveto

Seritinibi on toisen sukupolven ALK-tyyrosiinikinaasin estäjä, jonka hyväksytty käyttöindikatio — tässä evidenssipaketissa saadun tutkimus- ja katsauskirjallisuuden perusteella — on ALK:n uudelleenjärjestyneisyyteen liittyvä pieni-solaisesti keuhkosyöpä (NSCLC); lääkkeen oma rakenteellinen alkuperäisen indikaation kenttä on tyhjä tässä paketissa (tietojen puutos). TxGNN-mallin parhaiten ennustettu indikatio tälle lääkkeelle on **Gingiivinen fibromatoosi**, mutta tällä ennusteella ei ole **yhtään kliinistä tutkimusta eikä yhtään kirjallisuusviitettä** tuekseen, eikä sillä ole tunnettu mekanistista yhteyttä ALK-signalointireittiin — se on pelkästään mallin pistelukusignaali.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikatio | ALK-positiivinen (ALK:n uudelleenjärjestyneisyys) pieni-solaisesti keuhkosyöpä — pääteltävissä tässä evidenssipaketissa olevasta kirjallisuudesta (esim. ASCEND-4, "Ceritinib: first global approval"); ei saatavissa rakenteellisista `taiwan_regulatory`/`original_indications`-kentistä (tietojen puutos) |
| Ennustettu uusi indikatio | Gingiivinen fibromatoosi (Fibromatosis, Gingival) |
| TxGNN-ennusteen pisteluku | 99.86% (sijoitus 2020 kaikkien ehdokkaiden joukossa) |
| Evidenssin taso | L5 |
| Taiwanin markkinointi | Ei markkinoilla (Not marketed) |
| Valtuuksien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennuste on perusteltu?

Yksityiskohtaisia toimintamekanismitietoja ei ole saatavissa rakenteellisesta `original_moa`-kentästä (tietojen puutos, DG002). Tässä evidenssipaketissa saadun kirjallisuuden perusteella seritinibi on toisen sukupolven, suun kautta imeytyvästi kehitetty pieni-molekyylinen anaplastisen lymfoomasyypakinaasin (ALK) estäjä, joka on kehitetty ALK-geenin uudelleenjärjestyneisyydellä ohjautuviin kasvaimiin, erityisesti ALK-positiiviseen NSCLC:hen (PMID 24980964, 27738095, 28126333).

Gingiivinen fibromatoosi on tyypillisesti perinnöllinen tai lääkkeistä johtuva (esim. fenitoin, siklosporiini, kalsiumkanavansalpaajat) gingivaalisen sidekudoksen hyvänlaatuinen liikakasvaminen. ALK-reseptorityrosiinikinaasin signaloinnin ja gingivaalisen kuituisen liikakasvamisen välillä ei ole vakiintunutta biologista yhteyttä, eikä fibroblastien lisääntymis- tai sidekudomuutoksia ole mainittu missään toimitetuissa näytöissä.

Yhdenmukaisen kuvan mukaisesti tämän evidenssipaketin rationale sanoo suoraan: tämälle ehdokkaalle ei ole kliinisiä tutkimuksia, kirjallisuusviitteitä ei ole saatavilla, eikä ALK-signalointireitin ja gingivaalisen fibromaattosin välillä ole tunnettua mekanistista yhteyttä — kyseessä on puhtaasti TxGNN-mallin pisteluku, jolla ei ole mitään tukevaa näyttöä.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Taiwanin markkinoinnin tiedot

Seritinibi ei ole tällä hetkellä **markkinoilla Taiwanissa** — rekistereissä on 0 valtuutusta, ja `licenses`-järjestelmä on tyhjä, joten valtuutusnumeroa, tuotenimeä, annosmuotoa tai hyväksytyn indikaation tekstiä ei voi poimia tästä evidenssipaketista.

## Sytotoksisuus

Seritinibi on antineoplastinen lääke (ALK/ROS1-tyyrosiinikinaasin estäjä, jota käytetään NSCLC:ssä edellä mainitun kirjallisuuden mukaan), joten tämä osio on relevantti.

| Kohta | Sisältö |
|------|---------|
| Sytotoksisuusluokitus | Kohdennettu hoito (toisen sukupolven ALK-tyyrosiinikinaasin estäjä; ei tavanomainen sytostaattinen kemia) |
| Luuytimen vähenemisen riski | Ei ole erityisesti raportoitu toimitetuissa näytöissä; lääkkeluokkana ALK-estäjillä on tyypillisesti matalampi luuytimen vähenemisen riski kuin tavallisella sytostaattisella kemialla — katso pakkausselosteesta hematoloogisen toksisiteetin arviointia |
| Pahoinvoinnin luokitus | Kohtalainen — GI-toksisuus on raportoitu näytöissä (ASCEND-8-aliryhmäanalyysi, PMID 35344649, osoitti vähennettyä GI-toksisiteettia muutetulla ruoan kanssa ottamisella, mikä viittaa perustason GI-toksisiteetin kliiniseen merkitykseen) |
| Monitorointikohdat | EKG/QTc-väli (PMID 26008987, 29413968), maksantoiminta, GI-oireet (pahoinvointi, ripuli), tromboemboliset tapahtumat (PMID 39349372) ja keuhko-/yliherkkyystapahtumat (PMID 31280988 — tapaus diffuusista keuhkojen infiltratiivisesta sairaudesta, perikardiitista ja pleuraalihuuhtelusta seritinibin yliherkkyydessä) |
| Käsittelysuojaus | Ei määritelty toimitetussa evidenssissa. Suun kautta otettavana pienimolekyylisena kohdennetun hoidon aineena noudateta institutionaalisia suun kautta otettavien sytostaattien käsittelymenettelyjä, odottaen TFDA-pakkausselosteen vahvistusta (katso estävä tietojen puutos alla) |

## Turvallisuusnäkökohdat

Viittaa pakkausselosteeseen turvallisuustiedoista. (Tärkeitä varoituksia, vasta-aiheita ja lääkkeiden välisiä yhdysvaikutuksia koskevia tietoja ei ole saatavilla tässä evidenssissa; TFDA-pakkausselosteen hakemista ei ole vielä suoritettu.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Parhaiten ennustettu indikatio, gingiivinen fibromatoosi, ei ole kliinisten tutkimusten tai kirjallisuuden tuella, eikä sillä ole uskottavaa mekanistista yhteyttä ALK-inhibitioon — se on puhdas mallin pistelukuartefakti (L5, päätösvaihe S0). Mikään muista 9 ehdokkaasta tässä erässä ei ole parempi: kahdella, joilla on kirjallisuusviitteitä (keuhkohyväntapauksinen neoplasmi, keuhkon sukusolukasvain, molemmat L4), on omissa perusteluissaan merkitty ne selvästi ontologiaan perustuviksi ristiriidoiksi (näyttö koskee pahanlaatuista NSCLC:tä tai glioblastoomaa/keskushermostoon metastasoitumista, ei ennustettuja hyväntapauksisia kokonaisuuksia), ja loput 7:llä ei ole mitään näyttöä.

**Jatkaakseen seuraavaa tarvitaan:**
- TFDA-pakkausselosteen hakeminen ja jäsennys varoituksista/vasta-aiheista (estävä puutos DG001)
- DrugBank-mekanismin vahvistus (DG002)
- Jos jatketaan uudelleenkäyttötutkimusta, asetetaan etusijalle mekanistisesti uskottavat, tutkittavissa olevat ehdokkaat (esim. ALK-positiivisuuden ohjaamat kasvaimen alatyyppi) nykyisen parhaiten ennustetun indikaation sijaan
- Gingiiviselle fibromatoosille tai muille 9 ennustetuille indikaatioille tässä erässä ei suositella lisätutkimusta näyttöjen ja mekanistisen uskottavuuden puuttuessa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

