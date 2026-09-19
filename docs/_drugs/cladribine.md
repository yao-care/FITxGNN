---
layout: default
title: Cladribine
parent: Pelkkä mallin ennuste (L5)
nav_order: 102
evidence_level: L5
indication_count: 7
---

# Cladribine
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

## Cladribine: Hiirten silmäleukaemiasta parameningiaaliseen embryonaaliseen rabdomyosarkooomaan

## Yhden lauseen yhteenveto

Cladribine on puriinanukleosidia (deoksiadenosiini) analogni, jota on perinteisesti käytetty hiirten silmäleukaemian hoitoon ja joka vaikuttaa lymfosyyttien ja monosyyttien valikoivaan sytotoksisuuteen DNA-kaksoisjärkäisyyden katkeamisen kautta.
TxGNN-malli ennustaa mahdollista aktiivisuutta **parameningiaaliseen embryonaaliseen rabdomyosarkooomaan** (pistemäärä **99.77%**), mutta tämä on tällä hetkellä puhtaasti **graafipohjainen assosiaatio** — **0 kliinistä tutkimusta** ja **0 julkaisua** tukee tätä erityistä ennustusta, eikä mitään mekanistista yhteyttä cladribiinin tunnetun biologian ja rabdomyosarkooman patogeneesin välillä ole tunnistettu.

---

## Pikakatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Hiirten silmäleukaemia *(yleinen lääketieteellinen tieto; lisenssiin/indikatioon liittyviä tietoja ei ole olemassa näytön paketissa)* |
| Ennustettu uusi indikaatio | Parameningiaaliset embryonaaliset rabdomyosarkooma |
| TxGNN-ennustepistemäärä | 99.77% (sijoitus 2900) |
| Todisteen taso | L5 — vain mallin ennuste, ei kliinistä tai kirjallisuustukea |
| Suomen markkinatilanne | ✗ Ei markkinoilla |
| Myyntilupien lukumäärä | 0 |
| Suositeltu päätös | Pidä |

---

## Miksi tämä ennuste on perusteltavissa?

Strukturoituja MOA-tietoja ei ollut saatavilla näytön paketissa (`original_moa: [Data Gap]`). Kuitenkin mallin oman perustelun mukaan cladribine on deoksiadenosiinin lymfosyytti/monosyytti-selektiivinen sytotoksinen analogni, joka toimii DCK-välitteisen fosforylaation ja DNA-kaksoisjärkäisyyden katkeamisen induktion kautta — tämä on johdonmukaista sen vakiintuneen kliinisen roolin kanssa hiirten silmäleukaemiassa, immuunijärjestelmän/monosyyttien hematologisen pahanlaatuuden yhteydessä.

Parameningiaaliset embryonaaliset rabdomyosarkooma sen sijaan on luuranko-myoblastin lineaagin kiinteä kasvain, jolla on perustavanlaatuisesti erilainen lähtösolutyyppi ja proliferatiivinen biologia. Näytön paketin omassa repurposing-perustelussa todetaan selvästi, että **ei ole olemassa tunnettua suoraa mekanistista yhteyttä** cladribiinin lymfosyytteihin kohdistuvan sytotoksisuuden ja rabdomyosarkooman patogeneesin välillä — korkea TxGNN-pistemäärä heijastaa graafisuhteen ennustetta, ei vahvistettua farmakologista hypoteesia.

Tämä malli on johdonmukaista kaikissa 7 rankatussa ennusteessa tässä näytön paketissa (5 rabdomyosarkooman alatyyppiä, rabdomyosarkooma yleisenä kategoriana ja maksasarkooma) — kaikille annetaan L5/Pidä-status, eikä mikään niistä ole tuettu mekanistisella perustelulla. Ainoa tässä näytön paketissa löydetty kirjallisuusosuma (PMID 15241520, sijoitus 7 "maksasarkooma") käsittelee cladribiinin käyttöä pehmeässä systeemisessä mastoosytoosissa — immuunijärjestelmän mastoosyytti-häiriössä, ei sarkooman — eikä muodosta asiaankuuluvaa tukevaa näyttöä.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole asiaan liittyviä rekisteröityjä kliinisiä tutkimuksia

---

## Kirjallisuuden näyttö

Tällä hetkellä asiaan liittyviä kirjallisuustietoja ei ole saatavilla

---

## Sytotoksisuus

Cladribine on perinteinen syöpälääke (puriinanukleosidia/deoksiadenosiini-analogni, antimetaboliittiluokka), jota käytetään tällä hetkellä hematologisten pahanlaatuuksien hoidossa.

| Kohta | Sisältö |
|------|------|
| Sytotoksisuuden luokitus | Perinteinen sytotoksinen — puriinanukleosidia (deoksiadenosiini) analogni / antimetaboliitti |
| Myelosupressio-riski | Mekanistisesti oletetaan olevan merkittävä, sillä lääkkeen aktiivisuus riippuu valikoivasta lymfosyytin/monosyytin poistumisesta DNA-kaksoisjärkäisyyden katkeamisen kautta; kvantitatiivisia hematologisen myrkyllisyyden tietoja ei ole saatavilla tässä näytön paketissa — katso pakkausseloste |
| Emetogeniteettien luokitus | Katso pakkausselostetta varoituksista ja varotoimista |
| Seurantakohteet | Täydellinen verilaskenta eri muotojen kanssa (erityisesti lymfosyyttiluku), maksa- ja munuaistoiminta |
| Käsittelysuojaus | Antineoplastinen — sytotoksisen lääkkeen käsittelysuojaukset soveltuvat |

---

## Turvallisuusnäkökohtia

Katso turvallisuustiedot pakkausselosteesta.

*(Huomautus: TFDA/Fimea-pakkausselosteiden varoitukset ja vasta-aiheet on merkitty **Blocking**-tietoaukoksi (DG001) tässä näytön paketissa — tämä on ratkaistava ennen kuin mitään turvallisuusarviointia voidaan jatkaa.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidä**

**Perustelu:**
Tällä ehdokkaalla on vain L5-näyttö — TxGNN-assosiaatio ilman tukevaa kliinistä tutkimusta tai kirjallisuutta, eikä mitään tunnistettua mekanistista yhteyttä cladribiinin tunnetun lymfosyytti/monosyytti-selektiivisen sytotoksisuuden ja rabdomyosarkooman biologian välillä. Kaikilla 7 ennustetulla indikatiolla tässä näytön paketissa on sama Pidä-status samasta syystä. Lääke ei myöskään ole tällä hetkellä markkinoilla Suomessa, ja turvallisuus- ja merkintätiedot, joita tarvitaan jopa alustavan turvallisuusarvioinnin (S1) tekemiseen, puuttuvat.

**Etenemisen edellytyksenä tarvitaan seuraavat tiedot:**
- TFDA/Fimea-pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä Blocking-aukko (DG001)
- Vahvistetut alkuperäisen indikaation ja MOA-tiedot DrugBankista (DG002)
- Prekliiniset tai mekanistiset tutkimukset, jotka erityisesti yhdistävät cladribiinin rabdomyosarkooomaan tai sarkoomabiologiaan
- Lääkkeiden väliset vuorovaikutustiedot
- Matalarankisten ehdokkaiden uudelleenseulonta uuden tutkimus- ja kirjallisuustodisteen kerääntyessä

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

