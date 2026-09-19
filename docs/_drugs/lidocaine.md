---
layout: default
title: Lidocaine
parent: Pelkkä mallin ennuste (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidokaini: Paikallispuudutuksesta pisteinäiseen epiteelikeratokonjunktiviitiin

## Yhden lauseen yhteenveto

Lidokaini on vakiintunut amidityyppiinen paikallispuudute, jota käytetään kliinisesti paikallisesti/alueellisesti anesteettisenä aineena (mukaan lukien oftalmologisissa toimenpiteissä, kuten tässä tarkasteltavasta näyttöpohjasta käy ilmi). TxGNN-mallin parhaiten sijoittuva ennuste on **pisteinäinen epiteelikeratokonjunktiviitti**, mutta tällä erityisellä ehdokkaalla ei ole tällä hetkellä **nolla kliinistä tutkimusta** ja **nolla tutkimuskirjallisuutta** — se on puhdas mallin pisteluku -signaali, jolla ei ole ulkoista validointia.

## Pikasilmäys

| Erä | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Paikallinen/alueellinen puudutus (vakiintunut farmakologinen käyttö; Suomeen ominaisen hyväksytyn indikaation teksti ei ole saatavilla — lääkettä ei markkinoida) |
| Ennustettu uusi indikaatio | Pisteinäinen epiteelikeratokonjunktiviitti |
| TxGNN-ennusteen pistemäärä | 99.99% |
| Näyttötaso | L5 (vain mallin ennuste, tutkimuksia tai kirjallisuutta ei ole) |
| Suomen markkinatilanne | Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltu päätös | Pysäytys |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaista vaikutusmekanismin tietoa lidokaiiinista ei ole saatavilla tässä näyttöpaketissa. Olemassa olevien tukimateriaalien perusteella (kerätty samasta paketista muista ehdokkaista), lidokaini on natriumkanava-estävä paikallispuudute, jolla on vakiintunut oftalmologinen käyttö paikallisena/subkonjunktivaalisena puudutuksena silmäkirurgisissa toimenpiteissä (esim. intravitreaalinen injektio, pterygion poisto, kataraktaleikkaus).

Erityisesti parhaiten sijoittuneen ehdokkaan osalta näyttöpaketin omassa huomautuksessa todetaan selvästi: *"mitään kliinisen tutkimuksen tai kirjallisuuden näyttöä ei ole olemassa; tämä on puhdas mallin pisteluku -ennuste."* Pisteinäinen epiteelikeratokonjunktiviitti on sarveiskalvon epiteelisairaus (yleensä viraalinen, myrkyllinen tai kuiva silmä alkuperältään), eikä millään tavalla dokumentoidulla mekanismilla ole yhteyttä lidokaiiinin puuduttavan vaikutuksen ja tämän sairauden hoidon välillä.

Ainoa epäsuora uskottavuusargumentti on se, että lidokaiiinilla on jo hyväksytty muotoilu silmän pinnan soveltamiseen (oftalmologinen geeli/pisarat toimenpiteiden yhteydessä, kuten näkyy muista ehdokkaista), joten paikallinen reitti olisi teknisesti mahdollinen, jos hoitoperuste koskaan vahvistettaisiin — mutta sellaista perustaa ei tällä hetkellä ole olemassa.

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä kirjallisuuden näyttöä ei ole saatavilla.

## Suomen markkinatiedot

Suomen markkinoita koskevia lupia ei ole saatavilla — lidokaini ei ole tällä hetkellä markkinoilla Suomessa tämän näyttöpaketin perusteella (0 lupaa).

## Turvallisuusnäkökohdat

Viittaa pakkausselosteeseen turvallisuustiedoista. (Huomautus: TFDA/Fimea pakkausselosteen varoitukset ja vasta-aiheet ovat **Estävä** tietoaukko — DG001 — eikä niitä ole vielä haettu.)

## Muut seulotut ehdokkaat (Sijoitukset 2–10)

Kontekstiin, yhdeksän muuta TxGNN:n ennustamaa indikaatiota seulottiin parhaiten sijoittuneen ehdokkaan rinnalla. Vain yksi osoitti merkitsevää (ei pelkkää pistelukua) tukea:

| Sijoitus | Sairaus | Pistemäärä | Näyttötaso | Vaihe | Huomautus |
|------|---------|-------|-----------------|-------|------|
| 2 | Papillaarinen konjunktiviitti | 99.98% | L5 | S0 | Ei näyttöä |
| 3 | Rosacea-konjunktiviitti | 99.92% | L5 | S0 | Ei näyttöä |
| 4 | Altistuskeratitis | 99.87% | L5 | S0 | 1 aiheeseen liittymätön tapaussarja (metamfetamiini-keratitis) |
| 5 | Atooppinen konjunktiviitti | 99.86% | L4 | S0 | Vain epäsuora mekanistinen vihje (nenän puudutus/kyynelireflexi-tutkimus) |
| 6 | Konjunktivaalinen häiriö | 99.84% | L3 | S1 (Tutkimuskysymys) | Parhaiten tuettu ehdokas — IV-lidokaini-kirjallisuus SUNCT/SUNA:sta (trigeminaaliautonomiset kefalalgiat konjunktivaalisella injektiolla); suurin osa sen 18 tutkimuksesta heijastaa olemassa olevaa kirurgian-anestesian käyttöä, ei uutta indikaatiota |
| 7 | Nefroottinen oireyhtymä | 99.83% | L5 | S0 | Vain farmakokineettiset/turvallisuuskirjallisuus, ei tehokkuus |
| 8 | Ei-inhimillinen eläinsairaus | 99.82% | L4 | S0 | Ei-inhimillinen sairaus -merkintä; primaattikohtainen kuumeen tapaus (turvallisuussignaali, ei tehokkuus) |
| 9 | Kehonsieni | 99.82% | L5 | S0 | Ei mekaanista yhteyttä antifungaaliseen toimintaan |
| 10 | Steroidiresistentti nefroottinen oireyhtymä | 99.79% | L5 | S0 | Ei näyttöä, ei mekanistista hypoteesia |

Jos halutaan jatkaa tämän lääkkeen tutkimusta, **sijoitus 6 (konjunktivaalinen häiriö / SUNCT-SUNA)** on puolustettavampi tutkimussuunta, ei edellä raportoitu parhaiten sijoittunut ehdokas.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pysäytys**

**Perustelut:**
Parhaiten sijoittuneen ennustetun indikaation (pisteinäinen epiteelikeratokonjunktiviitti) tueksi on vain TxGNN-pisteluku, ilman kliinisiä tutkimuksia, ilman kirjallisuutta ja ilman mekanistista perustetta näyttöpaketissa — tämä ei täytä edes vähimmäisvaatimusta Tutkimuskysymys-vaiheelle (S1).

**Jatkamiseksi tarvitaan seuraavaa:**
- Suorat prekliiniset tai mekanistiset tutkimukset, jotka yhdistävät lidokaiiinin pisteinäiseen epiteelikeratokonjunktiviittin
- TFDA/Fimea pakkausselosteen tiedot (varoitukset, vasta-aiheet) — tällä hetkellä estävä aukko (DG001)
- DrugBank vaikutusmekanismin yksityiskohdat — tällä hetkellä korkean vakavuuden aukko (DG002)
- Harkitse uudelleenalueistamista sijoitukseen 6 ("konjunktivaalinen häiriö", erityisesti SUNCT/SUNA-signaalin), jolla on ainoa L3/S1-tason näyttö tässä paketissa

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

