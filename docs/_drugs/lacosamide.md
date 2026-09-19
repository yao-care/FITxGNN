---
layout: default
title: Lacosamide
parent: Kohtalainen näyttö (L3-L4)
nav_order: 210
evidence_level: L3
indication_count: 10
---

# Lacosamide
{: .fs-9 }

Näytön taso: **L3** | Ennustetut käyttöaiheet: **10** kpl
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

# Lakosamidi: Epilepsiasta maanis-bipolaariseen affektiiviseen häiriöön

## Yhden lauseen yhteenveto

Lakosamidi on antiepilepsiakään (AED), joka toimii natriumkanavamodulaattorina ja sitä käytetään osittaisten kohtauksien hoitoon. TxGNN-malli ennustaa, että se saattaa olla tehokas **maanisen bipolaarisen affektiivisen häiriön** hoitoon, mutta vahvin saatavilla oleva todistusaineisto (1 rekrytointivaiheessa oleva vaiheen 3 tutkimus ja useita retrospektiivisiä/tapausraportteja) koskee bipolaarisen häiriön **depressiivisiä** eikä maanisia vaiheita — polariteetin epäsuhta heikentää luottamusta tähän spesifiin ennustukseen.

*Huomautus: `original_indications` ja `original_moa` eivät täyttyneet todistusaineistossa (tietoaukko DG002). "Epilepsia (osittaiset kohtaukset)" on päätelty tukevasta kirjallisuudesta/tutkimuskuvailuista (esim. "FDA-hyväksynnässä osittaisiin kohtauksiin," "apukäyttö epilepsian osittaisissa kohtauksissa"), ei muodollisesta indikaatiokentästä.*

---

## Pikayleiskatsaus

| Kohta | Sisältö |
|------|------|
| Alkuperäinen indikaatio | Epilepsia (osittaiset kohtaukset) — päätelty kirjallisuudesta, ei muodollisen merkinnän perusteella |
| Ennustettu uusi indikaatio | Maanis-bipolaarinen affektiivinen häiriö |
| TxGNN-ennustuspistemäärä | 99,96% (sijoitus 711) |
| Todistusaineiston taso | L3 |
| Suomen markkinatilanne | Ei markkinoilla |
| Hyväksyntöjen lukumäärä | 0 |
| Suositeltu päätös | Tutkimuskysymys (Odotus vahvistavan aineiston saamiseen) |

---

## Miksi tämä ennustus on kohtuullinen?

Tällä hetkellä yksityiskohtaista vaikutusmekanismia koskeva tieto ei ole saatavilla (tietoaukko DG002). Tunnetun tiedon perusteella lakosamidi vahvistaa selektiivisesti jännitteestä riippuvien natriumkanavien hidasta inaktivaatiota — farmakologisesti mekanismi liittyy vahvistettuihin mielialan stabilisaattoreihin kuten lamotrigiiniin, jota käytetään kliinisesti bipolaariseen häiriöön. Tämä jaettu luokkatasoinen mekanismi on biologinen perustelu TxGNN-ennustukselle.

Alkuperäisen indikaation (epilepsia) ja ennustetun uuden indikaation (bipolaarinen **mania**) välinen suhde on kuitenkin epäsuora. Olemassa olevat kliiniset ja tapaustasoisen todisteet lakosamidista bipolaarisessa häiriössä keskittyvät jatkuvasti **depressiivisiin** ja sekaviin/ahdistusoireisiin — esim. avoin paranetus depressiivisistä oireista, ja ainoa käynnissä oleva vaiheen 3 tutkimus (NCT07412132) kohdistuu spesifisesti suuriin depressiivisiin jaksokausiin Bipolaarisen I/II häiriön yhteydessä. Mikään tämän todistusaineiston tutkimus tai julkaisu ei suoraan osoita antiimanista tehokkuutta, joten mekanistinen selitys (natriumkanavastabilisaatio → mielialan stabilisaatio) on uskottava mutta sitä ei ole osoitettu ulottuvan spesifisesti maaniselle navalle.

## Kliinisen tutkimuksen todisteet

| Tutkimusnumero | Vaihe | Tila | Osallistujat | Keskeiset löydökset |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Vaihe 3 | Rekrytointivaiheessa | 40 | Arvioi lakosamidia lisähoitona **suurissa depressiivisissä jaksoissa** bipolaarisessa I/II häiriössä (ei mania); perustuu edeltäviin havaintoihin/avoimiin oireista paranettavuuden signaaleista epilepsia- ja bipolaaripotilailta. Polariteetin epäsuhta "maanisen" ennustuksen kanssa — tuloksia ei vielä. |

## Kirjallisuuden todisteet

| PMID | Vuosi | Tyyppi | Julkaisu | Keskeiset löydökset |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospektiivinen kohortti | Psychiatry Clin Neurosci | 30 päivän vertailu lakosamidista vs. muut AED:t bipolaarisissa häiriöissä ilman epilepsiaa — ensimmäinen lakosamidin omistautunut tarkastelu bipolaarisessa häiriössä. |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Avoin piilotutkimus | J Clin Psychopharmacol | 12 viikon avoin piilotutkimus osoittaa tehokkuus/turvallisuussignaali spesifisesti **bipolaarisessa masennuksessa**. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospektiivinen monitupakeskustutkimus | Epilepsy Behav | Lakosamidi liittyy parantuneisiin depressio/ahdistus-oireisiin paikallisen epilepsian potilailla — edeltävä signaali psykiatriseen käyttöön. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Tapausraportti | Acta Biomed | Mielialan stabilisaatio saavutettiin lakosamidilla potilaalla, jolla oli mielialan häiriö, PTSD ja otsalohkon epilepsia. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Tapausraportti (haittavaikutus) | Indian J Psychol Med | Neutropenia, jonka laukaisi lakosamidi bipolaarisessa häiriössä ja epilepsiassa olevan potilaan yhteydessä — turvallisuussignaali. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Tapausraportti | Cureus | Monimutkainen Bipolaarisen I häiriön tapaus useilla komorbiditeetteilla mukaan lukien kohtauksenkaltainen aktiviteetti; havainnollistava pikemminkin kuin tehokkuuden todiste. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Katsaus | Ther Drug Monit | Huomioi AED:t, mukaan lukien lakosamidi-luokka, jota käytetään off-label-käytössä bipolaarisen häiriön hoidossa. |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Katsaus | Adv Drug Deliv Rev | Tausta lakosamidin kemiallisista/farmakokineetisista ominaisuuksista uudempien AED:ien joukossa. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Katsaus | ACS Chem Neurosci | Käsittelee CRMP2:a lääkeaineen kohteena, joka liittyy lakosamidin vaikutusmekanismiin. |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | Mekanistinen | PNAS | Lamotrigiinin kryo-EM-rakenteen mekanismi Nav-kanavan inhibitiosta, siihen liittyvä mielialan stabilisaattori AED — tukee jaetun mekanismin perustelu. |

---

## Turvallisuusnäkökohdat

Katso pakkausselosteesta turvallisuustietoja. *(Keskeiset varoitukset, vasta-aiheet ja DDI-tiedot eivät olleet saatavilla tässä todistusaineistossa — DG001, luokiteltu Estäviksi, estää täydellisen S1-turvallisuuden esiarviointia.)*

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Tutkimuskysymys (Odotus vahvistavan aineiston saamiseen)**

**Perustelut:**
Mekanistinen perustelu (natriumkanavan hidasta inaktivaatiota, luokkaekvivalenssi lamotrigiiniin) on uskottava, mutta kaikki saatavilla oleva lakosamidin kliininen todistusaineisto bipolaarisessa häiriössä käsittelee **depressiivistä** napaa (avoin piilotutkimus, retrospektiivinen kohortti, yksi rekrytointivaiheessa oleva vaiheen 3 tutkimus), ei ennustetulla tavalla maanista napaa — suora polariteetin epäsuhta, joka on merkitty todistusaineiston omassa relevanssiarvioinnissa (Luokka B). Mikään valmis tutkimus tai kirjallisuus ei tällä hetkellä tue antiimanista tehokkuutta.

**Edistymiseen vaaditaan seuraavaa:**
- TFDA/EMA-pakkausseloste sulkemaan blokkivan turvallisuusaukko (DG001) ennen S1-edistymistä
- Muodollinen MOA-dokumentaatio (DG002) natriumkanavaistaan mielialan stabilisaatioon mekanistisen linkin perustella
- Tulokset NCT07412132:sta (depressiivisten jaksojen tutkimus) saatavilla ollessa siirtokelpoisuuden arvioimiseksi maanisiin esityksiin
- Harkitse ehdokkaan indikaatiota "bipolaariseen masennukseen" spesifisesti, jossa todistusaineisto on materiaalisesti vahvempi kuin "maanis-bipolaarisessa affektiivisessa häiriössä"
- Huomio: samassa todistusaineistossa **migreeni** (sijoitus 5) osoittaa huomattavasti vahvemman todistusaineiston (L1, pää-pää vaihe 3 RCT:t vs. propranololi, päätösvaihe S3, "Jatka varauksilla") ja saattaa vaatia erillisen, korkeamman prioriteetin arvioinnin

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

