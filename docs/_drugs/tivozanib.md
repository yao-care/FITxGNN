---
layout: default
title: Tivozanib
parent: Pelkkä mallin ennuste (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: munuaissolucytokarsinoomasta endoservikaaliseen karsinoomaan

> **Huomio tietojen täydellisyydestä**: Tämä todistusaineisto ei täydennä kohteita `original_indications` tai `original_moa` (molemmat merkitty tietokuiluiksi DG001/DG002, DG001 arviointitasolla *Kriittinen*). Alla oleva alkuperäinen indikaatio perustuu tivozanibin yleiseen farmakologiseen tietoon (markkinoilla oleva VEGFR TKI munuaissolucytokarsinoomaa varten) ja vaatii vahvistusta TFDA/Fimea pakkausselvitystä vastaan ennen kuin tätä raporttia voidaan käyttää päätöksentekoon.

## Yhden lauseen yhteenveto

Tivozanib on erittäin selektiivinen VEGFR-1/2/3-tyrosiinikinaasin estäjä, joka kehitettiin alun perin munuaissolucytokarsinoomaa varten. TxGNN-malli ennustaa, että se saattaa olla tehokas **endoservikaaliseen karsinoomaan**, mutta tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** tukee tätä erityistä suuntaa — signaali on puhtaasti verkkopohjainen ennustus.

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Munuaissolucytokarsinooma (yleinen tieto; ei ole olemassa todistusaineistossa — tietokuilu) |
| Ennustettu uusi indikaatio | Endoservikaali karsinooma |
| TxGNN:n ennustepistemäärä | 99.81% |
| Todisteiden taso | L5 |
| Suomen markkinatila | Ei markkinoinnissa (Ei markkinoinnissa) |
| Valtuutuksien lukumäärä | 0 |
| Suositeltu päätös | Pidättäytyminen |

## Miksi tämä ennustus on järkevä?

Yksityiskohtainen alkuperäisen toimintamekanismin tieto on merkitty tietokuiluksi tässä todistusaineistossa. Kuitenkin ennusteeseen liittyvän siirtokäyttöperusteen mukaan tivozanib on erittäin selektiivinen VEGFR-1/2/3-tyrosiinikinaasin estäjä, joka tukahduttaa kasvainten angiogeneesiä.

Endoservikaali karsinooma voi, kuten munuaissolucytokarsinooma, olla angiogeneesistä riippuvainen, ja muut anti-angiogeneettisen aineet (esim. bevatsumabi) ovat jo hyväksytty edistyneen kohdunkaulan syövän hoitoon. Tämä antaa ennusteelle uskottavan mekanistisen analogian lääkeluokkatasolla.

Silti linkki on johdettu puhtaasti TxGNN:n tietokaavion samankaltaisuudesta — tivozanibin erityistä tutkimusta, tapausraporttia tai prekliinistä dataa endoservikaalisessa karsinoomassa ei ole olemassa vahvistamaan, että mekanismi todella siirtyy kliiniseksi hyödyksi tässä kasvaintyypissä.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla asiaan liittyviä kirjallisuustietoja.

## Suomen markkinatiedot

Tivozanibilla ei ole tällä hetkellä markkinointilupia Suomessa (0 lisenssejä tietueissa); tuotetaulukkoa ei ole saatavilla.

## Sytotoksisuus

Tivozanib on syöpälääke (VEGFR-tyrosiinikinaasin estäjä).

| Kohde | Sisältö |
|------|---------|
| Sytotoksisuuden luokitus | Kohdennettu hoito (VEGFR-1/2/3-tyrosiinikinaasin estäjä / anti-angiogeneettinen aine) |
| Ydinsolun tukahduttamisen riski | Katso pakkausselvityksestä varoitukset ja varotoimet |
| Emetogenisuuden luokitus | Katso pakkausselvityksestä varoitukset ja varotoimet |
| Valvontakohdat | Katso pakkausselvityksestä varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausselvityksestä varoitukset ja varotoimet |

## Turvallisuushuomiot

Katso turvallisuustiedoista pakkausselvityksestä.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidättäytyminen**

**Perustelut:**
Ennustus perustuu yksinomaan TxGNN:n graafin pisteeseen (L5, päätösvaihe S0), joilla ei ole lainkaan tukevaa kliinistä tutkimusta tai kirjallisuutta kaikista 10 kysetyistä gynekologisista indikaatoista, ja lääkkeen oman TFDA/Fimea-merkinnän tiedot ovat ratkaisemattomia (kriittisen vakavuuden kuilu DG001).

**Jatkaakseen, seuraavat ovat tarpeen:**
- TFDA/Fimea pakkausselvitys (varoitukset, vasta-aiheet, DDI) — tällä hetkellä kriittinen kuilu DG001
- Vahvistettu alkuperäinen MOA ja hyväksytty indikaatio DrugBankista/sääntelylähteestä — DG002
- Prekliinisiä tai tapaustason todisteita VEGFR-reitin merkityksellisyydestä erityisesti endoservikaalisessa karsinoomassa ennen mitään kliinisen tutkimuksen vaiheen investointia

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

