---
layout: default
title: Spironolactone
parent: Pelkkä mallin ennuste (L5)
nav_order: 351
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolaktoni: Hypertensio- ja ödeemasta Hypotrichosis Simplex of the Scalp -tilaan

## Yhden lauseen yhteenveto

Spironolaktoni on mineralokortikoidireceptorin antagonisti, jota käytetään laajasti hypertensioon, ödeemaan, sydämen vajaatoimintaan ja pääasialliseen hyperaldosteronismiin, ja sitä käytetään jo off-label androgeenikäytöissä aiheutuville hiusten häiriöille, kuten naisilla esiintyvälle hiusten katoamiselle ja hirsutismille. TxGNN-malli ennustaa, että se voi olla tehokas **Hypotrichosis Simplex of the Scalp** -tilassa, mutta tämä ennuste on tällä hetkellä tuettu **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja tauti itsessään on geneettinen/rakenteellinen hiusrakkuloiden häiriö, jolla ei ole tunnettua yhteyttä lääkkeen toimintamekanismiin.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Hypertensio, ödeema, pääasiallinen hyperaldosteronismi (yleinen lääketieteellinen tieto; ei sisälly tähän todistusjoukkoon — `original_indications` ja Taiwanin lisensointitiedot ovat molemmat tyhjät) |
| Ennustettu uusi indikaatio | Hypotrichosis Simplex of the Scalp |
| TxGNN-ennustepisteet | 99.26% (sijoitus 7,390) |
| Todistusten taso | L5 (vain mallin ennuste, ei kliinisiä tutkimuksia tai kirjallisuutta löydetty) |
| Taiwanin markkinatilanne | Ei markkinoilla (ei markkinoilla) |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Odottava |

---

## Miksi tämä ennuste on järkevä?

Yksityiskohtainen toimintamekanismin data ei ole tällä hetkellä saatavilla todistusjoukkossa (merkitty tietovajeeksi, DG002 — Korkea vakavuusaste). Yleisen farmakologisen tiedon perusteella spironolaktoni on mineralokortikoidireceptorin antagonisti, joka myös estää androgeenireseptoria ja estää steroidigeneesiä, minkä vuoksi sitä käytetään off-label naisten androgeenisen alopesian ja hirsutismin hoitoon.

Kuitenkin **hypotrichosis simplex of the scalp** on autosomaalisesti dominant hiusrakkuloiden kehityshäiriö, joka liittyy pääasiassa *APCDD1*-mutaatioihin. Se on rakenteellinen/kehitysperäinen häiriö, ei androgeeniksi tai mineralokortikoidiksi ohjattu prosessi, ja spironolaktonin toimintamekanismiin ei ole tunnettua patologista yhteyttä.

Toinen ennustettu indikaatio tässä paketissa, **congenital hypotrichosis with milia** (pisteet 99.04%, sijoitus 9,158), osoittaa saman kaavan — toinen harvinainen geneettinen hiusten/ihon häiriö (liittyvät geeneihin, kuten *LIPH*) ilman tunnettua androgeeniksi tai mineralokortikoidiksi liittyvää signaaliväylää. Se, että molemmat parhaat ennusteet osuvat samaan "hiusten katoaminen/hypotrikhiasis" -tautiklusteriin, viittaa siihen, että TxGNN-pisteet ovat todennäköisesti ohjattuja lääkkeen ↔ hiusten katoamisen käsitteiden yleisestä upottamisen läheisyydestä, eikä spesifisestä, tarkistetusta mekanistisesta yhteydestä näihin tiettyihin geneettisiin häiriöihin. Tämä on uskottava mutta tarkistamaton hypoteesi, ja sitä tulee käsitellä spekulatiivisena eikä vahvistettuna.

---

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä siihen liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla asiaankuuluvaa kirjallisuutta.

---

## Turvallisuusnäkökulmat

Katso pakkausselosteesta turvallisuustietoja.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odottava**

**Perustelut:**
Ennuste perustuu yksinomaan TxGNN-mallin pisteisiin (L5, ei tukevaa kliinisiä tutkimuksia tai kirjallisuutta), ja kohdetauti on geneettinen/rakenteellinen hiusrakkuloiden häiriö, jolla ei ole tunnettua mekanistista yhteyttä spironolaktonin antimineralokortikoidiseen/antiandrogeeniseen aktiivisuuteen. Näennäinen samankaltaisuus toiseen, liittymättömään hypotrikhiaasin ennusteeseen viittaa edelleen siihen, että pisteet voivat heijastaa tautiklusterin läheisyyttä mallin upottamisen tilassa eikä todellista farmakologista signaalia.

**Edetäkseen seuraava on tarpeen:**
- TFDA-pakkausseloste (varoitukset/vasta-aiheet) — tällä hetkellä estää (DG001)
- Vahvistettu toimintamekanismin data DrugBankista (DG002)
- Kohdennettu kirjallisuuden/prekliininen haku *APCDD1*-liittyvästä hypotrikhiaasista ja mahdollisesta androgeeniksi/mineralokortikoidiksi osallistuvasta signaaliväylästä
- Dermatologin/genetiikan asiantuntijan katsaus biologiseen uskottavuuteen ennen siirtymistä S0:n yli

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

