---
layout: default
title: Rasburicase
parent: Pelkkä mallin ennuste (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rasburicase: ennustettu uusi käyttöaihe Munuaisperäinen hypourikemia (hypouricemia, renal) (näytön taso L5). Alkuperäinen käyttöaihe: Hyperurikemia"
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "hepatoportal sclerosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

# Rasburikaasi: Hyperurikemian hoidosta munuaisperäiseen hypourikemiaan

## Yhden lauseen yhteenveto

Rasburikaasi on rekombinantti urikaasientsyymi, jota on alun perin käytetty **hyperurikemian** hoitoon. TxGNN-malli ennustaa sen mahdolliseksi käyttöaiheeksi **munuaisperäisen hypourikemian** (pistemäärä 99,99 %), mutta ennusteen tueksi ei ole **yhtään kliinistä tutkimusta eikä julkaisua**, ja mekanistinen perustelu on vastakkainen: lääke laskee virtsahappoa, joka on tässä sairaudessa jo valmiiksi matala.

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen käyttöaihe | Hyperurikemia |
| Ennustettu uusi käyttöaihe | Munuaisperäinen hypourikemia (hypouricemia, renal) |
| TxGNN-ennustepistemäärä | 99,99 % |
| Näytön taso | L5 |
| Markkinatilanne Suomessa | Vain peruutettuja myyntilupia |
| Myyntilupien määrä | 1 (peruutettu) |
| Suositeltu päätös | Hold (odota) |

## Miksi ennuste on (tai ei ole) perusteltu?

Rasburikaasi on rekombinantti urikaasi, joka muuntaa virtsahapon allantoiiniksi ja laskee siten seerumin virtsahappopitoisuutta. Yksityiskohtaista vaikutusmekanismitietoa ei ole tässä aineistossa saatavilla. Tunnetun entsyymitoiminnan perusteella lääkkeen vaikutus on kuitenkin selvä.

Munuaisperäisessä hypourikemiassa seerumin virtsahappo on jo matala URAT1- tai GLUT9-kuljettajan toimintaa heikentävien mutaatioiden vuoksi. Virtsahapon lisälasku olisi mekanistisesti epätarkoituksenmukaista ja voisi lisätä liikunnan aiheuttaman akuutin munuaisvaurion riskiä. Korkea TxGNN-pistemäärä johtuu todennäköisesti tietämysverkon yhteydestä virtsahappoaineenvaihduntaan, ei järkevästä hoidollisesta yhteydestä.

Muut ennusteet (sijat 2–10) ovat samankaltaisia: 
- **HGPRT-vajaus (osittainen):** virtsahapon ylituotanto antaisi teoriassa epäsuoran perustelun akuuttiin laskuun, mutta kyseessä on laskimoon annettava, immunogeeninen entsyymi lyhytaikaiseen käyttöön. Pitkäaikaishoitoon sopivat ksantiinioksidaasin estäjät, eikä lääke korjaa puriinien kierrätyksen vikaa.
- **Maksan porfyria:** mekanistista yhteyttä ei löydy. Rasburikaasi voi lisäksi aiheuttaa hemolyysiä ja methemoglobinemiaa, mikä on turvallisuusriski G6PD-puutoksessa.
- **Maksa- ja porttilaskimosairaudet** (hepatoportaaliskleroosi, primaari porttilaskimotromboosi, varhain alkava familiaalinen ei-kirroottinen portaalihypertensio, hepatopulmonaalinen oireyhtymä, idiopaattinen kupariin liittyvä kirroosi): ei mekanistista yhteyttä, ennusteet ovat todennäköisesti verkon artefakteja.
- **Munuaistubulusten asidoosi:** vain heikko yhteys virtsahapon ja munuaiskäsittelyn kautta. Lääke tuottaa sivutuotteena vetyperoksidia, mikä ei ole hyödyllistä.
- **Fenyylialaniiniaineenvaihdunnan häiriöt:** ainoa pinnallinen yhtäläisyys on entsyymihoidon luokka, ei mekanistinen yhteys.

## Kliinisen tutkimusnäytön tilanne

Aiheeseen liittyviä kliinisiä tutkimuksia ei ole tällä hetkellä rekisteröity.

## Kirjallisuusnäyttö

Aiheeseen liittyvää kirjallisuutta ei ole tällä hetkellä saatavilla.

## Suomen markkinatiedot

| Myyntiluvan numero | Valmisteen nimi | Lääkemuoto | Hyväksytty käyttöaihe |
|---------|------|------|-----------|
| EMEA/H/C/000331 | Fasturtec | – | Hyperurikemia (myyntilupa peruutettu) |

## Turvallisuusnäkökohdat

- **Lääkkeiden yhteisvaikutukset:** Tietokannasta löytyi yhteensä 13 yhteisvaikutusta.
  - **Merkittävät (Major):** prilokaiini ja nitriittihappo (nitrous acid).
  - **Kohtalaiset (Moderate):** paikallispuudutteet ja vastaavat valmisteet (tetrakaiini, lidokaiini, bentsokaiini, kokaiini, proparakaiini, oksibuprokaiini, sinkokaiini eri antoreiteillä) sekä idelalisibi.
- Myyntiluvan valmisteyhteenvedon varoituksia ja vasta-aiheita ei ole tässä aineistossa saatavilla, joten niiden osalta on tarkistettava valmisteyhteenveto. Lisäksi on huomioitava edellä mainittu hemolyysin ja methemoglobinemian riski G6PD-puutoksessa.

## Johtopäätös ja seuraavat askeleet

**Päätös: Hold (odota)**

**Perustelu:**
- Ennusteiden tueksi ei ole kliinistä tai kirjallista näyttöä (taso L5), ja ykkösennusteen mekanismi on lääkkeen vaikutukselle vastakkainen. Suomessa ainoa myyntilupa on peruutettu.

**Jatkoa varten tarvitaan:**
- Valmisteyhteenvedon varoitukset ja vasta-aiheet (turvallisuusseulonnan estävä aukko)
- Yksityiskohtainen vaikutusmekanismitieto
- Prekliininen tai mekanistinen näyttö ennen mitään jatkokehitystä
- Mahdollisen jatkotarkastelun osalta rajoittaminen lyhytaikaiseen akuuttiin hyperurikemiaan liittyviin tilanteisiin (esim. HGPRT-vajaus), vasta kun kliinistä tukea on olemassa
## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

