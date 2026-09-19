---
layout: default
title: Ivabradine
parent: Pelkkä mallin ennuste (L5)
nav_order: 206
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Näytön taso: **L5** | Ennustetut käyttöaiheet: **6** kpl
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

# Ivabradine: sydämen sykkeen alennuksesta (sydän- ja verenkiertosairaus) hypertrikoosiin

## Yhden lauseen yhteenveto

Ivabradine on sinoatriaalisolmun I_f ("funny") virran selektiivinen estäjä, jota käytetään farmakologisesti sydämen sykkeen alentamiseen sydän- ja verenkiertosairauksissa; sitä ei tällä hetkellä markkinoida Suomessa eikä paikallista tuoteselosteita ole saatavilla.
TxGNN-malli ennustaa, että se saattaa olla tehokas **hypertrikoosille (sairaus)**, mutta tätä suuntaa tuetaan tällä hetkellä **0 kliinisellä tutkimuksella** ja **0 julkaisulla** — se on puhdas graafipohjainen ennustus ilman tunnettua mekanistista yhteyttä.
Kliinisten tutkimusten, kirjallisuuden ja vahvistetun vaikutusmekanismin puuttumisen sekä turvallisuus-/selostetietojen kriittisen aukon vuoksi tämä kandidaatti ei ole valmis etenemään.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Ei dokumentoitu evidenssipakettiin (Suomi: ei markkinoitu, ei tuotelisenssia); tunnettu farmakologinen käyttö on sydämen sykkeen alennus sydän- ja verenkiertosairauksissa |
| Ennustettu uusi indikaatio | Hypertrikoosi (sairaus) |
| TxGNN-ennustuspistemäärä | 99.79% |
| Näyttötaso | L5 |
| Suomen markkinatilanne | Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odotus |

---

## Miksi tämä ennustus vaikuttaa kohtuulliselta?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismi-tietoja ivabradiinille ei ole saatavilla tässä evidenssipakettissa (DrugBank MOA-kenttä palautti tietoaukon). Muissa kerätyissä tiedoissa ivabradiinin tunnettu farmakologia on dokumentoitu sinoatriaalisolmun I_f-virran ("funny") selektiivisenä estäjänä, joka alentaa sydämen sykettä — tämä on perusta sen käytölle sydän- ja verenkiertosairauksien hoidossa.

Ei ole vakiintunutta eikä uskottavaa biologista polkua, joka yhdistäisi I_f-kanavan estämisen hiuskasvuun tai hypertrikoosiin. Evidenssipaktin oma arvio tälle kandidaatille toteaa selvästi, että kliinisiä tutkimuksia, kirjallisuutta eikä vaikutusmekanismi-tietoja ei ole olemassa tukeakseen tätä yhteyttä, ja että ennuste on puhdas TxGNN-graafipohjaiseen tulos eikä mekanismiin perustuva hypoteesi.

Neljä muuta parhaiten sijoittuvaa ennustusta tälle lääkkeelle (Ambrasi-tyypin hypertrikoosi, hammas- ja parodontaalinen kehityshäiriöoireyhtymä, Dandy-Walkerin kehityshäiriöoireyhtymä ja eristetty hiusvarren epänormaalisuus) ovat samoin ilman tukea — mikään ei osoita uskottavaa mekanistista yhteyttä sinoatriaalisolmun sykkeen hallintaan, ja vain yksi (hammas- ja parodontaalinen kehityshäiriöoireyhtymä) palautti mitään kirjallisuutta ollenkaan, ja se kirjallisuus on geneerinen parodontaalisen sairauden tausta-aineisto eikä ivabradiini-kohtaista tutkimusta.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä asiaan liittyviä kliinisiä tutkimuksia.

---

## Kirjallisuuden näyttö

Asiaan liittyviä kirjallisuuslähteitä ei ole tällä hetkellä saatavilla.

---

## Suomen markkinoiden tiedot

Ivabradiinilla ei ole markkinointilupia (`market_status`: Ei markkinoitu; `total_licenses`: 0). Tuotelisenssitietueita ei ole saatavilla yhteenvetoa varten.

---

## Turvallisuushuomiot

Turvallisuustietoja varten katso tuoteselosteesta. (Tärkeimmät varoitukset, vasta-aiheet ja lääkeinteraktiotiedot eivät ole tällä hetkellä saatavilla evidenssipakettissa; TFDA/selostetietojen varoitusaukkoa merkitään turvallisuusarviointia **estävänä** tekijänä.)

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odotus**

**Perustelut:**
Paras ennustettu indikaatio (hypertrikoosi) ei ole tuettu kliinisillä tutkimuksilla, kirjallisuudella eikä mekanistisilla perusteilla — evidenssipakki itse kuvaa sitä mallin kohinaksi. Tätä pahentaa TFDA/selostetietojen varoitustieto-aukkoa, joka estää jopa alustavaa turvallisuusseulontaa (S1).

**Etenemisen edellytykset:**
- TFDA/paikalliset tuoteselosteen varoitukset ja vasta-aiheet (tällä hetkellä estävä)
- Vahvistetut vaikutusmekanismi-tiedot DrugBankista
- Prekliiniset tai mekanistiset tutkimukset, jotka yhdistävät I_f-kanavan estämisen (tai minkä tahansa muun ivabradiinin kohteen) hiustupen biologiaan
- Kaikki pilotti-kliiniset tai tapaus-tason näytteet ennen kuin tämä kandidaatti voi edetä L5/S0:n yli

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

