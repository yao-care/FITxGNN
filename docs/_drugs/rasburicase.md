---
layout: default
title: Rasburicase
parent: Pelkkä mallin ennuste (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
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

# Rasburikaasi: syöpäsolujen hajoamiseen liittyvästä hyperurikemiasta munuaisten hypourikemiaan

## Yhden lauseen yhteenveto

Rasburikaasi on rekombinantti urataattioksidaasi, jonka vakiintunut käyttötarkoitus on hoitaa syöpäsolujen hajoamiseen liittyvää hyperurikemiaa syöpäpotilailla. TxGNN-mallin huipulle sijoittuva ennuste on **Munuaisten hypourukemia**, mutta tämä ennuste on mekanistisesti epätodennäköinen — rasburikaasi *alentaa* virtsahappoa, kun taas munuaisten hypourukemia on sairaus, jolle on ominaista *poikkeuksellisen alhainen* virtsahappo — ja sitä tukevat **nolla kliinistä tutkimusta ja nolla julkaisuja**. Vahvempi mekanistinen kandidaatti on olemassa alemmas rankatussa listassa (HPRT osittainen puutos), jolle ei myöskään ole tukitutkimuksia.

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen käyttötarkoitus | Syöpäsolujen hajoamiseen liittyvä hyperurukemia (farmakologisen kontekstin perusteella todistusmateriaalipaketissa; ei virallisesta luvasta, koska sellaista ei ole olemassa) |
| Ennustettu uusi käyttötarkoitus | Munuaisten hypourukemia |
| TxGNN-ennustepisteet | 99,99 % |
| Todistusaineiston taso | L5 (vain malliennuste, ei tukevia tutkimuksia) |
| Taiwan-markkinoiden tila | ✗ Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltava päätös | Pidätys |

## Miksi tämä ennuste on järkevä?

Yksityiskohtaista virallista vaikutusmekanismin tietoa merkitään tämän todistusmateriaalipaketissa tietovajeeksi (DG002). Paketin omasta perustelutekstistä kuitenkin käy ilmi rasburikaasin tunnettu farmakologia: se on rekombinantti urataattioksidaasi, joka hapettaa virtsahappoa allantoiinissa, ja sitä käytetään syöpäpotilaiden virtsahappolukujen *alentamiseen* syöpäsolujen hajoamisen riskissä.

**Paremmalle sijoitukselle nousevaa ennustetta, Munuaisten hypourukemiaa, olisi käsiteltävä huomattavalla varovaisuudella.** Munuaisten hypourukemia on sairaus, jolle on ominaista *poikkeuksellisen alhainen* virtsahappo, jonka aiheuttavat yleensä vialliset munuaisten tubulaarisen uridin kuljettimet. Virtsahappoa alentavan valmisteen antaminen potilaalle, jolla on jo liian vähän virtsahappoa, toimii suunnassa, joka on vastakkainen sairauden kanssa, ja sen voidaan odottaa pahentavan sairauden sijasta parantavan sitä. Todistusmateriaalipaketissa itsessään tämä on selvästi kuvattu TxGNN-mallin todennäköisesti korkeaksi pistemäärät saaneeksi vääräpositiiviseksi, ei biologisesti johdonmukaiseksi hypoteesiksi.

Mekanistisesti puolustettavampi kandidaatti esiintyy sijoilla 2: **HPRT osittainen puutos** (esim. Kelley-Seegmiller-oireyhtymä), jossa tukkeutunut puriinin pelastusreitti aiheuttaa virtsahappoylimuodostusta ja uraattinefropatia. Tässä rasburikaasin virtsahappoa alentava vaikutus on suora, looginen yhteys taustalla olevaan aineenvaihdunnan häiriöön. Tällä kandidaatilla ei kuitenkaan ole kliinisen kokeen tai kirjallisuuden tukea, ja se ei ollut mallin valitsema huippusijoitus.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä siihen liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden todisteet

Tällä hetkellä kirjallisuutta ei ole saatavilla.

## Taiwan-markkinoiden tiedot

Rasburikaasia ei tällä hetkellä myydä Taiwanissa (0 hyväksyntää saatavilla), joten tuote- tai hyväksyntätietoja ei ole saatavilla.

## Turvallisuusnäkökohdat

Katso turvallisuustiedot pakkausselosteesta. (Keskeiset varoitukset, vasta-aiheet ja lääkkeiden vuorovaikutustiedot eivät ole tällä hetkellä saatavilla — TFDA:n pakkausselosteen haku on estävä tietovaje, DG001.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätys**

**Perustelut:**
Huipulle sijoittuva ennuste (munuaisten hypourukemia) on mekanistisesti ristiriitainen rasburikaasin tunnetun farmakologian kanssa ja on parasta käsitellä todennäköisenä mallin virheenä pikemminkin kuin aito uudelleenkäytön signaalina. Mekanistisesti todennäköisempi kandidaatti (HPRT osittainen puutos) ei ole lainkaan kliinisen tai kirjallisuuden todisteen varassa. Koska todistusaineiston taso on L5 kaikkien kymmenen ennusteen osalta ja todellista käyttöä, markkinointia tai turvallisuusdokumentaatiota ei ole, yksikään näistä kandidaateista ei ole valmiina edelleen arvioitavaksi.

**Jatkamiseksi tarvitaan seuraavaa:**
- TFDA:n/valmistajan pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä (DG001)
- Vahvistettu alkuperäinen käyttötarkoitus ja virallinen vaikutusmekanismin dokumentaatio (DG002)
- Prekliininen tai tapaustutkimukseen perustuva todiste, joka testaa rasburikaasia erityisesti HPRT osittaiseen puutokseen liittyvässä uraattinefropatiassa, jos tätä kandidaattia aiotaan jatkaa huipulle sijoittuneen (epätodennäköisen) osuman sijasta
- Uudelleenpisteytyson tai manuaalisen tarkistusarvioinnin suorittaminen munuaisten hypourukemia-ennusteelle, koska edellä määritelty suuntaava mekanistinen ristiriita on tunnistettu

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

