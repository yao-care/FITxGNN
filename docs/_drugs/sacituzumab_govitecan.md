---
layout: default
title: Sacituzumab Govitecan
parent: Pelkkä mallin ennuste (L5)
nav_order: 337
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **4** kpl
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

# Sacituzumab Govitecan: [Alkuperäinen indikaatio ei ole saatavilla] → lääkeaineen aiheuttamaan osteoporoosiin

## Yhden lauseen yhteenveto

Sacituzumab Govitecan (DB12893) on Trop-2-kohdennettu vasta-aineen-lääkeaineyhdistelmä, joka toimittaa SN-38:a (topoisomeraasi I:n estäjä ja irinotekaanin aktiivinen metaboliitti) systeemisenä sytotoksisena kemiallisena hoitona. Sen alkuperäinen indikaatio ei ole dokumentoitu nykyisessä aineistossa (tietoauko). TxGNN ennustaa sen olevan tehokas **lääkeaineen aiheuttamaan osteoporoosiin**, mutta tämä ennuste perustuu tällä hetkellä **nollaan kliiniseen tutkimukseen** ja **nollaan julkaisuun**, ja todistepaketin oma mekanistinen analyysi osoittaa, että kausaalisuhde on todennäköisesti päinvastainen — sytotoksinen kemiallinen hoito on tunnettua luun tiheyden menetyksen aiheuttaja, ei sen hoito.

---

## Pika-yleiskatsaus

| Kohta | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | Ei saatavilla — lääkitystekstiä tai indikaatiotekstiä ei ole asiakirjoissa (tietoauko) |
| Ennustettu uusi indikaatio | Lääkeaineen aiheuttama osteoporoosi |
| TxGNN-ennustepisteet | 99.78% |
| Näyttötaso | L5 (mallin ennuste vain, ei tukevia tutkimuksia) |
| Markkinoinnin tila Suomessa | ✗ Ei markkinoitu |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pidätä |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista toimintamekanismia koskevia tietoja ei ole saatavilla strukturoidussa `original_moa`-kentässä (merkitty tietoaukoksi). Tämän todistepaketin mekanistisen perustelun mukaan Sacituzumab Govitecan on Trop-2-kohdennettu vasta-aineen-lääkeaineyhdistelmä (ADC), joka vapauttaa SN-38:a solunsisäisesti — topoisomeraasi I:n estäjä ja irinotekaanin aktiivinen metaboliitti — joka toimii systeemisenä sytotoksisena hoitona.

Ei ole tunnettua mekanistista reittia, jolla tämä sytotoksinen vaikuttava aine *hoitaisi* osteoporosia. Päinvastoin, systeeminen sytotoksinen kemiallinen hoito on tunnettua luun tiheyden menetyksen aiheuttaja myelosuppression ja sekundaarisen sukuhormonien vajaatoiminnan kautta. Todistepaketin oma analyysi päättelee, että tämän TxGNN-ennusteen sisältämä kausaalisuhde on todennäköisesti käänteinen — lääkeaine on pikemminkin riskitekijä lääkeaineen aiheuttamaan osteoporoosiin kuin ehdokas sen hoitamiseksi.

Huomattavasti kolme seuraavaksi korkeimpaan sijoittuneista ennusteista (vaikea nonproliferatiivinen diabetesretinopatiia, diabetesretinopatiia, diabeteskataratti) noudattavat samaa epätavallista kaavaa: korkeat TxGNN-pisteet (99.1–99.7%), nolla tukevia tutkimuksia tai kirjallisuutta ja ei yhtään järkevää mekanistista yhteyttä anti-tuumori-ADC-vaikuttavaan aineeseen. Yhdessä sen kanssa, että tämän lääkeaineen `original_indications`-luettelo ja DDI-tietueet ovat molemmat tyhjät, tämä ennusteiden ryhmä on enemmän yhteneväinen tietoverkkon tietojen harvuuden artefaktin (kylmäkäynnistys-solmu tietoverkossa) kanssa kuin aidoilla uudelleenkäyttösignaaleilla.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

Tällä hetkellä kirjallisuutta ei ole saatavilla.

---

## Sytotoksisuus

Sacituzumab Govitecan on antineoplastinen ADC (Trop-2-kohdennettu sytotoksisen topoisomeraasi I:n estäjän SN-38:n toimitus), joten tämä osa pätee.

| Kohta | Sisältö |
|-------|---------|
| Sytotoksisuuden luokittelu | Kohdennettu hoito (ADC), joka toimittaa perinteisen sytotoksisen vaikuttavan aineen (SN-38, topoisomeraasi I:n estäjä) |
| Myelosuppression riski | Merkitty todistepaketin mekanistisessä perustelussa SN-38-pohjaisen sytotoksisen hoidon oletetuksi luokkavaikutukseksi (luuydinsortumus, sekundaarinen sukuhormonien vajaatoiminta); virallista toksisiteettitietokantaa ei ole saatavilla — katso pakkausseloste |
| Emetogenisiteetti | Katso pakkausseloste varoituksissa ja varotoimissa |
| Seurantavaatimukset | Katso pakkausseloste varoituksissa ja varotoimissa |
| Käsittelysuojat | Sytotoksisena ADC-vaikuttavana aineena vakiosytotoksisen lääkeaineen käsittelysuojat todennäköisesti koskevat; vahvista pakkausselosteesta |

---

## Turvallisuushuomioon

Katso turvallisuustietoja pakkausselosteesta.

---

## Johtopäätökset ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Kaikki neljä TxGNN-ennustettua indikaatiota (lääkeaineen aiheuttama osteoporoosi, vaikea nonproliferatiivinen diabetesretinopatiia, diabetesretinopatiia, diabeteskataratti) sijaitsevat L5/S0:ssa nolla kliinisellä tutkimuksella tai kirjallisuudella, ja tämän todistepaketin mekanistinen analyysi osoittaa, että paras ennuste todennäköisesti heijastaa käänteistä kausaalisuutta kuin aitoa terapeuttista signaalia — tämä kaava yhdessä tyhjien alkuperäisen indikaation ja DDI-tietueiden kanssa viittaa tietoverkkon tietojen harvuuteen pikemminkin kuin aitoon uudelleenkäyttömahdollisuuteen.

**Jotta voitaisiin edetä, seuraavaa tarvitaan:**
- TFDA/valmistajan pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä tekijä (DG001)
- Vahvistettu toimintamekanismi DrugBank-ohjelmointirajapinnan kautta — tällä hetkellä korkea prioriteetti (DG002)
- Lääkeaineen alkuperäisen indikaation ja DDI-tietueiden rikastaminen ilmeisen tietoverkkon tietojen puutteen korjaamiseksi ennen kuin arvioidaan uudelleen mitään TxGNN-ennusteita tälle yhdisteelle
- Itsenäinen mekanistinen tai prekliininen näyttö kullekin ennustetulle indikaatiolle ennen kuin edetään S0:n ohi

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

