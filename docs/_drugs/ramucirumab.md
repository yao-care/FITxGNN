---
layout: default
title: Ramucirumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: Kiinteän kasvainten onkologiasta kohdun ligamenttien adenokarsinoomaan

## Yhteenveto yhdellä lauseella

Ramucirumab on anti-VEGFR2-monoklonaalinen vasta-aine, jota käytetään kiinteän kasvainten onkologiassa; sen tarkka alkuperäinen indikaatio ei ole kuvattu tässä näytöpaketissa. TxGNN-malli ennustaa, että se saattaa olla tehokas **kohdun ligamenttien adenokarsinoomaa** vastaan, mutta tätä ennustetta tuetaan tällä hetkellä **0 kliinisellä tutkimuksella** ja **0 julkaisulla** — se perustuu kokonaan tietograafin assosiaatiovahvuuteen ja luokkatason anti-angiogeneettisen mekanismin hypoteesiin.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Ei määritetty näytöpaketissa (original_indications-kenttä tyhjä; DrugBank-louhinta epätäydellinen) |
| Ennustettu uusi indikaatio | Kohdun ligamenttien adenokarsinooma |
| TxGNN:n ennustuskeskiarvo | 99.95% |
| Näyttötaso | L5 |
| Suomen markkinoiden asema | ✗ Ei markkinoilla |
| Hyväksyntöjen määrä | 0 |
| Suositeltu päätös | Pidetään odotuksissa |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia toimintamekanismin tietoja ei ole saatavilla jäsennellyssä muodossa (original_moa on tietojen puute). Tälle ehdokastutkimukselle kerätyn perustelun perusteella ramucirumab on anti-VEGFR2-monoklonaalinen vasta-aine, joka mekaanisesti estää angiogeneesiä kiinteissä kasvaimissa, mikä antaa sille teoreettisesti laaja-alaista potentiaalia erittäin verisuonittuja maligniteetteja vastaan — mukaan lukien gynekologisten syöpien kannalta.

Tämä on kuitenkin **luokkatason ekstrapolaatio, ei tautiin kohdistuva havainto**. Kohdun ligamenttien adenokarsinooma on harvinainen histologinen alatyyppi, eikä ramucirumabiin liittyvää suoraa kliinistä, prekliinistä tai havainnollista tietoa tähän indikaatioon ole missään kyselyyn kuuluneista lähteistä (ClinicalTrials.gov, ICTRP, PubMed kaikki palauttivat nollatulokset). Erittäin korkea TxGNN-pistemäärä (99.95 %) heijastaa mallin opitun kaariassosiaation vahvuutta, ei kliinistä vahvistusta — sama kuvio toistuu kaikissa tämän lääkkeen 10 parhaiten sijoittuvassa ennusteessa, jotka ovat kaikki harvinaisia kohtu-/emätinkanavien adenokarsinooma-alityyppejä TxGNN:n mukaan luokiteltuna 814–978, joista kukin on yhtä paljon näyttöä vailla.

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole liittyvää rekisteröityä kliinisiä tutkimuksia

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla liittyvää kirjallisuutta

---

## Suomen markkinatiedot

Ramucirumabilla ei ole markkinoinnin lupia Suomessa (markkinatilanne: ei markkinoilla, 0 lupaa tiedoissa).

---

## Sytotoksisuus

Ramucirumab on syöpänsäätöaine (anti-VEGFR2-monoklonaalinen vasta-aine, jota käytetään kiinteän kasvainten onkologiassa).

| Kohta | Sisältö |
|------|------|
| Sytotoksisuusluokitus | Kohdennettu hoito (anti-VEGFR2-monoklonaalinen vasta-aine / anti-angiogeneettinen aine) |
| Luuydinvaimennusriski | Katso pakkausseloste varoitukset ja varotoimet |
| Pahoinvointiluokitus | Katso pakkausseloste varoitukset ja varotoimet |
| Valvontakohdat | Katso pakkausseloste varoitukset ja varotoimet |
| Käsittelysuojaus | Katso pakkausseloste varoitukset ja varotoimet |

---

## Turvallisuusnäkökohdat

Katso pakkauselosteen turvallisuustiedot.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidetään odotuksissa**

**Perustelut:**
Tämä ehdokas ei voi vielä edetä S0-vaiheen (vain malliennuste) yli. TFDA/sääntelyyn liittyvän pakkausselosteen tietojen puute on luokiteltu **Estäväksi** — se estää nimenomaista S1-turvallisuuden esiarviointiin pääsyä — eikä yhdessäkään 10 parhaiten ennustetusta indikaatiosta (kaikki harvinaisia kohtu-/emätinkanavien adenokarsinooma-alityyppejä, TxGNN:n mukaan luokiteltuna 814–978) ole mitään tukevia kliinisen tutkimuksen tai kirjallisuuden näyttöä.

**Jatkamiseksi tarvitaan seuraavaa:**
- Ramucirumabiin liittyvät alkuperäinen indikaatio ja hyväksytyn merkinnän tiedot (tällä hetkellä puuttuvat näytöpaketista)
- TFDA/Fimean pakkausseloste (varoitukset, vasta-aiheet) — Estävä puute, vaaditaan ennen mitään S1-turvallisuusarvioita
- Vahvistettu toimintamekanismin yksityiskohta DrugBank-ohjelmointirajapinnan kautta (Korkean vakavuuden puute)
- Vähintään prekliiniset tai mekanistiset tutkimukset, jotka ovat spesifejä gynekologisten maligniteettien kannalta, ennen kuin tämä ehdokas voi ylittää vain-malliennuste-statuksen

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

