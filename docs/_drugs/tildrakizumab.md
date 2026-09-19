---
layout: default
title: Tildrakizumab
parent: Pelkkä mallin ennuste (L5)
nav_order: 375
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
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

# Tildrakizumab: immuunivälitteisestä tulehduksellisesta sairaudesta (alkuperäinen indikaatio ei saatavilla) vakavaan ei-proliferatiiviseen diabeettiseen retinopatiaan

## Yhden lauseen yhteenveto

Tildrakizumab (DrugBank DB14004) on anti-IL-23p19-monoklonaalinen vasta-aine; sen alkuperäinen hyväksytty indikaatio ei ole saatavilla nykyisessä todistusaineistossa. TxGNN-malli ennustaa mahdollisen vaikutuksen **vakavaan ei-proliferatiiviseen diabeettiseen retinopatiaan**, mutta tätä signaalia tukee tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua** — se on puhdas mallin ennuste ilman vahvistavia todisteita.

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|--------|
| Alkuperäinen indikaatio | Ei saatavilla (original_indications tyhjä, ei markkinoitua lupaa saatavilla) |
| Ennustettu uusi indikaatio | Vakava ei-proliferatiivinen diabeettinen retinopatia |
| TxGNN-ennusteen pistemäärä | 99.63% |
| Todistusten taso | L5 |
| Suomen markkinatilanne | ✗ Ei markkinoitu |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Odotusasema |

## Miksi tämä ennuste on järkevä?

Tildrakizumabin osalta ei ole tällä hetkellä saatavilla strukturoitua vaikutusmekanismin tietoa (`original_moa` on merkitty tiedon puutteeksi). Ennusteen perusteluihin sisältyneistä mekanistisista muistiinpanoista käy ilmi, että tildrakizumab on anti-IL-23p19-monoklonaalinen vasta-aine, joka estää Th17-signalointireittiä — sama kohderyhmä, jota käytetään IL-23/Th17-vetoisissa immuunivälitteissä tulehduksellisissa sairauksissa.

Ehdotettu yhteys diabeettiseen retinopatiaan perustuu epäsuoraan tulehdukselliseen hypoteesiin: kohonnut lasiaisen IL-17A on tutkimuksissa havaittu olevan yhteydessä diabeettisen retinopatian aktiivisuuteen, ja perusteluna on, että ylävirran IL-23-salpaaja voisi teoriassa vaimentaa tätä alavirran tulehduksellista ja neovaskulaarista vastausta. Parhaiten sijoittuvassa ehdokkaassa "vakava" ei-proliferatiivinen diabeettinen retinopatia käsitellään laajemman sairauden myöhäisenä alatyypinä, mutta todistusaineisto huomauttaa selvästi, että alatyyppikohtaisia mekanistisia tietoja ei ole — yhteys johdetaan yleisestä diabeettisen retinopatian hypoteesista, ei vahvistettu itsenäisesti.

Kolme siihen liittyvää mutta luotettavuusastaltaan alhaisempaa signaalia ilmestyy samassa ennustejoukkoon — diabeettinen retinopatia (yleinen), diabeettinen katarakta ja lääkkeen aiheuttama osteoporoosi — kukin myös arvioitu L5/Odotusasema. Diabeettisen kataraktan yhteys on todistusaineiston taholta selvästi merkitty sillä, että tunnettu mekanistinen silta IL-23/IL-17-biologiaan puuttuu (sen patofysiologia on polyoli-rata- ja glykosylaatiovetoinen), ja osteoporoosin yhteys perustuu vain yleiseen IL-17/osteoklasti-kirjallisuuteen eikä tildrakizumabin spesifisiin tietoihin. Mikään näistä neljästä ennusteesta ei tällä hetkellä saa kliinisten tutkimusten tai kirjallisuuden tukea — ne ovat pelkästään verkkoennausteiden tuloksia.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole kirjattuja aiheeseen liittyviä kliinisiä tutkimuksia.

## Kirjallisuuden todisteet

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta.

## Suomen markkinatiedot

Tildrakizumab ei ole markkinoitu Suomessa (0 markkinointilupia saatavilla). Tätä ehdokasta varten ei ole tällä hetkellä saatavilla hyväksyttyjen tuotteiden, annostelumuotojen tai indikaatioiden tietoja.

## Turvallisuusnäkökohdat

Turvallisuustiedot löytyvät pakkausselosteesta.

*(Huomautus: todistusaineisto merkitsee Fimea/pakkaustason varoitusten ja vasta-aiheisten puuttumisen estäväksi tiedon puutteeksi — katso Johtopäätös alla.)*

## Johtopäätös ja seuraavat vaiheet

**Päätös: Odotusasema**

**Perustelut:**
Tämä on puhtaasti laskennallinen (L5) signaali ilman tukevia kliinisiä tutkimuksia tai kirjallisuutta, ilman vahvistettua mekanistista siltaa ehdotettuun indikaatioon, ja lääke ei ole tällä hetkellä markkinoitu Suomessa. Ei ole vielä perusteita siirtää tätä ehdokasta alkuperäisen seulonnan ohi.

**Jatkaminen edellyttää seuraavaa:**
- Virallinen pakkauseloste / pakkaustason varoitukset ja vasta-aiheet (tällä hetkellä estävä tiedon puute — vaaditaan ennen mitään turvallisuuden esiseulontaa)
- Strukturoitu vaikutusmekanismin vahvistus DrugBankista tai vastaavasta lähteestä (tällä hetkellä korkean vakavuuden tiedon puute)
- Tildrakizumabin alkuperäinen hyväksytty indikaatio ja sääntelyhistoria
- Prekliininen tai translatoriaalinen data, joka erityisesti yhdistää IL-23/Th17-inhibition diabeettisen retinopatian patofysiologiaan (alatyyppikohtainen, ei johdettu yleisistä DR-hypoteeseista)
- Kaikki nousevat kliiniset tutkimukset tai tapausraporttien todisteet tässä indikaatiotilassa, evidence level L5:n yläpuolelle arviointiin

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

