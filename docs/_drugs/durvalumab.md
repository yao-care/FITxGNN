---
layout: default
title: Durvalumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: Anti-PD-L1 pistokkeen estäjä — Ennustettu uusi käyttöaihe: Prostataan kuuluvan virtsaputken uroteliaalikarsinooma

## Yhden lauseen yhteenveto

Durvalumab on anti-PD-L1 monoklonaalinen vasta-aine (immuunisen pistokkeen estäjä); tämä näyttöpaketti ei dokumentoi sen alkuperäistä hyväksyttyä käyttöaihetta tai yksityiskohtaisia toimintamekanismikohtaisia tietoja, ja lääke ei ole tällä hetkellä markkinoilla Suomessa.
TxGNN-mallin parhaiten rankattu ennuste on **Prostataan kuuluvan virtsaputken uroteliaalikarsinooma** (pistemäärä 99,98 %), mutta tätä erityistä ennustetta ei tällä hetkellä tueta klinisillä tutkimuksilla tai kirjallisuudella — se on pelkkä mallin hypoteesi.
Huomio: tämän paketin 10 ehdokkaasta kahdella muulla virtsateisiin/naisten sukupuolielimiin liittyvällä karsinooma-indikaatiolla (sijoitus 3 ja 6) on tutkimus- ja/tai kirjallisuustodisteita — katso johtopäätös yksityiskohtaisesti.

## Pika-yhteenveto

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen käyttöaihe | Ei dokumentoitu tässä näyttöpaketissa (`original_indications` tyhjä; Suomessa 0 lupaa tiedostossa) |
| Ennustettu uusi käyttöaihe | Prostataan kuuluvan virtsaputken uroteliaalikarsinooma |
| TxGNN-ennusteen pistemäärä | 99,98 % |
| Näyttötaso | L5 (vain mallin ennuste, ei tutkimuksia tai kirjallisuutta) |
| Suomen markkinatilanne | Ei markkinoilla (Ei markkinoilla) |
| Lupien määrä | 0 |
| Suositeltu päätös | Lykkää |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä durvalumabille ei ole saatavilla yksityiskohtaisia toimintamekanismikohtaisia tietoja tässä näyttöpaketissa (merkitty korkeamman vakavuusasteen tietoraukoksi). Käytettävissä olevan tukiperustelujen kentän tietojen perusteella durvalumab on **anti-PD-L1 monoklonaalinen vasta-aine**, joka toimii estämällä PD-1/PD-L1 pistokkeen signalointireittiä ja palauttamalla T-solujen välityksellä tapahtuvaa anti-tuumori-immuuniaktiivisuutta — mekanismi, joka on jo osoittautunut hoitostrategiaksi useissa uroteleiaalisissa ja muissa immuunisissa tuumorityypeissä, jotka ovat edustettuina tässä samassa ennustejoukkossa muualla.

Prostataan kuuluva virtsaputken uroteliaalikarsinooma jakaa kudoksen alkuperän virtsarakko- ja munuaisen pyhvöksen uroteleialisten karsinoomien kanssa — molemmat ovat osa laajempaa uroteleaalista karsinooma-perhettä. Tämän erityisen ennusteen perusteluna on mekanistinen ekstrapolointi: koska PD-L1 pistokkeen esto on tunnetusti biologisesti merkityksellinen uroteleiaalisissa karsinoomanissa yleensä, malli päättelee että sama saattaa päteä myös prostataan kuuluvan virtsaputken alatyyppiin.

Kuitenkin tämä ekstrapolointi ei ole **vielä tuettu minkään sairauden spesifisellä tutkimuksella tai julkaisulla** — yhtään clinicaltrials.gov-, ICTRP- tai PubMed-tietuetta ei löytynyt durvalumabista prostataan kuuluvassa virtsaputken uroteleiaalisessa karsinoomassa erityisesti (kyselylokin tunnukset 5–7, kaikki nolla tuloksia). Mekanistinen uskottavuus on peritty uroteleaalisen karsinoomaluokan kokonaisuudelta pikemminkin kuin suorilta todisteilta tässä tarkalleen määritellyssä histologisessa alatyyppissä.

## Kliinisten tutkimusten näyttö

Tällä hetkellä ei ole aiheeseen liittyviä rekisteröityjä kliinisiä tutkimuksia.

## Kirjallisuuden näyttö

Tällä hetkellä ei ole aiheeseen liittyvää saatavilla olevaa kirjallisuutta.

## Suomen markkinatiedot

Durvalumabilla ei ole tällä hetkellä markkinointilupaa Suomessa (`market_status`: Ei markkinoilla, `total_licenses`: 0). Tuotetietoja tai annostusmuoto-informaatiota ei ole saatavilla.

## Sytostaattisyys

| Kohta | Sisältö |
|------|---------|
| Sytostaattisyyden luokitus | Immunoterapia (anti-PD-L1 immuunisen pistokkeen estäjä) — ei tavanomainen sytostaattinen kemoterapiaaine |
| Luuydinsuppression riski | Katso pakkausseloste, varoitukset ja varotoimet |
| Pahoinvointiherkkyysluokitus | Katso pakkausseloste, varoitukset ja varotoimet |
| Seurantakohteet | Katso pakkausseloste, varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausseloste, varoitukset ja varotoimet |

## Turvallisuusnäkökohdat

Katso pakkausseloste turvallisuustiedoista.

## Johtopäätös ja seuraavat vaiheet

**Päätös: Lykkää**

**Perustelut:**
Parhaiten rankatulla ennustetulla käyttöaiheella (prostataan kuuluvan virtsaputken uroteliaalikarsinooma) on näyttötaso L5 — TxGNN-mallin pistemäärä, jolla ei ole yhtään vahvistavaa kliinistä tutkimusta tai kirjallisuutta. Lisäksi pakkausselosteeseen liittyvät varoitukset/vasta-aiheet durvalumabille on merkitty **Estäväksi** tietoraukoksi (DG001), joka itsessään estää tämän ehdokkaan siirtymisen S1-turvallisuuden esiarviointivaiheeseen riippumatta tehokkuustodisteista.

**Jotta voidaan edetä, tarvitaan seuraavaa:**
- TFDA/Fimea-pakkausseloste (varoitukset, vasta-aiheet) estävän tietorako (DG001) selvittämiseksi ja S1-turvallisuuden esiarviointivaiheelle pääsemiseksi
- Vahvistettu toimintamekanismi ja alkuperäisen hyväksytyn käyttöaihe-dokumentaatio (DG002)
- Sairauden spesifinen prekliininen tai varhaisen vaiheen kliininen tieto prostataan kuuluvasta virtsaputken uroteleiaalisesta karsinoomasta, koska nykyinen tuki perustuu pelkästään mekanistiseen ekstrapolointiin

**Huomio prioritarisoinnille:** Tässä samassa ennustejoukkossa on kaksi muuta ehdokasta, joilla on huomattavasti vahvempi näyttö ja jotka saattavat vaatia erillistä arviointia ennen tätä:
- **Invasiivinen virtsarakkon uroteliaalikarsinooma, sarkomatoidi variantti** (sijoitus 3, L3, päätösvaihe S1) — Phase 2 tutkimus (NCT03912818, keskeytetty, n=7) arvioitu "A" sairauden spesialisyydelle, sekä tukeva Phase 1 tutkimus (NCT02812420).
- **Endoselvikaalinen karsinooma** (sijoitus 6, L2, päätösvaihe S2) — kaksi tutkimusta (NCT04065269 Phase 2 käynnissä n=174; NCT03452332 Phase 1 valmis n=20) ja yksi tukeva katsaus (PMID 37467967).

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

