---
layout: default
title: Mogamulizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 252
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **7** kpl
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

# Mogamulizumab: Aikuisten T-soluleukeemiasta/lymfoomasta eturauhaseen virtsaputkeen sijoittuvaan uroteelisytolaarin karsinoomaan

## Yhden lauseen yhteenveto

Mogamulizumab on anti-CCR4-monoklonaalinen vasta-aine, jota käytetään tällä hetkellä aikuisten T-soluleukeemiaan/lymfoomaan ja mykoosin fungoidesiin/Sézary-syndroomaan (todistusaineiston mekanistisen perustelun mukaan; ei vahvistettu itsenäisesti Suomen lisensointitietojen perusteella).
TxGNN-malli ennustaa, että se saattaa olla tehokas **eturauhaseen virtsaputkeen sijoittuvassa uroteelisytolaarin karsinoomassa**, mutta tämä sijoitus perustuu **puhtaasti mallin pisteytyksen perusteella** — **0 kliinistä tutkimusta** ja **0 julkaisua** tukee tätä suuntaa.

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Aikuisten T-soluleukeemia/lymfooma; Mykoosin fungoides/Sézary-syndrooma (uudelleenkäyttöperustelutekstin mukaan; strukturoitua lisensointitietoa ei saatavilla) |
| Ennustettu uusi indikaatio | Eturauhaseen virtsaputkeen sijoittuva uroteelisytolaarin karsinooma |
| TxGNN-ennusteen pistemäärä | 99.44% |
| Todistusvahvuus | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkinoiden tila | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odottava |

## Miksi tämä ennuste on perusteltu?

Tällä hetkellä yksityiskohtaista vaikutusmekanismitietoa ei ole saatavilla strukturoidussa muodossa (merkitty tietoaukoksi). Tarjotun uudelleenkäyttöperustelun perusteella mogamulizumab on anti-CCR4-monoklonaalinen vasta-aine, ja sen tehokkuus aikuisten T-soluleukeemiaan/lymfoomaan ja mykoosin fungoidesiin/Sézary-syndroomaan on osoitettu. CCR4 ilmentyy säätävissä T-soluissa (Tregs), ja mogamulizumabin vaikutusmekanismi sisältää CCR4-positiivisten Tregien poistamisen syöpää vastustavan immuniteetin parantamiseksi.

Teoreettinen yhteys eturauhaseen virtsaputkeen sijoittuvaan uroteelisytolaarin karsinoomaan perustuu havaintoon, että CCR4-positiivisten Tregien infiltraatiota on kuvattu joissakin uroteelisen kasvaimen mikro-ympäristöissä — näiden Tregien poistaminen voisi periaatteessa lievittää paikallista immunosupressiota ja parantaa syöpää vastaan suuntautuvaa immuunivastausta. Tämä yhteys on kuitenkin mekanistinen hypoteesi, joka on johdettu yksinomaan TxGNN-upotusavaruudesta; sitä ei tueta millään esikliinisillä, translaatiotutkimuksellisilla tai kliinisillä tutkimuksilla, jotka olisivat uroteeliselle karsinoomalle erityisiä.

Kun otetaan huomioon kliinisten tutkimusten tai kirjallisuuden täydellinen puute (katso alla), tätä ennustetta tulisi pitää hypoteesin tuottavana signaalina eikä toimenpidekelpoisen uudelleenkäyttöehdokkaan sijaan tällä hetkellä.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröity asiaan liittyviä kliinisiä tutkimuksia

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla asiaan liittyviä kirjallisuuslähteitä

## Suomen markkinatiedot

Mogamulizumab ei ole tällä hetkellä markkinoilla Suomessa (0 hyväksyntöä tietueessa), joten tuote-/lisensointitietoja ei ole saatavilla.

## Sytotoksiisuus

Mogamulizumab on syöpää vastaan vaikuttava aine (indisoitu T-soluleukeemiaan/lymfoomaan).

| Kohta | Sisältö |
|------|---------|
| Sytotoksiisuuden luokittelu | Immunoterapia (anti-CCR4-monoklonaalinen vasta-aine; ei tavanomainen sytotoksinen aine) |
| Luuydintukahduttamisen riski | Katso pakkausseloste varoitukset ja varotoimet |
| Emetogeenisuuden luokitus | Katso pakkausseloste varoitukset ja varotoimet |
| Seurantakohdat | Katso pakkausseloste varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausseloste varoitukset ja varotoimet |

## Turvallisuusnäkökohdat

Katso pakkausselostetta turvallisuustiedoista.

*Huomautus: Suomen pakkausselosteen/varoitusetiketin hakeminen (estävä tietoaukko, DG001) ei ole vielä valmis, joten turvallisuusarvioita (S1 vaihe) ei voida suorittaa ennen tämän ratkaisemista.*

## TxGNN:n tunnistama lisäehdokkaat

Malli tunnisti kuusi muuta matalan luottamuksen ehdokasta samassa pistemäärävälissä (99,15–99,42%), kaikki samankaltaisesti ilman kliinistä tai kirjallisuustukea ja kaikki luokiteltu L5/Odottava: munuaisen pelviksen sarkomatiitti siirtymäsolukarsinooma, tunkeuttava virtsarakkouroteelisytolaarin karsinooma (sarkomatiitti muunnos), munuaisen pelviksen papillaarinen uroteelisytolaarin karsinooma, ihmisen herpesvirus 8 -liittyvä kasvain, ektomesenkymooma ja pahanlaatuinen ihoonsijoittuva rakeisolinen ihosyöpä. Mikään näistä ei oikeuta yksittäistä arviointia edellä olevan korkeimmin sijoitetun ehdokkaan lisäksi.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odottava**

**Perustelut:**
TxGNN-pistemäärä on korkea, mutta seitsemälle ennustetulle indikaatiolle ei ole yhtään kliinisen tutkimuksen tai kirjallisuustodistetta, ja mekanistinen perusteltu on vain teoreettinen. Lisäksi Suomen pakkausselosteen/varoitustiedot (estävä aukko) ei ole haettu, joten ehdokas ei voi vielä siirtyä turvallisuuden esikarsintaan (S1).

**Jatkaakseen tarvitaan seuraavaa:**
- Suomen (Fimea) pakkausselosteen varoitukset/vasta-aiheet (DG001, estävä)
- Vahvistettu vaikutusmekanismin yksityiskohta DrugBankista tai alkuperäiskirjallisuudesta (DG002)
- Esikliininen tai translaatiotieto CCR4/Treg-osallisuudesta erityisesti uroteelisytolaarin karsinoomassa
- Syntyvät kliinisen tutkimuksen tai tapausselostotiedot ennen tämän ehdokkaan uudelleenarvioita odottavan vaiheen jälkeen

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

