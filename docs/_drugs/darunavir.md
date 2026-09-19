---
layout: default
title: Darunavir
parent: Pelkkä mallin ennuste (L5)
nav_order: 111
evidence_level: L5
indication_count: 4
---

# Darunavir
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

# Darunavir: HIV-1-infektiosta simiaanin immuunivajaatuntaudin infektioon

## Yhteenveto yhdessä lauseessa

Darunavir on HIV-1-proteinaasi-inhibiittori, joka tunnetaan parhaiten osana antiretroviraalisen yhdistelmähoidon käyttöä ihmisten HIV-1-infektioissa.
TxGNN-mallin paras ennustus on **Simiaanin immuunivajaatuntaudin (SIV) -infektio** — ei-ihmisprimaattien lentiviraalihoitainen tauti, ei ihmisille tarkoitettu sairaus — tuettu ainoastaan **4 prekliinisellä/eläintutkimuksella**, joista yksikään ei erityisesti testaa darunaviriä. Tällä hetkellä ei ole saatavilla kliinisiä tutkimuksia, Fimean markkinaläsnäoloa tai turvallisuusasiakirjoja, joten tämä kandidaatti ei ole toimikelpoinen ilman merkittävää lisätietoa.

## Pikayleiskatsaus

| Kohde | Sisältö |
|-------|---------|
| Alkuperäinen indikaatio | HIV-1-infektio (johdettu mekanistisesta perustelusta tässä todistuspaketissa; virallinen indikaatioteksti ja MOA on merkitty tietovajeiksi — katso Perustelut alla) |
| Ennustettu uusi indikaatio | Simiaanin immuunivajaatuntaudin infektio |
| TxGNN-ennusteen pistemäärä | 99.97% |
| Todisteiden taso | L4 (prekliiniset/eläintutkimukset vain) |
| Suomen markkinoiden asema | ✗ Ei markkinoilla |
| Lupien lukumäärä | 0 |
| Suositeltava päätös | Pidätä |

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtainen toimintamekanismin tietoa ei ole saatavilla strukturoidussa `original_moa` -kentässä (merkitty tietovajeksi, DG002). Kuitenkin todistuspaketin omassa uudelleenkäyttöperustelussa darunavir tunnistetaan **HIV-1-proteinaasi-inhibiittoriksi**, joka vaikuttaa retroviraalisen Gag-Pol-polyproteiinin yhdisteltäviin vaiheisiin, joita vaaditaan viruksen kypsymiseen.

SIV ja HIV ovat molemmat *Lentivirus*-suvun jäseniä ja jakavat merkittävää rakenteellista samankaltaisuutta niiden proteinaasi-entsyymeissä. Tämä antaa ennusteelle periaatteessa uskottavan mekanistisen perustan: HIV-1-proteinaasi-inhibiittori voisi teoriassa säilyttää aktiivisuuden SIV-proteinaasia vastaan ei-ihmisprimaattien malleissa.

Siitä huolimatta mekanistinen linkki on epäsuora. Yksikään neljästä kirjallisuusennätyksestä ei tutkinut erityisesti darunaviriä — kaksi kuvaavat monilääkkeiden cART-rejiimiä (emtrisitiabini, tenofovir jne.) SIV-infektoiduissa makakeissa, ja kaksi muuta kuvaavat täysin erilaisia aineita (HDAC-inhibiittori SAHA ja kullanyhdiste auranofiin) testattuna samassa eläinmallissa viruksen säiliön tutkimukselle. Nämä ovat sivukohtaisia, mallijärjestelmää koskevia viittauksia eikä suoraa darunavirin tehokkuuden tietoa. Lisäksi SIV-infektio on eläinlääketieteellinen/tutkimuksellisen eläimen tauti, ei ihmisille tarkoitettu indikaatio, mikä rajoittaa tämän kandidaatin relevansssia ihmisille tarkoitetussa lääkkeiden uudelleenkäytössä.

## Kliinisen tutkimuksen todisteet

Tällä hetkellä ei ole rekisteröityjä niihin liittyviä kliinisiä tutkimuksia.

## Kirjallisuustodisteet

| PMID | Vuosi | Tyyppi | Lehti | Keskeiset tulokset |
|------|-------|--------|-------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Eläintutkimus | AIDS Research and Human Retroviruses | Arvioi kahta uutta injektoitavaa cART-rejiimiä (ei darunavir-spesifisiä) SIV-replikaation tukahduttamiseksi SIVmac239-infektoiduissa rhesus-makakeissa |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Eläintutkimus | PLoS One | Yhdisti suppressiivisen cART:n HDAC-inhibiittorin SAHA:n kanssa SIV-infektoiduissa kiinalaisissa rhesus-makakeissa viruksen säiliöiden tutkimiseksi |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Eläintutkimus | PLoS Pathogens | Erittäin tehostettu monilääkkeinen ART-rejiimi saavutti pitkäaikaisen viruksen suppressin ja säiliön rajoituksen SIVmac251-infektoiduissa makakeissa |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Eläintutkimus | AIDS (London, England) | Kullanyhdiste auranofiin (ei-darunavir-aine) rajoitti virussäiliötä apinantaudin mallissa |

Huomautus: yksikään edellä mainituista tutkimuksista ei testaa darunaviriä suoraan; kaikki ovat muiden aineiden tai yhdistelmärejiimien SIV/makakki-mallin tutkimuksia.

## Muut TxGNN-ennustetut indikaatiot (ei priorisoituja)

Tämä todistuspaketti sisältää kolme muuta kandidaattia parhaan ennusteen lisäksi, joita kannattaa mainita täydellisyyden vuoksi:

| Sijoitus | Sairaus | Pistemäärä | Todisteiden taso | Päätös | Keskeinen huomautus |
|----------|---------|-----------|------------------|--------|-------------------|
| 2 | Kissan hankkima immuunivajaatuntatauti (FIV) | 99.97% | L2 | Tutkimuskysymys | Yksi päättynyt vaihe 4 eläinlääketieteellinen RCT ([NCT02770508](https://clinicaltrials.gov/study/NCT02770508), n=145) testasi suoraan boostattua darunaviriä + lamivudiiniä kissoissa — mutta tutkittavat eivät ole ihmisiä, mikä rajoittaa relevansssia ihmisille tarkoitetussa lääkkeiden uudelleenkäytössä |
| 3 | Harvinainen hermoston kehityshäiriö (ataktinen kävely, puuttuva puhe, vähentyneempi valkoaine) | 99.97% | L5 | Pidätä | Ei tunnistettua mekanistista tai kliinistä linkkiä; vain ennuste |
| 4 | Perinnöllinen yhdistetty hyperlipidemiaemia (vanhentunut termi) | 99.19% | L5 | Pidätä | Mekanistisesti ristiriitainen — HIV-proteinaasi-inhibiittorit tunnetaan *aiheuttavan* dyslipidemian haittavaikutuksena, ei hoitavan sitä |

## Suomen markkinatiedot

Darunavir ei ole tällä hetkellä **markkinoilla** Suomessa (0 lupaa), joten tuote-/lupa-taulukko ei ole saatavilla.

## Turvallisuusnäkökohtia

Katso turvallisustiedot pakkausselosteesta. (Huomautus: TFDA/Fimean pakkausselosteen varoitukset ja vasta-aiheet on merkitty **estäväksi** tietovajeksi tässä todistuspaketissa — katso Johtopäätös alla.)

## Johtopäätös ja seuraavat vaiheet

**Päätös: Pidätä**

**Perustelut:**
Korkeimmin sijoitettu ennustettu indikaatio on eläinlääketieteellinen tauti (SIV, ei-ihmissairaus), tuettu ainoastaan prekliinisen eläinmallin kirjallisuudella, joka ei suoraan testaa darunaviriä, nolla kliinisellä tutkimuksella ja ilman markkinaläsnäoloa Suomessa. Turvallisuus-/merkintätietojen estävän vakavuuden tietovajeen yhdessä kanssa on riittämätöntä näyttöä edetä muodolliseen turvallisuustarkastukseen (S1).

**Edetäkseen seuraavaa vaaditaan:**
- TFDA/Fimean pakkausseloste (varoitukset, vasta-aiheet) — tällä hetkellä estävä tieto-vaje (DG001)
- Vahvistettu toimintamekanismi DrugBankista — tällä hetkellä korkean vakavuuden tieto-vaje (DG002)
- Darunavir-spesifinen (ei yhdistelmärejiimi) prekliininen aineisto SIV-mallissa
- Translaatiomahdollisuuksien selventäminen, koska kaksi parhainta ennustetta (SIV, FIV) ovat eläinlääketieteellisiä pikemminkin kuin ihmisille tarkoitettuja indikaatioita
- Jos tavoitteena on sen sijaan FIV-signaali (sijoitus 2, L2, Tutkimuskysymys), eläinlääketieteellisen-ihmisten välistä translaatioperustelua vaaditaan sen vahvemman tutkimustodistuksen vuoksi (NCT02770508)

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

