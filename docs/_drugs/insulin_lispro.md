---
layout: default
title: Insulin Lispro
parent: Pelkkä mallin ennuste (L5)
nav_order: 202
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **9** kpl
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

# Insulin lispro: Diabetes mellituksesta autoimmuuni ooforiittiin

## Yhden lauseen yhteenveto

Insulin lispro on nopeavaikutteinen insuliinin analoginen aine, jota käytetään diabetes mellituksen hoitoon.
TxGNN-mallin ylimpään rankingiin asettama ennuste tälle lääkkeelle on **autoimmuuni ooforiitti**,
mutta tätä kandidaattia tuetaan tällä hetkellä **0 kliinisellä tutkimuksella** ja **0 julkaisulla**,
ja mallin oma perustelu merkitsee sitä todennäköisesti epäsuoraksi graafisoksi assosiaatioksi pikemmin kuin aitojen mekanistiseksi hypoteesiksi.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Diabetes mellitus (verensokerin säätely) — perustuu yleisen lääkkeen identiteetille; Suomen lisensointiteksti ei ole saatavilla tässä todistepakkauksessa |
| Ennustettu uusi indikaatio | Autoimmuuni ooforiitti |
| TxGNN-ennustepistemäärä | 99.78% |
| Näyttöaste | L5 |
| Suomen markkina-asema | ✗ Ei markkinoilla |
| Hyväksynnöissä lukumäärä | 0 |
| Suositeltu päätös | Keskeytä |

---

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa ei ole saatavilla (DrugBank-kysely ei palauttanut tämän lääkkeen MOA-tekstiä). Yleisen farmakologisen tiedon perusteella insulin lispro on rekombinantti nopeavaikutteinen insuliinin analoginen aine (käänteinen Lys-Pro kohdissa B28–B29), joka sitoutuu insuliinireseptoriin verensokerin alentamiseksi; sitä käytetään tyypin 1 ja tyypin 2 diabetes mellituksen hoitoon.

Ylimpään rankingiin asetetun ennusteen osalta, **autoimmuuni ooforiitti**, todistepakkauksen oma mekanistinen arviointi on selkeä: insuliinin ja autoimmuuni ooforiittin välillä ei ole tunnettu patofysiologista yhteyttä. Ennuste heijastaa todennäköisesti sitä, että lääke ja tauti ryhmitellään epäsuorasti jaetun "autoimmuunihairainnon" solmun alle tietokaavion sisällä, pikemmin kuin mitään kausaalia tai terapeuttista mekanismia. Yksikään prekliininen, tapauskohtainen tai kliininen näyttö ei tällä hetkellä tue insuliinia tämän sairauden hoitona.

Koska mekanistinen perustelu puuttuu ja ei ole olemassa tukevia tutkimuksia, tämä kandidaatti ei tällä hetkellä täytä jatkoarviointiin etenemisen rajaa huolimatta sen korkeasta TxGNN-pisteestä.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole liittyviä rekisteröityjä kliinisiä tutkimuksia

## Kirjallisuuden näyttö

Tällä hetkellä ei ole käytettävissä liittyvää kirjallisuutta

## Suomen markkina-asema

Insulin lispro:lla ei ole rekisteröityjä hyväksynnöjä Suomessa tässä todistepakkauksessa (`market_status: Not marketed`, `total_licenses: 0`); mitään tuote-/antomuoto-/indikaatiotietueita ei ole saatavilla.

## Muut ehdokasindikaatiot tässä todistepakkauksessa

Tämä todistepakkaus (`TW-DB00046-multi`) arvioi 9 TxGNN:n ennustamaa insuliini lispro:n indikaatiota. Vain yksi — jonka pistemäärä on alempi — omaa tällä hetkellä kirjallisuuden tukea:

| Sijoitus | Sairaus | TxGNN-pistemäärä | Näyttöaste | Päätösvaihe | Suositus | Huomautus |
|---------|---------|-----------------|-----------|-----------|----------|----------|
| 1 | Autoimmuuni ooforiitti | 99.78% | L5 | S0 | Keskeytä | Ei tunnettua mekanistista yhteyttä |
| 2 | Tiamiiinille reagoiva dysfunktiosyndrooma | 99.37% | L5 | S0 | Keskeytä | Diabetes-komponentti vain; tiamii on ensisijaisesti, ei insuliini |
| 3 | Klassinen stiff person -syndrooma | 99.36% | L5 | S0 | Keskeytä | Yhteisesiintyvyys anti-GAD65:n kautta, ei hoitokohde |
| 4 | Paikallinen stiff limb -syndrooma | 99.36% | L5 | S0 | Keskeytä | Sama anti-GAD65 yhteisesiintyvyyden sekaannus |
| 5 | Opsimodysplasia | 99.34% | L5 | S0 | Keskeytä | Ei tunnettua reittienpäällystöpäällekkäisyyttä |
| 6 | Lääkkeen aiheuttama paikallinen lipodystroofia | 99.09% | L4 | S0 | Keskeytä | **Käänteinen syy-yhteys** — insuliiniinjektio on tunnettu tämän sairauden aiheuttaja |
| 7 | Pankreaan agenesia | 99.09% | L3 | S1 | Tutkimuskysymys | Insuliini (mukaan lukien lispro) on jo hoitostandardina PNDM:lle pankreaan agenesian vuoksi — olemassa olevan käytännön laajennus, ei uusi uudelleenkäyttösignaali |
| 8 | Säteittävä lipodystroofia | 99.04% | L5 | S0 | Keskeytä | Sama käänteisen syy-yhteyksen sekaannus kuin #6 |
| 9 | Paineen aiheuttama paikallinen lipoatroofia | 99.03% | L5 | S0 | Keskeytä | Sama käänteisen syy-yhteyksen sekaannus kuin #6 |

Kolme yhdeksästä kandidaatista (#6, #8, #9) ovat todennäköisesti insuliiniinjektiosta aiheutuvia ilmiöitä, jotka ovat **syy** paikalliselle lipostroofialle/lipoatrofalle, ei hoito sille, ja ne tulisi priorisoida alemmaksi pikemmin kuin edetä. Ehdokas #7 (pankreaan agenesia) omaa vahvimman tuen tässä pakkauksessa, mutta se edustaa olemassa olevan kliinisen käytännön vahvistusta pikemmin kuin uutta uudelleenkäyttömahdollisuutta.

---

## Turvallisuushuomiot

Katso turvallisuustiedot pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Keskeytä**

**Perustelut:**
Ylimpään rankingiin asetettu ennuste (autoimmuuni ooforiitti) ei omaa tuettuja kliinisiä tutkimuksia, ei kirjallisuutta ja ei uskottavaa mekanistista yhteyttä todistepakkauksen oman analyysin mukaan — se heijastaa todennäköisesti epäsuoraa tietokaavion assosiaatiota pikemmin kuin aitojen terapeuttisen signaalin. Tämä ei täytä S0:n ohitse etenemisen raja-arvoa.

**Jatkaakseen seuraavaa tarvitaan:**
- TFDA/Fimea-pakkausseloste-tiedot (varoitukset, vasta-aiheet) — tällä hetkellä **estävä** tietoaukko (DG001), vaaditaan ennen mitään S1 turvallisuusseulontaa
- DrugBank-vaikutusmekanismi-tiedot — tällä hetkellä **korkean prioriteetin** aukko (DG002), vaaditaan mekanistisen uskottavuuden asianmukaiseen arviointiin
- Spesifinen prekliininen tai tapauskohtainen perustelu, joka yhdistää insuliinisignaloinnin autoimmuuni ooforiittin patofysiologiaan, jos tätä kandidaattia on tarkoitus edetä eteenpäin
- Jos kiinnostus jatkuu tässä todistepakkauksessa, harkitse uudelleenarvioinnin siirtämistä kohti ehdokasta #7 (pankreaan agenesia), jolla on todellinen kirjallisuuden tuki, vaikka se heijastaa hoitostandardin vahvistusta pikemmin kuin uutta uudelleenkäyttöä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

