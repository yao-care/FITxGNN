---
layout: default
title: Brodalumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: kohteesta [Original Indication Not on File] Strongyloidiaasiin (merkitty turvavaroitukseksi, ei vahvistetuksi mahdollisuudeksi)

## Yhden lauseen yhteenveto

Brodalumab on anti-IL-17RA-monoklonaalinen vasta-aine; Evidence Pack -paketti ei sisällä täytettyjä `original_indications`-kenttiä, joten sen alkuperäisen hyväksynnän käyttöindikaatiota ei voida jäljittää tässä tietojoukossa. TxGNN-mallin parhaiten sijoitettu "uusi indikaatio", **Strongyloidiasis**, on tuettu **0 kliinisellä tutkimuksella** ja **0 julkaisulla**, ja mallin omassa uudelleenkäyttöperustelossa todetaan, että tämä assosiaatio on *mekanistisesti käänteinen* — IL-17-signaalointi on suojaava ruoansulatuskanavan helminttiinfektioita vastaan, joten IL-17RA:n estämisen odotetaan **pahentavan**, ei parantavan, strongyloidiaasia. Tämä kandidaatti tulee lukea mahdolliseksi farmakovigilanssi-signaaleiksi, ei uudelleenkäyttömahdollisuudeksi.

---

## Nopea yleiskatsaus

| Kohde | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei dokumentoitu tässä Evidence Pack -paketissa (`original_indications` tyhjä, `original_moa` = Data Gap; lääkettä ei ole markkinoitu Suomessa) |
| Ennustettu uusi indikaatio | Strongyloidiasis |
| TxGNN-ennusteen pistemäärä | 99.84% |
| Todistusaste | L5 (vain mallin ennuste, ei tukevia tutkimuksia) |
| Suomen markkinatilanne | Ei markkinoitu (Ei markkinoitu) |
| Hyväksynnän määrä | 0 |
| Suositeltu päätös | Odottava |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismitietoja brodalumaabille ei ole saatavilla tässä Evidence Pack -paketissa (`original_moa` = Data Gap). Uudelleenkäyttöperustelun kenttiin upotettujen tietojen perusteella brodalumaabi on kuvattu anti-IL-17RA-monoklonaaliksi vasta-aineeksi, eli IL-17-reseptorisignaloinnin täydelliseksi estäjäksi — samaa luokkaa kuin secukinumab ja ixekizumab, jotka kohdistuvat IL-17-välitteisiin tulehduksellisiin sairauksiin, kuten plakeksi psoriasisiin ja psoriaasiniveliöihin.

Parhaiten sijoitetun ennusteen, **strongyloidiaasian**, osalta mekanistinen suunta kulkee vastakkaiseen suuntaan terapeuttiseen hypoteesiin verrattuna. IL-17 on keskeinen isäntäpuolustuksen sytokiini ekstrasellulaarisia loisia vastaan, mukaan lukien *Strongyloides stercoralis*. IL-17RA:n estämisen odotetaan heikentävän helminti-vastustusta ja voisi uskottavasti *lisätä* infektioriski tai hyperinfektiosyndrooma alttiille potilaille — tunnettu IL-17-estäjien luokkakohtainen huolenaihe — sen sijaan että se antaisi terapeuttisen hyödyn. Evidence Pack -paketin oma perustelu merkitsee eksplisiittisesti tämän olevan "todennäköisesti käänteinen tai sekaantunut assosiaatio TxGNN-tietokannassa" todellisen hoitosignaalin sijaan, eikä mitään kliinisiä tutkimuksia, ICTRP-tietueita tai kirjallisuutta ole, joka vastustautuisi tälle tulkinnalle.

Jäljellä olevat ehdokkaat top-10-listalla noudattavat samankaltaista mallia: useimmat ovat harvinaisia oftalmologisia/optisen hermon sairauksia (esim. von Hippel anomaly, optinen perineuriitti, episkleriitin alatyyppi) ilman kliinisiä tai kirjallisuustodisteita (L5), ja useissa on sama suunnanmukainen varoitus — IL-17-estäjillä luokkana on dokumentoidut tapausraportit, jotka laukaisevat tai pahentavat demyelinisaatio-/optisen neuriitti-tyyppisiä tapahtumia, jotka tekevät näistä assosiaatioista turvatutkimussignaaliehdokkaita pikemminkin kuin uudelleenkäyttömahdollisuuksia. Sijoitus 2, "silmäsairaus", sisältää yhden linkitetyn tutkimuksen ja yhden julkaisun, mutta tutkimus on yleinen immuuni-välitteisen ihosairauden rekisteri (SKINERGY), joka ei liity oftalmologiaan, ja kirjallisuus on yleinen IL-17-esto-katsaus — kumpikaan ei muodosta tautikohtaisia todisteita.

---

## Kliinisten tutkimusten evidenssi

Tällä hetkellä ei ole liittyviä kliinisiä tutkimuksia rekisteröityinä.

---

## Kirjallisuuden evidenssi

Tällä hetkellä liittyvää kirjallisuutta ei ole saatavilla.

---

## Suomen markkinatiedot

Brodalumaabilla on 0 rekisteröityä hyväksyntää, eikä sitä ole tällä hetkellä markkinoitu Suomessa (`total_licenses: 0`, `licenses: []`). Tuotetason hyväksynnän tietoja ei ole saatavilla.

---

## Turvallisuushuomiot

Turvallisuu­stiedoista katso pakkauksessa olevaa selosteesta.

Huomio: tämä Evidence Pack -paketti merkitsee TFDA-merkinnän varoituksia/kontraindikaatioita **estäviksi** tietovajiksi (DG001) — turvallisuuden esiarviointi (S1) ei voi edetä, kunnes pakkauksen seloste on haettu ja jäsennetty. Lääkkeen interaktioiden haku ei myöskään palauttanut tuloksia (`query_status: not_found`).

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odottava**

**Perustelu:**
Parhaiten sijoitetulla ennusteella (strongyloidiasis) ei ole tukevia kliinisiä tai kirjallisuustodisteita (L5) ja sen oma mekanistinen perustelu osoittaa vastakkaiseen suuntaan — turvariskiin pikemminkin kuin terapeuttiseen hyötyyn. Mikään ehdokas top-10-listalla ei saavuta todistusastetta L4:ää korkeammaksi, ja ainoa ehdokas, jolla on liittyviä todisteita ("silmäsairaus", L4), ei ole tautikohtainen ja näyttää heijastavan tietokantavastaavuuden epäsuhta.

**Jatkaakseen tarvitaan seuraavaa:**
- Hae ja jäsennä TFDA/Fimea-pakkauksen seloste sulkeaksesi estävän turvatietovajeen (DG001) ennen S1-arviointia
- Hanki vahvistetut vaikutusmekanismitiedot DrugBankista (DG002) arvioidaksesi mekanistista uskottavuutta kunnolla
- Jos "silmäsairaus" jatketaan, supista ensin se tiettyyn IL-17-linkitettyyn silmädiagnoosiin (esim. uveiitti) ja kysy uudelleen tutkimuksia/kirjallisuutta tätä spesifiiä termia vastaan
- Ohjaa strongyloidiaasian assosiaatio farmakovigilanssi-/signaali-ilmaisun tarkistukseen pikemminkin kuin uudelleenkäyttöputkeen sen mekanistisesti käänteisen suunnan vuoksi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

