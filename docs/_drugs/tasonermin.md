---
layout: default
title: Tasonermin
parent: Pelkkä mallin ennuste (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Tasonermin
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

# Tasonermin: Pehmeiden kudosten sarkooomasta (raajan perfuusio) eturauhanen virtsaputken uroteliaalikarsinoomaan

## Yhden lauseen yhteenveto

Tasonermin (ihmisen rekombinantti TNF-alfa, muualla markkinoilla nimellä Beromun) on sytokiini-agentti, jonka vakiintunut kliininen käyttö on eristetty raajan perfuusio pehmeiden kudosten sarkooomassa. TxGNN-malli ennustaa, että se voi olla tehokas **eturauhanen virtsaputken uroteliaalikarsinoomassa**, mutta tämä on tällä hetkellä **puhtaasti mallin ennustus ilman tukevia kliinisiä tutkimuksia tai julkaisuja**.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | Pehmeiden kudosten sarkooma (eristetty raajan perfuusio) — tunnetun lääkkeen taustan mukaisesti; ei lisensöity Suomessa |
| Ennustettu uusi indikaatio | Eturauhanen virtsaputken uroteliaalikarsinooma |
| TxGNN-ennustuskeskiarvo | 99.81% |
| Todistusaineiston taso | L5 |
| Suomen markkina-asema | Ei markkinoilla |
| Valtuutuksien lukumäärä | 0 |
| Suositeltu päätös | Odota |

## Miksi tämä ennustus on järkevä?

Tasonerminin yksityiskohtaisia, lähde-varmennettuja toimintamekanismin tietoja ei ole vielä saatavilla (merkitty suuren vakavuusasteen tietokuiluksi). Tunnettujen yleistietojen perusteella tasonermin on ihmisen rekombinantti TNF-alfa, jolla on kasvaimeen liittyvien verisuonten endoteeliä tuhoava, apoptoosia edistävä ja immunimoduloiva aktiivisuus, mikä antaa sille teoreettisesti laajan spektrin syöpää vastustava potentiaali kiinteillä kasvaimilla.

Kuitenkin sen ainoa vakiintunut kliininen käyttö on eristetty raajan perfuusio pehmeiden kudosten sarkooomassa — paikallisen alueen antoväylä, joka valittiin erityisesti siksi, että TNF-alfan systeeminen antaminen aiheuttaa vakavaa, sokki-kaltaista toksisuutta. Eturauhanen virtsaputken uroteliaalikarsinoomalla ei ole vakiintunutta paikallisen alueen perfuusion hoitoparadigmaa, joka olisi verrattavissa raajan perfuusioon, joten tasonerminin kliinisessä käytössä käytetty paikallisen alueen antoväylä ei ilmeisesti sovellu tälle indikaatiolle.

Mikään uroteliaalikarsinooma-spesifinen, mekanistinen, prekliininen tai kliininen todistusaineisto ei tällä hetkellä tue tätä ennustusta — se johtuu puhtaasti TxGNN:n graafipohjaisen assosiaatiopisteytyksestä.

## Kliinisen tutkimuksen todistusaineisto

Tällä hetkellä asiaan liittyviä rekisteröityjä kliinisiä tutkimuksia ei ole.

## Kirjallisuuden todistusaineisto

Tällä hetkellä asiaan liittyvää saatavilla olevaa kirjallisuutta ei ole.

## Suomen markkina-tiedot

Tasonerminia ei ole tällä hetkellä markkinoilla Suomessa (0 valtuutusta rekisterissä); lisensointi- tai hyväksytyn indikaation tietoja ei ole saatavilla.

## Toksisuus

| Kohta | Sisältö |
|------|---------|
| Toksisuusluokitus | Immunoterapia / sytokiniherapia (ihmisen rekombinantti TNF-alfa) |
| Luuydintukahduttamisen riski | Katso turvaohjeet pakkausselosteesta; tunnettu systeeminen riski tälle luokalle on vakava sytokinievästyminen/sokki-kaltainen reaktio, ei klassinen luuydintukahduttaminen |
| Emetoisuusluokitus | Katso turvaohjeet pakkausselosteesta |
| Seurantakohteet | Hemodynamiikka-/sydänverenkiertoseuranta (erityisesti jos systeeminen tai perfuusioon perustuva altistus), CBC, maksan ja munuaisten toiminta |
| Käsittelyssuoja | Käsitellään laitoksen sytostaattisten/biologisten valmisteiden protokollien mukaisesti merkinnän vahvistamista odottaen |

## Turvahuomiot

Katso turvaohjeet pakkausselosteesta.

## Johtopäätelmät ja seuraavat vaiheet

**Päätös: Odota**

**Perustelut:**
Tämä ehdokas sijaitsee todistusaineiston tasolla L5 (päätösten vaihe S0) — ennustusta ei tue mikään kliininen tutkimus, ICTRP-tietue tai julkaisu, ja blokaava tietokuilu (puuttuvat TFDA/Fimea-pakkausselosteen varoitukset ja vasta-aiheet) estävät jopa alkuperäisen turvakatselmusvaiheen (S1). Mekanistinen perustelun on myös heikko: Tasonerminin ainoa vahvistettu käyttö perustuu paikallisen alueen perfuusion antoväylään, jota ei voida soveltaa tähän uuteen indikaatioon.

**Etenemiseksi tarvitaan seuraavat:**
- TFDA/Fimea-pakkausseloste (varoitukset, vasta-aiheet) S1-turvakatselmusvaiheen vapauttamiseksi
- Vahvistettu toimintamekanismin tieto DrugBankista tai pääasiallisista kirjallisista lähteistä
- Prekliininen tai varhainen kliininen todistusaineisto, joka koskee eturauhanen virtsaputken uroteliaalikarsinoomaa
- Toteuttamiskelpoinen antoväyläperuste ottaen huomioon TNF-alfan systeemisen toksisuuden rajoitukset

*Huomio: Tämä sama L5/Odota-tila ja tietokuilu koskevat myös muita 9 TxGNN-ennustettua indikaatiota tässä todistusaineiston pakkauksessa (sijoitukset 2–10), joista yksikään ei ole tuettu kliinisillä tutkimuksilla tai kirjallisuudella.*

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

