---
layout: default
title: Lorlatinib
parent: Pelkkä mallin ennuste (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: ALK-positiivisesta ei-pienisoluisesta keuhkosyövästä gingiaaaliseen fibromatoosiin

## Yhden lauseen yhteenveto

Lorlatinib on kolmannen sukupolven ALK/ROS1-tyrosiinikinaasin estäjä, jonka vakiintunut käyttöindikaatio on ALK-positiivinen ei-pienisoluinen keuhkosyöpä (NSCLC), kuten tässä evidenssipakkauksessa sisältyvä lääketurvallisuuskirjallisuus osoittaa. TxGNN-mallin parhaiten arvoitettu ennuste tälle kandidaatille on **gingiaalinen fibromatoosi**, mutta tätä assosiaatiota tukee tällä hetkellä **0 kliinistä tutkimusta** ja **0 julkaisua**, ja siihen liittyvä perusteltu viittaa siihen, että kyseessä on todennäköisesti mallin kohina eikä todellinen mekanistinen signaali.

---

## Nopea yleiskatsaus

| Kohta | Sisältö |
|------|---------|
| Alkuperäinen indikaatio | ALK-positiivinen ei-pienisoluinen keuhkosyöpä (NSCLC) — johdettu kirjallisuuskontekstista (esim. PMID 38554546); ei vahvistettu Suomen viranomaisten hakemuksella, koska sellaista ei ole |
| Ennustettu uusi indikaatio | Gingiaalinen fibromatoosi |
| TxGNN-ennusteen pistemäärä | 99.81% |
| Evidenssitaso | L5 |
| Suomen markkinoiden asema | Ei markkinoilla (Ei markkinoilla) |
| Markkinointilupauksien lukumäärä | 0 |
| Suositeltu päätös | Hold |

---

## Miksi tämä ennuste on järkevä?

Tällä hetkellä yksityiskohtaisia vaikutusmekanismin tietoja ei ole saatavilla (DrugBank MOA -kenttä on tietorako tässä tietueessa). Tämän kandidaatin laajemman evidenssisarjan perusteella haetusta kirjallisuudesta lorlatinib on aivoihin tunkeutuva, kolmannen sukupolven ALK/ROS1-tyrosiinikinaasin estäjä, jonka vakiintunut kliininen aktiivisuus on ALK:n uudelleen järjestäytyneiden pahanlaatuisissa kasvaimissa, pääasiassa NSCLC:ssä.

Gingiaalinen fibromatoosi on kuitenkin perinnöllinen sidekudoksen ylikasvun sairaus, joka on yleisimmin yhdistetty geeneihin, kuten *SOS1* ja *REST*. ALK- tai ROS1-signaloinnin osallisuutta sen patofysiologiassa ei tunneta, eikä onkogeeninä olevan ajurin suhdetta lorlatinibin kohdeprofiiliin ole.

Tähän kandidaattiin liitetty siirtokäyttöindikaation perusteltu eksplisiittisesti osoittaa, että ennusteella ei ole tukevaa kliinisen tutkimuksen tai julkaisun näyttöä ja kuvailee sen syntyvän "puhtaasti mallin ennusteen kohinasta" (原文：純屬模型預測雜訊), eikä lorlatinibin farmakologian ja tämän sairauden välille ole olemassa uskottavaa mekanistista yhteyttä. Tätä kandidaattia ei siis tulisi nykymuodossaan tulkita uskottavaksi siirtokäyttöindikaation signaaliksi.

*Huomautus: tämä evidenssipakkaus arvoitti 10 kandidaattindikaatiota lorlatinibille; tämä raportti kattaa parhaiten arvoitetun TxGNN-pisteytyksen mukaan. Kaksi muuta kandidaattia samassa erässä (keuhkojen juurikarsinooma; keuhkon sukusolun kasvain) saavuttivat evidenssitason L3 kirjallisuuden tuella, vaikka molempia merkittiin myös sairauden nimeämis-/ontologian kartoitusongelmista ja niiden tulisi ansaita erillistä arviointia.*

---

## Kliinisen tutkimuksen näyttö

Tällä hetkellä ei ole rekisteröityjä aiheeseen liittyviä kliinisiä tutkimuksia

---

## Kirjallisuuden näyttö

Tällä hetkellä ei ole saatavilla aiheeseen liittyvää kirjallisuutta

---

## Suomen markkinatiedot

Lorlatinibia ei ole tällä hetkellä markkinoilla Suomessa (markkinaasema: Ei markkinoilla). Tälle tuotteelle ei ole tiedostoissa markkinointilupia.

---

## Sytostaattisyys

| Kohta | Sisältö |
|------|---------|
| Sytostaattinen luokittelu | Kohdistettu lääkehoito (ALK/ROS1-tyrosiinikinaasin estäjä; ei-sytostaattinen mekanismi) |
| Luuytimen tukahduttamisen riski | Matala — ei tavallinen sytostaattinen aine; luuytimen tukahduttaminen ei ole merkittävä löydös saatavilla olevassa kirjallisuudessa |
| Pahoinvointiherkkyys | Matala, yhdenmukaisesti muiden ALK-estäjien kanssa |
| Seurantakohdat | Rasva-arvojen paneeli (hyperkolesterolemia/hypertriglyserideemia raportoitu tapauskirjallisuudessa), maksatoiminta, paino/BMI, mieliala ja kognitiivinen tila, keuhkooireet (harvinainen ARDS raportoitu tapauskirjallisuudessa) |
| Käsittelysuojaus | Suun kautta otettava kohdistettu lääkehoito; vakio-instituution suun kautta otettavat onkolyyttisen lääkehoidon varotoimet ovat voimassa. Ei vahvistettua sytostaattisen (vaarallisen lääkkeen) käsittelyluokitusta — katso lopullisen ohjauksen osalta pakkausselosteesta |

---

## Turvallisuusharkinnot

Katso turvallisuustiedot pakkausselosteesta.

---

## Johtopäätös ja seuraavat vaiheet

**Päätös: Hold**

**Perustelut:**
Tämä on TxGNN:n korkeimmin arvoitettu ennuste lorlatinibille, mutta sillä ei ole kliinisen tutkimuksen tai kirjallisuuden näyttöä, ja sairauden tunnettu geneettiset alkuperä (SOS1/REST-liittyvä) ei osoita mekanistista yhteyttä lorlatinibin ALK/ROS1-kohteeseen. Evidenssipakkaus itse merkitsee tätä todennäköisesti ennusteen kohinaksi, joten se ei täytä edellytyksiä jatkaa.

**Jatkamiseksi tarvitaan seuraavaa:**
- Vahvistettu alkuperäinen indikaatio ja vaikutusmekanismin tiedot DrugBankista (tällä hetkellä korkean vakavuuden tietorako DG001)
- TFDA:n vastaava (Suomi) pakkausseloste varoitukset/vasta-indikaatiot (tällä hetkellä estävä tietorako)
- Itsenäinen mekanistinen tai prekliininen näyttö ALK/ROS1:n estämisen yhdistämisestä gingiaaaliseen fibromatoosiin ennen muuta investointia
- Jos tämän lääkkeen siirtokäyttötutkimus jatkuu, aseta etusijalle korkeamman evidenssisen kandidaattien uudelleenarviointi samassa erässä (esim. keuhkojen juurikarsinooma, keuhkon sukusolun kasvain) niiden todettujen sairauden nimeämis-/ontologian kartoitusongelmien ratkaisemisen jälkeen tämän kandidaatin sijaan

## Vastuuvapauslauseke

Tämä sisältö on tarkoitettu ainoastaan tutkimuskäyttöön eikä se ole lääketieteellistä neuvontaa.
Kliininen validointi vaaditaan ennen kliinistä käyttöä.

---

