---
layout: default
title: Gilteritinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 201
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Gilteritinib: ennustettu uusi käyttöaihe Bulbaarinen polio (näytön taso L5). Alkuperäinen käyttöaihe: Akuutti myeloidinen leukemia"
monitor_inn: "Gilteritinib"
predicted_indications: ["bulbar polio"]
---

# Gilteritinib
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

## Gilteritinibi: Akuutista myeloidisesta leukemiasta bulbaariseen polioon
{: .text-alpha }

## Yhteenveto

Gilteritinibi on FLT3-tyrosiinikinaasin estäjä, jota on alun perin käytetty akuutin myeloidisen leukemian hoitoon. TxGNN-malli ennustaa sen voivan tehota **bulbaariseen polioon**, mutta ennusteelle ei löydy tukea: **kliinisiä tutkimuksia on 0** ja **julkaisuja on 0**. Ennuste perustuu pelkästään mallilaskentaan.

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Akuutti myeloidinen leukemia |
| Ennustettu uusi käyttöaihe | Bulbaarinen polio |
| TxGNN-ennustepistemäärä | 99,10 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste voisi olla perusteltu?

Yksityiskohtaisia tietoja lääkkeen alkuperäisestä vaikutusmekanismista ei ole tällä hetkellä saatavilla. Käytettävissä olevien farmakologisten tietojen mukaan gilteritinibi estää voimakkaasti FLT3-kinaasia, mukaan lukien villityypin ja mutatoituneen FLT3:n (esim. FLT3-ITD). Prekliinisissä solututkimuksissa IC50-arvo oli villityypin FLT3:lle noin 5 nM ja FLT3-ITD-mutantille alle 2 nM. Lääke vaikuttaa myös muihin kinaaseihin, kuten AXL, MERTK, LTK, ALK, ROS1, RET ja NTRK1.

Akuutti myeloidinen leukemia ja bulbaarinen polio ovat biologisesti hyvin kaukana toisistaan. Edellinen on verta muodostavan kudoksen syöpä, jälkimmäinen poliovirusinfektio, joka vaurioittaa aivorungon liikehermosoluja. FLT3- tai AXL-eston ja poliovirusinfektion välillä ei tunneta uskottavaa biologista yhteyttä. AXL:n on esitetty osallistuvan joidenkin muiden virusten soluun pääsyyn tai immuunivasteen välttämiseen, mutta poliovirukselle tätä ei ole osoitettu, joten yhteys olisi spekulatiivinen.

Tämän vuoksi TxGNN-pistemäärä (0,991) on vain mallin tuottama ennuste, eikä sitä tue mikään kliininen tai kirjallisuusnäyttö.

## Kliininen tutkimusnäyttö

Aiheeseen liittyviä kliinisiä tutkimuksia ei ole tällä hetkellä rekisteröity.

## Kirjallisuusnäyttö

Aiheeseen liittyvää kirjallisuutta ei ole tällä hetkellä saatavilla.

## Tiedot Suomen markkinoilta

| Myyntiluvan numero | Tuotenimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/004752 | Xospata | – | Akuutti myeloidinen leukemia (peruutettu) |

## Sytotoksisuus

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (tyrosiinikinaasin estäjä) |
| Myelosuppressioriski | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Oksettavuusluokitus | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Seurantakohteet | Katso valmisteyhteenvedon varoitukset ja varotoimet |
| Käsittelysuojaus | Katso valmisteyhteenvedon varoitukset ja varotoimet |

## Turvallisuushuomiot

**Lääkkeiden yhteisvaikutukset:** Yhteisvaikutushaku on tehty. Löydettyjä kohteita on 8, ja ne ovat farmakologisia kohdevaikutuksia, ei tavanomaisia lääke–lääke-yhteisvaikutuksia. Kohteet ovat FLT3, NTRK1, AXL, MERTK, LTK, ALK, ROS1 ja RET. Yhteisvaikutusten vaaraluokkia ei ole ilmoitettu.

**Muita huomioita:** Gilteritinibi on syöpälääke, jolla on immuunijärjestelmää ja luuytimen toimintaa heikentäviä vaikutuksia. Sen käyttö aktiivisessa hermoston virusinfektiossa voisi aiheuttaa turvallisuusongelmia. Lisäksi polio ehkäistään pääosin rokotuksilla ja hoidetaan oireenmukaisesti.

Muuten turvallisuustietojen osalta katso valmisteyhteenveto.

## Johtopäätös ja jatkotoimet

**Päätös: Hold (odota)**

**Perustelut:**
- Ennuste perustuu vain TxGNN-mallin pistemäärään. Kliinisiä tutkimuksia ja julkaisuja ei ole, eikä uskottavaa mekanistista yhteyttä gilteritinibin ja poliovirusinfektion välillä ole osoitettu. Lisäksi lääkkeen Suomen myyntiluvat on peruutettu.

**Eteenpäin siirtyminen edellyttää:**
- Valmisteyhteenvedon varoitusten ja vasta-aiheiden hankkimista Fimeasta, koska ne puuttuvat tällä hetkellä
- Vaikutusmekanismin tietojen täydentämistä
- Prekliinistä näyttöä FLT3/AXL-eston vaikutuksesta poliovirukseen tai aivorungon motoneuroneihin
- Turvallisuusarviota immunosuppressiivisen lääkkeen käytöstä aktiivisessa viruksen aiheuttamassa hermostoinfektiossa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

